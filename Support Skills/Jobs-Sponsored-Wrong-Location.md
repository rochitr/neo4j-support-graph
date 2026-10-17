# Skill: Jobs Sponsored in Wrong Location

**Theme:** Jobs appearing on publishers in incorrect geographic locations
**SLA Severity:** Severity 0
**Primary Owner:** CSE / Ad Ops
**Internal SLA:** 1 hr response | 2 hr resolution
**Escalation Path:** CS Manager → CSM → CSD → CS Ops Director

---

## When to Use This Skill

Use this skill when:
- A client reports that specific jobs are being sponsored in cities, states, or regions other than the job's actual location.
- A candidate applies to what appears to be a local job but finds it is listed with an incorrect or distant location.
- A client notices their job for "Austin, TX" is appearing in searches for "New York, NY" (or similar geographic mismatch).
- Publisher reporting shows job traffic from unexpected geographic markets.

This is a Severity 0 issue because incorrect location targeting wastes client budget on unqualified candidates and erodes the quality of their applicant pool. Begin triage immediately. The root cause can sit in three different places — the ATS feed, the MOJO campaign configuration, or the publisher-side targeting — so follow the diagnostic steps in order.

---

## Step 1 — Acknowledge & Set Expectation

Send within **15 minutes** of receiving the report.

> **Subject:** Re: Jobs Appearing in Wrong Locations — [Client Name] — Investigating Now
>
> Hi [Client Name],
>
> Thank you for flagging this. I've received your report and have started investigating why your jobs are appearing in incorrect locations.
>
> This is being treated as a Severity 0 issue with a target resolution of 2 hours.
>
> To help me investigate as quickly as possible, could you please confirm:
> 1. The specific Req IDs or job titles that are appearing in incorrect locations.
> 2. The location the jobs should be appearing in.
> 3. The location(s) where they are actually appearing.
> 4. Which publisher(s) you've observed this on (if known).
>
> I will send a full status update within 1 hour.
>
> Best,
> [Your Name] | Joveo Support

---

## Step 2 — Confirm Scope

Before diagnosing, establish exactly which jobs are affected and the full extent of the problem.

1. Collect from the client (or identify yourself in MOJO): all affected **Req IDs** and **job titles**.
2. For each affected job, note:
   - The **intended location** (what the client expects)
   - The **observed location** (where it is actually appearing or being targeted)
   - The **publisher(s)** where the mismatch is occurring
3. Determine whether this is:
   - A small subset of jobs (e.g., 5 specific reqs) — likely a data or mapping issue on specific records
   - A broad pattern across many jobs — likely a systematic campaign geo-targeting or feed mapping issue
4. Note the approximate start date of the issue based on client report and any available publisher impression data.

---

## Step 3 — Diagnose / Execute

Work through each layer in sequence. The root cause almost always lives in one of three places: the feed, the campaign targeting settings, or the publisher targeting configuration.

**3-1. Check location data in the inbound feed**
- In MOJO, retrieve the most recent inbound feed data for the affected Req IDs.
- For each affected job, review the raw feed values for:
  - City
  - State
  - Postal / ZIP code
  - Country
- Confirm whether the feed location fields **match the client's intended job location**.
- If the feed shows an incorrect location → the root cause is in the client's ATS. The wrong location data is being published at the source.
- Example: Job is for Austin, TX but the feed shows `<city>Remote</city>` or a blank location field that defaults to a fallback value.

**3-2. Check campaign geo-targeting settings in MOJO**
- Open the relevant campaign(s) in MOJO for the affected jobs.
- Review all geo-targeting settings:
  - Is there a geo-targeting override applied at the campaign or job group level?
  - Is there a radius setting (e.g., "target jobs within 50 miles of [city]") that is either too broad or pointing to the wrong city?
  - Has a recent geo-targeting change been made? Check the campaign change log.
- If the campaign geo-targeting is overriding or conflicting with the job's actual location data → the root cause is in MOJO campaign configuration.

**3-3. Check publisher-level location targeting**
- Review how location data is being passed to the specific publisher(s) where the mismatch is observed.
- In MOJO's publisher feed configuration, confirm:
  - Which location field is being mapped to the publisher's location parameter.
  - Whether the correct field (city/state/postal code) is being used in the publisher feed output.
- On the publisher side (if you have access to publisher reporting or feed preview): confirm whether the job's listed location matches the Joveo feed output.
- If the location passed to the publisher does not match the MOJO data → the root cause is a feed field mapping issue at the publisher integration layer.

**3-4. Cross-check with a known-good job**
- Select a job that the client confirms is appearing correctly.
- Run the same checks (feed location data, campaign geo-targeting, publisher feed output) for that job.
- Compare the configuration between the working job and the broken job to isolate the specific difference.

---

