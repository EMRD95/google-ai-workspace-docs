---
title: "Build a Google Chat app with Google Apps Script  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/quickstart/apps-script-app"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:16:12Z"
extraction_method: "web_extract"
---

# Build a Google Chat App with Google Apps Script — Summary

**Source:** https://developers.google.com/workspace/chat/quickstart/apps-script-app  
**Last updated:** 2026-04-20 UTC  
**Goal:** Create a Google Chat app using **Google Apps Script** that can receive direct messages and echo user messages back.

---

## Key Purpose

This quickstart shows how to build a simple Google Chat app that:

- Can be directly messaged in Google Chat.
- Responds by echoing the user’s message.
- Is implemented with **Google Apps Script**.
- Runs using Google Cloud infrastructure.
- Can optionally integrate with Google Workspace and Google services.

> Create a Google Chat app that you can directly message and that responds by echoing your messages.

---

## Architecture & Message Flow

The app follows this interaction pattern:

1. A user sends a message to the Chat app, either in a direct message or in a Chat space.
2. The Chat app logic, implemented in Apps Script and hosted in Google Cloud, receives and processes the message.
3. Optionally, the app logic can integrate with:
   - Google Workspace services, such as Calendar or Sheets.
   - Other Google services, such as Google Maps or YouTube.
4. The app logic sends a response back to the Chat app service.
5. Google Chat delivers the response to the user.

---

## Objectives

By the end of the guide, you will:

- Set up your environment.
- Set up the Apps Script project.
- Configure the Chat app.
- Test the Chat app.

---

## Prerequisites

You need:

- A **Business or Enterprise Google Workspace account** with access to [Google Chat](https://workspace.google.com/products/chat/).
- A **Google Cloud project**.

Reference:

- [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project)

---

# Setup Steps

---

## 1. Set Up Your Environment

### Open Your Cloud Project

If you already have a Google Cloud project:

1. Go to the **Select a project** page in the Google Cloud console.
2. Select the project you want to use.

If you don’t have one:

1. Click **Create project**.
2. Follow the on-screen instructions.
3. If required, enable billing for the project.

Useful link:

- [Select a Cloud project](https://console.cloud.google.com/projectselector2)

---

### Enable the Google Chat API

Before using Google APIs, enable them in your Google Cloud project.

Action:

- Enable the **Google Chat API** in the Google Cloud console.

Useful link:

- [Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=chat.googleapis.com)

---

## 2. Configure the OAuth Consent Screen

All apps using OAuth 2.0 require a consent screen configuration.

The consent screen:

- Defines what users and app reviewers see.
- Registers the app so it can be published later.

Go to:

- **Google API Console > Google Auth platform > Branding**

Useful link:

- [Go to Branding](https://console.developers.google.com/auth/branding)

---

### OAuth Consent Configuration Steps

If the Google Auth platform is not configured yet, click **Get Started**.

Then configure:

1. Under **App Information**:
   - In **App name**, enter a name for the app.
   - In **User support email**, choose a support email address.

2. Click **Next**.

3. Under **Audience**:
   - Select **Internal**.

4. Click **Next**.

5. Under **Contact Information**:
   - Enter an **Email address** for project notifications.

6. Click **Next**.

7. Under **Finish**:
   - Review the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy).
   - If you agree, select:

> I agree to the Google API Services: User Data Policy

8. Click **Continue**.

9. Click **Create**.

---

### Notes About Scopes and External Apps

For this quickstart, you can skip adding scopes.

Important future consideration:

> In the future, when you create an app for use outside of your Google Workspace organization, you must change the **User type** to **External**. Then add the authorization scopes that your app requires.

Reference:

- [Configure OAuth consent](https://developers.google.com/workspace/guides/configure-oauth-consent)

---

# Set Up the Apps Script Project

---

## Create the Script from the Template

1. Go to the [Apps Script Getting Started page](https://script.google.com/home/start).
2. Click the **Chat App** template.
3. Click **Untitled project**.
4. Rename it:

```text
Quickstart app
```

5. Click **Rename**.

---

### Cloud Project Association Note

For this guide, you **don’t need** to associate your Apps Script project with your Google Cloud project.

However, in the future, you must associate them if you want to:

- Use certain Google APIs.
- Publish your app.

Reference:

- [Google Cloud projects guide](https://developers.google.com/apps-script/guides/cloud-platform-projects)

---

## Create a Test Deployment

You need a deployment ID for the Apps Script project.

Steps:

1. In the Apps Script project, click:

```text
Deploy > Test deployments
```

2. Copy the *

[... summary truncated for context management ...]
