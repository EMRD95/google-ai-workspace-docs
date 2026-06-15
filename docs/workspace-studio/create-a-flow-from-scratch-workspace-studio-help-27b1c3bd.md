---
title: "Create a flow from scratch - Workspace Studio Help"
source_url: "https://support.google.com/workspace-studio/answer/16447954?hl=en"
product_area: "workspace-studio"
retrieved_at: "2026-06-15T11:30:07Z"
extraction_method: "web_extract"
---

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
