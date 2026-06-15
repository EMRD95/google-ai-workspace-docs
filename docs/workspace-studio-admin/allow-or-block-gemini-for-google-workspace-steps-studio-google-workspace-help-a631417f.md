---
title: "Allow or block Gemini for Google Workspace steps  |  Studio  |  Google Workspace Help"
source_url: "https://knowledge.workspace.google.com/admin/studio/allow-or-block-gemini-for-ws-steps"
product_area: "workspace-studio-admin"
retrieved_at: "2026-06-15T09:46:36Z"
extraction_method: "web_extract"
---

# Allow or Block Gemini for Google Workspace Steps — Summary

**Source:** Google Workspace Help  
**URL:** https://knowledge.workspace.google.com/admin/studio/allow-or-block-gemini-for-ws-steps  
**Last updated:** 2026-06-11 UTC

---

## Purpose

Google Workspace administrators can control whether **Gemini for Google Workspace** is enabled for **Google Workspace Studio**.

When enabled, Gemini lets users:

- Create custom AI steps from a prompt
- Use those AI steps in Workspace Studio flows

If admins only want to block specific AI-powered steps, Google recommends using the separate setting:

- [Allow or block Workspace service–specific steps](https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-service-specific-steps)

---

## Supported Editions

> _Supported editions for this feature: Enterprise Standard and Enterprise Plus; Teaching and Learning add-on and Education Plus; Google AI Pro for Education, and AI Ultra Access. [Compare your edition](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-google-workspace-editions)_

Supported editions include:

- **Enterprise Standard**
- **Enterprise Plus**
- **Teaching and Learning add-on**
- **Education Plus**
- **Google AI Pro for Education**
- **AI Ultra Access**

---

## Age Restriction

> _Users designated as under 18 can't use AI features in Workspace Studio._

Users marked as **under 18** are not allowed to use AI features in Workspace Studio.

---

## Privacy Note

> **Note:** AI features in Workspace Studio follow the privacy principles in the  
> [Generative AI in Google Workspace Privacy Hub](https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub).

---

## Required Admin Privilege

To change this setting, an admin must have the:

- [Gemini Settings administrator privilege](https://knowledge.workspace.google.com/admin/users/administrator-privilege-definitions#gemini)

---

## How to Allow or Block Gemini for Workspace Studio

### Steps in the Google Admin Console

1. In the Google Admin console, go to:

   **Menu → Generative AI → Gemini for Workspace**

   Direct link:

   [Go to Gemini for Workspace](https://admin.google.com/ac/managedsettings/793154499678)

2. Click the **Feature access panel**.

3. Optional: To apply the setting only to certain users, select one of the following from the side panel:

   - An **organizational unit**, often used for departments
   - A configuration **group**, for advanced configuration

   > Group settings override organizational units. [Learn more](https://knowledge.workspace.google.com/admin/users/advanced/customize-service-settings-using-configuration-groups#how-groups-work)

4. Next to **Workspace Studio**, click **Edit**.

5. Select either:

   - **On**
   - **Off**

6. Click **Save**.

   Alternatively, for an organizational unit, you might click **Override**.

---

## Restoring Inherited Settings

To later restore the inherited value:

- Click **Inherit** for an organizational unit
- Click **Unset** for a group

---

## What Happens When Gemini Is Turned Off for Workspace Studio

When Gemini for Google Workspace is turned off for Workspace Studio, users cannot:

- Create flows from a prompt
- Use AI steps

Important operational impact:

> Any active flows that have AI steps in them stop working.

---

## Related Topics

- [Troubleshoot Workspace Studio for your users](https://knowledge.workspace.google.com/admin/studio/troubleshoot-workspace-studio-for-your-users)
- [Troubleshooting and FAQ](https://support.google.com/workspace-studio/#topic=16430802)
- [Create & use custom steps in flows](https://support.google.com/a/users/answer/16433731)
- [Allow or block Workspace service–specific steps](https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-service-specific-steps)
- [Allow or block Workspace Integrations steps](https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-integrations-steps)
- [Allow or block Google Workspace custom steps](https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-custom-steps)
- [Allow or block Send a webhook](https://knowledge.workspace.google.com/admin/studio/allow-or-block-send-a-webhook)

---

## Licensing

Unless otherwise noted:

- Page content is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
- Code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
- See [Google Developers Site Policies](https://developers.google.com/site-policies) for details
- Java is a registered trademark of Oracle and/or its affiliates.
