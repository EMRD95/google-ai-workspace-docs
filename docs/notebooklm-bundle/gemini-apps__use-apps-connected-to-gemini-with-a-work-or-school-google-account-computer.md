# Use apps connected to Gemini with a work or school Google Account - Computer - Gemini Apps Help

**Product Area:** gemini-apps
**Source:** https://support.google.com/gemini/answer/14959807?hl=en

# Use Apps Connected to Gemini with a Work or School Google Account — Summary

Source: Google Gemini Apps Help  
URL: https://support.google.com/gemini/answer/14959807?hl=en

## Overview

Gemini Apps can connect with other services, called **apps**, to provide more useful responses for work or school Google Accounts.

With connected apps, Gemini can help you:

- Find information from **Gmail**
- Summarize documents from **Google Drive**
- Find and summarize information from **Google Chat** in English
- Add and show tasks from **Google Tasks**
- Create and show notes and lists in **Google Keep**
- Create, find, and edit events in **Google Calendar**
- Attach a **GitHub repository** to better understand a codebase and debug issues

> **Important:** If you’re using Gemini Apps with a personal account, see Google’s separate guidance on using Connected Apps in Gemini.

---

## Requirements

To connect apps to Gemini with a work or school Google Account, all of the following must be true:

- You have a **qualifying edition of Google Workspace**.
- Your **Keep Activity** setting is turned on.
  - Only your organization’s Google Workspace administrator can manage this setting.
- Your Google Workspace administrator has enabled the ability to connect apps to Gemini.
  - Workspace administrators can manage access to apps in Gemini through the admin settings.

---

## How to Use Apps in Gemini

> **Important:** Gemini Apps can hallucinate responses or provide outdated information, such as referencing an older email when a newer one exists. To verify information, click and review the sources listed after Gemini’s response.

### Steps

1. Go to [gemini.google.com](https://gemini.google.com/).
   - If connecting to a Google Workspace app, make sure you’re signed in to the same Google Account you use with Google Workspace.

2. In the text box, enter:

   ```text
   @
   ```

   Then select the app you want to use.

   - Tip: Enter `@`, select **Google Drive**, and reference Workspace content using keywords from the content.

3. Ask Gemini to get information from the selected app or service.

4. Click **Submit**.

If the app has been enabled by your Workspace administrator, Gemini Apps will automatically use it.

---

## Example Prompts

### Find information

```text
What dates did Erik propose in the email about the team offsite?
```

### Summarize a document

```text
Find notes from the latest team meeting titled “Team Meeting June 2023” from my drive and summarize it to a short paragraph
```

### Simplify and organize information

```text
Find the doc from Ashley about the website clean-up project and summarize the proposal for me in 5 bullets
```

---

## Available Connected Apps

> **Important:** Availability of Connected Apps varies by account type, Google Workspace edition, location, language, device, and Gemini app.

When signed in with a work or school account, Gemini can interact with services through the **Google Workspace app**, including:

- **Gmail**
- **Google Calendar**
- **Google Chat**
  - Currently available in English if you have Gemini Apps as a core service
- **Google Docs**
- **Google Drive**
- **Google Keep**
- **Google Tasks**

On the **Gemini web app on a computer**, you can also import a **GitHub repository** into your chat and ask Gemini questions about its code using the **GitHub app**.

---

## Troubleshooting: Why You Can’t Use an App

### You need to explicitly mention the app

For a new conversation, you must explicitly ask Gemini to use the app or service.

Example workflow:

1. Enter:

   ```text
   @
   ```

2. Select **Google Drive**.
3. Use keywords from the content you want Gemini to reference in your prompt.

You do **not** need to repeat this for follow-up questions in the same conversation.

---

### The app may not be enabled by your organization

For work or school accounts, app access must be enabled by your Google Workspace administrator.

If your prompt includes multiple actions requiring separate apps or services, and one or more of those services are not enabled, **none of the related actions will be completed**.

Example:

- You ask Gemini to:
  - Create a calendar event
  - Create a reminder for that event
- But the **Tasks app** is not enabled

Result:

- The calendar event will **not** be added.
- The reminder will **not** be created.

Workspace administrators can manage access to apps in Gemini through admin controls.

---

## What Gemini Can’t Do with Connected Apps

> **Important:** Your Google Workspace administrator can enable or disable access to apps. If you can’t access a certain app in Gemini, contact your administrator.

Gemini Apps **can’t**:

- Access attachments, comments, or images in **Docs** or **Gmail**
- Access folders, presentations, spreadsheets, pictures, or videos in **Drive**
  - This includes any content that isn’t in a document or PDF
  - To access multiple documents in one prompt, mention all desired files in the prompt
- Create email drafts or d

[... summary truncated for context management ...]
