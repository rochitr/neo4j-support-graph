# Skill: Publisher & Channel Management

**Theme:** Publisher & Channel Management
**JIRA Theme:** Publisher & Channel Management (426 tickets)
**SLA Severity:** Severity 1
**Primary Owner:** CSE / Ad Ops / Publisher Relations
**Internal SLA:** 1 hr response | 6 hr resolution
**Escalation Path:** CS Manager → CSM → CSD → CS Ops Director

---

## When to Use This Skill

Use this skill when a ticket involves any of the following:

- Jobs are not sponsoring (appearing as paid/promoted) on a specific publisher
- A publisher feed is broken, rejected, or delivering incorrect data
- A publisher needs to be activated, deactivated, or reconfigured
- Indeed campaign setup, changes, or optimization is required
- Amazon channel configuration or spend/volume issues
- Slot rotation or pinning configuration on a publisher
- Manual posting of a job on a publisher portal
- Duration-based postings for enterprise accounts (Wells Fargo, Uber Corp, JET, GEDU)

These tickets are Severity 1 because publisher delivery issues directly affect job visibility, candidate flow, and client ROI. Respond within 1 hour. Do not assume pacing issues are normal — always verify root cause before reassuring the client.

---

## Step 1 — Acknowledge & Set Expectation

Send within **1 hour** of ticket creation.

**Email Template — Acknowledge:**

> Subject: Re: [Ticket Subject] — [Client Name] — Investigating Now
>
> Hi [Client Name],
>
> Thank you for reaching out. I've picked up your ticket and am investigating now.
>
> **Issue reported:** [Jobs not sponsoring / Feed issue / Publisher activation / Manual posting / Duration posting / etc.]
> **Publisher(s) affected:** [Publisher name(s)]
> **Scope:** [Req IDs, job groups, or campaigns as stated]
>
> I'm targeting a resolution or a detailed update within **6 hours**. I'll reach out sooner if I have a quick fix or need additional information from your side.
>
> Best,
> [Your Name]
> Joveo Customer Support

---

## Step 2 — Classify / Confirm Scope

Confirm the following before executing any changes:

| Request Type | Required Inputs |
|---|---|
| Jobs not sponsoring | Publisher name, Req IDs, expected go-live date, how long since last confirmed live |
| Publisher feed issue | Publisher name, what the issue is (jobs missing, wrong data, feed rejected), since when |
| Publisher activation/deactivation | Publisher name, client account, desired status, effective date |
| Indeed campaign management | Campaign name, objective (setup / optimize / fix), specific issue or request |
| Amazon channel | Nature of issue (spend, volume, feed delivery, reporting) |
| Slot rotation / pinning | Jobs involved, publishers, rotation schedule or pin target |
| Manual posting | Job title, location, description, Req ID, apply URL, publisher(s), special instructions |
| Duration-based posting | Job titles, Req IDs, target publishers, duration (start and end date), client contract context |

If the client says "our jobs aren't showing up" without specifying publisher, Req IDs, or timeframe — ask before investigating. A broad question leads to a broad investigation and a slower resolution.

---

## Step 3 — Diagnose / Execute

Work through the relevant sub-SOP below.

---

### 3A — Jobs Not Sponsoring

1. **Confirm scope:** Publisher name, specific Req IDs, and how long since jobs were expected to go live.
2. **Check feed delivery in MOJO:**
   - Is the publisher feed active in MOJO?
   - Are the specific Req IDs present in the feed being delivered to this publisher?
   - If jobs are not in the feed at all, open a parallel [[Inbound-Feed-Jobs-Down]] track — this is a feed-level issue, not a publisher issue.
3. **Check campaign status in MOJO:**
   - Is the campaign active (not paused)?
   - Is there remaining budget for this campaign?
   - Are the Req IDs mapped to an active job group targeting this publisher?
4. **Publisher-side checks:**
   - **Indeed:** Log into the Indeed agency dashboard. Confirm jobs are in an active campaign, budget is available, and the campaign status is Active. Check for: budget exhaustion, Trust & Safety flags, job quality score issues, or campaign-level errors.
   - **Programmatic publishers:** Check the DSP for feed acceptance status. Look for feed rejection errors, eligibility failures, or bid-below-floor warnings.
   - **LinkedIn, ZipRecruiter, other direct publishers:** Log into the respective portal. Confirm job is submitted, active, and not flagged.
5. **Validate apply URL:** Test the apply URL for each affected Req ID. A broken apply URL causes many publishers to suppress the job automatically.
6. **Fix and validate:** Apply the appropriate fix (see Step 4 table). After fixing, confirm jobs appear as sponsored within the expected indexing window for that publisher.

**Publisher indexing windows (approximate):**
- Indeed: 2–4 hours after campaign activation
- LinkedIn: 24–48 hours for new postings
- Programmatic (Appcast, Pandologic): 4–12 hours after feed acceptance
- ZipRecruiter: 4–8 hours

---

### 3B — Publisher Feed Issues

