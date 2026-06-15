---
title: "Troubleshoot issues with flows - Workspace Studio Help"
source_url: "https://support.google.com/workspace-studio/answer/16430806"
product_area: "workspace-studio"
retrieved_at: "2026-06-15T17:46:37Z"
extraction_method: "web_extract"
---

# Troubleshoot Issues with Flows — Workspace Studio Help

**Source:** Google Workspace Studio Help  
**URL:** https://support.google.com/workspace-studio/answer/16430806

---

## Important Eligibility Note

> **Important:**  
> If you're signed in with a school account and are under 18, you can’t use any AI features in Workspace Studio. If a flow containing AI steps is shared with you, those steps will be removed when you open the flow.

---

## Error Indicators

When a flow has an issue, Workspace Studio shows notifications in several places:

- A **red dot** on the **Google Workspace Studio icon** in Gmail.
- A message on the **My flows** tab in the Studio web app.
- A red dot in the **Activity** tab in the Studio web app.

### Common Causes of Flow Failures

Flows can fail because of:

- **Invalid data during a run**
  - Example: drafting an email to an invalid email address.
- **Step configuration errors**
  - Example: losing access to a Chat space or a deleted Google Doc used by a step.
- **Usage limits or proactive security measures**
  - Flows that run too often may hit usage limits.
  - Flows may stop if malicious content or a possible prompt injection attack is detected.

### How to Investigate

- Click the flow that had the problem.
- For **invalid data issues**:
  - Review the flow’s **activity feed** to find problematic data.
  - Add **“Check If”** steps to detect invalid or empty variables.
- For **configuration issues**:
  - Check the error message on the affected step.

> After you resolve the issue, dismiss the warning. If you don’t, the flow still counts as a flow with issues.

---

## General Troubleshooting Note

> **Note:** Workspace Studio is in active development and bugs are fixed regularly. If a flow stops working, review its set up and then try turning on the flow again to pick up any bug fixes.

---

# Common Issues and Fixes

## Issues When Turning On a Flow

| Error message | Reason and resolution |
|---|---|
| **The starter or a step isn't set up correctly** | The flow setup is missing a required field. Click each item to find and fix the issue. |
| **Couldn’t turn on flow. Please try again.** | Possible causes:<br><br>- You already have **100 flows turned on**. Turn off or delete an active flow to enable a new one.<br>- You already have **25 active flows that use the Gmail starter**. Turn off or delete an active Gmail-starter flow.<br>- Workspace Studio encountered an error. Wait a few minutes and try again. If it still fails, click **Help → Send feedback to Google** to report a bug. |

---

## Issues While Running a Flow

Errors during a flow run appear in the **activity log**.

| Error message | Reason and resolution |
|---|---|
| **After trying several times, your flow couldn't complete this run** | Possible causes:<br><br>- For work or school accounts, your Google Workspace administrator may have disabled the app or service used in the step.<br>- Make sure **Smart features** are turned on.<br>- The step may be restricted to the **Gemini Alpha program**.<br>- The app developer may have removed or ended support for the step.<br>- The step hit a bug and could not complete. |
| **Workspace Studio is missing permissions** | Workspace Studio needs permission to connect to other apps and services. Try turning the flow on again.<br><br>- **Work or school accounts:** If it still fails, your admin may have blocked access.<br>- **Personal accounts:** Check that you haven’t revoked Workspace Studio access in your Google Account security settings. |
| **The prompt, including content referenced with variables and links, exceeded Gemini limits. Consider editing your prompt, such as using fewer variables.** | Applies to AI steps. The prompt must be under approximately **144,000 characters**, or roughly **18,000 words**, including linked content and variables.<br><br>This often happens when a variable includes a long email body or thread. Reduce the number of variables in the prompt. |
| **Couldn't start because "Google Workspace smart features" in your Gmail settings are turned off** | Some flows require Google Workspace smart features. Ensure both **Smart features** and **Google Workspace smart features** are turned on. |
| **Content couldn’t be shared with Gemini** | **Work or school accounts:** Admin settings may prevent downloading or copying files, which also prevents Gemini access. Contact your admin.<br><br>**Personal accounts:** The file may have encryption or restrictive sharing settings. Ensure the file isn’t restricted. |
| **Flow was automatically turned off because it hasn't run in 6 months** | If a flow doesn’t run for **6 months**, it automatically turns off.<br><br>To turn it back on:<br>1. Go to **My flows**.<br>2. Click the flow.<br>3. Click **Turn on**. |
| **Couldn’t send message** | **Personal accounts:** This can happen if the flow has a Chat step but you haven’t used Google Chat before.<br><br>To fix:<br>1. In Gmail, click **Chat** to initialize the service.<br>2. Ru

[... summary truncated for context management ...]
