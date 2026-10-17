# Skill: Campaign Management

**Theme:** Campaign Management & Campaign Requests
**JIRA Theme:** Campaign Management (643 tickets — highest volume theme)
**SLA Severity:** Standard
**Primary Owner:** CSE / Ad Ops / Customer Support
**Internal SLA:** 1 hr response | 2 hr resolution
**Escalation Path:** CS Manager → CSM → CSD → CS Ops Director

---

## When to Use This Skill

Use this skill when a ticket involves any of the following:

- Creating a new campaign or job group from scratch
- Pausing one or more campaigns, job groups, or individual jobs
- Boosting a specific job with additional budget or priority
- Updating monthly or campaign-level budgets
- Updating UTM tracking parameters on any campaign or job
- Extending the end date of an existing campaign
- Any Severity 1 campaign extension (active campaign about to expire mid-cycle)

This is the highest-volume theme in the queue. Most tickets are actionable immediately — the key is confirming scope precisely before executing any change in MOJO, as errors here directly impact client spend and visibility.

---

## Step 1 — Acknowledge & Set Expectation

Send within **1 hour** of ticket creation.

**Email Template — Acknowledge:**

> Subject: Re: [Ticket Subject] — [Client Name] — Acknowledged
>
> Hi [Client Name],
>
> Thank you for reaching out. I've received your request and have picked it up for immediate action.
>
> Here's what I'm working on:
> **Request type:** [Campaign creation / Pause / Boost / Budget update / UTM update / Extension]
> **Scope confirmed:** [Campaigns / Job groups / Req IDs as stated in ticket — or "pending confirmation" if ambiguous]
>
> I'll follow up with a confirmation of the change within **2 hours**. If I need any additional details to proceed, I'll reach out shortly.
>
> Best,
> [Your Name]
> Joveo Customer Support

---

## Step 2 — Classify / Confirm Scope

Before touching MOJO, confirm the following based on request type. If any item is missing, reply to the client immediately — do not guess.

| Request Type | Required Information |
|---|---|
| Campaign Creation | Campaign name, job group structure, target locations, Req IDs, budget by publisher, go-live date |
| Pause Campaign/Jobs | Exact Req IDs, job groups, or campaign names; scope (partial or all); confirmation if a hiring event is active |
| Boost a Job | Req IDs, additional budget amount, target publishers, boost duration |
| Update Budget | New budget amount, effective date, breakdown by campaign/job group/publisher, mid-month or new monthly cycle |
| Update UTM Tags | Complete updated UTM parameter set, affected campaigns/jobs |
| Campaign Extension | New end date, any associated budget changes |

If scope is ambiguous (e.g., "pause our jobs in Texas"), reply and ask: "Could you confirm the specific Req IDs, job groups, or campaign names you'd like paused? This ensures we don't inadvertently pause active campaigns you intend to keep running."

---

## Step 3 — Diagnose / Execute

Work through the relevant sub-SOP below. Execute only after scope is fully confirmed.

---

### 3A — Campaign Creation

1. **Gather all inputs:** Campaign name, job group structure, target locations, Req IDs, budget by publisher, go-live date. Do not proceed until all are confirmed.
2. **Verify jobs in feed:** Check that all submitted Req IDs are present in the inbound feed and correctly formatted. If Req IDs are missing, do not proceed — open a parallel track using [[Inbound-Feed-Jobs-Down]] before creating the campaign.
3. **Create in MOJO:**
   - Set up job groups with correct hierarchy.
   - Apply geo-targeting per client specification.
   - Set budget caps at campaign and job group level.
   - Map Req IDs correctly. Double-check for typos — mismatched Req IDs result in zero delivery.
4. **Configure publisher settings:**
   - Indeed: set daily budget cap, apply CPC bid strategy per account standards.
   - Programmatic publishers: apply appropriate bid strategy and priority tier.
   - If a specific publisher configuration is non-standard, loop in Ad Ops before going live.
5. **Internal QA:** Before confirming to client, verify all settings in MOJO. Check: budget applied, publisher active, targeting correct, Req IDs mapped.
6. **Confirm go-live with client:** Send go-live confirmation email (see Step 5 template) with a brief campaign summary.