1. **Identify the publisher and the nature of the issue:**
   - Jobs missing from feed (publisher received fewer jobs than expected)
   - Jobs with wrong data (title, location, description, apply URL incorrect)
   - Feed rejected by publisher (publisher-side parse failure)
   - Feed URL not responding or returning non-200
2. **Pull the publisher feed from MOJO** and inspect the content directly:
   - Open the feed URL and look at a sample of jobs.
   - Compare against what is expected (check a known Req ID — is it present? Is the data correct?).
3. **Check for structural issues:**
   - Missing required fields (publisher-specific: e.g., Indeed requires `<referencenumber>`, `<city>`, `<state>`, `<country>`)
   - Malformed XML or JSON (syntax errors break the entire feed)
   - Special characters not properly encoded (ampersands, quotes in job titles or descriptions)
   - Apply URLs not properly encoded or containing redirect loops
4. **Check publisher eligibility criteria:** Some publishers reject jobs that don't meet their quality bar (e.g., description too short, missing compensation, generic job title).
5. **Fix:**
   - Simple field or formatting issues: fix in MOJO feed configuration.
   - Structural feed issues or large-scale data problems: coordinate with Feed Engineering via Ad Ops.
6. **Monitor re-indexing:** After a feed fix, monitor the publisher dashboard to confirm the corrected jobs are re-indexed within the expected window.

---

### 3C — Indeed Campaign Management

1. **Log into the Indeed agency dashboard** for the specific client account. Verify you are in the correct account (client name visible in account switcher).
2. **For campaign setup (new):**
   - Create the Indeed campaign with the correct name, budget, job targeting criteria (titles, locations), and bid strategy.
   - Link to the correct Req IDs or job titles.
   - Set daily budget cap aligned with the client's agreed Indeed budget.
   - Enable Smart Targeting if part of the client's package.
   - Confirm campaign is Active and jobs are in the campaign.
3. **For performance optimization:**
   - Review campaign pacing — is the daily budget being spent? If under-pacing, review bid levels and job quality scores.
   - Review CPC bids — if below Indeed's suggested bid range, jobs will lose auction and underdeliver.
   - Review job quality scores — low quality scores suppress delivery. Identify low-scoring jobs and recommend JD improvements.
4. **For campaign issues:**
   - Budget exhausted: Increase budget or confirm with client if additional budget is approved.
   - Trust & Safety flag: Review the flagged job, update content per Indeed's guidelines, and resubmit.
   - Campaign disapproved: Review disapproval reason in dashboard, fix the underlying issue, resubmit.
5. **Coordinate with the Indeed account team** for enterprise-level issues: campaign approvals, Trust & Safety disputes, credit adjustments, and Hiring Events. Contact via the shared Indeed agency account team channel.

---

### 3D — Amazon Channel Management

Amazon has a dedicated, high-volume distribution setup that differs from standard programmatic publishers.

1. **For all Amazon-specific configurations:** Coordinate with the Publisher Relations team. Do not attempt to configure Amazon independently without Publisher Relations involvement.
2. **For spend or volume issues:**
   - Review the MOJO campaign setup for Amazon — is the campaign active, budgeted, and targeting the correct job groups?
   - Verify feed delivery to Amazon — confirm the feed is being delivered and accepted.
   - Check Amazon-side reporting (via Publisher Relations) for delivery, click, and apply data.
3. **For escalation:** If Publisher Relations cannot resolve within the 6-hour window, escalate to CS Manager with the investigation notes and a request for Amazon account team involvement.

---

### 3E — Duration-Based Postings (Wells Fargo, Uber Corp, JET, GEDU)

These enterprise accounts use duration-based job postings on specific publishers, meaning jobs are posted for a fixed duration (e.g., 30 days) rather than run-rate budget.

1. **Confirm inputs:** Job titles, Req IDs, target publishers, start date, end date (duration), and any special formatting or posting instructions specific to the client account.
2. **Verify jobs in the feed:** Confirm all Req IDs are present in the inbound feed and correctly formatted. Do not proceed with posting if a Req ID is missing — open [[Inbound-Feed-Jobs-Down]] in parallel.
3. **Contact the publisher/supply team:** Duration-based postings are typically submitted through a specific channel (publisher portal, email to publisher rep, or a managed service workflow). Follow the account-specific process. Confirm with Ad Ops if the process is unclear.
4. **Submit postings on publisher portal:**
   - Follow publisher-specific formatting requirements (title length, description format, location format).
   - Note the publisher confirmation or reference number for each posting submitted.
5. **Validate jobs are live:** After the expected activation window, search for the jobs on the publisher site to confirm they are visible.
6. **Track expiry:** Log the end date in the ticket or account notes. Schedule a reminder 5–7 days before expiry to proactively discuss renewal with the CSM.

---

### 3F — Slot Rotation / Pinning

1. **Confirm scope:** Which jobs are involved, which publishers, and what the desired configuration is:
   - **Pinning:** A specific job is locked into a fixed position on the publisher.
   - **Rotation:** Multiple jobs rotate through a position on a scheduled basis.
