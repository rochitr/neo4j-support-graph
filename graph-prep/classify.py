"""Hand-reviewed ticket -> SkillStep mapping (each of the 100 tickets read by Claude, not keyword-matched).
Writes out/rel_ticket_step.csv and out/unmatched_tickets.csv. Step ids are '<skillId>#<order>' from skill_steps.csv."""
import csv, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
CM, MF, MP, PR, PU, IN, TR, WL, SS = ("Campaign-Management", "Manual-Feed-Management", "Media-Planning-Media-Buying",
    "Performance-ROI-Investigation", "Publisher-Channel-Management", "Informational-Requests",
    "Tracking-Attribution-Investigation", "Jobs-Sponsored-Wrong-Location", "Spend-Spike-Investigation")
H, M, L = "high", "medium", "low"
# ticket number -> (skill, step order, confidence)
m = {101:(PU,6,M),102:(PU,11,M),103:(PU,11,M),104:(PR,6,M),105:(CM,5,H),107:(CM,5,H),108:(CM,4,L),109:(MP,8,L),
 110:(IN,4,H),111:(IN,8,H),112:(CM,7,L),113:(MP,3,M),114:(MP,3,M),115:(CM,7,M),116:(PU,6,M),117:(CM,7,M),118:(PU,7,L),
 119:(SS,4,L),120:(PU,5,M),121:(PR,8,L),122:(MP,8,M),123:(CM,5,H),124:(CM,5,M),125:(CM,5,H),126:(TR,5,H),127:(PU,6,M),
 128:(PU,5,H),129:(PR,8,M),130:(CM,8,H),131:(WL,4,H),132:(MP,8,H),133:(PU,7,L),134:(CM,7,M),136:(CM,7,H),137:(MP,3,M),
 138:(CM,5,H),139:(CM,5,M),140:(CM,9,M),141:(CM,7,H),142:(CM,7,M),143:(MF,1,M),144:(CM,8,M),145:(MF,6,M),146:(CM,5,M),
 147:(MP,8,M),148:(CM,5,M),149:(CM,8,M),150:(CM,5,H),151:(CM,7,M),152:(PU,5,H),153:(PU,7,M),154:(CM,7,M),155:(PR,5,M),
 156:(CM,7,L),157:(CM,7,H),158:(CM,7,H),159:(PU,5,M),161:(CM,7,H),162:(CM,7,H),164:(CM,7,H),165:(CM,7,H),166:(CM,7,H),
 167:(CM,7,H),168:(CM,7,M),169:(CM,7,M),170:(MP,4,M),171:(MP,4,M),172:(CM,7,H),173:(CM,7,L),174:(CM,7,H),175:(PU,5,M),
 176:(CM,7,H),177:(CM,7,H),178:(CM,7,H),179:(CM,7,H),180:(CM,7,H),181:(CM,7,M),182:(CM,7,H),183:(CM,7,M),184:(CM,7,L),
 185:(PU,5,M),186:(CM,7,H),187:(CM,7,M),188:(CM,5,H)}
for n in list(range(189, 201)): m[n] = (CM, 7, H)
unmatched = {106: "career-site copy updates; no Career-Site-Updates SOP exists",
             135: "acknowledgement / screening-question follow-up; no SOP",
             160: "change of email recipients; no SOP",
             163: "follow-up with no request details"}
assert set(m) | set(unmatched) == set(range(101, 201)), "every ticket must be classified"
with open(os.path.join(OUT, "rel_ticket_step.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["ticketId", "stepId", "skillId", "confidence"])
    for n, (s, o, c) in sorted(m.items()): w.writerow([f"TKT-{n}", f"{s}#{o}", s, c])
with open(os.path.join(OUT, "unmatched_tickets.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["ticketId", "reason"])
    for n, r in sorted(unmatched.items()): w.writerow([f"TKT-{n}", r])
print(len(m), "matched,", len(unmatched), "unmatched")