If client needs a media plan or budget recommendation before creation can proceed, pause and reference [[Media-Planning-Media-Buying]].

---

### 3B — Pausing Campaigns / Jobs

1. **Confirm scope precisely:** Req IDs, job groups, campaign names, or all campaigns for a given location. If the client says "pause everything" — confirm what "everything" means before acting.
2. **Check for active hiring events:** If a hiring event is currently running, flag this to the client before pausing. Pausing jobs mid-event will remove them from event targeting and reduce RSVP volume.
3. **Document current MTD spend:** Pull current month-to-date spend from MOJO for all campaigns in scope. Note this for the client confirmation message — clients often ask "how much have we spent?" after a pause.
4. **Execute pause in MOJO:** Set campaign/job group/job status to Paused. Do not delete — always pause.
5. **Confirm with screenshot or status confirmation:** Take a MOJO screenshot showing the paused status or confirm status in writing in the client reply.

---

### 3C — Boost a Job

1. **Confirm inputs:** Req IDs to boost, additional budget amount, target publishers, boost duration (start and end date).
2. **Verify job is in feed:** Confirm the Req ID is present and active in the feed before applying any boost configuration.
3. **Baseline current performance:** Pull current spend and apply volume for the Req ID. Note this so you can measure boost impact.
4. **Apply boost in MOJO:**
   - Option A (dedicated job group): Create a dedicated job group for the boosted job with a separate budget cap.
   - Option B (increase budget cap): Increase the budget cap on the existing job group.
   - For Indeed: increase the daily budget or CPC bid specifically for this job.
   - For programmatic: increase bid priority or CPX bid.
5. **Loop in Ad Ops:** For publisher-specific bid adjustments (e.g., LinkedIn, Appcast, ZipRecruiter), notify Ad Ops via the internal channel and provide: Req ID, publisher, desired boost amount, duration.
6. **Confirm boost is live and pacing:** Check MOJO within 30 minutes of applying to confirm delivery has started. Flag to Ad Ops if not pacing.

---

### 3D — Update Budget

1. **Capture full details:** New budget amount, effective date, breakdown by campaign / job group / publisher, and whether this is a mid-month change or a new monthly budget.
2. **Cross-check against MTD spend:**
   - Pull current MTD spend from MOJO.
   - If the new budget is **less than current MTD spend**, this is a critical flag. Do not proceed without alerting the CSM and client: "The new budget of $X is below the current MTD spend of $Y. Please confirm how you'd like to handle the remaining spend this month."
3. **Flag edge cases:**
   - If budget is split across multiple channels, recalculate splits to ensure they add up to the new total.
   - If prior month had a rollover balance, factor this in before updating.
4. **Update MOJO:** Apply the new budget at the correct level (campaign, job group, or publisher). If publisher-level changes are needed, coordinate with Ad Ops.
5. **Confirm in writing:** Reply to client with: new budget amount, effective date, breakdown by channel, and MOJO confirmation.

---

### 3E — Update UTM Tags

