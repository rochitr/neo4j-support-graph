# Support Knowledge Graph + Support Agent

Support tickets and support playbooks ("skills") loaded into a **Neo4j knowledge graph**, plus a **local chat agent** that answers from the playbooks stored in Aura and can raise tickets.

- [What it does](#what-it-does) · [Architecture](#architecture) · [Graph model](#graph-model) · [Data and findings](#data-and-findings)
- [Setup](#setup) · [Running the agent](#running-the-agent) · [Logs](#logs) · [Repository layout](#repository-layout) · [Limitations](#limitations) · [Security notes](#security-notes)

## What it does

1. **Knowledge graph.** 100 anonymized support tickets and 11 support playbooks become one connected graph. Tickets link to accounts, contacts, owners, tags, SLAs and timeline data. Each playbook is split into ordered steps, and each ticket is linked to the step that handles it.
2. **Support agent.** A chat UI on `localhost` that retrieves playbook steps from Aura, answers *only* from them with citations, and offers to raise a ticket when a team member must act or the knowledge base has no answer.
3. **Logging.** Every chat, every created ticket and a per-session event timeline are written to separate local log files.

## Architecture

```
Browser chat UI (localhost:8000)
        │
FastAPI server  graph-prep/agent/server.py
   ├─ retrieve → Aura fulltext search: SkillStep (playbook steps) + similar past Tickets
   ├─ answer   → `claude -p` (logged-in Claude Code CLI), grounded in retrieved text only, cites skill + step
   ├─ propose  → "Create ticket" card when action is needed or the question is out of scope
   ├─ create   → on user click: Ticket + MATCHES_STEP written to Aura (primary), local Neo4j + JSONL (backup)
   └─ log      → chats.jsonl · tickets.jsonl · timeline.jsonl
```

The retrieved playbook text, similar tickets and user messages are passed to the model as data, with instructions to ignore any commands inside them. Tool use is disabled for the model call, so it can read text but cannot run commands or edit files.

## Graph model

```
(Ticket)-[:FOR_ACCOUNT]->(Account)        (Ticket)-[:REPORTED_BY]->(Contact)     (Ticket)-[:OWNED_BY]->(Agent)
(Ticket)-[:IN_SUBCATEGORY]->(SubCategory)-[:IN_CATEGORY]->(Category)
(Ticket)-[:TAGGED]->(Tag)   (Ticket)-[:ON_PART]->(Part)   (Ticket)-[:UNDER_SLA]->(SLA)
(SubCategory)-[:HANDLED_BY]->(Skill)
(Skill)-[:HAS_STEP]->(SkillStep)          (Skill)-[:RELATED_TO]->(Skill)
(Ticket)-[:MATCHES_STEP {confidence}]->(SkillStep)      (Ticket)-[:MATCHES_SKILL]->(Skill)
```

Timeline data (created, closed and modified dates, resolution and first-response hours, reopens) lives as properties on `Ticket`. Tickets with no suitable playbook carry `noSkillMatch = true` and a reason. Tickets created by the agent carry `source = 'support-agent'`.

| Node | Count | | Relationship | Count |
|---|---|---|---|---|
| Ticket | 100 | | FOR_ACCOUNT / REPORTED_BY / OWNED_BY / IN_SUBCATEGORY / ON_PART / UNDER_SLA | 100 each |
| SkillStep | 133 | | TAGGED | 128 |
| Contact | 59 | | HAS_STEP | 133 |
| Account | 27 | | RELATED_TO | 24 |
| Skill | 11 | | MATCHES_STEP / MATCHES_SKILL | 96 each |
| Agent / SLA / Tag / Part | 6 / 6 / 6 / 5 | | HANDLED_BY / IN_CATEGORY | 2 each |
| SubCategory / Category | 2 / 1 | | | |

Full model notes and data decisions: [graph-prep/GRAPH_MODEL.md](graph-prep/GRAPH_MODEL.md).

## Data and findings

- **Tickets:** `hackathon_support_tickets_anonymized.csv` (the `.xlsx` is the same data plus a "Timeline Summary" sheet). Two sub-categories, 50 tickets each: *Creation/setup of a new campaign* and *Boost a job*.
- **Use the CSV, not the xlsx, for loading.** The xlsx collapses Account-ID, Owner-ID and reporter email to a single placeholder, so every ticket would share one account, owner and contact. The CSV keeps the 27 / 6 / 59 distinct values.
- **Playbooks:** 11 Markdown files in `Support Skills/`. Each `##` / `###` heading becomes a `SkillStep`; `[[wiki-links]]` between playbooks become `RELATED_TO`. Ten links point to playbooks that do not exist yet (e.g. `Career-Site-Down`, `Invoice-Billing-Support`) and are skipped; they are a ready-made list of playbooks still to write.
- **Ticket → step mapping.** Each of the 100 tickets was read and assigned to a playbook step (`graph-prep/classify.py`), with a confidence rating: **46 high, 40 medium, 10 low**. **96 tickets matched; 4 had no suitable playbook** (TKT-106, 135, 160, 163).
- **Category labels are a poor guide to the right playbook.** Tickets filed under *Boost a job* map to 4 different playbooks, and tickets filed under *Creation/setup of a new campaign* map to 9. Overall, 62 of the 96 matched tickets map to Campaign Management, 14 to Publisher Channel Management and 9 to Media Planning; the remaining 11 are spread over six other playbooks.
- **Cleaning decisions:** dropped constant or placeholder columns (`Date`, `Enrich Stamp`, `Visibility`, `Is Spam`, approve/reject counts); removed anonymization-leaked email addresses from `Tags` (19 tickets); kept `Resolution Hrs Net` but note it is often much larger than gross resolution hours and its definition should be confirmed before analysis.
- **Mapping method caveat.** The ticket-to-step links come from a manual read-through, not an automated, measured classifier, so they have not been validated against a second reviewer.

## Setup

Requirements: Docker, Python 3.10+, `fastapi` and `uvicorn`, and the [Claude Code CLI](https://claude.com/claude-code) logged in (it is the agent's LLM). You also need a Neo4j Aura instance (Free is enough).

1. **Credentials (both gitignored).**
   - Copy `.neo4j-credentials.example` → `.neo4j-credentials` with `username/password` for the local Neo4j.
   - Copy `Neo4j-Created.example.txt` → `Neo4j-<id>-Created-<date>.txt` and fill in your Aura values (the file Aura gives you when you create the instance).
2. **Local Neo4j (Docker).**
   ```bash
   docker run -d --name neo4j -p 7474:7474 -p 7687:7687 \
     -e NEO4J_AUTH="$(cat .neo4j-credentials)" \
     -v "$PWD/neo4j-data":/data -v "$PWD/graph-prep/out":/var/lib/neo4j/import \
     neo4j:2026.09.0
   ```
   (The import mount must be writable; a read-only mount makes the container restart-loop.)
3. **Build the CSVs.**
   ```bash
   python3 -I graph-prep/prepare.py      # tickets + skills -> graph-prep/out/*.csv
   python3 -I graph-prep/classify.py     # ticket -> skill-step links
   ```
4. **Load the graph.**
   - Local: `docker exec -i neo4j cypher-shell -u neo4j -p '<password>' < graph-prep/load.cypher`
   - Aura: `python3 -I graph-prep/push_aura.py Neo4j-<id>-Created-<date>.txt` (uses Aura's HTTPS Query API, since Aura cannot `LOAD CSV` from your machine). Both loaders are idempotent (`MERGE` + uniqueness constraints).
5. **Aura search indexes (required by the agent).** Run once in Aura:
   ```cypher
   CREATE FULLTEXT INDEX step_text   IF NOT EXISTS FOR (n:SkillStep) ON EACH [n.heading, n.text];
   CREATE FULLTEXT INDEX ticket_text IF NOT EXISTS FOR (n:Ticket)    ON EACH [n.title, n.body];
   ```

## Running the agent

```bash
cd graph-prep/agent
pip install fastapi uvicorn
python3 -m uvicorn server:app --host 127.0.0.1 --port 8000
```

Open <http://localhost:8000>. The two dots in the header show whether Aura and local Neo4j are reachable. Try:

- *"Please boost job JR23091 in Montgomery AL with an extra $300 on Indeed for 10 days"* → cites **Campaign Management → 3C Boost a Job**, asks for missing details, offers a ticket.
- *"Can you reset my email password?"* → no sources, declined, offered a ticket flagged as a knowledge-base gap.

Set `AGENT_MODEL` (default `sonnet`) to change the model used through the CLI.

## Logs

Written to `graph-prep/agent/logs/` (gitignored):

| File | Contents |
|---|---|
| `chats.jsonl` | Every user and assistant message with session ID, retrieved step IDs, in-scope flag, whether a ticket was proposed |
| `tickets.jsonl` | Every ticket the agent creates, with title, summary, linked steps and whether the write to Aura and local Neo4j succeeded |
| `timeline.jsonl` | Per-session events: `chat_started`, `answered`, `ticket_proposed`, `ticket_created` |

Tickets are numbered from the highest existing ID (`TKT-201` onward). If the Aura write fails, the ticket is still kept in the local log and the user is told it is backup-only.

## Repository layout

```
Support Skills/                 11 playbooks (Markdown) — source of the SkillStep nodes
hackathon_support_tickets_anonymized.{csv,xlsx}
graph-prep/
  prepare.py                    tickets + skills -> import CSVs
  classify.py                   reviewed ticket -> skill-step mapping
  load.cypher                   constraints + LOAD CSV for local Neo4j
  push_aura.py                  loads the same CSVs into Aura over HTTPS
  GRAPH_MODEL.md                model, decisions, data quirks
  agent/
    server.py                   FastAPI agent (retrieval, answer, tickets, logs)
    static/index.html           chat UI
    logs/                       runtime logs (gitignored)
```

## Limitations

- **Demo scale:** 100 tickets, 11 playbooks, two ticket sub-categories. Nothing here has been load-tested.
- **Keyword search only:** the fulltext index misses paraphrases. Embeddings and a vector index would be the next step.
- **Latency:** each reply takes roughly 5–15 seconds because the LLM runs through `claude -p`. A direct API integration would be faster and more suitable for production.
- **Session memory is in-process:** chat history lives in server memory and is lost on restart (the logs persist).
- **Ticket lifecycle:** the agent creates tickets but does not yet update their stage from follow-up messages.
- **No authentication:** the server binds to `127.0.0.1` and has no login.
- **Unmatched playbooks:** 10 referenced playbooks do not exist, and 4 tickets have no matching playbook.

## Security notes

- Credentials live only in gitignored files (`.neo4j-credentials`, `Neo4j-*-Created-*.txt`). Do not commit them.
- The `Support Skills/` playbooks are internal operating procedures. Only publish this repository somewhere they are allowed to be shared.
- The model is told never to repeat personal identifiers in replies or tickets, and tickets are created only after the user confirms.
