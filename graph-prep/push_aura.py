"""Push graph-prep/out/*.csv to Aura via the HTTPS Query API (LOAD CSV can't read local files on Aura).
Usage: python3 -I push_aura.py <aura-credentials-file>   (idempotent: MERGE + constraints)"""
import base64, csv, json, os, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "out")
c = dict(l.strip().split("=", 1) for l in open(sys.argv[1]) if "=" in l and not l.startswith("#"))
URL = f"https://{c['NEO4J_URI'].split('://')[1]}/db/{c['NEO4J_DATABASE']}/query/v2"
AUTH = "Basic " + base64.b64encode(f"{c['NEO4J_USERNAME']}:{c['NEO4J_PASSWORD']}".encode()).decode()
def run(stmt, rows=None):
    body = {"statement": stmt}
    if rows is not None: body["parameters"] = {"rows": rows}
    req = urllib.request.Request(URL, json.dumps(body).encode(), {"Content-Type": "application/json", "Authorization": AUTH})
    try: return json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e: sys.exit(f"FAILED: {stmt[:80]}\n{e.read().decode()[:400]}")
def load(name): return list(csv.DictReader(open(os.path.join(OUT, name), encoding="utf-8")))
def push(name, stmt, batch=50):
    rows = load(name)
    for i in range(0, len(rows), batch): run("UNWIND $rows AS r " + stmt, rows[i:i + batch])
    print(f"{name}: {len(rows)}")

for label, key in [("Ticket","ticketId"),("Account","accountId"),("Contact","email"),("Agent","agentId"),("SubCategory","name"),
                   ("Category","name"),("Tag","name"),("Part","name"),("SLA","name"),("Skill","skillId"),("SkillStep","stepId")]:
    run(f"CREATE CONSTRAINT {label.lower()}_key IF NOT EXISTS FOR (n:{label}) REQUIRE n.{key} IS UNIQUE")
nul = lambda x: f"nullIf(r.{x},'')"
push("tickets.csv", f"""MERGE (t:Ticket {{ticketId:r.ticketId}}) SET t.title=r.title, t.body=r.body, t.stage=r.stage, t.state=r.state,
 t.severity=r.severity, t.sentiment={nul('sentiment')}, t.channel=r.channel, t.sourceChannel={nul('sourceChannel')},
 t.aiResolutionStatus={nul('aiResolutionStatus')}, t.kbGap=(r.kbGap='true'), t.createdDate=date(r.createdDate),
 t.closeDate=CASE r.closeDate WHEN '' THEN null ELSE date(r.closeDate) END, t.modifiedDate=date(r.modifiedDate), t.weekNo=r.weekNo,
 t.firstResponseMins=toFloat(r.firstResponseMins), t.firstResponseStatus=r.firstResponseStatus,
 t.resolutionHrsGross=toFloat({nul('resolutionHrsGross')}), t.resolutionHrsNet=toFloat({nul('resolutionHrsNet')}),
 t.resolutionHrsActive=toFloat(r.resolutionHrsActive), t.pausedHrsCust=toFloat(r.pausedHrsCust), t.dormantHrs=toFloat(r.dormantHrs),
 t.reopens=toInteger(r.reopens), t.resolutionStatus=r.resolutionStatus, t.workDurationDays=toFloat({nul('workDurationDays')}), t.url=r.url""")
push("accounts.csv", "MERGE (n:Account {accountId:r.accountId}) SET n.name=r.name")
push("contacts.csv", "MERGE (n:Contact {email:r.email}) SET n.name=r.name")
push("agents.csv", "MERGE (n:Agent {agentId:r.agentId}) SET n.name=r.name")
push("subcategories.csv", "MERGE (s:SubCategory {name:r.subCategory}) MERGE (c:Category {name:r.category}) MERGE (s)-[:IN_CATEGORY]->(c)")
push("tags.csv", "MERGE (:Tag {name:r.tag})"); push("parts.csv", "MERGE (:Part {name:r.part})"); push("slas.csv", "MERGE (:SLA {name:r.sla})")
for f, k, lab, prop, rel in [("account","accountId","Account","accountId","FOR_ACCOUNT"),("contact","email","Contact","email","REPORTED_BY"),
        ("owner","agentId","Agent","agentId","OWNED_BY"),("subcat","subCategory","SubCategory","name","IN_SUBCATEGORY"),
        ("tag","tag","Tag","name","TAGGED"),("part","part","Part","name","ON_PART"),("sla","sla","SLA","name","UNDER_SLA")]:
    push(f"rel_ticket_{f}.csv", f"MATCH (t:Ticket {{ticketId:r.ticketId}}),(x:{lab} {{{prop}:r.{k}}}) MERGE (t)-[:{rel}]->(x)")
push("skills.csv", "MERGE (s:Skill {skillId:r.skillId}) SET s.name=r.name, s.theme=r.theme, s.severity=r.severity, s.owner=r.owner, s.internalSla=r.internalSla, s.escalationPath=r.escalationPath, s.fullText=r.fullText")
push("skill_steps.csv", "MATCH (s:Skill {skillId:r.skillId}) MERGE (p:SkillStep {stepId:r.stepId}) SET p.order=toInteger(r.order), p.level=toInteger(r.level), p.heading=r.heading, p.text=r.text MERGE (s)-[:HAS_STEP]->(p)")
push("rel_skill_related.csv", "MATCH (a:Skill {skillId:r.fromSkill}),(b:Skill {skillId:r.toSkill}) MERGE (a)-[:RELATED_TO]->(b)")
run("MATCH (s:SubCategory),(k:Skill {skillId:'Campaign-Management'}) MERGE (s)-[:HANDLED_BY]->(k)")
push("rel_ticket_step.csv", "MATCH (t:Ticket {ticketId:r.ticketId}),(p:SkillStep {stepId:r.stepId}),(k:Skill {skillId:r.skillId}) MERGE (t)-[m:MATCHES_STEP]->(p) SET m.confidence=r.confidence MERGE (t)-[:MATCHES_SKILL]->(k)")
push("unmatched_tickets.csv", "MATCH (t:Ticket {ticketId:r.ticketId}) SET t.noSkillMatch=true, t.noSkillReason=r.reason")
res = run("MATCH (n) RETURN labels(n)[0] AS item, count(*) AS n UNION ALL MATCH ()-[r]->() RETURN type(r) AS item, count(*) AS n")
for item, n in res["data"]["values"]: print(f"{item:16}{n}")