## Step 4 — Fix or Escalate

| Root Cause | Action | Owner |
|---|---|---|
| Location data wrong in the inbound feed (ATS issue) | Notify client immediately with the specific Req IDs and the incorrect field values observed. Request that the ATS team correct the location data and republish. Monitor feed after correction to confirm fields update. See [[ATS-Integration-Triage]]. | Customer Support → Client ATS Team |
| Campaign geo-targeting override is too broad or misconfigured | Correct the geo-targeting settings in MOJO for the affected campaign or job group. If a radius setting is causing the issue, adjust or remove the radius. Confirm the change takes effect and monitor publisher distribution. | CSE / Ad Ops |
| Geo-targeting was recently changed incorrectly | Revert to prior geo-targeting configuration using the change log as reference. Document who made the change and when. | CSE / Ad Ops |
| Publisher feed field mapping is incorrect (wrong location field passed to publisher) | Work with Ad Ops to correct the field mapping in the publisher feed configuration. Test with a feed preview before pushing the fix live. | Ad Ops → Tech Ops if platform-level mapping change required |
| Publisher-side targeting is misconfigured independent of Joveo feed | Raise with the publisher's account team. Provide the correct location data from the Joveo feed as evidence. | CSE / Ad Ops → Publisher Account Team |
| Location field is blank in feed and defaulting to a fallback | Flag to client: their ATS is not populating the location field for affected jobs. Client must correct at ATS level. See [[ATS-Integration-Triage]]. | Customer Support → Client |
| Root cause cannot be identified | Escalate to Tech Ops with all feed data, MOJO config screenshots, and publisher feed output evidence. | Escalate to Tech Ops |

**After implementing any fix:**
1. Verify the corrected location data is present in the MOJO feed within one ingestion cycle.
2. Confirm publisher-side targeting reflects the correct location (check publisher feed preview or publisher reporting).
3. Document all affected Req IDs and the date range during which they were incorrectly targeted.

---

## Step 5 — Post-Resolution Message

Send once affected jobs are confirmed appearing in the correct locations.

> **Subject:** Resolved: Jobs Now Appearing in Correct Locations — [Client Name]
>
> Hi [Client Name],
>
> I'm pleased to confirm that the location targeting issue affecting your jobs has been resolved. The following jobs are now appearing in their correct geographic locations:
>
> [List of affected Req IDs / job titles and their correct locations]
>
> **Root Cause:** [E.g., "The location fields for these jobs were missing in your inbound feed, causing our system to apply a default geo-targeting fallback. Your ATS team has corrected the location data and the updated feed has been re-ingested."]
>
> **Actions Taken:**
> - [E.g., "Identified incorrect location values in the inbound feed for [X] Req IDs."]
> - [E.g., "Coordinated with your ATS team to publish corrected location data."]
> - [E.g., "Confirmed re-ingestion and verified publisher-side location targeting is now correct."]
>
> **Affected Period:** [Date range] — we have documented the affected Req IDs and date range for your records.
>
> Please let us know if you notice any further location discrepancies.
>
> Best,
> [Your Name] | Joveo Support

---

## Escalation Triggers

Escalate immediately (do not wait for resolution window) if any of the following are true:

- **All jobs across a campaign are appearing in wrong locations** — systematic issue likely requiring Tech Ops involvement.
- **Root cause identified as a platform-level feed mapping bug** — cannot be fixed by Ad Ops configuration alone; escalate to Tech Ops.
- **Client's ATS team is unresponsive** and the incorrect location data has been active for more than 2 hours — escalate to CS Manager to engage client account escalation.
- **Erroneous targeting has driven significant spend to incorrect geographic markets** — flag to CSM immediately; may require budget adjustment or credit discussion. Cross-reference [[Spend-Spike-Investigation]].
- **Client has an active recruiting event or hiring push in the correct location** and jobs are not reaching that market — treat as high urgency; escalate to CS Manager.

Escalation path: **CS Manager → CSM → CSD → CS Ops Director**

When escalating, always include: affected Req IDs, feed location field values (screenshots), campaign geo-targeting configuration, publisher(s) affected, and date range.

---

## Related Skills

- [[ATS-Integration-Triage]] — Use if the location data is wrong at the source in the client's ATS feed; the fix must happen on the ATS side before Joveo can ingest correct data.
- [[Campaign-Management]] — Use if the root cause is geo-targeting settings misconfigured at the campaign or job group level in MOJO.
- [[Publisher-Channel-Management]] — Use if the publisher-side targeting is the issue — correct location data is flowing from Joveo but the publisher is not applying it correctly.
- [[Inbound-Feed-Jobs-Down]] — Use if the feed has broader structural issues beyond just location fields, or if checking location data reveals other feed problems.

---

*Last updated: June 2026 | Owner: Support Ops*
