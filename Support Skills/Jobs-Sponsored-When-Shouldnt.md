# Skill: Jobs Sponsored When They Shouldn't Be

**Theme:** Jobs being actively sponsored that should not be (closed, filled, out-of-scope, or erroneously included)
**SLA Severity:** Severity 0
**Primary Owner:** CSE / Ad Ops
**Internal SLA:** 1 hr response
**Escalation Path:** CS Manager → CSM → CSD → CS Ops Director

---

## When to Use This Skill

Use this skill when:
- A client reports that specific jobs are being sponsored on publishers but those jobs should not be active (e.g., the position has been filled, the req has been closed, the role was cancelled).
- A client reports that jobs they did not intend to sponsor are appearing on job boards.
- Internal monitoring detects spend on jobs that are flagged as closed or inactive in the client's ATS.
- A client reports that a large number of unexpected jobs were activated — possibly due to a bulk action.

This is a Severity 0 issue because erroneous sponsorship directly wastes client budget on jobs that will generate no valid hires, and can damage employer brand if candidates apply to filled or non-existent roles. The priority upon identifying the issue is **immediate pause** — do not delay pausing while investigating root cause.

---

## Step 1 — Acknowledge & Set Expectation

Send within **15 minutes** of receiving the report.

> **Subject:** Re: Jobs Incorrectly Being Sponsored — [Client Name] — Investigating Now
>
> Hi [Client Name],
>
> Thank you for flagging this immediately. I've received your report and I am investigating which jobs are being sponsored incorrectly and why.
>
> This is a Severity 0 issue. My first step is to pause the affected jobs in our system to stop any ongoing spend while I investigate the root cause.
>
> I will send you a full status update within 1 hour.
>
> To help me act as quickly as possible, please confirm:
> 1. The specific Req IDs or job titles that should NOT be sponsored.
> 2. The reason they should not be active (e.g., filled, closed, cancelled, wrong campaign).
> 3. The publisher(s) where you've observed them appearing (if known).
>
> Best,
> [Your Name] | Joveo Support

---

## Step 2 — Pause Immediately

**This step must happen before any further diagnosis.** If jobs are actively spending on a publisher, every minute of delay increases erroneous spend.

