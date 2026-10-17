# Skill: Platform Outage Response

**Theme:** Joveo platform and product outages (full or partial)
**SLA Severity:** Severity 0
**Primary Owner:** Tech Ops
**Internal SLA:** 1 hr response | Updates every 30 min until resolved
**Escalation Path:** Tech Ops Lead → CS Manager → CS Ops Director

---

## When to Use This Skill

Use this skill when any of the following Joveo products or services becomes unavailable or significantly degraded:

- **UA / Reporting** — the Unified Analytics dashboard is inaccessible, returning errors, or showing no data.
- **Career Site** — a client's Joveo-powered career site is down, returning errors, or showing incorrect content.
- **Conversational AI** — the conversational AI product is unresponsive or producing errors for candidates.
- **AI Interviewer** — the AI Interviewer product is down; candidates may be mid-interview session.
- **AI Talent CRM** — the AI Talent CRM is inaccessible, data is missing, or workflow states are corrupted.

This skill covers both full outages (product completely unavailable) and partial outages (degraded performance, specific features non-functional, specific client accounts affected). Tech Ops owns resolution for all outages. Customer Support's role is to: confirm the outage, escalate to Tech Ops immediately, communicate with affected clients, and validate restoration.

**Do not attempt to fix platform or infrastructure issues yourself.** Your job is rapid escalation and client communication.

---

## Step 1 — Acknowledge & Set Expectation

Send within **15 minutes** of receiving the first report or detecting the issue.

> **Subject:** Re: [Product Name] Issue — [Client Name] — Investigating Now
>
> Hi [Client Name],
>
> Thank you for reporting this. I have received your report and our technical team has been alerted.
>
> We are investigating the issue with [product name] as a Severity 0 incident. I will provide you with a status update within 30 minutes, and will continue to send updates every 30 minutes until the issue is resolved.
>
> In the meantime, [if applicable: "as a precaution I have paused your active campaigns to prevent any wasted spend during the outage"].
>
> We apologize for the inconvenience and are treating this with the highest priority.
>
> Best,
> [Your Name] | Joveo Support

If you have already confirmed the outage is system-wide (affecting multiple clients), you may send a single proactive notification to all known affected clients rather than waiting for each to report individually.

---

## Step 2 — Confirm Scope: System-Wide or Isolated?

Before escalating, spend no more than **5 minutes** doing a quick scope check. Do not delay escalation to complete an exhaustive investigation.

