---
title: "Get started: Workspace Studio set up guide for admins  |  Google Workspace Help"
source_url: "https://support.google.com/a/answer/16704187?hl=en"
product_area: "admin-console"
retrieved_at: "2026-06-15T09:45:35Z"
extraction_method: "web_extract"
---

# Get started: Workspace Studio set up guide for admins — Summary

**Source:** Google Workspace Help  
**URL:** https://support.google.com/a/answer/16704187?hl=en  
**Last updated:** 2026-06-11 UTC

---

## Overview

Google Workspace Studio lets users create **“flows”** to automate routine work across Google Workspace apps such as **Gmail, Drive, and Chat**, as well as third-party services.

Users with access to **Gemini** can build flows by describing what they want to do.

> “Flows can act on users' behalf, drafting emails, creating and updating files, creating tasks, and more.”

Because flows can perform actions on behalf of users, admins should configure access, sharing, alerts, and monitoring to reduce risks such as accidental data edits/deletions or excessive notifications.

---

## Key Admin Goals

Admins should use this guide to:

- Configure Workspace Studio access and guardrails.
- Control access to Studio features, Gemini features, steps, integrations, and custom steps.
- Manage who can share flows.
- Set up alerts for risky or high-volume activity.
- Help users understand limits and troubleshoot issues.
- Monitor activity through audit/security tools.
- Stop problematic flows when needed.

---

# Step 1. Set up Workspace Studio for your organization

Before enabling broad use, Google recommends configuring access and safeguards so flows behave as expected and data remains secure.

---

## 1. Manage access to Studio

### Where to find the setting

**Admin console → Menu → Apps → Google Workspace → Workspace Studio**

### Action

- Confirm **Service status** is set to **ON** for the correct:
  - Organizational units
  - Groups

### Recommendation

> “Create a child organizational unit that has access to Studio turned off. This lets you quickly move a user to it to stop a flow they own.”

This provides an emergency control mechanism if a user-owned flow misbehaves.

### Related help

- [Turn Google Workspace Studio on or off for your organization](https://knowledge.workspace.google.com/admin/users/access/turn-google-workspace-studio-on-or-off-for-your-organization)

---

## 2. Manage access to Studio features

Admins can control whether users can:

- Use **Gemini** to create flows.
- Use **AI-powered steps** in flows.
- Use steps for other Workspace services.
- Use integrations or custom steps.

### Recommendations

- Allow users with **Gemini for Google Workspace** access to use Gemini features in Studio.
- Allow users to use steps for Workspace services they already have access to.
- Only block steps for a Workspace service if there is a risk of abuse.
- Use the **Google Workspace Marketplace allowlist** to control which integrations and published custom steps users can use.

### Related help

- [Manage access to steps and starters in Workspace Studio](https://knowledge.workspace.google.com/admin/studio/manage-access-to-steps-and-starters-in-workspace-studio)

---

## 3. Manage who can share flows

Flow sharing allows users to distribute useful automation templates internally, improving productivity and reducing duplicate work.

### How sharing works

> “When a user shares a flow, the recipient clicks a link to get a _copy_ of the flow.”

The copied flow includes the owner’s setup, such as:

- Text entered by the owner
- Email addresses
- Links to Drive files

Important access behavior:

> “The recipient does not get access to the owner's private data, like emails or Drive files, only the content that they can already access.”

### Where to find the setting

**Admin console → Apps → Google Workspace → Workspace Studio → Sharing settings**

### Recommendation

Allow sharing for **trusted organizational units and groups** so they can distribute standardized flow templates.

### Related help

- [Allow people to share flows in Workspace Studio](https://knowledge.workspace.google.com/admin/studio/allow-people-to-share-flows-in-workspace-studio)

---

## 4. Set up alerts

Admins can create activity rules to receive notifications about specific Workspace Studio activity.

### Recommended alert: High-frequency flow activity

Purpose: Detect flows that may be looping or running excessively.

- **Condition:** Create a rule for **Rule log events** where the event is **Start run**.
- **Threshold:** Alert if the count exceeds **100** in **1 hour**.
- **Action:** Send an email to all admins.

### Recommended alert: AI usage

Purpose: Monitor generative AI use in automations.

- **Condition:** Create a rule where **Step name** contains **"Ask Gemini"**.
- Optionally include other AI-powered steps.
- For the full list of available steps, see:
  - [Guide to Starters & Steps in Workspace Studio](https://support.google.com/workspace-studio/answer/16765661)
- **Action:** Send a notification to the Super Admin.

### Related help

- [Set up activity alerts for Workspace Studio](https://knowledge.workspace.google.com/admin/studio/set-up-activity-alerts-for-workspace-studio)

---

# Step 2. Support your users

Admins sh

[... summary truncated for context management ...]
