---
title: "Stop a Workspace Studio flow as an admin  |  Google Workspace Help"
source_url: "https://knowledge.workspace.google.com/admin/studio/stop-a-workspace-studio-flow-as-an-admin"
product_area: "workspace-studio-admin"
retrieved_at: "2026-06-15T09:47:15Z"
extraction_method: "web_extract"
---

# Stop a Workspace Studio Flow as an Admin — Summary

**Source:** Google Workspace Help  
**URL:** https://knowledge.workspace.google.com/admin/studio/stop-a-workspace-studio-flow-as-an-admin  
**Last updated:** 2026-06-11 UTC

---

## Purpose

Google Workspace Studio lets users create **flows** that automate work across Google Workspace and allowed third-party services. While flows can improve productivity, they may sometimes behave in **unexpected or unwanted ways**.

Admins can stop problematic flows by:

1. Identifying which flow is causing the issue.
2. Contacting Google Workspace Support to stop that specific flow.
3. If urgent, temporarily disabling **all Workspace Studio flows** for the flow owner.

---

## Key Excerpts

> With Google Workspace Studio, people in your organization can create flows to automate work across Workspace and third-party services they're allowed to connect to.

> These flows can make people more productive by automating routine tasks, but they can sometimes work in unexpected or unwanted ways.

> To stop a flow, first you figure out which flow is causing the problem, then send a request to Support to stop it.

> **Important:** These steps turn off all the user's flows. Make sure that they don't have any business critical flows before you continue.

---

## How Unwanted Flow Activity Is Usually Discovered

Admins typically detect problematic Studio flow activity through:

- **User reports**
- **Workspace event logs**

Examples of suspicious or unwanted activity include:

### High Frequency Activity

Examples:

- More Gmail messages sent than normal
- More Google Chat messages sent than normal
- More file changes than expected
- More files created than would be possible for a human user

**Tip:** Chat messages sent by Studio flows include a **chip next to the sender’s name** showing they were sent by a Studio flow.

### Regularly Scheduled Unwanted Activity

Examples:

- Activity repeating approximately every hour
- Activity occurring at all times of day

**Note:** Flows have built-in staggering, so repeated activity may not happen at exactly the same interval each time.

---

## Step 1: Find Which Flow Is Causing the Problem

Use **Workspace Studio log events** in either:

- **Audit and investigation tool**
- **Security investigation tool**

Reference: [Workspace Studio log events](https://knowledge.workspace.google.com/admin/reports/workspace-studio-log-events)

### Recommended Attribute Filters

Use these filters when searching Studio logs:

#### Actor

Set the **Actor** filter to the affected user’s email address.

#### Event

If you know when the problem occurred:

- Filter by **Step complete**
- Look for a step that finished around the same time as the unwanted activity

You may also filter by **Step app** if you know where the activity occurred, such as:

- Gmail
- Google Chat
- Another Workspace app

### Record the Flow ID

Once you identify the flow in the results list, note the:

- **Flow ID**

This is required when contacting Google Workspace Support.

---

## Step 2: Stop a User’s Flow

### Preferred Method: Contact Google Workspace Support

Contact Google Workspace Support and provide the **Flow ID** for the flow you want stopped.

Support will stop the specific flow for you.

Reference: [Contact Google Workspace support](https://knowledge.workspace.google.com/admin/support/contact-google-workspace-support)

---

## Urgent Option: Stop All Flows Owned by the User

If the flow must be stopped immediately and you cannot wait for Support, you can stop **all** flows owned by that user.

> **Important:** These steps turn off all the user's flows. Make sure that they don't have any business critical flows before you continue.

### Steps

1. **Add an organizational unit**
   - Set the user’s current organizational unit as the parent.
   - Reference: [Add an organizational unit](https://knowledge.workspace.google.com/admin/users/advanced/add-an-organizational-unit)

2. **Move the user to the new organizational unit**
   - Reference: [Move the user to an organizational unit](https://knowledge.workspace.google.com/admin/users/advanced/move-users-to-an-organizational-unit)

3. In the **Google Admin console**, go to:

   ```text
   Menu > Apps > Google Workspace > Workspace Studio
   ```

   Direct link: [Go to Workspace Studio](https://admin.google.com/ac/managedsettings/243976345647)

   **Required privilege:**  
   [Service Settings administrator privilege](https://knowledge.workspace.google.com/admin/users/administrator-privilege-definitions#service_settings)

4. Click **Service status**.

5. On the left, select the new organizational unit.

6. Change **Service status** to **Off**.

7. Click **Override**.

8. After Support stops the problematic flow:
   - Move the user back to their original organizational unit.
   - The user can use Workspace Studio again.
   - The stopped flow remains off until the user manually turns it back on.

---

## Important Notes and Cautions

-

[... summary truncated for context management ...]
