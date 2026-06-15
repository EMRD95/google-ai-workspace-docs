# Workspace Studio — Google AI Documentation (12 docs)

Combined for easy NotebookLM import. Each section is a separate help article.

---

## 1. Create a flow from scratch - Workspace Studio Help

**Source:** https://support.google.com/workspace-studio/answer/16447954?hl=en

# Create a Flow from Scratch – Workspace Studio Help

## Overview
Build a fully custom automation in Google Workspace Studio by creating a flow from scratch. Every flow consists of:

- **Starter** – the event or schedule that launches the flow (only one per flow).  
- **Step(s)** – tasks the flow performs after starting (actions, notifications, etc.). You can add multiple steps.

**Variables** are placeholders that automatically fill with data from previous steps, making flows dynamic (e.g., inserting the email subject into a Chat message).

---

## Quick Creation Steps

1. Go to [https://studio.workspace.google.com](https://studio.workspace.google.com/) and click **New flow**.
2. Click the **Starter** to choose the event or schedule that launches your flow.
3. Click **Choose a step** and select the task the flow will perform.
4. Name your flow by clicking the pencil icon at the top.
5. **(Optional)** Click **Test run** → **Start** to verify the flow immediately. A “Run Completed” message indicates success.
6. Once satisfied, click **Turn on**.

---

## Detailed Example: Auto-draft an Invoice Reply

This example creates a flow that automatically drafts a Gmail reply whenever an email containing the word “Invoice” arrives.

### Step 1 – Choose Your Starter
1. Click **New flow** → **Choose a starter** → **When I get an email**.
2. In the configuration panel, under *Which messages to check*, select **Specific emails**.
3. In the **Has the words** field, enter: `Invoice`.  
   *(This runs the flow only when an email’s subject or body contains “Invoice”.)*

### Step 2 – Add a Step
4. Below the starter, click **Choose a step** → under **Gmail**, select **Draft a reply**.

### Step 3 – Use Variables for a Dynamic Message
5. Inside the **Message** field of the “Draft a reply” step, type:

   ```
   Hello,

   I received the invoice regarding: [Email subject]

   I will review it and get back to you.
   ```
   - Insert `[Email subject]` by clicking **Variables +** → **Step 1: When I get an email** → **Email subject**.  
   - When the flow runs, the variable chip is replaced with the actual email subject.

### Step 4 – Name, Test & Turn On
6. Click the pencil icon to name your flow (e.g., “Invoice Draft Reply”).
7. Click **Test run**.
   - In the test window, type `Invoice` in the “Email received” field to find a matching recent email.
   - Select an email and click **Start**.
   - A “Run Completed” message indicates success; check your Gmail Drafts for the new draft.
8. Click **Turn on** to activate the flow.

---

## Key Concepts

- **Starter**: Event or schedule that triggers the flow. Example: “When I get an email” with filters.
- **Step**: An action (e.g., “Draft a reply”) or notification.
- **Variables**: Insert dynamic content from previous steps, like `[Email subject]`.  
  *Learn more: [How to use variables to pass data in your flow](https://support.google.com/workspace-studio/answer/16448468).*

> **Tip:** Variables let you create powerful, context-aware automations.

---

## Related Resources
- [Create a flow with Gemini AI](https://support.google.com/workspace-studio/answer/16448469)
- [Create a flow from a template](https://support.google.com/workspace-studio/answer/16448808)
- [Manage and share your flows](https://support.google.com/workspace-studio/answer/16766368)

---

*For a full list of starters and steps, see the [Guide to Starters and Steps in Workspace Studio](https://support.google.com/workspace-studio/answer/16765661).*

---

## 2. Create a flow with Gemini AI - Workspace Studio Help

**Source:** https://support.google.com/workspace-studio/answer/16448469?hl=en

[Skip to main content](https://support.google.com/workspace-studio/answer/16448469?hl=en#search-form)

# Create a flow with Gemini AI

**Important:**

If you're signed in with a school account and are under 18, you can’t use any AI features in Workspace Studio. If a flow containing AI steps is shared with you, those steps will be removed when you open the flow.

To quickly create a flow, describe the tasks you want to automate and let Gemini build it for you.

For the best results, be specific in your description. Make sure to include:

- When the flow should start
- Which apps to use
- What steps the flow should take

To create a flow with Gemini AI:

1. On your computer, go to [https://studio.workspace.google.com](https://studio.workspace.google.com/).
2. In the "Describe a task for Gemini" box, enter a detailed description of what you want the flow to do.
   - **Good example:** "Notify me in Google Chat whenever I get an email from person@example.com"
   - **Bad example:** "Handle emails from person@example.com."
3. Click **Create**.

   - Gemini generates the steps for your flow.
     - Review each step to make sure it's correct.
     - You can edit, reorder, delete, or add new steps.
4. If a step needs info from a previous step, such as an email's subject line, add a variable. [Learn how to use variables to pass data in your flow](https://support.google.com/workspace-studio/answer/16448468).
5. Optional: Before you turn on your flow, to make sure it works properly, click **Test run**![and then](https://lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **Start**.

   - This runs the flow immediately so you can verify the output.
   - If everything works fine, you get a “Run Completed” message.
6. After you complete your edits, click **Turn on**.

## Related resources

- [Create a flow from a template](https://support.google.com/workspace-studio/answer/16448808)
- [Create a flow from scratch](https://support.google.com/workspace-studio/answer/16447954)
- [Manage & share your flows in Google Workspace Studio](https://support.google.com/workspace-studio/answer/16766368)

Give feedback about this article

Choose a section to give feedback on

true

Main menu

Google apps

8077214387172116138

true

Search Help Center

false

true

true

true

[Google Help](https://support.google.com/)

[Help Center](https://support.google.com/workspace-studio/?hl=en) [Workspace Studio](https://studio.workspace.google.com/)

[Privacy Policy](https://www.google.com/intl/en/privacy.html) [Terms of Service](https://www.google.com/accounts/TOS)Submit feedback

false

false

## What is the issue with this selection?

What is the issue with this selection?

Inaccurate - doesn't match what I see in the product

Hard to understand - unclear or translation is wrong

Missing info - relevant but not comprehensive

Irrelevant - doesn’t match the title and / or my expectations

Minor errors - formatting issues, typos, and / or broken links

Other suggestions - ideas to improve the content

## Share additional info or suggestions

​

​

Do not share any personal info

Cancel

Submit

By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/workspace-studio/answer/16448469?hl=en#) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).

false

false

false

---

## 3. Create and use custom steps in flows - Workspace Studio Help

**Source:** https://support.google.com/workspace-studio/answer/16433731?hl=en

[Skip to main content](https://support.google.com/workspace-studio/answer/16433731?hl=en#search-form)

# Create and use custom steps in flows

_This feature is in limited preview._

You can extend and customize Google Workspace Studio using Google Workspace add-ons. Just like add-ons for other services, you and other people in your organization can create custom steps so you can automate what you need most.

## On this page

- [Create custom steps](https://support.google.com/workspace-studio/answer/16433731?hl=en#create)
- [Install custom steps](https://support.google.com/workspace-studio/answer/16433731?hl=en#install)
- [Use custom steps in flows](https://support.google.com/workspace-studio/answer/16433731?hl=en#use)
- [Manage account access for add-on steps](https://support.google.com/workspace-studio/answer/16433731?hl=en#access)

## Create custom steps

![](https://storage.googleapis.com/support-kms-prod/4BMw4ze7sYv0aoC6pJUaNVGDdmDUWd1gje7A)

You and developers in your organization can create custom steps using Google Apps Script or your preferred coding language. You make them available to others by publishing them in the Google Workspace Marketplace.

[Learn how to create add-on steps](https://developers.google.com/workspace/add-ons/workflows).

## Install custom steps

![](https://storage.googleapis.com/support-kms-prod/4BMw4ze7sYv0aoC6pJUaNVGDdmDUWd1gje7A)

1. Go to [workspace.google.com/marketplace?host=workflow](https://workspace.google.com/marketplace?host=workflow).

This link takes you to a pre-filtered view of only add-ons and integrations that work with Workspace Studio.

2. When you find one you want to install, click it.
3. Click **Install**.
4. Follow the on-screen instructions to give the add-on permissions to access your Google Account data and complete the installation.

To uninstall an add-on step, go back to Workspace Marketplace, find the add-on, and click **Uninstall**. If your administrator installed the add-on for you, you might not be able to uninstall it.

## Use custom steps in flows

![](https://storage.googleapis.com/support-kms-prod/4BMw4ze7sYv0aoC6pJUaNVGDdmDUWd1gje7A)

After you install a Workspace Studio add-on, the steps show up in Studio.

The steps from the add-on are available wherever you create and edit flows, including:

- **When you create a flow with AI** on the Studio **Discover** page.
- **In the step-selection panel** in the flow editor. To find an add-on step, scroll to the section with the name of the add-on.

**Important:** When you add variables to third-party integration steps or add-on steps, they might contain your Google Account data, such as the contents of a message in Gmail or Chat, or event information from Calendar. The flow can then share your Google Account data with a third-party service. Make sure you trust the third-party service.

## Manage account access for add-on steps

![](https://storage.googleapis.com/support-kms-prod/4BMw4ze7sYv0aoC6pJUaNVGDdmDUWd1gje7A)

If you’re concerned about an add-on’s access to your Google Account data, you can delete its connections with your account. However, add-on steps might not work anymore and flows that use them could stop working.

1. Go to [https://myaccount.google.com/connections](https://myaccount.google.com/connections).
2. Search for the add-on in the list of apps and services and click it.
3. Click **Delete all connections you have with** **_add-on name_** and confirm you want to delete them.

To allow the add-on to connect again, in a flow, add an add-on step. You’re prompted to allow the required connections.

Give feedback about this article

Choose a section to give feedback on

true

15006943263800917801

true

Search Help Center

false

true

true

true

[Google Help](https://support.google.com/)

[Help Center](https://support.google.com/workspace-studio/?hl=en) [Workspace Studio](https://studio.workspace.google.com/)

[Privacy Policy](https://www.google.com/intl/en/privacy.html) [Terms of Service](https://www.google.com/accounts/TOS)Submit feedback

false

false

## What is the issue with this selection?

What is the issue with this selection?

Inaccurate - doesn't match what I see in the product

Hard to understand - unclear or translation is wrong

Missing info - relevant but not comprehensive

Irrelevant - doesn’t match the title and / or my expectations

Minor errors - formatting issues, typos, and / or broken links

Other suggestions - ideas to improve the content

## Share additional info or suggestions

​

​

Do not share any personal info

Cancel

Submit

By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/workspace-studio/answer/16433731?hl=en#) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).

false

false

false

Main menu

Google apps

---

## 4. Extend Google Workspace Studio  |  Google Workspace add-ons  |  Google for Developers

**Source:** https://developers.google.com/workspace/add-ons/studio

# Extend Google Workspace Studio — Summary

**Source:** Google for Developers — Google Workspace add-ons  
**URL:** https://developers.google.com/workspace/add-ons/studio  
**Last updated:** 2026-04-20 UTC  
**License:** Content under Creative Commons Attribution 4.0; code samples under Apache 2.0.

---

## Purpose of the Guide

These guides explain how developers can **extend Google Workspace Studio** by building **custom steps** that can be run inside Workspace Studio flows.

> “These guides explain how to extend the functionality of Google Workspace Studio by building custom steps that flows can run.”

### Recommended starting point

To begin, Google recommends the quickstart:

- [Build a calculator step with Apps Script](https://developers.google.com/workspace/add-ons/studio/quickstart-calculator)
- “Try the quickstart” link points to the same guide.

---

## What Workspace Studio Flows Do

**Flows** let Google Workspace users automate tasks across services by combining steps **without writing code**.

> “Flows let Google Workspace users automate tasks across services by combining a series of steps without writing any code.”

Developers can extend flows by exposing their app’s functionality as flow steps:

> “By extending flows, you let users add your app's functions as steps.”

---

## Example Flow: Customer Question Triage

A sample flow for handling customer emails:

1. Starts when an email from a customer is received.
2. Prompts Gemini to triage the email.
3. Creates a task for follow-up with the sales or support team.

The page includes a figure showing a user configuring a flow that triages customer questions with Gemini.

> **Figure 1:** A user configures a flow that triages customer questions with Gemini.

---

## Workspace Studio Concepts

### Flows

Users build **flows** in Workspace Studio to automate tasks in Google Workspace and beyond.

Key traits:

- Deep system integration
- Contextual awareness
- Can optionally use AI

> “Flows have deep system integration, contextual awareness, and can optionally use AI.”

---

### Step

A **step** is a single task in a flow’s automated process.

Important details:

- Represents one task in a sequence.
- Follows a starting event.
- Runs **synchronously**:
  - Each step completes before the next step begins.
- Users determine the order of steps.
- Steps can have inputs and outputs, but they are not required.

Examples of steps:

- “send an email”
- “post in a Chat space”
- “ask Gemini”
- Tasks outside Google Workspace, such as creating a CRM lead

> “Each step runs synchronously, meaning it completes its operation before the next step in the sequence begins.”

---

### Input Variable

An **input variable** is received by a step.

Key points:

- Set by the user on a step’s configuration card.
- Used while configuring the step.
- Examples:
  - Email address
  - Datetime
  - Gemini prompt

> “Input variables are received by steps.”

---

### Output Variable

An **output variable** is returned by a step and can be passed to another step.

Example use case:

- A step outputs an email address.
- Another step uses that email address as the recipient of an email.

> “Output variables are returned by steps, and can be sent to another step.”

---

### Dynamic Variable

A **dynamic variable** is a variable whose data can only be determined when the user configures the flow.

Example:

- Google Forms can have varying questions and answers.
- The number and content of those questions and answers are unknown until a specific Form starts a flow.

> “Dynamic variables account for this case.”

---

### Custom Resource

A **custom resource** is a custom data structure used to group multiple variables together.

Example:

- To create a CRM lead, pass a custom resource containing:
  - Email address
  - Street address
  - Name

> “A custom data structure that you can define to group multiple variables together.”

---

### Card

A **card** is a building block for user interfaces in add-ons.

Cards support:

- Defined layouts
- Interactive UI elements, such as buttons
- Rich media, such as images

Cards include special features for building flows:

- `IncludeVariables`: A property that enables dynamic variable inclusion.
- `Type`: Defines the type of data that input variables expect.

---

### Activity Log

An **activity log** describes what happens when a flow runs.

By default:

- Activity logs include the name of the starter or step.
- These names are statically defined in the manifest.

Developers can also provide customized activity logs.

> “Describes what happens when an flow runs.”

---

## What You Can Build

Workspace Studio flows are built on the **Google Workspace add-ons platform**.

If you already have an existing add-on:

- You can extend it to include flows.
- This is done by updating the add-on manifest to include a flow-specific section.

> “If you already have an existing add-on, you can extend its functionality to include Flows by updating its manifest to 

[... summary truncated for context management ...]

---

## 5. Get started with Google Workspace Studio - Workspace Studio Help

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

---

## 6. Get started: Workspace Studio set up guide for admins  |  Google Workspace Help

**Source:** https://knowledge.workspace.google.com/admin/studio/manage-access-to-steps-and-starters-in-workspace-studio

# Workspace Studio Admin Setup Guide – Summary

## Overview
- **Workspace Studio** lets users create automated **flows** across Google Workspace apps (Gmail, Drive, Chat, etc.) and third-party services.
- Users with Gemini can describe flows; others use manual steps.
- Flows act on a user's behalf – can draft emails, create/update files, create tasks, etc.

> "Poorly configured flows could unintentionally edit or delete data, or send excessive notifications. Administrators can manage these risks through policy and monitoring."

## Step 1: Set up Workspace Studio for Your Organization

### 1.1 Manage Access to Studio
- **Setting location:** Admin console → Apps → Google Workspace → Workspace Studio
- **Action:** Ensure **Service status** = **ON** for the desired OUs/groups.
- **Emergency contingency recommendation:**
    > "Create a child organizational unit that has access to Studio turned off. This lets you quickly move a user to it to stop a flow they own."
- [Turn on/off Workspace Studio for your org](https://knowledge.workspace.google.com/admin/users/access/turn-google-workspace-studio-on-or-off-for-your-organization)

### 1.2 Manage Access to Studio Features
Control: Gemini flow creation, AI-powered steps, steps for other Workspace services, integrations/custom steps.

**Recommendations:**
- Allow Gemini features for users who already have Gemini for Google Workspace.
- Allow steps for Workspace services users can normally access; block only if abuse risk.
- Use the **Google Workspace Marketplace allowlist** to control which integrations and published custom steps are usable.

[Manage access to steps and starters in Workspace Studio](https://knowledge.workspace.google.com/admin/studio/manage-access-to-steps-and-starters-in-workspace-studio)

### 1.3 Manage Who Can Share Flows
> "When a user shares a flow, the recipient clicks a link to get a **copy** of the flow. The copy includes the owner's setup, such as text they entered, email addresses, and links to files in Drive. The recipient does not get access to the owner's private data, like emails or Drive files, only the content that they can already access."

- **Setting location:** Admin console → Apps → Google Workspace → Workspace Studio → Sharing settings
- **Recommendation:** Allow sharing for trusted OUs/groups to distribute standardized flow templates.

[Allow people to share flows in Workspace Studio](https://knowledge.workspace.google.com/admin/studio/allow-people-to-share-flows-in-workspace-studio)

### 1.4 Set Up Alerts
Create activity rules for critical events.

#### High-Frequency Alert
- **Condition:** Rule log events where event is **Start run**
- **Threshold:** Count > **100** in **1 hour**
- **Action:** Email all admins

#### AI Usage Alert
- **Condition:** Step name contains **"Ask Gemini"** (optionally other AI-powered steps)
- **Action:** Notify Super Admin

[Set up activity alerts for Workspace Studio](https://knowledge.workspace.google.com/admin/studio/set-up-activity-alerts-for-workspace-studio)

## Step 2: Support Your Users

### 2.1 Getting Started
- Direct users to [studio.workspace.google.com](https://studio.workspace.google.com)
- Point them to the [Workspace Studio Help Center](https://support.google.com/a/users/answer/16275487) for tutorials.

### 2.2 Understanding Limits
| Limit | Value |
|-------|-------|
| Max flows per user | **25** (includes active and stopped) |
| Max steps per flow | **20** |
| Max active flows from Gmail starter | **25** |
| Daily runs per user | Limited; flows pause until the next 24‑hour cycle if exceeded |

[Learn about Google Workspace Studio limits](https://support.google.com/workspace-studio/answer/16765942)

### 2.3 Troubleshooting Common Issues
- Admin guide: [Troubleshoot Workspace Studio for your users](https://knowledge.workspace.google.com/admin/studio/troubleshoot-workspace-studio-for-your-users)
- User help: [Troubleshoot issues with flows](https://support.google.com/workspace-studio/answer/16430806)

## Step 3: Monitor and Manage Studio Activity

### 3.1 Investigate Activity
Use the **audit and investigation tool** (or security investigation tool) with data source **Rule log events**.
Filter by: Actor (user email), Flow ID, Event, Step name, etc.
**Example use case:** Find the owner of a flow that runs an "Ask Gemini" step several times per minute.

[Workspace Studio log events](https://knowledge.workspace.google.com/admin/reports/workspace-studio-log-events)

### 3.2 Stop a Flow

| Option | How |
|--------|-----|
| **1 – User stops it** | Ask the user to turn off the flow or edit its setup. |
| **2 – Support stops it** | 1. Use investigation tool to get the **Flow ID**. <br> 2. Contact Google Workspace support with the ID to have it stopped. |
| **3 – Emergency stop** | Move the user to an OU that has Studio access **turned off** → stops **all** flows for that user immediately. |

[Stop a Workspace Studio flow as an admin](https://knowledge.workspace.google.com/admin/studio/stop-a-wo

[... summary truncated for context management ...]

---

## 7. Google Workspace Studio: Automate Workflows with Agentic AI Powered by Gemini

**Source:** https://workspace.google.com/studio/

# Google Workspace Studio — AI-Powered Workflow Automation Summary

**Source:** <https://workspace.google.com/studio/>  
**Title:** *Google Workspace Studio: Automate Workflows with Agentic AI Powered by Gemini*

---

## Overview

**Google Workspace Studio** is an AI-powered automation tool for Google Workspace that lets users automate everyday work and complex business processes **without coding**. It uses **Gemini 3** to help users create “flows” or AI-powered agents from plain-language descriptions.

> **AI-powered automation, made simple**  
> Automate everyday work, from simple tasks to complex processes—no coding required.

Primary calls to action:

- **Get started:** Workspace business signup
- **Learn more:** Google Workspace Studio Help documentation
- **Sign in / access Studio:** <https://studio.workspace.google.com/>

---

## Core Capabilities

### 1. Build AI Agents from Plain Language

Users can describe what they want to automate, and Gemini 3 generates a functional workflow.

> **Turn an idea into a fully functional agent in minutes**  
> Simply describe what you want to automate in plain language and Gemini 3 will create a flow for it.

Example prompt shown in product imagery:

> “What would you like to automate?”

---

### 2. Use Pre-Configured Workflow Steps

Workspace Studio includes prebuilt workflow steps to speed up creation.

> **Build fast with pre-configured steps**  
> Create custom flows quickly with prebuilt steps to accelerate the creation process.

Example workflow shown:

- Summarize meeting notes
- Send summaries to the team in Google Chat
- Draft a follow-up email

---

### 3. Manage Flows Inside Workspace Apps

Flows can be modified and monitored directly from Google Workspace apps.

> **Manage your flows from your Workspace apps**  
> Modify flows and track their activity without leaving your Workspace apps like Gmail, Chat, and Drive.

Supported native Workspace contexts mentioned:

- **Gmail**
- **Google Chat**
- **Google Drive**

---

## Example Automation Use Cases

Workspace Studio is positioned for both simple and complex business workflows.

### Prepare for Every Meeting

Automatically generate meeting prep summaries.

> Summarize upcoming meetings in Chat based on the meeting’s details, attendees, and attachments.

Possible inputs:

- Meeting details
- Attendees
- Attachments

Output:

- Summary posted in Google Chat

---

### Translate Action Items

Capture, translate, and distribute action items from meetings.

> Automatically capture meeting action items, translate them, and draft an email to share them with your team.

Workflow may include:

- Extracting action items from a meeting
- Translating them
- Drafting an email for the team

---

### Auto-Label Priority Emails

Use AI to detect important emails and apply labels.

> Intelligently detect and label high priority emails in your inbox.

Use case:

- Identify high-priority Gmail messages
- Apply labels automatically

---

### Save Attachments to Drive

Automate attachment handling from Gmail.

> Save attachments to a Drive folder and record them in Sheets—all without leaving Gmail.

Workflow may include:

- Detect email attachments
- Save them to a specified Google Drive folder
- Log records in Google Sheets

---

## Cross-App and Third-Party Integrations

Workspace Studio can coordinate workflows across Google Workspace and external business apps.

> **Orchestrate work across all your business apps**  
> Connect to the apps your business relies on with prebuilt connectors and custom extensions.

Third-party apps shown as examples:

- **Asana**
- **Jira**
- **Mailchimp**
- **Salesforce**

---

## Customer Quotes

### Kärcher

> Google Workspace Studio has been a powerful driver for individual and team productivity. It allows us to decentralize routine problem-solving, empowering teams to resolve 'quick wins' and delivering measurable, tangible productivity benefits right out of the gate.

— **Marina Kunert**, Product Lead for AI Enablement, Kärcher

---

### Zoi

> We view Workspace Studio as the tool that democratizes AI for the business. By giving all users immediate, practical benefits, companies are empowering business units to solve their own 'quick win' problems so IT can focus on defining their AI strategy.

— **Benjamin Hermann**, Managing Director, Zoi

---

## Templates

Google Workspace Studio includes “dozens of popular templates” to help users start quickly.

### Featured Template Categories and Examples

| Category | Template |
|---|---|
| **Stay on top of email** | Get a daily summary of unread emails |
| **Respond quickly** | Notify me about emails from key people |
| **Track new requests** | Label emails that have action items |
| **Highlight key emails** | Star emails for follow-up |
| **Streamline my follow-up** | Send email summaries and action items after meetings |
| **Catch up on news** | Get news headlines summarized daily |

Template-related apps/icons shown include:

- Gemini
- Gmai

[... summary truncated for context management ...]

---

## 8. Guide to Starters & Steps in Workspace Studio - Workspace Studio Help

**Source:** https://support.google.com/workspace-studio/answer/16765661?hl=en

[Skip to main content](https://support.google.com/workspace-studio/troubleshooter/17081293?hl=en&visit_id=639171125046689512-1751812781&rd=1#search-form)

# Guide to Starters & Steps in Workspace Studio

Every flow has 2 main parts:

1. **Starter:**
   - This is the event that starts your flow. A starter can be a schedule, like “every Friday at 5 PM,” or an event, like to receive a new email with an attachment.
   - Each flow has only one starter.
2. **Step:**
   - This is a task your flow performs after it starts. A step can be an action, like “draft a reply,” or a notification, like “notify me in Chat.”

   - You can add multiple steps to a flow.

Choose your account type:Personal accountWork or School account

false

15215561379184798596

true

Search Help Center

false

true

true

true

[Google Help](https://support.google.com/)

[Help Center](https://support.google.com/workspace-studio/?hl=en) [Workspace Studio](https://studio.workspace.google.com/)

[Privacy Policy](https://www.google.com/intl/en/privacy.html) [Terms of Service](https://www.google.com/accounts/TOS)Submit feedback

Send feedback on...

This help content & informationGeneral Help Center experience

false

false

false

Main menu

Google apps

---

## 9. Manage & share your flows in Google Workspace Studio - Workspace Studio Help

**Source:** https://support.google.com/workspace-studio/answer/16766368?hl=en-GB

# Manage & share your flows in Google Workspace Studio

> **Important:** If you're signed in with a school account and are under 18, you can’t use any AI features in Workspace Studio. If a flow containing AI steps is shared with you, those steps will be removed when you open the flow.

## Access your flows
- Go to [studio.workspace.google.com](https://studio.workspace.google.com/) and click **My flows** to see all your flows.

## Edit, rename, or copy a flow

### Edit a flow
1. Open a flow from the **My flows** list.
2. **Edit a step:** Click the step.
3. **Delete a step:** Next to the step name, click **More** ![](https://storage.googleapis.com/support-kms-prod/iwMAMe1lEk5FwSU7G8VhBiTE8PuXATWhvq8t) → **Delete**.
4. **Add a step:** Click **Add step** ![](https://storage.googleapis.com/support-kms-prod/fOTQBMfNfoP4BI7YSuoHSAKDrduj82OhB4l7) → then click **More** and the up arrow to move it into position.
5. **Save behavior depends on the flow’s state:**
   - **Flow is on:** Click **Save changes** to apply edits. Closing without saving stores changes but does **not** apply them.
   - **Flow is off:** Changes are saved automatically.

### Rename a flow
- Open the flow in the editor → at the top, click the pencil icon ![](https://storage.googleapis.com/support-kms-prod/CrWIa3sXECOnWEejW63vmtGv2bkDrtSEL2P9) to rename.

### Copy a flow
- From the **My flows** list, next to the flow, click **More menu** ![](https://lh3.googleusercontent.com/ab4OReCNNa-HGlI2dzu8Wto7uYx3oh1Q3Aur1IgnyC0A1S3CgIo1m4sfkXhk22y8TUSF=h36) → **Make a copy**. The copy appears at the top of your list.

## Turn a flow on or off
- From **My flows**, next to the flow, click **More menu** → **Turn off** (or **Turn on**).
- Turning off stops the flow immediately, including any in-progress runs. It can be turned back on later.

## Delete a flow
> **Important:** Deletion is permanent and cannot be undone.

- From **My flows**, next to the flow, click **More menu** → **Delete**.

## Get flow activity

### All flows
- Go to **My flows** and click **Activity**.
- You can filter by **Complete**, **In progress**, or flows with issues.

### Single flow
- Next to the flow, click **More** → **Activity**, **or** open the flow in the editor and click **Activity** at the top.

**Tip:** Flow activity is also accessible from the Workspace Studio side panel in Gmail (click ![](https://storage.googleapis.com/support-kms-prod/txkAdXXVcfQ2gvh7Km5ma9aicztobNesqpxN) **Flows**).

## Share a flow
- Sharing is available **only within your organization**.
- Shared flows can only be **copied**; recipients **cannot** edit your original flow or see its run history.

### Steps to share
1. From **My flows**, open the flow you want to share.
2. At the top, click **Get a link to copy** ![Share](https://storage.googleapis.com/support-kms-prod/6ht7LJHynnz1QbC0PQkeYKFycuKzyfeAHPFr).
3. Change permission from **Private** to **"Anyone in your organization with the link can make a copy."**
4. Click **Copy link** and share the link (e.g., via Chat or Gmail).

> **Note:** Copies include your latest setup (files, text, email addresses). Anyone with the link sees your email address as the flow creator.

## Related resources
- [Guide to starters and steps in Workspace Studio](https://support.google.com/workspace-studio/answer/16765661)
- [Create a flow with Gemini AI](https://support.google.com/workspace-studio/answer/16448469)

---

## 10. Take actions in third-party services with flows - Workspace Studio Help

**Source:** https://support.google.com/workspace-studio/answer/16658279?hl=en

# Summary: Take actions in third-party services with flows

**Status:** Limited preview. Integrations allow flows in Google Workspace Studio to perform tasks in third-party services like Asana, Mailchimp, and Salesforce. Many also work with Gemini Apps.

## Important Warning
> **Important:** When you add variables to integration steps, they might contain your Google Account data, such as the contents of a message in Gmail or Chat, or event information from Calendar. The flow can then share your Google Account data with the third-party service. Make sure you trust the third-party service.

## Using Integration Steps in Flows
Integration steps are available when creating a flow with AI, using a template, or in the step selector under the third-party service name.

**Steps:**
1. Go to [studio.workspace.google.com](https://studio.workspace.google.com) and [create a flow](https://support.google.com/a/users/answer/16430397).
2. In the left panel, click the integration step.
3. If not yet connected, click **Connect** and follow prompts. You may need to install a helper app from the third‑party service. (For issues, see troubleshooting below.)
4. Set up the step.
5. (Optional) Click **Test run** to run the flow once with real actions. Select starting conditions, then **Start**. [Learn more about test runs](https://support.google.com/workspace-studio/answer/16663517).
6. Click **Turn on**.

## Connecting from Google Workspace Marketplace
Pre‑connect an integration so you won’t need to connect again when adding it to a flow.

1. Visit the [Marketplace integrations page](https://workspace.google.com/marketplace?host=workflow) (pre‑filtered for integrations).
2. Click the desired integration.
3. Click **Connect** and follow the on‑screen instructions. You may need to install a helper app.

**Disconnecting:** Return to the Marketplace listing, click **Disconnect**. If your admin set up the integration, you might not be able to disconnect.

## Managing Account Access
If you’re worried about data access, delete the integration’s connections to your account. Flows using the integration may stop working.

1. Go to [myaccount.google.com/connections](https://myaccount.google.com/connections).
2. Find and click the integration.
3. Click **Delete all connections you have with** *integration name* and confirm.

The Marketplace will still show “connected”. To reconnect, add the step again and go through the connection process.

## Troubleshooting Integration Steps
- **Paid third‑party services:** You need a subscription for that service.
- **Admin restrictions:** Your Workspace admin may limit who can connect or which integrations are allowed. Ask your admin to allow or connect it for you.
- **Helper apps:** Some integrations (e.g., Salesforce, monday) require a helper app installed by you or your admin. Check the Marketplace listing’s **Overview** section.
- **Missing permissions:** Integrations like HubSpot let you select permissions individually. If a required permission is missing (e.g., get contact data, create a contact), the step fails. Reconnect and grant all permissions. If error messages persist, your admin may be blocking some permissions—contact them for help.

*Google, Google Workspace, and related marks are trademarks of Google LLC. Other product names are trademarks of their respective companies.*

---

## 11. Tips to create flows with conditional steps - Workspace Studio Help

**Source:** https://support.google.com/workspace-studio/answer/16431010?hl=en

# Tips to Create Flows with Conditional Steps — Google Workspace Studio

**Source:** [Workspace Studio Help](https://support.google.com/workspace-studio/answer/16431010?hl=en)  
**Topic:** Using conditional logic in Google Workspace Studio flows so certain steps run only when specified conditions are met.

---

## Key Excerpts

> “In Google Workspace Studio, you can have certain steps in your flows happen only if certain conditions are met.”

> “Conditional steps set off certain steps into substeps that the flow does only in certain scenarios.”

Workspace Studio supports **2 steps** for checking conditions:

- **Decide** – uses Gemini to evaluate if conditions you describe are true or false
- **Check if** – compares values

Important limitations:

> “You can’t use variables from a substeps in steps in the main flow.”

> “An flow can’t have nested conditional steps. But a flow can have more than one conditional step, they just run in order.”

Gemini availability note:

> “The Decide step is only available if you have access to Gemini. If you don’t have Gemini, use Check if instead.”

---

## Overview: How Conditional Steps Work

Conditional steps let a flow run certain **substeps** only in specific situations.

You can add conditional logic in two ways:

- **Describe conditions when creating a flow with AI**
- **Manually add conditional steps** to an existing or new flow

After adding a conditional step, you add the actions that should happen inside its **substeps**. You can also add regular steps after the conditional section; those top-level steps run for all flow runs.

---

## Conditional Flow Limitations

### 1. Substep variables cannot be used in the main flow

Variables created inside conditional substeps are not available to later top-level steps.

Example:

- A conditional substep uses **Ask Gemini** to draft a reply.
- The main flow cannot later add that draft to a tracking document.

### 2. No nested conditional steps

A flow cannot place one conditional step inside another conditional section.

However:

- A flow **can have multiple conditional steps**
- They run sequentially, in order

---

# AI-Powered Conditions with **Decide**

## What “Decide” Does

**Decide** uses Gemini to evaluate natural-language conditions and return a true/false result.

How it works:

- You tell Gemini what conditions to check.
- Gemini determines whether the conditions are **true** or **false**.
- A **Decide** step is automatically paired with a **Check if** step.
- The paired **Check if** step is prefilled to check whether the **Decide** result is **true**.
- You can change the paired **Check if** step so substeps run when the result is **false** instead.
- The flow runs the substeps only if the paired **Check if** condition matches.
- Any other main-flow steps after the condition still run afterward.

---

## Set Up a **Decide** Step

1. Go to [https://studio.workspace.google.com](https://studio.workspace.google.com/) and create a flow.
2. If building manually, or if Gemini did not add it automatically, add a **Decide** step.
   - A **Check if** step is automatically added with it.
3. In the **Decide** step, describe the conditions Gemini should evaluate.

### Tips for describing Decide conditions

- **Start from a common use case**
  - Click one of the suggested options below the field, such as **Is urgent**, to begin the condition description.
- **Add variables**
  - Use variables from previous steps to give Gemini context.
  - Example: Add the email message body variable so Gemini can check whether it has a negative tone.

---

## Run Substeps When Decide Is False

To make the substeps run only when the **Decide** condition is **not met**:

1. Click the paired **Check if** step.
2. Change the matching condition from **is true** to **is false**.

---

## Add Conditional Actions

Below the **Check if** step:

- Add or edit the steps you want the flow to run when the condition matches.
- You **cannot** add another **Check if** step inside these substeps.

Optional:

- Add more top-level steps after the conditional section if they should run for all flow executions.
- Remember: those top-level steps **cannot use variables from the substeps**.

---

## Tip: Handle the Opposite Condition

> “To have the flow do steps for the opposite condition, add another Check if step with the matching set to the opposite of the first.”

Example:

- First conditional branch: run substeps when the decision is **true**
- Second conditional branch: run different substeps when the decision is **false**

---

## Test and Turn On a Decide-Based Flow

Optional testing:

1. Click **Test run**.
2. Select the starting conditions.
3. Click **Start**.

Important:

> “A test run runs your flow once, taking real actions so you can see the outcome.”

When ready:

- Click **Turn on**.

---

# Condition Matching with **Check if**

## What “Check if” Does

**Check if** compares values from the flow against specified conditions.

How it works:

- You 

[... summary truncated for context management ...]

---

## 12. Tips to use AI steps in flows - Workspace Studio Help

**Source:** https://support.google.com/workspace-studio/answer/16431105?hl=en

# Tips to Use AI Steps in Flows — Google Workspace Studio

**Source:** [Workspace Studio Help](https://support.google.com/workspace-studio/answer/16431105?hl=en)  
**Topic:** How to incorporate Gemini and AI-powered steps into Workspace Studio flows.

---

## Overview

Google Workspace Studio lets you incorporate **Gemini** into automated flows. Gemini can help flows:

- Analyze content
- Write or draft text
- Research information
- Determine whether a flow should run
- Summarize, extract, or recap information

The article explains when to use different types of AI steps:

- **General AI steps**
  - Ask Gemini
  - Ask a Gem
- **AI action steps**
  - Decide
  - Extract
  - Summarize
  - Recap unread emails

---

## Account Type Requirements

### Personal Accounts

> **Personal accounts:** If you have a Google AI Pro or Ultra plan, you can use flows in Workspace Studio. You can't share flows with others.

### School Accounts

> **School accounts:** If you use a school account and are under 18, you can't get AI features in Workspace Studio. If someone shares a flow with AI steps with you, those steps are removed when you open the flow.

---

## How to Use AI Steps Successfully

The article identifies **4 keys to success** when using any AI step.

---

### 1. Provide Context in Your Request

Gemini does **not** automatically know what happened in earlier steps of your flow.

> Gemini doesn’t know about the other steps in your flow. Prompts like “Write a professional reply to the email” won’t work because Gemini doesn’t know which email you mean.

#### Actionable Tips

- Reference data from earlier flow steps.
- Include variables from previous steps.
- Link to specific Google Drive files.
- Link to relevant websites.
- Add enough context for Gemini to understand the request.

#### For Open Prompt AI Steps

For steps such as **Ask Gemini** and **Decide**, add context directly into the prompt for better results.

> **Reference data from earlier steps and specific files**: For AI steps with open prompts, such as 'Ask Gemini' and 'Decide', add context to your prompt to get better results.

---

### 2. Control Data Sources Gemini Can Use

By default, Gemini can use:

- The web
- Workspace content you can access
- Connected integrations you can access

To limit access, choose **Web only**.

> **Allow Google Workspace data sources**: By default, Gemini can reference the web, as well as all content that you can access in Google Workspace and connected integrations. To prevent Gemini from accessing your personal or organization's data, choose **Web only**.

---

### 3. Use Gemini’s Response as a Variable Later

Gemini’s response becomes a variable tied to the AI step.

> **Access Gemini’s response by adding a variable in a later step**. The response from Gemini or a Gem is available as a variable associated with the AI-powered step.

You can reuse that output in later steps, such as:

- A message
- A document
- A spreadsheet
- Another Gemini request

---

### 4. Use Multiple AI Steps in One Flow

You can chain AI steps together by passing variables from one step to another.

Example workflow from the article:

> You could use the **Sales pitch ideator** Gem in **Ask a Gem** to analyze a form response, use an **Extract** step find any questions in an open-ended response, use a **Ask Gemini** step draft an email message using the Gem response and extracted questions for additional context, and use an **Ask Gemini** step to create a subject line for your message.

---

### 5. Use AI Action Steps When Appropriate

Although **Ask Gemini** can handle many requests, Workspace Studio includes specialized AI action steps optimized for common tasks.

> Though you can use Ask Gemini for almost all types of requests, Workspace Studio has AI steps that are optimized for certain actions, such as extracting information from text, summarizing ideas and insights, or writing text for specific scenarios.

---

## General AI Steps

General AI steps are used similarly to Gemini in Workspace.

| Step | Best For | Examples / Notes |
|---|---|---|
| **Ask Gemini** | General inquiries or text generation | Web research, summarizing project status, creative writing |
| **Ask a Gem** | Using the agentic expertise of a pre-built or custom Gem | Sales pitch ideation, custom file-grounded content generation |

---

### Ask Gemini

Best for **general inquiries** or **text generation** needs.

Examples:

- Do a quick web search on the company of a person who submitted a form or contacted you.
- Summarize the state of a project based on the latest meeting notes and tracking spreadsheet.
- Write a poem about the importance of updating a meeting agenda to send to attendees.

Important tip:

> **Tip:** For common drafting, summarizing, and extracting tasks, you can save time crafting prompts by using AI action steps instead.

---

### Ask a Gem

Use **Ask a Gem** when you need the expertise of a specific Gem, either pre-built or custom.

Examples:

- Have t

[... summary truncated for context management ...]

---