1. **Confirm the complete updated UTM parameter set:** Do not make partial updates. Get the full set: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term` — and any custom parameters.
2. **Identify all affected campaigns and jobs:** Confirm scope with client — all campaigns, specific campaigns, or specific job groups.
3. **Coordinate with Ad Ops:** UTM updates require changes at two levels — MOJO tracking URL configuration and publisher-level URLs. Ad Ops must update both. Create an internal task for Ad Ops with: client name, old UTM string, new UTM string, affected scope.
4. **Test post-update:** After Ad Ops confirms changes, test a sample apply URL from each affected publisher. Click the URL and confirm the UTM parameters are passing correctly to the destination (client ATS or landing page). If UTMs are not passing, refer to [[Tracking-Attribution-Investigation]] before closing the ticket.
5. **Confirm with client:** Reply with confirmation that UTMs have been updated and tested, along with a sample URL showing the new parameters.

---

### 3F — Campaign Extension

1. **Confirm new end date and budget changes:** Ask: "Are you extending the budget as well, or keeping the same total budget across the longer duration?"
2. **Check current campaign status:**
   - Current end date in MOJO.
   - Current MTD spend and remaining budget.
   - Whether the campaign is currently active or paused.
3. **Update end date in MOJO:** Set the new campaign end date. If budget is also increasing, apply the new budget at the same time.
4. **Coordinate with Ad Ops for publisher-level updates:** Some publishers (Indeed, LinkedIn) require manual campaign end date updates in their dashboards. Notify Ad Ops with: client name, campaign name, old end date, new end date.
5. **Validate in MOJO:** Confirm the updated end date is saved correctly.
6. **Confirm to client:** Include new end date, updated budget (if applicable), and which publishers have been updated.

**Severity 1 extension (campaign about to expire mid-cycle):** If a campaign is within 24 hours of expiry and should not expire, treat this as Sev 1. Escalate to CS Manager immediately if you cannot execute the extension within 30 minutes.

---

## Step 4 — Fix or Escalate

| Issue | Fix | Escalate To |
|---|---|---|
| Req IDs not in feed | Open parallel [[Inbound-Feed-Jobs-Down]] track | Feed Engineering via Ad Ops |
| New budget < MTD spend | Alert CSM + client before proceeding | CSM |
| Publisher config non-standard | Loop in Ad Ops before going live | Ad Ops |
| UTMs not passing post-update | Open [[Tracking-Attribution-Investigation]] | Ad Ops + Tech Ops if unresolved in 2 hrs |
| MOJO system error / cannot save | Screenshot error, try again, if persistent | Tech Ops |
| Campaign expired — Sev 1 | Immediate extension execution | CS Manager if blocked |
| Spend spike after budget update | Open [[Spend-Spike-Investigation]] | Ad Ops + CSM |
| Client requesting media plan before creation | Pause creation, open [[Media-Planning-Media-Buying]] | CSM |

---

## Step 5 — Post-Resolution Message

Send after all changes are confirmed live in MOJO.

**Email Template — Resolution:**

> Subject: Re: [Ticket Subject] — [Client Name] — Completed
>
> Hi [Client Name],
>
> Your request has been completed. Here's a summary of what was done:
>
> **Action taken:** [Brief description — e.g., "Campaign paused", "Budget updated", "UTM tags updated and tested"]
> **Effective as of:** [Date/Time]
> **Details:**
> - [Bullet 1 — e.g., Campaigns paused: [Campaign Names]]
> - [Bullet 2 — e.g., New budget: $X, effective [Date]]
> - [Bullet 3 — e.g., Publisher-level changes coordinated with Ad Ops]
>
> If you notice any discrepancies in pacing or delivery in the next 24 hours, please don't hesitate to reach out and we'll investigate immediately.
>
> Best,
> [Your Name]
> Joveo Customer Support

---

## Escalation Triggers

Escalate immediately (do not wait for the 2-hour resolution window to expire) in any of the following situations:

- Campaign is live and overspending after a budget update → [[Spend-Spike-Investigation]] + CS Manager
- Req IDs are missing from feed and campaign creation is blocked → Feed Engineering + Ad Ops
- Client threatens churn or expresses high dissatisfaction → CSM immediately
- Sev 1 campaign extension cannot be executed within 30 minutes → CS Manager
- MOJO is not saving changes / system error affecting multiple tickets → Tech Ops + CS Manager (potential outage)
- Budget update results in a value below MTD spend and client cannot be reached → Do not apply update; escalate to CSM

---

## Related Skills

- [[Performance-ROI-Investigation]] — when a campaign change is motivated by poor performance results
- [[Publisher-Channel-Management]] — when publisher-specific setup or activation is needed as part of campaign creation
- [[Tracking-Attribution-Investigation]] — when UTM update is prompted by tracking breaking or data discrepancy
- [[Spend-Spike-Investigation]] — when budget changes are related to or triggered by an overspend event
- [[Inbound-Feed-Jobs-Down]] — when Req IDs are not in feed during campaign setup
- [[Media-Planning-Media-Buying]] — when client needs a media plan or recommendation before campaign creation proceeds

---

*Last updated: June 2026 | Owner: Support Ops*
