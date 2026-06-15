---
title: "Tips to create flows with AI - Google Workspace Learning Center"
source_url: "https://support.google.com/a/users/answer/16430486"
product_area: "workspace-studio"
retrieved_at: "2026-06-15T17:31:28Z"
extraction_method: "web_extract"
---

# Tips to Create Flows with AI — Google Workspace Studio

**Source:** Google Workspace Learning Center  
**URL:** https://support.google.com/a/users/answer/16430486

## Overview

Google Workspace Studio lets users automate routine tasks across Google Workspace and other supported services by describing a workflow in natural language. Gemini can then attempt to create the flow automatically.

> “To quickly automate routine tasks across Google Workspace and more, you can describe a workflow in Google Workspace Studio and Gemini will try to create it for you.”

**Action:** [Open Studio](https://studio.workspace.google.com/)

---

## Important Availability Note

- Users signed in with a **school account** who are **under 18** cannot use AI features in Workspace Studio.
- If a flow containing AI steps is shared with such a user, the AI steps are removed when they open the flow.

> “If you're signed in with a school account and are under 18, you can’t use any AI features in Workspace Studio. If a flow containing AI steps is shared with you, those steps will be removed when you open the flow.”

---

# Best Practices for Prompting Gemini in Workspace Studio

For best results, requests should be specific, structured, and explicit about triggers, people, apps, and supported content.

## 1. Say When the Flow Should Start

A flow only runs when certain conditions are met. Gemini needs a clear trigger, such as a schedule, an incoming message, or an edit to a specific file.

**Key guidance:**

- Be specific about timing.
- Identify exact senders or files.
- Provide links or names where relevant.

### Examples

| Instead of... | Try this... |
|---|---|
| Each week | Every Monday at 4 pm |
| When I hear from my manager | When I get email from `<manager’s email address>` |
| When our tracker is edited | When the `<link or name of file in Drive>` is edited |

---

## 2. Specify People by Email Address

Gemini may not reliably infer who “my manager” or another role refers to. Use exact email addresses.

### Example

| Instead of... | Try this... |
|---|---|
| Send an email to my manager | Send an email to `<email address>` |

---

## 3. Say Which Apps to Use

Specify the Google Workspace app or destination so Gemini understands how to perform the task.

### Examples

| Instead of... | Try this... |
|---|---|
| Send me a message after the weekly sync with my action items | Message me in Chat after the weekly sync with my action items |
| Track action items I get in messages | Create tasks from action items in my email<br>_or_<br>Add action items from my email to `<link to document>` |

---

# Unsupported or Limited Content to Avoid

Gemini in Workspace Studio is still improving. Current limitations include:

- Requests should be entered in **English**.
- Only include links to:
  - Files in Google Drive
  - Other websites
- Gemini **cannot use links** to:
  - Calendar events
  - Meet video conferences
- Specify people using **email addresses**, not `@mentions`.
- Avoid external apps and services in AI-generated requests, including:
  - [Add-on steps you install](https://support.google.com/workspace-studio/answer/16433731)
  - [Integration steps](https://support.google.com/workspace-studio/answer/16658279)
- Unsupported steps can be added manually later.

---

# Practical Prompting Checklist

Before submitting a request to Gemini in Workspace Studio, make sure your prompt includes:

- **Trigger:** When should the flow start?
  - Example: “Every Monday at 4 pm”
- **People:** Who is involved?
  - Use exact email addresses.
- **Apps:** Where should actions happen?
  - Example: Gmail, Chat, Tasks, Docs, Drive
- **Files or locations:** Which document, tracker, or Drive file should be used?
  - Provide a file name or Drive link.
- **Supported content only:**
  - English prompts
  - No Calendar event or Meet conference links
  - No `@mentions`
  - No external app or integration steps unless added manually later

---

## Related Resource

- [Print, save, or customize Learning Center guides](https://support.google.com/a/users/answer/9343015?hl=en&ref_topic=10769893) — Learn how to print Learning Center guides, save them as PDFs, or customize them for your organization.
