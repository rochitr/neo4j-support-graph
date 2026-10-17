# Skill: Performance & ROI Investigation

**Theme:** Performance & ROI Optimization
**JIRA Theme:** Performance & ROI Optimization (567 tickets)
**SLA Severity:** Severity 1
**Primary Owner:** CSE / Ad Ops / CSD
**Internal SLA:** 1 hr response | 4–6 hr resolution
**Escalation Path:** CS Manager → CSM → CSD → CS Ops Director

---

## When to Use This Skill

Use this skill when a ticket involves any of the following:

- Client reports CPA is much higher than expected or agreed target
- Client reports applicant quality is poor or hire volumes are too low
- A publisher has been activated but ads are not visible on the publisher site
- Indeed hiring event attendance (RSVPs) is lower than expected
- Indeed Smart License credits need to be added for recruiters
- Resume files are not opening, corrupted, or in the wrong format
- Apply form submission is failing on a landing page

These tickets are Severity 1 — they directly affect client ROI and can trigger churn conversations. Respond within 1 hour and communicate clearly what investigation steps are underway. Do not close the ticket until root cause is confirmed and a resolution or optimization plan is delivered to the client.

---

## Step 1 — Acknowledge & Set Expectation

Send within **1 hour** of ticket creation.

**Email Template — Acknowledge:**

> Subject: Re: [Ticket Subject] — [Client Name] — Investigating Now
>
> Hi [Client Name],
>
> Thank you for flagging this. I've picked up your ticket and have started an investigation.
>
> **Issue reported:** [High CPA / Poor applicant quality / Publisher visibility / Hiring event attendance / Smart License credits / Resume issue / Form submission failure]
> **Scope:** [Campaigns, publishers, Req IDs, or roles as stated]
> **Time period under review:** [Date range from ticket]
>
> Given the nature of this issue, I'm treating this as a priority. I'll follow up with initial findings within **4–6 hours**. If I need additional context from your side, I'll reach out shortly.
>
> Best,
> [Your Name]
> Joveo Customer Support

---

## Step 2 — Classify / Confirm Scope

Before beginning the investigation, confirm the following:

| Issue Type | Required Inputs |
|---|---|
| High CPA | Target CPA, current CPA, date range, affected campaigns/publishers |
| Poor applicant quality | Definition of "poor quality" (wrong location, experience, not progressing in ATS), roles affected, time period |
| Publisher ads not visible | Publisher name, job titles and Req IDs, how long since expected go-live |
| Indeed hiring event low | Event name, event dates, target role/location, current RSVP count vs. target |
| Smart License credits | Recruiter names, emails, credit count needed, subscription tier |
| Resume format issue | Req ID, candidate email, submission timestamp, type of error |
| Form submission failure | Landing page URL, exact error message, when first observed, any recent changes |

---

## Step 3 — Diagnose / Execute

Work through the relevant sub-SOP below.

---

### 3A — High CPA Investigation

1. **Pull performance data from MOJO:**
   - CPA trend for the affected date range.
   - CPA broken down by campaign, job group, and publisher.
   - Compare current CPA vs. target CPA vs. prior period CPA.
2. **Identify high-CPA sources:**
   - Which publishers, campaigns, or job types are driving the elevated CPA?
   - Is the CPA elevated across the board or isolated to specific sources?
3. **Review apply volume:**
   - Is CPA high because spend is high — or because apply volume is low?
   - Low apply volume with normal spend = delivery/targeting problem. High apply volume with low hire rate = quality problem (see 3B).
4. **Assess job quality factors:**
   - Are job descriptions clear, accurate, and compelling?
   - Are apply URLs functional? (Test a sample.)
   - Is geo-targeting precise enough to drive relevant applicants?
5. **Review publisher mix:**
   - Is the current publisher mix optimal for the target roles and locations?
   - Are high-spend publishers delivering proportionally high apply volumes?
6. **Identify and implement optimizations:**
   - Shift budget from high-CPA publishers to low-CPA publishers.
   - Tighten geo-targeting if too broad.
   - Flag JD improvements to CSM for client conversation.
   - Adjust bid strategy if programmatic CPX is misaligned with conversion rate.
   - Coordinate specific bid adjustments with Ad Ops.
7. **Set a review milestone:** Agree with CSM on a follow-up date (typically 5–7 days) to assess impact of optimizations.

If CPA data is inconsistent with what the client's ATS shows, open a parallel [[Tracking-Attribution-Investigation]] to rule out a measurement problem before making campaign changes.

---

### 3B — Poor Applicant Quality / Not Enough Hires

1. **Understand specifics — ask if not stated:**
   - What defines "poor quality"? (Wrong experience level, wrong location, not progressing past screening, low offer acceptance?)
   - Which specific roles and locations are affected?
   - What time period are we looking at?
2. **Review publisher apply-to-hire conversion rates:**
   - Pull apply data from MOJO by publisher.
   - If the client can share ATS stage data, identify which publishers have the lowest conversion from apply to interview/hire.
   - Flag publishers with high apply volume but disproportionately low quality.
