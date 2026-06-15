# Get started with Google Workspace Studio - Workspace Studio Help

**Product Area:** workspace-studio
**Source:** https://support.google.com/workspace-studio/answer/16444479?hl=en

# Get Started with Google Workspace Studio — Summary

**Source:** [Google Workspace Studio Help](https://support.google.com/workspace-studio/answer/16444479?hl=en)

## Overview

Google Workspace Studio lets you automate routine tasks across Google Workspace and other apps using Gemini. It can connect services such as Gmail, Sheets, Drive, Chat, Forms, and third-party apps to create automated workflows called **flows**.

Example automations include:

- Saving email attachments to a specific Google Drive folder.
- Sending a Google Chat notification when someone submits a Google Form.
- Analyzing new emails and generating an AI-powered summary.

---

## Core Concepts: Flows, Starters, and Steps

Every Workspace Studio flow has **2 main parts**:

### 1. Starter

> **Starter:**  
> This is the event that starts your flow. A starter can be a schedule, like “every Friday at 5 PM,” or an event, like to receive a new email with an attachment.

Key facts:

- Each flow has **only one starter**.
- Starters define **when or why** a flow begins.
- Examples:
  - A schedule, such as every weekday morning.
  - An event, such as receiving a new email with an attachment.

### 2. Step

> **Step:**  
> This is a task your flow performs after it starts. A step can be an action, like “draft a reply,” or a notification, like “notify me in Chat.”

Key facts:

- A flow can have **multiple steps**.
- Steps define the actions taken after the starter runs.
- Examples:
  - Drafting a reply.
  - Sending a notification in Google Chat.
  - Summarizing emails with Gemini.

---

## Workspace Studio Requirements

### Device Requirement

- You must use a **computer with a supported web browser** to create flows.
- Once a flow is active, it can run on **any device**.

### Eligible Accounts

Workspace Studio is available for:

- Work accounts
- School accounts
- Personal Google accounts

#### Personal Accounts

Personal accounts require an eligible Google AI plan:

- **Google AI Pro**
- **Google AI Ultra**

#### Work or School Accounts

Work or school accounts require either an eligible Google Workspace edition or a Google AI expansion add-on.

Eligible editions/add-ons include:

- **Business Starter, Standard, and Plus**
- **Enterprise Standard and Plus**
- **Education Fundamentals, Standard, and Plus**
- **Teaching and Learning add-on**
- **Google AI Pro for Education**

### Smart Features

To get the most out of Workspace Studio, Google recommends turning on smart features in Google Workspace.

- Resource: [Turn on smart features in Google Workspace](https://support.google.com/workspace-studio/answer/16666382)

### Admin Settings

For work or school accounts:

- Your Google Workspace admin must enable **Gemini** on your account.

### App Access

Available templates depend on which Google apps your account can access.

Example:

- If Gmail is not enabled for your account, templates using Gmail steps will not appear.

Workspace Studio integrates with:

- Gemini
- Gmail
- Google Calendar
- Google Chat
- Google Drive
- Google Docs
- Google Forms
- Google Sheets
- Google Tasks

It also integrates with third-party apps, including:

- Asana
- Mailchimp
- Salesforce

### Age Restriction

> If you're signed in with a school account and are under 18, you can’t use any AI features in Workspace Studio. If a flow containing AI steps is shared with you, those steps will be removed when you open the flow.

---

## Tutorial: Create Your First Flow

The article recommends starting with a template as the easiest way to learn Workspace Studio.

The tutorial example creates a flow that:

- Uses Gemini to review unread emails.
- Sends a daily summary to you in Google Chat.

---

## Step 1: Choose a Template

1. On your computer, go to [studio.workspace.google.com](http://studio.workspace.google.com/).
2. On the **Discover** page, review the list of pre-built flow templates.
3. Click the **Get a daily summary of unread emails** template.

This opens the flow editor, where you can configure the flow.

---

## Step 2: Configure Your Flow

The selected template already contains the logic, but you can review each part to understand how it works.

### Step 1: On a Schedule

- This is the **starter**.
- It controls when the flow runs.
- By default, it may run every weekday morning.
- You can change the time or frequency.

### Step 2: Recap Unread Emails

- This is an **AI-powered step**.
- It looks at emails from **“Yesterday.”**
- Gemini generates a summary.
- The default prompt and settings can be left unchanged.

### Step 3: Notify Me in Chat

- This step sends the summary to Google Chat.
- In the **Message** field, there is a blue variable chip:

```text
[Step 2: Summary of unread email]
```

This variable tells the flow to use the AI summary created in Step 2 and send it as a Chat message.

---

## Step 3: Test and Turn On Your Flow

### Important Warning

> **Important:** A test run takes real actions. It will send messages, update files, and set up meetings.

To 

[... summary truncated for context management ...]
