# Skill: Tracking & Attribution Investigation

**Theme:** Tracking & Attribution  
**SLA Severity:** Severity 0 / Severity 1 (depending on scope)  
**Primary Owner:** Tracking & Analytics Engineering / Data Science  
**Internal SLA:** Response 1 hr | Resolution 2–4 hr  
**Escalation Path:** Customer Support → Customer Support Manager → CSE → CSM → CS Ops Director

---

## When to Use This Skill

Trigger this skill when a client reports **any** of the following:
- Pixel not firing / conversion events missing
- UTM tags incorrect or not passing through
- Click/apply counts in Joveo don't match client's internal system or publisher dashboard
- Funnel data (Click → Apply → Hire) showing gaps or zeros
- Cookieless tracking setup needed or broken
- Source attribution wrong (candidates attributed to wrong channel)

> ⚠️ **Connected Skills:** If the client's report is specifically about numbers in the UA dashboard looking wrong, start with [[UA-Reporting-Discrepancy]] first — it will route here if the root cause is tracking.

---

## Step 1 — Acknowledge & Set Expectation

Send immediately on ticket receipt:

```
Hi [Client Name],

Thank you for flagging this. We've received your report of a [tracking/attribution discrepancy] and are investigating immediately.

Our team will review the pixel setup, UTM parameters, and data pipeline to identify the root cause. We'll have an update within 1 hour.

Regards,
[CSE Name] | Joveo Customer Support
```

---

## Step 2 — Confirm the Scope

Before diagnosing, answer these questions:

| Question | Where to Check |
|---|---|
| Which channel(s) are affected? | MOJO → Campaign → Publisher Breakdown |
| What date range shows the discrepancy? | Client's report vs. UA date filter |
| Is it all jobs or specific Req IDs? | MOJO → Jobs tab, filter by Req ID |
| Is pixel-based or UTM-based tracking in use? | Client onboarding docs / MOJO Settings |
| Is the client using cookieless setup? | MOJO → Tracking Settings |

---

## Step 3 — Diagnose the Root Cause

Work through each check in order. Stop at the first confirmed failure.

### 3a. Pixel / Conversion Tracking
1. Open the client's apply URL in a browser with network inspector open.
2. Confirm the Joveo pixel fires on the confirmation page (look for a `joveo.com/track` or `mojotrk` call).
3. If pixel is missing: check if it was removed during a career site update → escalate to Career Site team.
4. If pixel fires but data is missing in UA: check if the `req_id` and `source` parameters are populated in the pixel call.

### 3b. UTM Parameters
1. Pull 5 sample apply URLs from the affected publisher's feed in MOJO.
2. Verify UTM tags are present: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`.
3. If UTMs are missing or malformed: check the campaign's Target URL template in MOJO → Campaign Settings.
4. Common failure: client changed their ATS apply URL and the UTM append logic broke. Fix the Target URL template.

### 3c. Funnel Data Gaps (Click → Apply → Hire)
1. In MOJO UA, pull funnel report for the affected date range.
2. Identify the stage where the drop-off is abnormal (>80% drop at any single stage is suspect).
3. If **Click → Apply** gap: likely a pixel or redirect issue. Go to 3a.
4. If **Apply → Hire** gap: likely an ATS integration issue. → Hand off to [[ATS-Integration-Triage]] *(link to that skill when created)*.

### 3d. Cookieless / Cross-Domain Attribution
1. Confirm whether the client's career site and apply page are on different domains.
2. If yes: verify the cookieless tracking snippet is deployed on both domains.
3. Check that the `client_id` parameter is being passed in the redirect chain.
4. If not: coordinate with Career Site / TAO team for snippet deployment.

---

## Step 4 — Fix or Escalate

| Root Cause Found | Action |
|---|---|
| UTM template broken in MOJO | Fix the Target URL template directly in MOJO → notify client |
| Pixel missing from career site | Raise internal ticket to Career Site / TAO team with pixel code and placement instructions |
| ATS not passing source param | Raise ticket to Integrations squad with affected Req IDs and ATS name |
| Cookieless snippet not deployed | Coordinate TAO deployment — set client expectation of 1–2 business days |
| Cannot identify root cause within 2 hr | Escalate to CSE + Analytics Engineering with full diagnostic notes |

---

## Step 5 — Post-Resolution Message

```
Hi [Client Name],

We've identified and resolved the tracking issue affecting [channel/date range].

Root cause: [e.g., "The UTM template on the Indeed campaign was missing the utm_content parameter following a Target URL update on [date]. This caused applies from Indeed to not be attributed correctly in your dashboard."]

Actions taken:
- [e.g., "Corrected the Target URL template in MOJO for all active Indeed campaigns."]
- [e.g., "Verified pixel is firing correctly on 5 sample applications."]

Data impact: [e.g., "Applies from [date] to [date] may be under-reported by approximately X. We recommend cross-referencing with your ATS for that window."]

Please let us know if you have any questions.

Regards,
[CSE Name] | Joveo Customer Support
```

---

## Escalation Triggers

Escalate immediately (do not wait for the 2-hr window) if:
- Tracking has been broken for **more than 24 hours** before being reported
- The discrepancy affects **budget/billing** calculations → also loop in Finance
- The client is a Sev-0 account (e.g., Amazon, CVS Health, Tenet Healthcare)
- The issue involves a **cookieless rollout** blocking a go-live date

---

## Related Skills

- [[UA-Reporting-Discrepancy]] — Start here if the complaint is "numbers look wrong in the dashboard"
- [[Spend-Discrepancy-Investigation]] *(coming soon)* — If the tracking issue is causing spend to be misreported
- [[ATS-Integration-Triage]] *(coming soon)* — If Apply → Hire data gap points to ATS sync failure
- [[Career-Site-Down]] *(coming soon)* — If pixel is missing because the career site itself had a deployment

---

*Last updated: June 2026 | Owner: Support Ops*
