CREATE CONSTRAINT ticket_id IF NOT EXISTS FOR (n:Ticket) REQUIRE n.ticketId IS UNIQUE;
CREATE CONSTRAINT account_id IF NOT EXISTS FOR (n:Account) REQUIRE n.accountId IS UNIQUE;
CREATE CONSTRAINT contact_email IF NOT EXISTS FOR (n:Contact) REQUIRE n.email IS UNIQUE;
CREATE CONSTRAINT agent_id IF NOT EXISTS FOR (n:Agent) REQUIRE n.agentId IS UNIQUE;
CREATE CONSTRAINT subcat_name IF NOT EXISTS FOR (n:SubCategory) REQUIRE n.name IS UNIQUE;
CREATE CONSTRAINT category_name IF NOT EXISTS FOR (n:Category) REQUIRE n.name IS UNIQUE;
CREATE CONSTRAINT tag_name IF NOT EXISTS FOR (n:Tag) REQUIRE n.name IS UNIQUE;
CREATE CONSTRAINT part_name IF NOT EXISTS FOR (n:Part) REQUIRE n.name IS UNIQUE;
CREATE CONSTRAINT sla_name IF NOT EXISTS FOR (n:SLA) REQUIRE n.name IS UNIQUE;
CREATE CONSTRAINT skill_id IF NOT EXISTS FOR (n:Skill) REQUIRE n.skillId IS UNIQUE;
CREATE CONSTRAINT step_id IF NOT EXISTS FOR (n:SkillStep) REQUIRE n.stepId IS UNIQUE;

LOAD CSV WITH HEADERS FROM 'file:///tickets.csv' AS r
MERGE (t:Ticket {ticketId: r.ticketId})
SET t.title=r.title, t.body=r.body, t.stage=r.stage, t.state=r.state, t.severity=r.severity,
    t.sentiment=nullIf(r.sentiment,''), t.channel=r.channel, t.sourceChannel=nullIf(r.sourceChannel,''),
    t.aiResolutionStatus=nullIf(r.aiResolutionStatus,''), t.kbGap=(r.kbGap='true'),
    t.createdDate=date(r.createdDate), t.closeDate=CASE r.closeDate WHEN '' THEN null ELSE date(r.closeDate) END,
    t.modifiedDate=date(r.modifiedDate), t.weekNo=r.weekNo,
    t.firstResponseMins=toFloat(r.firstResponseMins), t.firstResponseStatus=r.firstResponseStatus,
    t.resolutionHrsGross=toFloat(nullIf(r.resolutionHrsGross,'')), t.resolutionHrsNet=toFloat(nullIf(r.resolutionHrsNet,'')),
    t.resolutionHrsActive=toFloat(r.resolutionHrsActive), t.pausedHrsCust=toFloat(r.pausedHrsCust),
    t.dormantHrs=toFloat(r.dormantHrs), t.reopens=toInteger(r.reopens), t.resolutionStatus=r.resolutionStatus,
    t.workDurationDays=toFloat(nullIf(r.workDurationDays,'')), t.url=r.url;

LOAD CSV WITH HEADERS FROM 'file:///accounts.csv' AS r MERGE (n:Account {accountId:r.accountId}) SET n.name=r.name;
LOAD CSV WITH HEADERS FROM 'file:///contacts.csv' AS r MERGE (n:Contact {email:r.email}) SET n.name=r.name;
LOAD CSV WITH HEADERS FROM 'file:///agents.csv' AS r MERGE (n:Agent {agentId:r.agentId}) SET n.name=r.name;
LOAD CSV WITH HEADERS FROM 'file:///subcategories.csv' AS r
MERGE (s:SubCategory {name:r.subCategory}) MERGE (c:Category {name:r.category}) MERGE (s)-[:IN_CATEGORY]->(c);
LOAD CSV WITH HEADERS FROM 'file:///tags.csv' AS r MERGE (:Tag {name:r.tag});
LOAD CSV WITH HEADERS FROM 'file:///parts.csv' AS r MERGE (:Part {name:r.part});
LOAD CSV WITH HEADERS FROM 'file:///slas.csv' AS r MERGE (:SLA {name:r.sla});

