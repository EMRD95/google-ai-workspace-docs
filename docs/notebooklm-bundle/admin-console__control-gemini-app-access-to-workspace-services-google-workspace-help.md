# Control Gemini App access to Workspace services  |  Google Workspace Help

**Product Area:** admin-console
**Source:** https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/turn-google-apps-in-gemini-on-or-off

# Control Gemini App Access to Workspace Services – Summary

**Source:** [Google Workspace Help](https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/turn-google-apps-in-gemini-on-or-off)  
**Last updated:** 2026-06-11 UTC

## Overview

As an admin, you can allow the Gemini app to interact with other Google services so users get more helpful, context-aware responses. This setting is available for most Google Workspace editions and qualifying Education plans with the Gemini app core service or add-on. You can also manage access to non-Google apps (e.g., Gemini for GitHub) via the Marketplace allowlist.

## Prerequisites

- **Smart features:** Google Workspace smart features must be turned on for your users.  
  → [Manage Google Workspace smart features for your users](https://knowledge.workspace.google.com/admin/security/manage-google-workspace-smart-features-for-your-users)
- **Conversation history:** The Gemini conversation history setting must be enabled for Workspace apps to work.  
- **Admin privilege:** You need the **Gemini Settings** administrator privilege.

## Supported Apps

### Workspace Apps (require Google Workspace license)
- Google Calendar
- Google Docs
- Google Drive
- Gmail
- Google Keep
- Google Tasks

> **Note:** Users with Gemini as an additional Google service **cannot** use Workspace apps.

### Other Google Apps (available to all Google users, including those without a Workspace license)
- Google Maps
- YouTube (including YouTube Music)
- Google Hotels
- Google Flights

These are treated as additional services and governed by the [Google Terms of Service](https://policies.google.com/terms).

## Using Workspace Apps – Key Behaviors

- **Service dependencies:** If your organization has disabled a particular Workspace service (e.g., Tasks), the corresponding Workspace app is unavailable in Gemini.  
  **Critical:** When a prompt contains multiple actions involving different services, and *any* of them is disabled, **none** of the actions are completed.  
  > Example: “Create a Calendar event and add a reminder” → If Tasks is off, the event won’t be created and no reminder is set.

- **Citations in Gmail:** To get links to additional Gmail information in Gemini’s responses (citations), Workspace apps must be turned on.

- **File uploads:** Users can upload Drive files to Gemini or to Gems only when Workspace apps are enabled.  
  → [Upload & analyze files in Gemini Apps](https://support.google.com/gemini/answer/14903178)  
  → [Use Gems in Gemini Apps](https://support.google.com/gemini/answer/15146780)

- **Turning off Workspace apps:** Existing chats that used Workspace apps remain available, but Gemini can no longer access additional Workspace data beyond the original prompt. Workspace access resumes only after re-enabling.

## Steps to Turn Google Apps in Gemini On or Off

1. Go to the **Google Admin console** → **Menu** → **Generative AI** → **Gemini app**.  
   *(Direct link: [Go to Gemini app](https://admin.google.com/ac/managedsettings/47208553126))*
2. Under **Apps**, select:
   - **Allow access to Workspace apps** (for Gmail, Calendar, Docs, etc.)
   - **Allow access to other Google apps** (for Maps, YouTube, Flights, Hotels)
3. (Optional) Choose an **organizational unit** or **configuration group** to scope the setting.  
   → Group settings override organizational units. [Learn more](https://knowledge.workspace.google.com/admin/users/advanced/customize-service-settings-using-configuration-groups#how-groups-work)
4. Click **Save**.

> Changes typically take effect within a few minutes but can take up to **24 hours**.

## Important Notes

- Users can individually turn off smart features for their accounts, which may affect Gemini’s ability to access Workspace data.  
  → [Turn Google Workspace smart features on or off (user instructions)](https://support.google.com/mail/answer/15604322)
- For non-Google apps (like third-party integrations), use the [Marketplace app allowlist](https://knowledge.workspace.google.com/admin/apps/manage-the-marketplace-app-allowlist-for-your-organization).

## Related Topics

- [Gemini Apps Help Center](https://support.google.com/gemini)
- [Use apps connected to Gemini with a work or school Google Account](https://support.google.com/gemini/answer/14959807)
- [Google Workspace with Gemini FAQ](https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/gemini-for-google-workspace-faq-business)
