# Get started: Workspace Studio set up guide for admins  |  Google Workspace Help

**Product Area:** admin-console
**Source:** https://support.google.com/a/answer/16796372?hl=en

# Get Started: Workspace Studio Set Up Guide for Admins — Summary

**Source:** Google Workspace Help  
**URL:** https://support.google.com/a/answer/16796372?hl=en  
**Last updated:** 2026-06-11 UTC

---

## Overview

Google Workspace Studio lets users create **“flows”** that automate routine tasks across Google Workspace apps such as **Gmail, Drive, and Chat**, plus third-party services. Users with **Gemini access** can build flows by describing what they want to automate.

Admins should configure access, sharing, feature permissions, alerts, monitoring, and emergency controls before broad rollout.

> “Flows can act on users' behalf, drafting emails, creating and updating files, creating tasks, and more.”

Because flows can make changes and send notifications, misconfigured flows may cause unwanted actions:

> “Poorly configured flows could unintentionally edit or delete data, or send excessive notifications.”

---

# Step 1. Set Up Workspace Studio for Your Organization

Before enabling Workspace Studio broadly, Google recommends configuring **access and guardrails** to ensure flows behave as expected and data remains secure.

---

## 1. Manage Access to Studio

### Admin Console Path

> **Admin console → Menu → Apps → Google Workspace → Workspace Studio**

### Required Action

- Confirm **Service status** is set to **ON** for the appropriate:
  - Organizational units
  - Groups

### Recommendation

Create a dedicated child organizational unit where Studio access is turned off:

> “Create a child organizational unit that has access to Studio turned off. This lets you quickly move a user to it to stop a flow they own.”

### Related Help

- [Turn Google Workspace Studio on or off for your organization](https://knowledge.workspace.google.com/admin/users/access/turn-google-workspace-studio-on-or-off-for-your-organization)

---

## 2. Manage Access to Studio Features

Admins can control whether users can:

- Use **Gemini** to create flows
- Use **AI-powered steps** in flows
- Use steps for other Google Workspace services
- Use integrations or custom steps

### Recommendations

- Allow users with **Gemini for Google Workspace** access to use Gemini features in Studio.
- Allow users to use steps for Workspace services they already have access to.
- Only block steps for a service if there is a specific risk of abuse.
- Use the **Google Workspace Marketplace allowlist** to control:
  - Integrations
  - Published custom steps

### Related Help

- [Manage access to steps and starters in Workspace Studio](https://knowledge.workspace.google.com/admin/studio/manage-access-to-steps-and-starters-in-workspace-studio)

---

## 3. Manage Who Can Share Flows

Flow sharing allows users to distribute useful automations internally as templates, helping others avoid recreating the same flows.

### How Sharing Works

> “When a user shares a flow, the recipient clicks a link to get a _copy_ of the flow.”

The copied flow includes the original owner’s setup, such as:

- Text they entered
- Email addresses
- Links to Drive files

Important privacy detail:

> “The recipient does not get access to the owner's private data, like emails or Drive files, only the content that they can already access.”

### Admin Console Path

> **Admin console → Apps → Google Workspace → Workspace Studio → Sharing settings**

### Recommendation

Allow sharing for trusted organizational units and groups so they can distribute standardized flow templates.

### Related Help

- [Allow people to share flows in Workspace Studio](https://knowledge.workspace.google.com/admin/studio/allow-people-to-share-flows-in-workspace-studio)

---

## 4. Set Up Alerts

Admins can create activity rules to be notified about specific Studio activity.

---

### High-Frequency Alert

Purpose: Detect flows that may be looping or running excessively.

#### Rule Configuration

- **Condition:** Create a rule for **Rule log events** where the event is **Start run**
- **Threshold:** Alert if count exceeds **100** in **1 hour**
- **Action:** Send an email to all admins

---

### AI Usage Alert

Purpose: Monitor generative AI usage in automations.

#### Rule Configuration

- **Condition:** Create a rule where **Step name** contains **"Ask Gemini"**
- Optionally include other AI-powered steps
- **Action:** Send a notification to the Super Admin

For available steps, see:

- [Guide to Starters & Steps in Workspace Studio](https://support.google.com/workspace-studio/answer/16765661)

### Related Help

- [Set up activity alerts for Workspace Studio](https://knowledge.workspace.google.com/admin/studio/set-up-activity-alerts-for-workspace-studio)

---

# Step 2. Support Your Users

Admins should help users create flows, understand limits, and troubleshoot issues.

---

## 1. Getting Started

Direct users to:

- [studio.workspace.google.com](https://studio.workspace.google.com/)

Encourage users to review:

- [Workspace Studio Help Center](https://support.google.com/a/users/answer/16275487)

The 

[... summary truncated for context management ...]