LOAD CSV WITH HEADERS FROM 'file:///rel_ticket_account.csv' AS r MATCH (t:Ticket {ticketId:r.ticketId}),(x:Account {accountId:r.accountId}) MERGE (t)-[:FOR_ACCOUNT]->(x);
LOAD CSV WITH HEADERS FROM 'file:///rel_ticket_contact.csv' AS r MATCH (t:Ticket {ticketId:r.ticketId}),(x:Contact {email:r.email}) MERGE (t)-[:REPORTED_BY]->(x);
LOAD CSV WITH HEADERS FROM 'file:///rel_ticket_owner.csv' AS r MATCH (t:Ticket {ticketId:r.ticketId}),(x:Agent {agentId:r.agentId}) MERGE (t)-[:OWNED_BY]->(x);
LOAD CSV WITH HEADERS FROM 'file:///rel_ticket_subcat.csv' AS r MATCH (t:Ticket {ticketId:r.ticketId}),(x:SubCategory {name:r.subCategory}) MERGE (t)-[:IN_SUBCATEGORY]->(x);
LOAD CSV WITH HEADERS FROM 'file:///rel_ticket_tag.csv' AS r MATCH (t:Ticket {ticketId:r.ticketId}),(x:Tag {name:r.tag}) MERGE (t)-[:TAGGED]->(x);
LOAD CSV WITH HEADERS FROM 'file:///rel_ticket_part.csv' AS r MATCH (t:Ticket {ticketId:r.ticketId}),(x:Part {name:r.part}) MERGE (t)-[:ON_PART]->(x);
LOAD CSV WITH HEADERS FROM 'file:///rel_ticket_sla.csv' AS r MATCH (t:Ticket {ticketId:r.ticketId}),(x:SLA {name:r.sla}) MERGE (t)-[:UNDER_SLA]->(x);

LOAD CSV WITH HEADERS FROM 'file:///skills.csv' AS r
MERGE (s:Skill {skillId:r.skillId})
SET s.name=r.name, s.theme=r.theme, s.severity=r.severity, s.owner=r.owner, s.internalSla=r.internalSla,
    s.escalationPath=r.escalationPath, s.fullText=r.fullText;
LOAD CSV WITH HEADERS FROM 'file:///skill_steps.csv' AS r
MATCH (s:Skill {skillId:r.skillId})
MERGE (p:SkillStep {stepId:r.stepId}) SET p.order=toInteger(r.order), p.level=toInteger(r.level), p.heading=r.heading, p.text=r.text
MERGE (s)-[:HAS_STEP]->(p);
LOAD CSV WITH HEADERS FROM 'file:///rel_skill_related.csv' AS r
MATCH (a:Skill {skillId:r.fromSkill}),(b:Skill {skillId:r.toSkill}) MERGE (a)-[:RELATED_TO]->(b);

MATCH (s:SubCategory),(k:Skill {skillId:'Campaign-Management'}) MERGE (s)-[:HANDLED_BY]->(k);

// ---- step-level links (classify.py; every ticket individually reviewed)
LOAD CSV WITH HEADERS FROM 'file:///rel_ticket_step.csv' AS r
MATCH (t:Ticket {ticketId:r.ticketId}),(p:SkillStep {stepId:r.stepId}),(k:Skill {skillId:r.skillId})
MERGE (t)-[m:MATCHES_STEP]->(p) SET m.confidence=r.confidence
MERGE (t)-[:MATCHES_SKILL]->(k);
LOAD CSV WITH HEADERS FROM 'file:///unmatched_tickets.csv' AS r
MATCH (t:Ticket {ticketId:r.ticketId}) SET t.noSkillMatch=true, t.noSkillReason=r.reason;