3. **Review targeting configuration:**
   - Is geo-targeting broad or precise? Overly broad targeting draws in applicants who are not local.
   - Are keyword targeting or audience targeting filters enabled? If not, consider adding them.
4. **Review job description quality:**
   - Do JDs clearly communicate required experience, location, compensation range, and screening criteria?
   - Vague JDs attract high-volume, low-quality applicants.
5. **Recommendations — document and share with CSM:**
   - Shift budget toward publishers with historically higher quality for similar roles.
   - Tighten geo-targeting.
   - Recommend JD content improvements to client.
   - For Indeed: explore Indeed Smart Targeting or Targeted Job Ads.
   - For programmatic: apply audience filters to improve candidate relevance.
6. **Escalate to CSD if client is considering churn:** If the client expresses frustration about sustained poor quality and is questioning the contract value, notify CSD immediately.

---

### 3C — Publisher Ads Not Visible

1. **Confirm scope:** Publisher name, specific job titles and Req IDs, how long since the jobs were expected to go live.
2. **Check MOJO publisher status:**
   - Is the publisher feed active in MOJO?
   - Are the specific Req IDs being sent in the publisher feed?
   - Is the campaign active and budgeted?
3. **Publisher-side checks:**
   - **Indeed:** Log into the Indeed agency dashboard. Confirm jobs are in an active campaign with available budget and Active status. Check for: budget exhausted, Trust & Safety flag on the job, job not meeting Indeed's quality requirements.
   - **Programmatic publishers:** Check that the feed was accepted by the DSP. Look for feed acceptance errors or eligibility rejections.
   - **Other direct publishers:** Check the publisher portal for the client account status and job delivery logs.
4. **Common root causes and fixes:**

| Root Cause | Fix |
|---|---|
| Campaign budget exhausted | Increase budget or wait for next billing cycle |
| Indeed Trust & Safety flag | Review flagged job, update content, resubmit |
| Job not in publisher feed | See [[Publisher-Channel-Management]] → feed issue track |
| Apply URL broken | Fix apply URL; test before resubmitting |
| Publisher account paused | Reactivate via Ad Ops or publisher portal |
| Indexing delay (new jobs) | Wait standard indexing window (24–48 hrs); monitor |

5. **If no root cause found within 2 hours:** Escalate to Publisher Relations with: client name, publisher, Req IDs, timeline, and all checks performed so far.

---

### 3D — Indeed Hiring Events — Low Attendance

1. **Review event setup in Indeed dashboard:**
   - Event dates, times, and location.
   - Budget allocated to the event.
   - Event description and linked requisitions.
   - Is the event currently Active and published?
2. **Review budget pacing:**
   - Is the budget actually being spent? Low pacing drives low RSVP volume.
   - Is the daily budget too low for the market? Indeed Hiring Events require sufficient daily budget to achieve broad reach.
3. **Assess event structure:**
   - Events spread over many days with a flat budget dilute daily spend, reducing daily reach.
   - Best practice: concentrate into 1–3 consecutive event days with concentrated budget.
4. **Review market conditions:**
   - Check Indeed's hiring insights for the role and location: candidate availability, competition level, and salary competitiveness.
   - Are competitors offering significantly better compensation or benefits?
5. **Recommendations:**
   - Consolidate event days if spread too thin.
   - Increase daily budget for the event duration.
   - Improve event description — include specific perks, benefits, and a compelling reason to attend.
   - Check if the event location is accessible and clearly communicated.
   - Share recommendations with CSM for client discussion.

---

### 3E — Indeed Smart License Credits

1. **Confirm inputs:** Recruiter full names, email addresses associated with their Indeed recruiter profiles, number of credits needed for each, and subscription tier (Professional or Standard).
2. **Log into the Indeed agency dashboard → Subscription Management section.**
3. **Add credits:**
   - **Professional tier subscriptions:** Credits can be moved from the shared pool to individual recruiter accounts.
   - **Standard tier subscriptions:** Credits cannot be transferred between accounts. A new credit purchase may be required. Confirm with the client before purchasing.
4. **Verify:** After adding credits, confirm each recruiter's credit balance in the dashboard.
5. **Notify client:** Confirm credits have been added with a list of recruiter names and updated credit balances.

---

### 3F — Resume Format Issues

1. **Confirm the exact issue:** File not opening, wrong file format, corrupted file, display error in the ATS or platform.
2. **Get examples:** Obtain specific Req ID, candidate email address, and application submission timestamp from the client.
3. **Reproduce the issue:** Pull the affected resumes from the Joveo platform or the ATS integration layer. Attempt to open and render each file.
4. **Diagnose by root cause:**

| Root Cause | Fix |
|---|---|
| Unsupported file format | Advise candidate/client to resubmit in PDF or Word (.docx) |
| ATS not passing resume correctly | Escalate to [[ATS-Integration-Triage]] — integration layer may be corrupting or dropping the file |
| Corrupted file from candidate | Candidate must resubmit |
| Platform display bug | Escalate to Tech Ops with reproduction steps |

