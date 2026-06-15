# Manage access to Gemini features in Workspace services  |  Generative AI  |  Google Workspace Help

**Product Area:** admin-console
**Source:** https://support.google.com/a/answer/15698295?hl=en

# Manage Access to Gemini Features in Workspace Services — Summary

**Source:** Google Workspace Help — “Manage access to Gemini features in Workspace services”  
**URL:** https://support.google.com/a/answer/15698295?hl=en  
**Last updated:** 2026-06-11 UTC

---

## Purpose

Google Workspace administrators can manage whether **Gemini features and the Gemini side panel** are available in specific Workspace services.

---

## Supported Editions

> _Supported editions for this feature: Enterprise Standard and Enterprise Plus; Teaching and Learning add-on and Education Plus; Google AI Pro for Education, and AI Ultra Access._

Administrators should verify their edition using Google’s edition comparison page if unsure.

---

## Workspace Services Covered

Admins can enable or disable Gemini features and the side panel in the following services:

- **Gmail**
- **Calendar**
- **Drive, Docs, Sheets, Slides, Forms, Drawings, and Vids**
- **Meet**
- **Chat**
- **Google Workspace Studio**

---

## Default Behavior

> The default setting for Gemini features in Workspace services is **on**.

Important access behavior:

> Even if Gemini is off for a specific app, users can still access its data when using Gemini in other apps. For example, a user in Gmail can ask Gemini about a Drive file when Gemini is turned off for Drive.

**Implication:** Turning Gemini off for one app does **not** fully prevent Gemini from referencing that app’s data through Gemini features in other enabled apps.

---

## How to Turn Gemini On or Off in a Google Service

### Required Admin Privilege

Admins need the:

> [Gemini Settings administrator privilege](https://knowledge.workspace.google.com/admin/users/administrator-privilege-definitions#gemini)

### Steps

1. In the **Google Admin console**, go to:

   > **Menu → Generative AI → Gemini for Workspace**

   Direct link:

   > [Go to Gemini for Workspace](https://admin.google.com/ac/managedsettings/793154499678)

2. Click the **Feature access** panel.

   > **Note:** Available only with supported editions.

3. Optional: Apply the setting to specific users by selecting either:
   - An **organizational unit** — often used for departments
   - A configuration **group** — advanced option

   Important hierarchy rule:

   > Group settings override organizational units.

4. Click **Edit** next to the service you want to enable or disable.

5. Select:
   - **On**, or
   - **Off**

   Then click **Save**.

---

## User Requirement: Smart Features and Personalization

To use Gemini in Workspace services, users must enable smart features and personalization.

> **Note:** To access Gemini in Workspace services, users need to [turn on smart features and personalization](https://support.google.com/mail/answer/10079371).

---

## Other Related Admin Controls

Google lists several additional controls that are separate from the per-service Gemini feature access settings.

### Gemini App

Admins can turn access to the standalone Gemini app on or off:

- **Gemini app:** `gemini.google.com`

Important limitation:

> this has no effect on other AI features in Google Workspace services.

---

### NotebookLM

Admins can turn **NotebookLM** on or off as an **additional service**.

---

### Google Vids

Admins can separately control access to **Google Vids**.

---

### Google Meet AI Notes

Admins can control whether users can:

> let Google AI take notes in meetings

---

### Google Workspace Smart Features

Admins can turn **Google Workspace smart features** on or off.

Users can also control smart features in Google products individually.

---

### AppSheet Gemini Features

Admins can manage:

- **Gemini for App Creation**
- **Gemini in AppSheet Solutions**

---

### Workspace Studio

Admins can:

- Turn **Workspace Studio** on or off
- Block Gemini from Workspace Studio using **API controls**

---

## Key Takeaways

- Gemini features in Workspace services are **on by default** for supported editions.
- Admins can manage Gemini access per supported Workspace service from the **Feature access** panel in **Gemini for Workspace**.
- Settings can be scoped by **organizational unit** or **configuration group**.
- **Group settings override organizational unit settings**.
- Disabling Gemini in one app does **not necessarily block Gemini from accessing that app’s data** through another app.
- Users must enable **smart features and personalization** to access Gemini in Workspace services.
- Separate admin controls exist for the standalone Gemini app, NotebookLM, Vids, Meet AI notes, Workspace smart features, AppSheet Gemini features, and Workspace Studio.

---

## Licensing Note

The page states:

> Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
