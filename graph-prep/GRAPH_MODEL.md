# Support Knowledge Graph — model & prep notes

Inputs: `hackathon_support_tickets_anonymized.csv` (100 tickets), `Support Skills/*.md` (11 SOPs).
Regenerate CSVs: `python3 -I graph-prep/prepare.py` → `graph-prep/out/`.

## Model

```
(Contact)<-[:REPORTED_BY]-(Ticket)-[:FOR_ACCOUNT]->(Account)
(Ticket)-[:OWNED_BY]->(Agent)
(Ticket)-[:IN_SUBCATEGORY]->(SubCategory)-[:IN_CATEGORY]->(Category)
(Ticket)-[:TAGGED]->(Tag)   (Ticket)-[:ON_PART]->(Part)   (Ticket)-[:UNDER_SLA]->(SLA)
(SubCategory)-[:HANDLED_BY]->(Skill)          <- the key link: ticket type -> SOP
(Skill)-[:HAS_STEP]->(SkillStep)              <- one node per ## / ### section, ordered
(Skill)-[:RELATED_TO]->(Skill)                <- from [[wiki-links]] in the SOPs
```

Timeline lives on `Ticket` as properties (createdDate, closeDate, modifiedDate, weekNo, resolution/first-response
hours, pausedHrsCust, dormantHrs, reopens). Dates are ISO (`date()` in Cypher). If you want time-based
traversal, add `(:Week)` nodes keyed on `weekNo` (14 weeks) in the load step.

## Files in `out/`

| File | Rows | Key |
|---|---|---|
| tickets.csv | 100 | ticketId |
| accounts / contacts / agents | 27 / 59 / 6 | accountId / email / agentId |
| subcategories / tags / parts / slas | 2 / 6 / 5 / 6 | natural key |
| rel_ticket_{account,contact,owner,subcat,tag,part,sla}.csv | 100,100,100,100,128,100,100 | ticketId → target |
| skills.csv / skill_steps.csv | 11 / 133 | skillId / stepId |
| rel_skill_related.csv | 24 | fromSkill → toSkill |

## Decisions & data quirks

- **Use the CSV, not the xlsx.** In the xlsx, Account-ID, Owner-ID and Reported-by-email are collapsed to one
  placeholder (`DEMO-ACC-000`, etc.) so every ticket would share one account/owner/contact. The CSV has the distinct values.
  The xlsx "Timeline Summary" sheet is the same tickets restricted to date/duration columns, so no separate load is needed.
- **Dropped columns:** `Date` and `Enrich Stamp` (always `[demo phone]`), `Visibility`, `Is Spam`, `Approve/Reject Count`
  (constant), and the redundant minutes duplicates of the hour columns.
- **Tags:** 19 tickets have an anonymised email in `Tags` — filtered out. 6 real tags remain.
- **Only 2 sub-categories exist** (Creation/setup of a new campaign, Boost a job; 50 tickets each) and one category
  (Campaign Management). Both sub-categories are linked to the `Campaign-Management` skill via `HANDLED_BY`, but the
  step-level mapping (`classify.py`, `MATCHES_STEP`) shows the real spread: 62 of the 96 matched tickets map to Campaign Management,
  14 to Publisher-Channel-Management, 9 to Media-Planning, 11 to six other skills. 4 tickets have no suitable skill.
- **Missing values:** 2 tickets have no close date/resolution; 8 no sentiment; 9 no source channel; 62 no AI resolution status.
- **Suspicious metric:** `Resolution Hrs Net` is often much larger than `Resolution (Hrs)` (TKT-101: 444 vs 114).
  Confirm definitions before using either for analysis.
- **Stage** has inconsistent casing for the 2 non-resolved tickets (`awaiting_customer_response`, `Awaiting Adops Response`).
- **Dangling skill links:** 10 `[[...]]` targets have no SOP file (ATS-Integration-Triage, Career-Site-Down,
  Career-Site-Updates, Inbound-Feed-Jobs-Down, Invoice-Billing-Support, Market-Competitive-Insights,
  Onboarding-Project-Management, Proactive-Consulting-Advisory, Spend-Discrepancy-Investigation,
  UA-Reporting-Discrepancy). They are excluded from RELATED_TO for now; they are a ready-made list of SOPs to write.
- **Knowledge Base Gap** is True on only 7 tickets — these are the most direct "ticket without matching SOP" signal.

## Next steps

1. Copy `out/` into the Neo4j import dir (or serve it), create uniqueness constraints, load with `LOAD CSV` — the container's
   `neo4j-data/` has no import mount yet, so `docker run`/compose needs `-v .../graph-prep/out:/var/lib/neo4j/import`.
2. Link tickets to specific SOP steps (e.g. Boost a job → `Campaign-Management#3C`) by title/body similarity or an LLM pass.
3. Optionally extract entities from tickets/SOPs (publishers such as Monster/Naukri/Indeed, tools like MOJO) as `(:Publisher)`, `(:Tool)`.
4. Add embeddings on `Ticket.body` and `SkillStep.text` + a vector index for retrieval.
