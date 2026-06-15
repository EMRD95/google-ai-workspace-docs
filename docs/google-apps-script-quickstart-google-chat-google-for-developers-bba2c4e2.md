---
title: "Google Apps Script quickstart  |  Google Chat  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/api/guides/quickstart/apps-script"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:16:12Z"
extraction_method: "web_extract"
---

# Google Apps Script Quickstart for Google Chat API — Summary

**Source:** Google Developers — Google Chat API  
**URL:** https://developers.google.com/workspace/chat/api/guides/quickstart/apps-script  
**Last updated:** 2026-04-20 UTC

---

## Purpose

This quickstart shows how to create a **Google Apps Script** that calls the **Google Chat API** to **list Chat spaces**.

It demonstrates how to:

- Configure a Google Cloud project.
- Enable the Google Chat API.
- Configure OAuth consent.
- Configure a Google Chat app.
- Create and configure an Apps Script project.
- Link Apps Script to the Cloud project.
- Use an Advanced Google service to call the Chat API.
- Run and authorize the sample script.

> Quickstarts explain how to set up and run an app that calls a Google Workspace API.

The guide uses a **simplified authentication approach** intended for testing.

> This quickstart uses a simplified authentication approach that is appropriate for a testing environment.

For production apps, Google recommends learning about authentication and authorization before choosing credentials.

---

## Key Concepts

### Apps Script + Google Workspace APIs

In Apps Script, Google Workspace quickstarts use **Advanced Google services** to call Google Workspace APIs.

> In Apps Script, Google Workspace quickstarts use Advanced Google services to call Google Workspace APIs and handle some details of the authentication and authorization flow.

### Google Chat app configuration is required

To call the Google Chat API, you must configure a **Google Chat app**. For write requests, Google Chat uses the app’s configured identity in the Chat UI.

---

## Objectives

- Configure the environment.
- Create and configure the script.
- Run the script.

---

## Prerequisites

You need:

- A **Google Cloud project**.
- A **Business or Enterprise Google Workspace account** with access to **Google Chat**.

---

# Setup Workflow

## 1. Configure Your Google Cloud Project

If using a new Cloud project, configure it and add yourself as a test user. If already configured, skip ahead.

---

## 2. Open or Create a Cloud Project

In the Google Cloud console:

1. Go to **Select a project**.
2. Select an existing Google Cloud project, or click **Create project**.
3. If creating a new project, you might need to enable billing.

Link:

- [Select a Cloud project](https://console.cloud.google.com/projectselector2)

---

## 3. Enable the Google Chat API

Before using Google APIs, enable them in a Cloud project.

Action:

- Enable the **Google Chat API** in the Google Cloud console.

Link:

- [Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=chat.googleapis.com)

---

## 4. Configure the OAuth Consent Screen

In the Google API Console:

1. Go to **Menu > Google Auth platform > Branding**.
2. If the Google Auth platform is not configured, click **Get Started**.
3. Configure the following:

### App Information

- **App name:** enter a name for the app.
- **User support email:** choose an address users can contact for consent questions.

### Audience

- Select **Internal**.

### Contact Information

- Enter an email address to receive project change notifications.

### Finish

- Review the **Google API Services User Data Policy**.
- If you agree, select:

> I agree to the Google API Services: User Data Policy

Then click:

- **Continue**
- **Create**

### Scopes

For this quickstart:

- You can skip adding scopes for now.

Important production note:

> In the future, when you create an app for use outside of your Google Workspace organization, you must change the User type to External. Then add the authorization scopes that your app requires.

Reference:

- [Configure OAuth consent](https://developers.google.com/workspace/guides/configure-oauth-consent)

---

## 5. Configure the Google Chat App

To call the Google Chat API, configure a Chat app.

Open:

- [Chat API Configuration page](https://console.developers.google.com/apis/api/chat.googleapis.com/hangouts-chat)

Under **Application info**, enter:

| Field | Value |
|---|---|
| **App name** | `Chat API quickstart app` |
| **Avatar URL** | `https://developers.google.com/chat/images/quickstart-app-avatar.png` |
| **Description** | `Quickstart for calling the Chat API` |

Then:

1. Under **Interactive features**, turn **Enable interactive features** off.
2. Click **Save**.

---

# Create the Apps Script Project

## 1. Create a New Script

Go to:

- [script.google.com/create](https://script.google.com/create)

## 2. Add the Sample Code

Replace the contents of the script editor with:

```javascript
/**
 * This quickstart sample shows how to list spaces with user credential
 *
 * It relies on the OAuth2 scope 'https://www.googleapis.com/auth/chat.spaces.readonly'
 * referenced in the manifest file (appsscript.json).
 */
function listSpaces() {
  // Initialize request argument(s)
  // Filter spaces by space type (SPACE or GROUP_CHAT or DIRECT_MESSAGE)
  const filter = 'space_type = "SPACE

[... summary truncated for context management ...]
