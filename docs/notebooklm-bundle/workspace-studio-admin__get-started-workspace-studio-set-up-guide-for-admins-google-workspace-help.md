# Get started: Workspace Studio set up guide for admins  |  Google Workspace Help

**Product Area:** workspace-studio-admin
**Source:** https://knowledge.workspace.google.com/admin/studio/get-started-workspace-studio-set-up-guide-for-admins

# Get started: Workspace Studio set up guide for admins — Summary

**Source:** https://knowledge.workspace.google.com/admin/studio/get-started-workspace-studio-set-up-guide-for-admins  
**Last updated:** 2026-06-11 UTC  
**Audience:** Google Workspace administrators

---

## Overview

Google Workspace Studio lets users create **“flows”** to automate routine work across Google Workspace apps such as **Gmail, Drive, and Chat**, as well as third-party services.

Users with access to **Gemini** can build flows by describing what they want the automation to do.

> Google Workspace Studio allows users to create "flows" that automate routine work tasks across Google Workspace apps, including Gmail, Drive, and Chat, and third-party services.

Flows can act on behalf of users, including:

- Drafting emails
- Creating and updating files
- Creating tasks
- Performing other automated actions across connected services

Because flows can modify data and send communications, poorly configured flows may create risk.

> Poorly configured flows could unintentionally edit or delete data, or send excessive notifications.

Admins can manage risks using:

- Access policies
- Feature controls
- Sharing settings
- Alerts
- Audit and investigation tools
- Emergency stop procedures

---

# Step 1. Set up Workspace Studio for your organization

Before enabling users, Google recommends configuring access and guardrails so flows behave as expected and data remains secure.

---

## 1. Manage access to Studio

### Admin setting location

**Admin console → Menu → Apps → Google Workspace → Workspace Studio**

### Required action

Check that **Service status** is set to **ON** for the correct:

- Organizational units
- Groups

### Recommendation

Create a **child organizational unit** with Workspace Studio access turned **off**.

This gives admins a fast emergency control: move a user into that OU to stop all flows they own.

> **Recommendation**: Create a child organizational unit that has access to Studio turned off. This lets you quickly move a user to it to stop a flow they own.

### Related help

- [Turn Google Workspace Studio on or off for your organization](https://knowledge.workspace.google.com/admin/users/access/turn-google-workspace-studio-on-or-off-for-your-organization)

---

## 2. Manage access to Studio features

Admins can control whether users can:

- Use **Gemini** to create flows
- Use **AI-powered steps** in flows
- Use steps for other Google Workspace services
- Use integrations or custom steps

### Recommendations

- Allow users with **Gemini for Google Workspace** access to use Gemini features in Studio.
- Allow users to use steps for Workspace services they already have access to.
- Only block service-specific steps if there is a clear risk of abuse.
- Use the **Google Workspace Marketplace allowlist** to control:
  - Integrations
  - Published custom steps

### Related help

- [Manage access to steps and starters in Workspace Studio](https://knowledge.workspace.google.com/admin/studio/manage-access-to-steps-and-starters-in-workspace-studio)

---

## 3. Manage who can share flows

Allowing flow sharing can improve productivity by letting trusted users distribute reusable flow templates.

### How sharing works

When someone shares a flow:

- The recipient receives a **copy** of the flow.
- The copy includes the owner’s setup, such as:
  - Text entered into the flow
  - Email addresses
  - Links to Drive files
- The recipient does **not** get access to private data they could not already access.

> When a user shares a flow, the recipient clicks a link to get a _copy_ of the flow. The copy includes the owner's setup, such as text they entered, email addresses, and links to files in Drive. The recipient does not get access to the owner's private data, like emails or Drive files, only the content that they can already access.

### Admin setting location

**Admin console → Apps → Google Workspace → Workspace Studio → Sharing settings**

### Recommendation

Allow sharing for **trusted organizational units and groups** so they can distribute standardized flow templates.

### Related help

- [Allow people to share flows in Workspace Studio](https://knowledge.workspace.google.com/admin/studio/allow-people-to-share-flows-in-workspace-studio)

---

## 4. Set up alerts

Admins can create activity rules to be notified about specific Workspace Studio activity.

---

### Recommended alert: High-frequency flow activity

Purpose: Detect flows that may be looping or running excessively.

**Condition:**

- Create a rule for **Rule log events**
- Event: **Start run**

**Threshold:**

- Alert if count exceeds **100** in **1 hour**

**Action:**

- Send an email to all admins

---

### Recommended alert: AI usage

Purpose: Monitor generative AI use in automations.

**Condition:**

- Create a rule where **Step name** contains **"Ask Gemini"**
- Optionally include other AI-powered steps

For the full list of available steps, see:

- [Guide t

[... summary truncated for context management ...]
