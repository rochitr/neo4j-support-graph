# Skill: Spend Spike Investigation

**Theme:** Abnormal spend spike on client campaigns
**SLA Severity:** Severity 0
**Primary Owner:** Customer Support
**Internal SLA:** 1 hr response | 2 hr resolution
**Escalation Path:** CS Manager → CSE → CSM → CS Ops Director

---

## When to Use This Skill

Use this skill when:
- A client reports that their spend is significantly higher than expected for a given day, week, or month.
- Internal monitoring flags a campaign or account exceeding its budget threshold.
- Finance or a CSM alerts Support to an overspend situation requiring immediate investigation.
- A client's monthly budget has been exhausted unusually early.

This is a Severity 0 issue. Erroneous spend directly impacts client trust and financial liability. Begin triage immediately upon receipt. If the spike is **ongoing and actively spending**, your first action after acknowledging is to **pause the affected campaigns** — do not wait until you have identified root cause.

---

## Step 1 — Acknowledge & Set Expectation

Send within **15 minutes** of receiving the report.

> **Subject:** Re: Spend Spike — [Client Name] — Investigating Now
>
> Hi [Client Name],
>
> Thank you for bringing this to our attention. I've received your report and have begun investigating the abnormal spend activity on your account immediately.
>
> This is being treated as a Severity 0 issue. Our target resolution time is within 2 hours.
>
> As a precautionary first step, I am reviewing whether any campaigns need to be paused to prevent further erroneous spend while I investigate the root cause. I will provide a full update within 1 hour.
>
> If you can share the specific time window, campaign names, or spend figures you're seeing, it will help me investigate faster.
>
> Best,
> [Your Name] | Joveo Support

---

## Step 2 — Classify: Confirm Scope of the Spike

Before diagnosing root cause, establish the full picture of the spike. Do this immediately — do not skip even if the root cause seems obvious.

1. Log into **MOJO UA** (Unified Analytics). Pull the spend report for the affected client account.
2. Set the date range to cover: today, yesterday, and the past 7 days for trend context.
3. Break down spend by:
   - **Campaign** — which campaign(s) show abnormal spend?
   - **Job Group** — is a specific job group driving the spike?
   - **Publisher** — which publisher(s) account for the majority of the spike?
4. Compare the abnormal spend figure against:
   - The client's **daily budget cap**
   - The client's **monthly budget cap**
   - The same period in prior weeks (week-over-week comparison)
5. Determine: Is the spike still **actively occurring** right now, or is it a historical spike that has already stopped?

**If actively occurring → proceed to Step 3, but pause affected campaigns immediately before continuing diagnosis.**

---

## Step 3 — Diagnose / Execute

Work through each check in sequence. Document all findings.

**3-1. Check budget cap configuration**
- In MOJO, open the affected campaign(s). Review:
  - Daily budget cap — is it set? Is it set to the correct amount?
  - Monthly budget cap — is it set? Is it set to the correct amount?
- Check the **change log** for the campaign. Has any budget cap been recently modified, removed, or set to an abnormally high value?
- If a cap is missing or was recently removed → this is likely the root cause.

**3-2. Check publisher-level data**
- In MOJO UA, drill into the publisher breakdown for the spike period.
- Identify which publisher is responsible for the majority of the spend increase.
- Compare the publisher's CPC and click volume during the spike vs. prior periods. Is the CPC elevated? Is click volume unusually high?
- Cross-reference with any publisher-side notifications or rate change announcements.

**3-3. Check for recent bulk changes**
- Review the MOJO change log for the account for the 48 hours prior to the spike beginning.
- Look for: bulk bid changes, bulk budget changes, bulk campaign activations, job group additions that removed spending limits.
- If a bulk action was applied incorrectly → this is likely the root cause.

**3-4. Check for job groups or campaigns with no daily limit**
- Review all active job groups within the affected campaigns.
- Confirm each job group has an appropriate daily spend limit configured.
- A job group with no daily limit can exhaust budget very quickly, especially on high-traffic publishers.

**3-5. Assess publisher overbilling**
- Compare MOJO's recorded spend against any publisher-provided spend reports (if available).
- If MOJO records significantly more spend than expected but publisher data does not show a corresponding traffic increase → possible publisher overbilling.
- If MOJO spend and publisher data are consistent but the total is unexpectedly high → likely a configuration issue, not overbilling.

**3-6. Check for reporting discrepancy**
- Confirm whether the spend is real or a reporting artifact. If the UA dashboard shows a spike but campaign spend logs do not corroborate → may be a reporting issue rather than actual overspend. See [[UA-Reporting-Discrepancy]] and [[Tracking-Attribution-Investigation]] for further triage.

