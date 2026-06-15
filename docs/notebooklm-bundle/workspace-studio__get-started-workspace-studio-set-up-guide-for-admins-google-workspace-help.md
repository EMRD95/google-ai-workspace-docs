# Get started: Workspace Studio set up guide for admins  |  Google Workspace Help

**Product Area:** workspace-studio
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
