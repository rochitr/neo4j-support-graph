# Skill: Manual Feed Management
**Theme:** Manual Feed Creation & Editing
**SLA Severity / Category:** Sev 2 — Standard / Feed Operations
**Primary Owner:** Customer Support
**Internal SLA:** 1 hr acknowledgement | 6 hr resolution (edits to existing feeds) | 10 hr resolution (job additions)
**Escalation Path:** CS Manager → CSM → CS Ops Director

---

## When to Use This Skill

Use this skill when a client requests:
- **Edits to an existing manual feed** — updating job titles, locations, descriptions, apply URLs, removing jobs, or structural changes to feed format
- **Addition of new jobs to a manual feed** — adding net-new job records with all required fields

This skill applies only to **manual feeds** — feeds that Joveo manages directly, not feeds generated automatically by an ATS. If the issue is that an ATS-generated feed has stopped delivering jobs, refer to [[ATS-Integration-Triage]]. If the feed itself appears to be broken or jobs have dropped off the platform unexpectedly, refer to [[Inbound-Feed-Jobs-Down]].

---

## Step 1 — Acknowledge the Request

Reply within 1 hour of receiving the request.

**Acknowledgement Email Template:**

> Subject: Re: Feed Update Request — [Client Name]
>
> Hi [Name],
>
> Thank you for reaching out. I've received your request to [edit jobs in / add jobs to] your manual feed and will get started on this now.
>
> To complete the update accurately, could you please confirm/provide the following:
> - The specific jobs or fields to be updated (for edits)
> - Full job details for all new jobs to be added: job title, location, Req ID, job description, apply URL, and any publisher-required fields
> - Confirmation of any apply URLs — please verify these are live and directing to the correct job page
>
> I'll have this completed and confirmed within [6 / 10] hours.
>
> Best,
> [Your Name]

---

## Step 2 — Confirm the Scope of Changes

Before touching any feed file, confirm exactly what changes are required. Do not make assumptions — incorrect feed edits can cause jobs to stop delivering or apply URLs to break.

**For edits to existing feeds:**
- Which specific jobs need to be edited (identify by Req ID or job title + location)
- Which fields need to change (title, location, description, apply URL, salary, etc.)
- Whether any jobs need to be fully removed from the feed
- Whether there are structural changes to the feed format itself (e.g., adding a new required field)

**For job additions:**
- Full details for every new job being added — see required fields in Step 4B
- Confirmation of which campaign(s) these jobs should be assigned to in MOJO after ingestion

---

## Step 3 — Access the Feed

1. Locate the feed file in MOJO or the designated feed management storage location for this client.
2. **Download a backup copy** of the current feed file before making any edits. Save it with the date in the filename (e.g., `ClientName_Feed_Backup_2026-06-04.xml`). This is mandatory — if the edit causes a validation failure, you need to restore from the backup.
3. Open the feed file in the appropriate editor.

---

## Step 4A — Execute Edits to an Existing Feed

1. Make the confirmed edits:
   - **Field updates**: Update the relevant XML/CSV fields for each identified job. Ensure values are correctly formatted and do not contain characters that break XML parsing (e.g., unescaped `&`, `<`, `>`).
   - **Job removals**: Remove the complete job record for any jobs being taken down. Do not leave partial records.
   - **Structural changes**: If adding or removing a feed-level field, apply the change consistently across all job records — partial field population causes ingestion failures.
2. **Validate apply URLs** — for any job being edited, paste the apply URL into a browser and confirm it loads a live, correct job page. A broken apply URL means the job cannot receive applications even if it appears on publisher sites.
3. **Check for duplicate job IDs** — ensure no two jobs share the same Req ID / job ID field in the feed. Duplicates cause ingestion errors in MOJO.
4. Ensure all **required fields are present** on every job record: title, location, Req ID, description, apply URL, and any publisher-mandated fields (e.g., Indeed requires `<category>`, some boards require salary).

---

## Step 4B — Execute Job Additions to a Feed

Collect all required fields for each new job before adding to the feed. Do not add incomplete records.