---

## Step 4 — Fix or Escalate

**If the spike is ongoing: pause affected campaigns NOW if not already done.**

| Root Cause | Action | Owner |
|---|---|---|
| Budget cap missing or removed | Add/restore correct daily and monthly budget caps in MOJO immediately. Resume campaigns only after caps are confirmed. Notify CSM of the gap period. | Customer Support |
| Budget cap set too high (incorrect value) | Correct the cap in MOJO. Document who made the change and when. | Customer Support |
| High-CPC publisher receiving disproportionate traffic | Adjust publisher-level bid or budget allocation. Consider publisher-level daily cap. Notify CSM. | Customer Support / Ad Ops |
| Job group with no daily limit activated | Add a daily spend limit to the job group. Review all other job groups for the same gap. | Customer Support |
| Erroneous bulk change | Reverse the bulk change in MOJO. Restore prior configuration. Document the change log entry that caused the issue. | Customer Support |
| Publisher overbilling | Pause publisher campaign. Raise a formal dispute with the publisher including date range, MOJO spend data, and discrepancy amount. Escalate to CSM. | Customer Support → CSM → Publisher |
| MOJO bug (caps not being enforced despite correct config) | Escalate to Tech Ops immediately. Provide cap configuration screenshots and spend log evidence. | Escalate to Tech Ops |
| Reporting discrepancy only (no real overspend) | Follow [[UA-Reporting-Discrepancy]] or [[Tracking-Attribution-Investigation]] as appropriate. Do not flag as overspend to Finance until confirmed. | Customer Support |

**Finance/CSM notification threshold:** If actual overspend exceeds the client's monthly budget by any amount, or if total erroneous spend exceeds $500, notify the CSM and Finance team immediately with: client name, affected campaigns, date range, overspend amount, and root cause summary.

---

## Step 5 — Post-Resolution Message

Send once the spike has stopped, root cause is confirmed, and corrective action is in place.

> **Subject:** Resolved: Spend Spike Investigation — [Client Name]
>
> Hi [Client Name],
>
> I have completed the investigation into the abnormal spend activity on your account. Here is a summary:
>
> **Root Cause:** [E.g., "The daily budget cap on campaign [X] was inadvertently removed during a bulk configuration change on [date]. This allowed uncapped spend to flow through the [publisher name] channel."]
>
> **Actions Taken:**
> - [E.g., "Paused affected campaigns at [time] to stop ongoing spend."]
> - [E.g., "Restored the correct daily budget cap of $[X] to campaign [X]."]
> - [E.g., "Resumed campaigns at [time] with corrective caps in place."]
>
> **Affected Period:** [Date/time range]
>
> **Estimated Overspend:** $[Amount] — this has been flagged to our Finance and Client Success teams for review.
>
> We are monitoring the account closely over the next 24 hours to confirm spend is tracking within expected parameters.
>
> Please let me know if you have any questions or concerns.
>
> Best,
> [Your Name] | Joveo Support

---

## Escalation Triggers

Escalate immediately (do not wait for resolution window) if any of the following are true:

- **Overspend exceeds the client's full monthly budget** — this is a financial liability situation requiring CS Ops Director awareness.
- **Root cause is a MOJO platform bug** (caps configured correctly but not being enforced) — escalate to Tech Ops immediately.
- **Spike is ongoing and you cannot pause campaigns in MOJO** — platform access or permissions issue; escalate to CS Manager and Tech Ops.
- **Publisher overbilling is suspected** — CSM must be looped in immediately to manage client relationship while dispute is raised.
- **Multiple clients simultaneously experiencing spend spikes** — may indicate a platform-wide configuration or billing issue; escalate to CS Ops Director.
- **Root cause is unclear after completing all diagnostic steps within 45 minutes** — escalate to CSE and CS Manager.

Escalation path: **CS Manager → CSE → CSM → CS Ops Director**

When escalating, always include: affected campaign names, spend figures (normal vs. spike), time window, budget cap configuration (current and historical), change log entries, and publisher breakdown.

---

## Related Skills

- [[Invoice-Billing-Support]] — Use if the overspend needs to be addressed on the client's invoice, whether as a credit, adjustment, or dispute resolution.
- [[Campaign-Management]] — Use if a campaign configuration change (budget cap, bid setting, job group setup) was the root cause of the spike.
- [[Tracking-Attribution-Investigation]] — Use if the spend figures appear inflated but may be a tracking or attribution reporting error rather than actual overspend.
- [[UA-Reporting-Discrepancy]] — Use if the spend numbers in the MOJO UA dashboard look incorrect and may not reflect real spend.

---

*Last updated: June 2026 | Owner: Support Ops*