1. Attempt to access the affected product yourself using your internal Joveo credentials.
2. Check the **internal monitoring dashboards** (Datadog, Grafana, or the equivalent tool currently used by Tech Ops — confirm the URL with your team lead).
3. Check the **Tech Ops Slack channel** (#tech-ops-alerts or equivalent). Is there already an active incident thread? If yes, add your client reports to the existing thread and follow that incident's updates.
4. Check with one or two colleagues: can they access the product? If yes, the issue may be isolated to the client's account or a specific browser/environment.
5. Determine scope:
   - **System-wide** — multiple clients affected, or internal access also fails, or Tech Ops Slack confirms an incident.
   - **Isolated to client account** — only one client affected, internal access works, no Slack alerts.
   - **Isolated to browser/environment** — client's specific browser or network, not the platform itself.

Document scope determination before proceeding.

---

## Step 3 — Escalate to Tech Ops Immediately

Regardless of scope determination, **escalate to Tech Ops now.** Do not wait to fully diagnose the issue before escalating.

Post in the Tech Ops Slack channel with the following structured message:

> **[OUTAGE ALERT — Sev 0]**
> **Product affected:** [UA / Career Site / Conversational AI / AI Interviewer / AI Talent CRM]
> **First reported:** [Time and date]
> **Scope:** [System-wide / Isolated to client / Isolated to environment]
> **Error observed:** [Exact error message, HTTP status code, or symptom description]
> **Affected clients:** [Client name(s) and account IDs]
> **Reported by:** [Your name]

If no Tech Ops team member acknowledges within **10 minutes**, escalate by direct message to the **Tech Ops Lead** and simultaneously notify the **CS Manager**.

---

## Step 4 — Product-Specific Diagnostic Checks

While Tech Ops investigates, run the product-specific checks appropriate for the affected product. These checks are not fixes — they provide additional data to hand off to Tech Ops and help you understand the scope of client impact.

### UA / Reporting Down

- Attempt to load the UA dashboard in an incognito browser window (to rule out caching).
- Check whether the dashboard loads but shows no data, or fails to load entirely. Note the distinction — "loads but empty" suggests a data pipeline issue; "fails to load" suggests a UI/infrastructure issue.
- Check whether historical data (prior to the outage window) is still visible, or whether all data has disappeared.
- Note the approximate time window affected based on when data last appeared correctly.
- Document: is the issue specific to one client account, or does it affect all accounts you can access?

### Career Site Down

- Attempt to load the client's career site URL in a fresh browser session.
- Note the exact error: 404, 500, SSL error, timeout, or blank page.
- Check DNS resolution: perform a DNS lookup for the career site domain to confirm it is resolving to the expected IP address.
- Check the SSL certificate: confirm it has not expired or been revoked (most browsers will show a warning if so).
- Check whether the career site was working earlier today. If yes, ask the client: were any changes made to the site recently (new deployment, domain change, DNS record change)?
- Note whether this affects the live candidate-facing career site, the admin portal, or both.

### Conversational AI Down

- Attempt to interact with the Conversational AI interface if accessible to you.
- Note the error type: no response, error message from the AI, authentication failure, or infinite loading.
- Check whether the issue is affecting all candidate interactions or only specific conversation flows.
- Check with Tech Ops: are there any upstream NLP API dependencies (e.g., third-party AI service providers) with known outages?
- Check upstream authentication services — if SSO or OAuth is involved, confirm auth services are operational.

### AI Interviewer Down

- Confirm whether the AI Interviewer is fully unavailable or only partially degraded (e.g., audio works but transcript fails).
- **Immediately assess:** Are any candidates currently mid-interview when the outage occurred? If yes:
  - Collect their names, email addresses, and the time their sessions were interrupted.
  - Flag this to Tech Ops as a **candidate experience priority** — these candidates may need to be rescheduled.
  - Notify the CSM so they can communicate with the client about impacted candidates.
- Document: which client(s) are affected, and whether the outage occurred during an active hiring campaign with scheduled interview slots.

### AI Talent CRM Down

- Attempt to access the CRM interface.
- If partially accessible, check whether: candidate profiles are loading, workflow stages are displaying correctly, and no records appear deleted or duplicated.
- **Data integrity check:** If the CRM was mid-operation during the outage (e.g., a bulk workflow action was in progress), flag to Tech Ops that data integrity validation is needed before restoration is declared complete.
- Confirm with Tech Ops: no candidate data or workflow states were corrupted or lost.
- Do not advise clients to make any CRM changes until Tech Ops confirms data integrity.

---

## Step 5 — Client Communication During Outage

**Send a status update every 30 minutes** from the time of acknowledgment until the issue is resolved. Do not wait for clients to follow up — proactive communication is essential during a Sev 0 incident.

> **Subject:** [Product Name] Issue — Status Update — [HH:MM]
>
> Hi [Client Name],
>
> This is a status update on the [product name] issue first reported at [time].
>
> **Current Status:** Our technical team is actively investigating. [If known: "The root cause has been identified as [brief description] and the team is working on a fix."]
>
> **Impact:** [Brief description of current impact, e.g., "UA dashboard is unavailable for all users."]
>
> **Next Update:** I will send another update at [time + 30 min] or sooner if there is a resolution.
>
> We apologize for the disruption and are working to resolve this as quickly as possible.
>
> Best,
> [Your Name] | Joveo Support

---

## Step 6 — Post-Restoration Validation

**Do not send a resolution message until you have personally confirmed the product is operational.** Do not rely solely on Tech Ops confirmation — validate yourself.

For each product, complete the following before declaring the incident resolved:

| Product | Validation Steps |
|---|---|
| UA / Reporting | Log in and confirm the dashboard loads. Verify data is populating correctly for the current day and prior day. Confirm no data gaps in the outage window. |
| Career Site | Load the career site URL in a fresh browser. Confirm pages render, job listings display, and the apply flow is accessible. Confirm SSL certificate is valid. |
| Conversational AI | Initiate a test conversation. Confirm the AI responds correctly through at least 3 conversational turns. |
| AI Interviewer | Confirm the interview interface is accessible. If candidates were interrupted, confirm with the client and Tech Ops that a rescheduling or session recovery plan is in place. |
| AI Talent CRM | Log in and confirm candidate profiles, workflow stages, and historical data are intact. Confirm with Tech Ops that a data integrity check has been completed. |

---

## Step 7 — Post-Resolution Message

Send only after validation in Step 6 is complete.

> **Subject:** Resolved: [Product Name] is Now Operational — [Client Name]
>
> Hi [Client Name],
>
> I'm pleased to confirm that [product name] has been fully restored and is now operational as of [resolution time].
>
> **Summary of Incident:**
> - **Outage began:** [Start time]
> - **Resolved at:** [Resolution time]
> - **Total duration:** [Duration]
> - **Root cause:** [Brief non-technical description once available from Tech Ops — e.g., "A database configuration change caused the reporting pipeline to stop processing incoming data."]
>
> **Actions Taken:** [Brief summary of what Tech Ops did to restore service]
>
> **Impact to Your Account:** [E.g., "Your UA dashboard was unavailable for approximately 2 hours. Historical data for this period has been backfilled and should now be visible." Or: "Your career site was down for 45 minutes during off-peak hours. No active candidate sessions were impacted."]
>
> [If applicable: "We are initiating a post-incident review and will share any relevant findings or preventive measures with you."]
>
> We sincerely apologize for the disruption. Please reach out if you have any further questions or if you notice any residual issues.
>
> Best,
> [Your Name] | Joveo Support

---

## Escalation Triggers

These conditions require **immediate escalation** — do not wait for Tech Ops to respond on their own timeline:

- **AI Interviewer is down and candidates are actively mid-session** → Page the Tech Ops Lead immediately. This is the highest priority sub-scenario within platform outages due to direct candidate experience impact.
- **Career site is down and the client has active job campaigns running** → In addition to escalating to Tech Ops, pause the affected campaigns in MOJO immediately to prevent spend on a broken destination. See [[Campaign-Management]].
- **UA is down during a scheduled client exec review or QBR** → Notify CSM immediately so they can manage client expectations and potentially reschedule or present data from exports.
- **Tech Ops does not acknowledge within 10 minutes of escalation** → Direct message Tech Ops Lead and notify CS Manager.
- **Outage affects more than 3 clients simultaneously** → Notify CS Ops Director and prepare a templated proactive outreach for all affected accounts.
- **Data corruption suspected in AI Talent CRM** → Do not allow any CRM activity until Tech Ops completes a data integrity check. Escalate to Tech Ops Lead immediately.
- **Outage has not been resolved within 2 hours** → CS Ops Director must be informed and client-facing CSMs must be looped in for escalation communication.

Escalation path: **Tech Ops Lead → CS Manager → CS Ops Director**

---

## Related Skills

- [[UA-Reporting-Discrepancy]] — Use when UA is restored after an outage but data appears incorrect, missing, or inconsistent; post-outage data gaps are common and require separate investigation.
- [[Career-Site-Updates]] — Use for post-outage career site verification, particularly to confirm content, job listings, and apply flows are fully intact after restoration.
- [[Inbound-Feed-Jobs-Down]] — Use if the career site outage has affected job display or if jobs are not appearing on the career site following restoration.
- [[Campaign-Management]] — Use to pause active campaigns when a career site outage is confirmed, and to resume campaigns after restoration is validated.

---

*Last updated: June 2026 | Owner: Support Ops*
