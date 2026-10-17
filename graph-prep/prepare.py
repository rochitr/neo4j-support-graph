"""Prepare import-ready CSVs for the support-ticket knowledge graph.
Run: python3 -I prepare.py   (reads ../ files, writes ./out/*.csv)"""
import csv, re, os, glob
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True)

def d(s):
    s = (s or "").strip()
    return datetime.strptime(s, "%m/%d/%Y").date().isoformat() if s else ""
def f(s):
    s = (s or "").strip().replace(" days", "")
    return s
def write(name, rows, cols):
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, cols); w.writeheader(); w.writerows(rows)
    print(f"{name}: {len(rows)} rows")

# ---- tickets (xlsx is source of truth; Timeline Summary sheet is a subset of the same columns)
# NOTE: the xlsx collapses Account-ID/Owner-ID/Reported-by-email to one placeholder value; the CSV keeps the distinct ones.
with open(os.path.join(ROOT, "hackathon_support_tickets_anonymized.csv"), encoding="utf-8-sig") as fh:
    T = list(csv.DictReader(fh))

tickets, accounts, contacts, agents, subcats, tags, parts, slas = [], {}, {}, {}, {}, set(), set(), set()
rel = {k: [] for k in ["account", "contact", "owner", "subcat", "tag", "part", "sla"]}
for t in T:
    i = t["Items"]
    tickets.append({
        "ticketId": i, "title": t["Title"], "body": t["Body"], "stage": t["Stage"], "state": t["State"],
        "severity": t["Severity"], "sentiment": t["Sentiment"], "channel": t["Channel"],
        "sourceChannel": t["Source channel"], "aiResolutionStatus": t["AI Resolution Status"],
        "kbGap": str(t["Knowledge Base Gap"] == "True").lower(),
        "createdDate": d(t["Created date"]), "closeDate": d(t["Close date"]), "modifiedDate": d(t["Modified date"]),
        "weekNo": t["Week No"], "firstResponseMins": t["F Response (Mins)"], "firstResponseStatus": t["F Response Status"],
        "resolutionHrsGross": t["Resolution (Hrs)"], "resolutionHrsNet": t["Resolution Hrs Net"],
        "resolutionHrsActive": t["Resolution Hrs (Active)"], "pausedHrsCust": t["Paused Hrs (Cust)"],
        "dormantHrs": t["Dormant Hrs"], "reopens": t["Reopens"], "resolutionStatus": t["Resolution Status"],
        "workDurationDays": f(t["Work duration"]), "url": t["Ticket URL"]})
    accounts[t["Account-ID"]] = t["Account"]
    rel["account"].append({"ticketId": i, "accountId": t["Account-ID"]})
    cid = t["Reported by email"].strip().lower()
    contacts[cid] = t["Reported by"]
    rel["contact"].append({"ticketId": i, "email": cid})
    agents[t["Owner-ID"]] = t["Owner"]
    rel["owner"].append({"ticketId": i, "agentId": t["Owner-ID"]})
    subcats[t["Sub Category"]] = t["Category"]
    rel["subcat"].append({"ticketId": i, "subCategory": t["Sub Category"]})
    for g in [x.strip() for x in t["Tags"].split(",")]:
        if g and "@" not in g:            # anonymisation artefact: emails leaked into Tags
            rel["tag"].append({"ticketId": i, "tag": g}); tags.add(g)
    rel["part"].append({"ticketId": i, "part": t["Part"]}); parts.add(t["Part"])
    rel["sla"].append({"ticketId": i, "sla": t["SLA Name"]}); slas.add(t["SLA Name"])

write("tickets.csv", tickets, list(tickets[0]))
write("accounts.csv", [{"accountId": k, "name": v} for k, v in accounts.items()], ["accountId", "name"])
write("contacts.csv", [{"email": k, "name": v} for k, v in contacts.items()], ["email", "name"])
write("agents.csv", [{"agentId": k, "name": v} for k, v in agents.items()], ["agentId", "name"])
write("subcategories.csv", [{"subCategory": k, "category": v} for k, v in subcats.items()], ["subCategory", "category"])
write("tags.csv", [{"tag": g} for g in sorted(tags)], ["tag"])
write("parts.csv", [{"part": p} for p in sorted(parts)], ["part"])
write("slas.csv", [{"sla": s} for s in sorted(slas)], ["sla"])
for k, cols in [("account", ["ticketId", "accountId"]), ("contact", ["ticketId", "email"]), ("owner", ["ticketId", "agentId"]),
                ("subcat", ["ticketId", "subCategory"]), ("tag", ["ticketId", "tag"]), ("part", ["ticketId", "part"]),
                ("sla", ["ticketId", "sla"])]:
    write(f"rel_ticket_{k}.csv", rel[k], cols)

# ---- skills (markdown SOPs)
skills, steps, related, meta_keys = [], [], [], {}
for p in sorted(glob.glob(os.path.join(ROOT, "Support Skills", "*.md"))):
    text = open(p, encoding="utf-8").read(); sid = os.path.basename(p)[:-3]
    title = re.search(r"^# Skill:\s*(.+)$", text, re.M).group(1).strip()
    meta = dict(re.findall(r"^\*\*([^:*]+):\*\*\s*(.+)$", text[:text.find("\n---")], re.M))
    skills.append({"skillId": sid, "name": title, "theme": meta.get("Theme", ""), "severity": meta.get("SLA Severity", ""),
                   "owner": meta.get("Primary Owner", ""), "internalSla": meta.get("Internal SLA", ""),
                   "escalationPath": meta.get("Escalation Path", ""), "fullText": text})
    # split at ## and ### headings -> one SkillStep per section
    parts_ = re.split(r"^(#{2,3})\s+(.+)$", text, flags=re.M)
    n = 0
    for j in range(1, len(parts_), 3):
        lvl, head, body = len(parts_[j]), parts_[j + 1].strip(), parts_[j + 2].strip(" \n-")
        n += 1
        steps.append({"stepId": f"{sid}#{n}", "skillId": sid, "order": n, "level": lvl, "heading": head, "text": body})
    for m in set(re.findall(r"\[\[([^\]|#]+)", text)):
        if m != sid: related.append({"fromSkill": sid, "toSkill": m.strip()})
write("skills.csv", skills, list(skills[0]))
write("skill_steps.csv", steps, ["stepId", "skillId", "order", "level", "heading", "text"])
known = {s["skillId"] for s in skills}
write("rel_skill_related.csv", [r for r in related if r["toSkill"] in known], ["fromSkill", "toSkill"])
miss = sorted({r["toSkill"] for r in related if r["toSkill"] not in known})
print("skill links to skills that have no file:", miss)
