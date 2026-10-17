# Skill: Informational Requests
**Theme:** Informational Requests
**SLA Severity / Category:** Sev 3 — Low / Informational
**Primary Owner:** Customer Support
**Internal SLA:** 1 hr acknowledgement | 4 hr resolution
**Escalation Path:** CS Manager → CSM → CS Ops Director

---

## When to Use This Skill

Use this skill when a client asks a question that requires information but not a technical fix or configuration change. Typical examples:
- "Where do I find [metric / report / export] in UA or MOJO?"
- "How do I filter by [dimension] in my analytics dashboard?"
- "Does Joveo support [feature or capability]?"
- "Can Joveo integrate with [tool or ATS]?"
- "What happens to my campaigns when [scenario]?"

> If the client cannot find data because it is **actually missing** from the platform (not just hard to locate), this is not an informational request — refer to [[UA-Reporting-Discrepancy]].
>
> If the question is being asked during onboarding (first 60 days) and relates to platform configuration — refer to [[Onboarding-Project-Management]] for escalation to the Implementation team.

---

## Step 1 — Acknowledge the Request

Reply within 1 hour.

**Acknowledgement Email Template:**

> Subject: Re: [Client Name] — Question About [Topic]
>
> Hi [Name],
>
> Thanks for reaching out. Happy to help with this.
>
> I'm looking into [their question] now and will come back to you with a clear answer shortly — typically within a few hours.
>
> If I need any clarification to make sure I'm answering the right question, I'll be in touch.
>
> Best,
> [Your Name]

---

## Step 2 — Understand the Exact Question

Before researching an answer, make sure you understand precisely what the client needs. A vague question leads to a vague answer that generates a follow-up ticket.

- If the question is about navigation: what exactly are they trying to find? Which metric, dimension, time period, or export format?
- If the question is about capability: what is the specific use case they are trying to solve? "Does Joveo support X" is better answered as "here's how you can solve [use case]" rather than a binary yes/no.
- If the question is unclear: reply with a quick clarifying question before researching. Do not spend time researching the wrong thing.

---

## Step 3A — Answer Navigation / Analytics Questions

Use the lookup table below to identify the correct location for common requests. Provide **step-by-step navigation instructions** in your reply — not just the name of the report.

### UA Navigation Reference

| What the client wants to find | Where to find it |
|---|---|
| Overall spend and applies | UA → Reports → Campaign Performance → select date range → review Spend and Applies columns |
| Publisher-level breakdown | UA → Reports → Publisher Performance → filter by campaign or date range |
| CPA / Cost per apply | UA → Reports → Campaign Performance → CPA column (or calculate: Spend ÷ Applies) |
| Funnel / conversion data | UA → Campaign Intelligence → Funnel Report → select campaign |
| Job-level performance | UA → Reports → Job Performance → filter by campaign or job title |
| Candidate data and profiles | Talent CRM → Candidates → search by name, job, or campaign |
| Budget utilization | UA → Reports → Campaign Performance → compare Spend to Budget column |
| Organic vs. paid breakdown | UA → Reports → Source Breakdown → filter by traffic type |
| Exporting data | Any UA report → click Export → select CSV or Excel format |

### MOJO Navigation Reference

| What the client wants to find | Where to find it |
|---|---|
| Active job list | MOJO → Jobs → Active Jobs |
| Campaign configuration | MOJO → Campaigns → select campaign name |
| Feed status | MOJO → Feeds → view last ingestion time and status |
| Publisher assignment | MOJO → Campaigns → Publishers tab |
| Budget settings | MOJO → Campaigns → Budget tab |

### Steps:
1. Identify exactly what the client is looking for using the table above.
2. Write step-by-step navigation instructions specific to the client's question. Example:
   > "To find your publisher-level CPA breakdown: log in to UA → click Reports in the left menu → select Publisher Performance → set your date range in the top right → the CPA column shows cost per apply by publisher. You can click any column header to sort. To export, click the Export button in the top right and choose CSV."
3. If the question requires a screenshare to explain clearly, offer a 15-minute live walkthrough:
   > "If it would be easier, I'm happy to walk you through this on a quick screenshare — just let me know and I can get something scheduled today."