**Minimum required fields for all jobs:**
| Field | Notes |
|---|---|
| Job Title | Must be a clear, recognizable job title — avoid internal jargon |
| Location | City, State at minimum; include ZIP code if available |
| Req ID / Job ID | Unique identifier — must not duplicate any existing job in the feed |
| Job Description | Full job description; minimum 150 words recommended for publisher acceptance |
| Apply URL | Must be a live URL directing to the correct application page |

**Publisher-specific additional fields (check per publisher requirements):**
- Salary / pay range (increasingly required by Indeed, LinkedIn, and others)
- Employment type (Full-time, Part-time, Contract)
- Job category
- Company name
- Remote/hybrid indicator

Steps:
1. Add each new job record to the feed file, formatted consistently with existing entries. Copy an existing record as a template to avoid format mismatches.
2. Validate every apply URL before saving — open each one in a browser and confirm it is live.
3. Check that all new Req IDs are unique within the feed.
4. Save the updated feed file.

---

## Step 5 — Trigger Feed Refresh in MOJO

1. Upload the updated feed file to MOJO or trigger a manual feed re-ingestion from the MOJO feed management interface.
2. Monitor the ingestion process — check for any errors or warnings in the MOJO feed log.
3. If ingestion fails: review the error message carefully. Common causes:
   - XML parsing error → a field contains an unescaped special character
   - Duplicate job ID → two records share the same Req ID
   - Missing required field → a mandatory field is blank on one or more records
   - Apply URL format error → URL is malformed
4. Fix the issue and re-trigger ingestion. If the error is unclear, escalate to CS Manager.

---

## Step 6 — Validate in MOJO

After successful ingestion:
1. Navigate to the job list in MOJO for this client account.
2. Confirm:
   - New jobs appear in the MOJO job list with correct titles, locations, and apply URLs
   - Edited jobs reflect the updated field values
   - Removed jobs no longer appear
3. Confirm new/edited jobs are assigned to the correct campaigns. If they need to be manually assigned to a campaign, refer to [[Campaign-Management]].
4. Spot-check 3–5 apply URLs directly from the MOJO job list to ensure they are resolving correctly.

---

## Step 7 — Confirm with Client

**Confirmation Email Template:**

> Subject: Re: Feed Update — [Client Name] — Complete
>
> Hi [Name],
>
> The feed update has been completed. Here is a summary of what was done:
>
> - [X jobs updated / Y jobs added / Z jobs removed]
> - All changes have been validated in MOJO and jobs are appearing correctly
> - Apply URLs have been verified as live
>
> If you notice any discrepancies or have additional changes, please let me know.
>
> Best,
> [Your Name]

---

## Escalation Triggers

Escalate immediately if any of the following apply:

- **Feed ingestion is failing repeatedly** after multiple fix attempts — escalate to CS Manager and flag for engineering review
- **Apply URLs are broken and the client cannot provide working URLs** — do not add jobs to the feed with broken apply links; escalate to CSM to resolve with the client
- **Structural feed changes are required** that go beyond adding/editing individual job records (e.g., feed schema changes, new field types, feed format conversion) — escalate to Tech Ops or engineering
- **Jobs are not appearing in MOJO after successful ingestion** — may indicate a campaign assignment or platform issue; refer to [[Inbound-Feed-Jobs-Down]] and escalate if unresolved within 2 hours
- **Client requests changes to more than 50 jobs** in a single update — flag to CS Manager for prioritization and to assess whether a bulk import tool is more appropriate

---

## Related Skills

- [[Inbound-Feed-Jobs-Down]] — For feed structural or ingestion failures that occur outside of manual editing; also for jobs disappearing unexpectedly from the platform
- [[ATS-Integration-Triage]] — If the underlying issue is an ATS not exporting jobs automatically and the client needs a manual feed as a workaround
- [[Campaign-Management]] — If new jobs added to the feed need to be assigned to active campaigns after ingestion

---

*Last updated: June 2026 | Owner: Support Ops*
