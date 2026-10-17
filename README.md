# Neo4j Support Knowledge Graph + Support Agent

Support tickets and support-skill SOPs loaded into Neo4j as a knowledge graph, with a local chat agent that answers from the SOPs and can raise tickets.
Model and data notes: [graph-prep/GRAPH_MODEL.md](graph-prep/GRAPH_MODEL.md).

## Setup
1. Copy `.neo4j-credentials.example` → `.neo4j-credentials` (local Docker Neo4j, `user/password`) and `Neo4j-Created.example.txt` → `Neo4j-<id>-Created-<date>.txt` (Aura). Both are gitignored.
2. Local Neo4j: `docker run -d --name neo4j -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=<user/password> -v $PWD/neo4j-data:/data -v $PWD/graph-prep/out:/var/lib/neo4j/import neo4j:2026.09.0`
3. Build CSVs: `python3 -I graph-prep/prepare.py && python3 -I graph-prep/classify.py`
4. Load local: pipe `graph-prep/load.cypher` into `cypher-shell`. Load Aura: `python3 -I graph-prep/push_aura.py Neo4j-<id>-Created-<date>.txt`
5. Aura only: create fulltext indexes `step_text` on `SkillStep(heading,text)` and `ticket_text` on `Ticket(title,body)`.

## Agent
`cd graph-prep/agent && pip install fastapi uvicorn && python3 -m uvicorn server:app --host 127.0.0.1 --port 8000` → http://localhost:8000
Uses the logged-in `claude` CLI (`claude -p`) as the LLM. Logs go to `graph-prep/agent/logs/` (chats, tickets, timeline; gitignored).