2. **Coordinate with Ad Ops:** Slot rotation and pinning are managed at the publisher level and require Ad Ops involvement. Open an internal Ad Ops request with: client name, publisher, job list, desired configuration, and start date.
3. **Apply configuration:**
   - For publisher-side pinning/rotation: Ad Ops coordinates directly with the publisher account team.
   - For MOJO-managed rotation: Ad Ops applies the configuration in MOJO's publisher settings.
4. **Validate:** After the configuration is applied, confirm with Ad Ops that the jobs are displaying as configured. Perform a spot check on the publisher site if possible.

---

### 3G — Manual Posting

1. **Gather all required information:**
   - Job title, location, full job description, Req ID, apply URL, target publisher(s), any special instructions from the client.
2. **Validate the apply URL:** Click the apply URL and confirm it is live, loads correctly, and routes to the intended application form or ATS. A broken apply URL must be corrected before posting.
3. **Submit on publisher portal or via MOJO manual posting workflow:**
   - Follow the publisher's specific formatting requirements (character limits on title/description, required fields, location format).
   - If posting via publisher portal directly (e.g., ZipRecruiter, Glassdoor): log in with the agency credentials, create the posting, and submit.
4. **Note the publisher reference number:** Each manual posting typically generates a confirmation or reference number. Record this in the ticket.
5. **Validate live and searchable:** After the expected activation window, search for the job on the publisher site by title and location to confirm it is visible.

---

## Step 4 — Fix or Escalate

| Issue | Fix | Escalate To |
|---|---|---|
| Jobs not in MOJO feed at all | Open [[Inbound-Feed-Jobs-Down]] | Feed Engineering via Ad Ops |
| Campaign budget exhausted | Increase budget (confirm with CSM if approval needed) | CSM if budget requires client approval |
| Indeed Trust & Safety flag | Update job content per Indeed guidelines, resubmit | Indeed account team if disputed |
| Feed malformed (structural issue) | Feed Engineering via Ad Ops | Ad Ops → Feed Engineering |
| Publisher eligibility rejection | Fix job data; check publisher quality requirements | Ad Ops |
| Broken apply URL | Fix URL, resubmit job | Client to provide corrected URL if needed |
| Amazon configuration | Coordinate with Publisher Relations | Publisher Relations |
| Duration posting — Req ID missing | Open [[Inbound-Feed-Jobs-Down]] before posting | Feed Engineering |
| No root cause found after 2 hrs | Escalate with full investigation notes | Publisher Relations |
| Client reports no visibility for >48 hrs | Immediate escalation | CS Manager + Publisher Relations |

---

## Step 5 — Post-Resolution Message

Send after jobs are confirmed live on the publisher or configuration is validated.

**Email Template — Resolution:**

> Subject: Re: [Ticket Subject] — [Client Name] — Resolved
>
> Hi [Client Name],
>
> I'm happy to confirm that this has been resolved.
>
> **Issue:** [Brief description]
> **Root cause:** [Clear explanation]
> **Resolution:**
> - [Action 1 — e.g., Reactivated campaign budget on Indeed]
> - [Action 2 — e.g., Fixed feed eligibility issue for 3 Req IDs]
> - [Action 3 — e.g., Confirmed jobs live and searchable on [Publisher] as of [Time]]
>
> **Validation:** [How you confirmed jobs are live — e.g., "Confirmed in Indeed agency dashboard" or "Searched publisher site and confirmed job is visible"]
>
> Please let me know if you see any further delivery issues in the next 24 hours.
>
> Best,
> [Your Name]
> Joveo Customer Support

---

## Escalation Triggers

Escalate immediately — do not wait for the 6-hour window:

- Jobs have had zero delivery on a publisher for more than 48 hours with no identifiable root cause → Publisher Relations + CS Manager
- Trust & Safety flag is disputed by client and involves a large volume of jobs → CS Manager + Indeed account team
- Amazon channel issue — always loop Publisher Relations in from the start
- Duration-based posting deadline is today and Req IDs are missing from feed → CS Manager + Feed Engineering as P1
- Client is reporting zero job visibility across all publishers simultaneously → Potential MOJO or feed-level outage. Escalate to CS Manager and Tech Ops immediately.
- Publisher rejects entire feed → Feed Engineering via Ad Ops as P1

---

## Related Skills

- [[Inbound-Feed-Jobs-Down]] — when the root cause of jobs not sponsoring is a feed delivery or inbound feed failure
- [[Campaign-Management]] — when campaign configuration is the cause of publisher issues
- [[Performance-ROI-Investigation]] — when publisher underperformance (not just visibility) is the concern
- [[Tracking-Attribution-Investigation]] — when publisher data does not match MOJO reporting
- [[Media-Planning-Media-Buying]] — for new publisher selection, activation planning, and budget allocation

---

*Last updated: June 2026 | Owner: Support Ops*
