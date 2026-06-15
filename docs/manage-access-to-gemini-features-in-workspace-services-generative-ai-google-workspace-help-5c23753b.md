---
title: "Manage access to Gemini features in Workspace services  |  Generative AI  |  Google Workspace Help"
source_url: "https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/manage-access-to-gemini-features-in-workspace-services"
product_area: "admin-console"
retrieved_at: "2026-06-15T11:23:14Z"
extraction_method: "web_extract"
---

# Manage access to Gemini features in Workspace services – Summary

This guide explains how administrators can enable or disable **Gemini features** and the **side panel** in specific Google Workspace services. The default setting for Gemini in these services is **ON**.

---

## Supported Editions

- Enterprise Standard
- Enterprise Plus
- Teaching and Learning add-on
- Education Plus
- Google AI Pro for Education
- AI Ultra Access

[Compare editions](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-google-workspace-editions)

---

## Services Where Gemini Access Can Be Managed

- **Gmail**
- **Calendar**
- **Drive, Docs, Sheets, Slides, Forms, Drawings, and Vids**
- **Meet**
- **Chat**
- **Google Workspace Studio**

---

## Important Cross‑Service Data Behavior

Even when Gemini is disabled for a specific app, users can still **access its data** via Gemini in other apps.

> *“Even if Gemini is off for a specific app, users can still access its data when using Gemini in other apps. For example, a user in Gmail can ask Gemini about a Drive file when Gemini is turned off for Drive.”*

---

## Steps to Turn Gemini On or Off in a Google Service

1. Go to the **Google Admin Console** → Menu → **Generative AI** → **Gemini for Workspace**.  
   *(Requires the **Gemini Settings** administrator privilege.)*  
   [Direct link](https://admin.google.com/ac/managedsettings/793154499678)
2. Click the **Feature access** panel.  
   *Note: Available only with the [supported editions](#supported-editions).*
3. (Optional) To scope the setting, select an **organizational unit** or **configuration group** from the side panel.  
   - Group settings override organizational units. [Learn more](https://knowledge.workspace.google.com/admin/users/advanced/customize-service-settings-using-configuration-groups#how-groups-work)
4. Click **Edit** next to the service you want to change.
5. Select **On** or **Off**, then click **Save**.

**User requirement:** To use Gemini in Workspace services, users must [turn on smart features & personalization](https://support.google.com/mail/answer/10079371).

---

## Additional Controls Available to Administrators

- **Gemini app (gemini.google.com)** – Turn on/off independently (does not affect AI features within Workspace services). [Link](https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/turn-the-gemini-app-on-or-off)
- **NotebookLM** – Manage as an [additional service](https://knowledge.workspace.google.com/admin/users/advanced/turn-on-or-off-additional-google-services).
- **Google Vids** – [Turn on/off for users](https://knowledge.workspace.google.com/admin/users/access/turn-vids-on-or-off-for-users).
- **Google AI notes in Meet** – Control whether users can [let Google AI take notes](https://knowledge.workspace.google.com/admin/meet/let-google-meet-ai-take-notes-for-my-users).
- **Google Workspace smart features** – [Turn on/off at the admin level](https://knowledge.workspace.google.com/admin/security/manage-google-workspace-smart-features-for-your-users); users can also [control smart features individually](https://support.google.com/mail/answer/10079371).
- **Gemini for App Creation** – Enable/disable via [AppSheet support](https://support.google.com/appsheet/answer/11918568#gemini-for-app-creation).
- **Gemini in AppSheet Solutions** – [Manage separately](https://support.google.com/appsheet/answer/16106849).
- **Workspace Studio** – [Turn on/off](https://knowledge.workspace.google.com/admin/users/access/turn-google-workspace-studio-on-or-off-for-your-organization); also block Gemini from Workspace Studio using [API controls](https://knowledge.workspace.google.com/admin/studio/manage-access-to-steps-and-starters-in-workspace-studio#service).