1. Log into MOJO immediately.
2. Locate the affected jobs by Req ID or job title (use the list provided by the client, or use MOJO's job search to identify candidates).
3. **Pause the jobs or their parent campaigns/job groups in MOJO.** If the scope is unclear, pause the campaign level to be safe — you can resume specific jobs once the investigation is complete.
4. Confirm in MOJO that the jobs are in a paused state.
5. Note the exact **pause timestamp** — this is needed for erroneous spend calculation.
6. Notify the client that pausing is in progress.

---

## Step 3 — Diagnose / Execute

After pausing, investigate the root cause. Work through each check in sequence.

**3-1. Confirm the jobs that should not be sponsored**
- Cross-reference the Req IDs provided by the client against the MOJO job list.
- For each Req ID, confirm:
  - Current status in MOJO (active, paused, inactive)
  - Current status in the client's ATS (open, filled, closed, cancelled)
  - Which publisher(s) the jobs appeared on and for how long

**3-2. Check the inbound feed**
- Retrieve the current inbound feed for the client.
- Check whether the affected Req IDs are **still present in the feed**.
  - If they are still in the feed → the client's ATS has not removed them. The ATS is still publishing these jobs as active. The feed is the source of the problem.
  - If they are no longer in the feed → the jobs were recently removed from the ATS but Joveo has not yet processed the removal, or there is a delay in deactivation propagation.
- Note: Joveo ingests the feed periodically. If a job was removed from the ATS very recently, there may be a short lag before MOJO reflects the closure.

**3-3. Check campaign and job group assignment**
- In MOJO, review which campaign(s) and job group(s) the affected jobs are assigned to.
- Were these jobs added to a campaign they should not be in? Review the campaign's job inclusion rules (e.g., keyword filters, job family tags, location filters) — could those rules be inadvertently matching jobs that should be excluded?
- Check the campaign's change log for the past 48–72 hours. Were any new inclusion rules added, or were job groups modified to include a broader set of reqs?

**3-4. Check for bulk actions**
- Review the MOJO account-level change log for bulk actions in the past 48–72 hours.
- Look for: bulk campaign activation, bulk job group changes, bulk feed rule modifications, or bulk sponsorship triggers.
- If a bulk action was applied incorrectly and activated jobs that should not be sponsored → document the change log entry, the user who made the change, and the timestamp.

**3-5. Check ATS closure propagation**
- If the client states the jobs were closed/filled in the ATS, confirm:
  - When were they marked closed/filled in the ATS?
  - Is the ATS configured to automatically remove closed jobs from the Joveo feed endpoint?
  - Is there a known delay in the ATS-to-feed propagation for this client?
- Some ATS platforms have a lag of several hours between a job being closed and being removed from the feed. This is a systemic issue that should be flagged to the client for ATS configuration review. See [[ATS-Integration-Triage]].

**3-6. Verify no recurrence risk**
- Once root cause is identified, assess: are there other jobs in the same situation?
  - Other closed/filled reqs still in the feed?
  - Other jobs assigned to incorrect campaigns?
  - Other jobs that might be activated by the same erroneous bulk action?
- Proactively identify and pause any additional at-risk jobs before they generate further spend.

---

## Step 4 — Fix or Escalate

| Root Cause | Action | Owner |
|---|---|---|
| Jobs closed/filled in ATS but still present in feed | Notify client immediately: their ATS is not removing closed jobs from the Joveo feed. Request that client's ATS/IT team remove the jobs from the feed endpoint and verify ATS closure propagation is working. See [[ATS-Integration-Triage]]. | Customer Support → Client ATS Team |
| Jobs added to wrong campaign via incorrect inclusion rules | Fix the campaign's job inclusion rules in MOJO to exclude the affected jobs. Remove affected jobs from campaign assignment. Review similar campaigns for the same rule error. | CSE / Ad Ops |
| Bulk action applied incorrectly (wrong jobs activated) | Reverse the bulk action in MOJO. Restore prior campaign/job group state. Document the bulk change log entry. Identify all jobs affected by the erroneous bulk action, not just the ones the client reported. | CSE / Ad Ops |
| ATS closure-to-feed delay is too long | Flag as systemic to client. Recommend ATS configuration change to reduce propagation delay. Short-term: manually deactivate in MOJO. Long-term: work with client's ATS team. See [[ATS-Integration-Triage]]. | Customer Support → Client ATS Team |
| Jobs mistakenly included due to a feed rule or tag error | Identify and correct the incorrect rule or tag. Confirm the affected jobs are excluded from sponsorship. | CSE / Ad Ops |
| Root cause unknown after all checks | Escalate to Tech Ops with full evidence: affected Req IDs, feed status, MOJO campaign assignment, change log. | Escalate to Tech Ops |

**After implementing the fix:**
1. Confirm the affected jobs remain paused or are fully removed from active distribution.
2. Verify the fix prevents recurrence (e.g., if ATS closes a job tomorrow, will it be removed from the feed promptly?).
3. Calculate erroneous spend: pull spend data for the affected Req IDs from the erroneous period. Document the total.

---

## Step 5 — Post-Resolution Message

Send once all incorrectly sponsored jobs are confirmed paused/removed and root cause is resolved.

> **Subject:** Resolved: Erroneous Sponsorship Stopped — [Client Name]
>
> Hi [Client Name],
>
> I can confirm that the following jobs have been paused and are no longer being sponsored:
>
> [List of affected Req IDs / job titles]
>
> **Root Cause:** [E.g., "These jobs were marked as filled in your ATS on [date], but due to a delay in your ATS feed propagation, they remained active in your Joveo inbound feed and continued to be sponsored. We have deactivated them manually in MOJO and your ATS team has confirmed the feed has been updated."]
>
> **Actions Taken:**
> - Paused affected jobs in MOJO at [timestamp] to stop erroneous spend.
> - [Root cause fix action]
> - [Preventive action, if applicable]
>
> **Erroneous Spend:** Estimated spend on these jobs during the erroneous period ([date range]) is approximately $[amount]. This has been documented and flagged to our Finance and Client Success teams for review.
>
> We recommend [any preventive recommendation, e.g., "ensuring your ATS is configured to remove jobs from the feed within 1 hour of closure"]. We can assist your ATS team with this if needed.
>
> Please let us know if any other jobs appear to be incorrectly sponsored.
>
> Best,
> [Your Name] | Joveo Support

---

## Escalation Triggers

Escalate immediately (do not wait for the response window) if any of the following are true:

- **You cannot pause the affected jobs in MOJO** — platform access or permissions issue; escalate to CS Manager and Tech Ops simultaneously.
- **Erroneous sponsorship has been ongoing for more than 24 hours** — financial impact may be significant; escalate to CSM and document erroneous spend immediately.
- **The bulk action that caused the issue affected more than 50 jobs or more than one client account** — possible systemic error; escalate to CS Ops Director.
- **Root cause cannot be identified within 45 minutes** — escalate to CSE and CS Manager.
- **Erroneous spend calculation exceeds $1,000** — notify Finance and CSM immediately regardless of whether root cause has been found.
- **Client is threatening chargeback or escalating externally** — loop in CSM immediately.

Escalation path: **CS Manager → CSM → CSD → CS Ops Director**

When escalating, always include: affected Req IDs, pause timestamp, estimated erroneous spend, feed status (jobs still in feed or not), campaign assignment, and change log evidence.

---

## Related Skills

- [[ATS-Integration-Triage]] — Use when the root cause is that the client's ATS is not removing closed/filled jobs from the Joveo feed endpoint in a timely manner; the fix requires ATS-side configuration changes.
- [[Inbound-Feed-Jobs-Down]] — Use for context on feed behavior and ingestion mechanics; also useful if investigating whether feed removal delays are part of a broader feed health issue.
- [[Spend-Spike-Investigation]] — Use if the erroneous sponsorship has resulted in a significant budget spike; the two skills may need to be run in parallel.
- [[Campaign-Management]] — Use if the root cause is a campaign or job group misconfiguration that caused the wrong jobs to be included in an active campaign.

---

*Last updated: June 2026 | Owner: Support Ops*
