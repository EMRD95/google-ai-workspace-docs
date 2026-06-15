---
title: "Build a Google Chat app with Google Apps Script  |  Google for Developers"
source_url: "https://developers.google.com/apps-script/quickstart/chat-app"
product_area: "apps-script-ai"
retrieved_at: "2026-06-15T18:18:54Z"
extraction_method: "web_extract"
---

# Build a Google Chat App with Google Apps Script — Summary

**Source:** https://developers.google.com/apps-script/quickstart/chat-app  
**Last updated:** 2026-04-20 UTC  
**Goal:** Create a Google Chat app using **Google Apps Script** that can receive direct messages or messages in Chat spaces and respond by echoing user messages.

---

## Page Summary

> Create a Google Chat app that you can directly message and that responds by echoing your messages.

The guide walks through how to:

- Set up a Google Cloud environment.
- Enable the Google Chat API.
- Configure the OAuth consent screen.
- Create an Apps Script project from a Chat App template.
- Create a test deployment and copy its deployment ID.
- Configure the Chat app in the Google Chat API console.
- Test the app in Google Chat.
- Troubleshoot errors and clean up Cloud resources.

---

## Architecture and Message Flow

The app is implemented with **Apps Script**, hosted in **Google Cloud**, and connected to Google Chat.

### Message flow

1. A user sends a message to the Chat app:
   - In a direct message, or
   - In a Chat space.
2. The Chat app logic, implemented in **Apps Script**, receives and processes the message.
3. Optionally, the app can integrate with:
   - Google Workspace services such as **Calendar** or **Sheets**
   - Other Google services such as **Google Maps** or **YouTube**
4. The Apps Script logic sends a response back to the Chat app service.
5. Google Chat delivers the response to the user.

---

## Objectives

By the end of the guide, you should be able to:

- Set up your environment.
- Set up the script.
- Configure the Chat app.
- Test the Chat app.

---

## Prerequisites

You need:

- A **Business or Enterprise Google Workspace account** with access to **Google Chat**.
- A **Google Cloud project**.

Relevant links:

- [Google Workspace account information](https://support.google.com/a/answer/6043576)
- [Google Chat](https://workspace.google.com/products/chat/)
- [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project)

---

# Setup Instructions

## 1. Open Your Cloud Project

If your intended Cloud project is not already open:

1. Go to the **Select a project** page in the Google Cloud console.
2. Select the project you want to use.

Alternatively:

- Click **Create project**.
- Follow the on-screen instructions.
- If required, enable billing for the project.

Links:

- [Select a Cloud project](https://console.cloud.google.com/projectselector2)
- [Enable billing for a project](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)

---

## 2. Enable the Google Chat API

Before using Google APIs, you must enable them in a Google Cloud project.

Action:

- In the Google Cloud console, enable the **Google Chat API**.

Link:

- [Enable the Google Chat API](https://console.cloud.google.com/flows/enableapi?apiid=chat.googleapis.com)

---

## 3. Configure the OAuth Consent Screen

All apps using OAuth 2.0 require a consent screen configuration. This defines what users and app reviewers see and registers the app so it can be published later.

### Open OAuth Branding

1. In the Google API Console, go to:

   **Menu > Google Auth platform > Branding**

2. If the Google Auth platform is already configured, update settings in:
   - **Branding**
   - **Audience**
   - **Data Access**

3. If you see:

> **Google Auth platform not configured yet**

Click **Get Started**.

Link:

- [Go to Branding](https://console.developers.google.com/auth/branding)

### OAuth Consent Setup Steps

1. Under **App Information**, in **App name**, enter a name for the app.
2. In **User support email**, choose a support email address.
3. Click **Next**.
4. Under **Audience**, select **Internal**.
5. Click **Next**.
6. Under **Contact Information**, enter an **Email address** for project notifications.
7. Click **Next**.
8. Under **Finish**, review the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy).
9. If you agree, select:

> **I agree to the Google API Services: User Data Policy**

10. Click **Continue**.
11. Click **Create**.

### Scopes Note

For this quickstart:

- You can skip adding scopes.

For future apps used outside your Google Workspace organization:

- Change **User type** to **External**.
- Add the authorization scopes required by your app.

Reference:

- [Configure OAuth consent](https://developers.google.com/workspace/guides/configure-oauth-consent)

---

# Set Up the Apps Script Project

## 4. Create the Script from the Template

Use the Apps Script Chat App template.

Steps:

1. Go to the [Apps Script Getting Started page](https://script.google.com/home/start).
2. Click the **Chat App** template at the top of the page.
3. Click **Untitled project**.
4. Rename it to:

```text
Quickstart app
```

5. Click **Rename**.

### Cloud Project Association Note

For this guide, you **don’t need** to associate your Cloud proje

[... summary truncated for context management ...]