4. **Flag recurring navigation confusion** to the CSM. If the same client is asking navigation questions repeatedly, this is a signal that they need a UA training session — refer to [[Proactive-Consulting-Advisory]].

---

## Step 3B — Answer Capability Questions

1. **Understand the exact use case** before researching. Ask: what is the client trying to accomplish? What problem are they solving?
2. Research the answer internally using the following hierarchy:
   a. **Check Joveo's internal knowledge base / product documentation** — is this capability documented?
   b. **Ask the CSM or a senior CSE** — does someone on the team know the answer from direct experience?
   c. **Check the product roadmap** (internal) — is this feature planned?
   d. **Check JIRA** — has this been requested before? What was the outcome?
3. Categorize the answer:
   - **Already supported and available**: explain how to use it with navigation steps
   - **Supported but requires configuration**: explain that it can be set up and initiate the configuration request
   - **On the product roadmap**: share roadmap status carefully (see caveat below)
   - **Not currently supported**: acknowledge clearly and log as a feature request if appropriate
4. **Frame your answer as a solution to their use case**, not just a yes/no on the feature.
5. **NEVER overpromise** — do not commit to capabilities that have not been confirmed by Product. Do not share specific roadmap delivery dates unless explicitly cleared by the Product team. If uncertain, say: "Let me confirm the current status with our product team and come back to you — I want to make sure I'm giving you accurate information."

---

## Step 4 — Log Feature Requests (Sev 2: Product / Feature Roadmap Suggestions)

When a client's capability question reveals a genuine need that Joveo does not currently support, log it as a feature request:

1. **Log in JIRA** with the following information:
   - Client name and account ID
   - Feature or capability requested
   - Business use case — what problem is the client trying to solve? Why does this matter to them?
   - Impact estimate — how many clients might benefit from this feature?
   - Priority assessment — is this blocking the client, or is it a nice-to-have?
   - Date logged
2. **Validate with the client** that your understanding of the request is correct:
   > "I've logged your request for [feature] with our product team. Just to confirm — the core need is [your description of their use case]. Is that right?"
3. **Check existing roadmap** — has this been logged before? If so, reference the existing ticket and check on its status.
4. **Share with the Product team** — add the JIRA ticket to the relevant product backlog triage queue. Tag the CSM.
5. **Update the client** on roadmap status:
   - If it's on the roadmap: share a general timeframe if known and explicitly approved to share ("We hope to have this available in Q3 — I'll keep you posted as it progresses.")
   - If it's not currently on the roadmap: acknowledge the request warmly and honestly ("I've logged this with our product team. I can't make any commitments on timing, but I want to make sure your feedback is captured.")
6. **Follow up when status changes** — if the feature ships or reaches a milestone, proactively notify the client.

---

## Step 5 — Close the Ticket

1. Confirm the client received a complete and useful answer.
2. If no response from the client within 48 hours of your answer: send a brief follow-up to confirm the question was answered.
3. Mark the ticket resolved only after confirmation or after the 48-hour follow-up receives no further questions.
4. **Document recurring questions** — if this question has come up before from this client or from multiple clients, flag it to the CSM as a training opportunity per [[Proactive-Consulting-Advisory]].

---

## Escalation Triggers

Escalate immediately if any of the following apply:

- **You cannot find the answer** within the knowledge base, product documentation, or from a senior team member — escalate to CS Manager before providing a response to the client
- **The client's capability question reveals a significant gap** that may affect their contract, expectations, or ability to achieve their hiring goals — escalate to CSM immediately
- **The client is asking capability questions that suggest they were sold something Joveo cannot deliver** — escalate to CSM and CS Ops Director; do not handle this as a standard informational request
- **A navigation question reveals that data is actually missing** from the platform — refer to [[UA-Reporting-Discrepancy]]

---

## Related Skills

- [[UA-Reporting-Discrepancy]] — If the client cannot find data because it is actually missing or incorrect (not just hard to locate)
- [[Proactive-Consulting-Advisory]] — Recurring informational requests signal a need for proactive training; flag patterns to the CSM
- [[Onboarding-Project-Management]] — Capability questions during the first 60 days of a new client relationship should be escalated to the Implementation team

---

*Last updated: June 2026 | Owner: Support Ops*