5. **Document examples and pass to the appropriate team** if the issue is not a simple format problem.

---

### 3G — Form Submission Failures

1. **Reproduce the failure:** Navigate to the exact landing page URL provided. Submit a test application and document the exact error message and behavior (error code, what happens after submission, etc.).
2. **Check the ATS/CRM endpoint:**
   - Is the endpoint returning a 200 OK?
   - Test the endpoint directly if API access is available.
3. **Check for recent changes:** Ask the client: "Were there any recent updates to the landing page, ATS configuration, or API credentials in the past 48 hours?"
4. **Review error logs** for the following:
   - 401/403: Authentication/authorization failure — credentials expired or invalid.
   - 503/500: ATS-side server error — escalate to client's ATS admin.
   - Required field error: Form is missing a required field that the ATS expects.
   - CORS error: Domain not whitelisted in ATS API configuration.
   - JavaScript error on form: Front-end form script failure.
5. **Fix or escalate:**

| Error Type | Fix | Escalate |
|---|---|---|
| Expired API credentials | Coordinate credential rotation with client ATS admin | Client ATS team |
| Required field missing | Add missing field to form configuration | Tech Ops |
| CORS misconfiguration | Update CORS settings in ATS API config | Client ATS team + Tech Ops |
| ATS server error | Wait and retest; if persistent, notify client ATS admin | Client ATS team |
| Form JS error | Document and escalate with reproduction steps | Tech Ops |

6. **Validate fix:** Re-test the full application submission flow end-to-end after any fix is applied.

---

## Step 4 — Fix or Escalate

| Issue | Fix | Escalate To |
|---|---|---|
| High CPA across all publishers | Budget reallocation + bid strategy optimization | Ad Ops |
| High CPA on single publisher | Publisher-level bid adjustment | Ad Ops |
| CPA measurement inconsistent with ATS | Open [[Tracking-Attribution-Investigation]] | Ad Ops + Analytics |
| Poor quality — targeting too broad | Tighten geo + audience targeting in MOJO | Ad Ops |
| Client considering churn over quality | Immediate notification | CSD |
| Publisher ads not visible — no root cause in 2 hrs | Escalate with full investigation notes | Publisher Relations |
| Indeed event low RSVPs — budget/structure fix | Consolidate days, increase budget | Ad Ops + Indeed account team |
| Smart License credits — Standard tier purchase needed | Confirm with client first | Indeed account team |
| Resume issue — ATS integration | Open [[ATS-Integration-Triage]] | Integrations Squad |
| Form failure — server or CORS error | Tech Ops + client ATS admin | Tech Ops |

---

## Step 5 — Post-Resolution Message

Send after root cause is confirmed and fix or optimization plan is in place.

**Email Template — Resolution:**

> Subject: Re: [Ticket Subject] — [Client Name] — Update & Next Steps
>
> Hi [Client Name],
>
> I've completed my investigation and wanted to share what I found along with the steps we've taken.
>
> **Issue:** [Brief description]
> **Root cause identified:** [Clear 1–2 sentence explanation]
>
> **Actions taken:**
> - [Action 1 — e.g., Shifted 30% of budget from Publisher A to Publisher B based on CPA comparison]
> - [Action 2 — e.g., Tightened geo-targeting to 25-mile radius for all active job groups]
> - [Action 3 — e.g., Flagged JD improvements to your account team for follow-up]
>
> **Expected impact:** [What the client should see change, and by when]
>
> **Review checkpoint:** I've scheduled a follow-up review on [Date] to assess the impact of these changes. I'll share a performance summary at that point.
>
> Please don't hesitate to reach out if you have any questions in the meantime.
>
> Best,
> [Your Name]
> Joveo Customer Support

---

## Escalation Triggers

Escalate immediately — do not wait for the resolution window to expire:

- Client mentions potential contract cancellation or churn → CSD immediately
- CPA has been consistently above target for more than 2 billing cycles with no improvement → CSD + CSM
- Publisher ads have been invisible for more than 48 hours with no root cause → Publisher Relations
- Form submission failure is affecting all applicants (zero successful submissions) → Tech Ops as P1
- Resume issue is systemic (affecting more than one candidate) and root cause is in integration → Integrations Squad as P1
- Indeed Trust & Safety flag on multiple jobs → Publisher Relations + Indeed account team

---

## Related Skills

- [[Campaign-Management]] — for executing optimization actions (budget shifts, pauses, boosts)
- [[Publisher-Channel-Management]] — for publisher visibility issues and feed delivery problems
- [[ATS-Integration-Triage]] — for resume format issues and form submission failures with integration root cause
- [[Tracking-Attribution-Investigation]] — for data discrepancies that affect CPA calculation
- [[Proactive-Consulting-Advisory]] — if client raises performance concerns repeatedly and needs a strategic review
- [[Career-Site-Updates]] — for landing page issues and form failures on career site

---

*Last updated: June 2026 | Owner: Support Ops*
