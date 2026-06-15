---
title: "Build an HTTP Google Chat app  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/quickstart/gcf-app"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:14:37Z"
extraction_method: "web_extract"
---

# Build an HTTP Google Chat App — Comprehensive Summary

**Source:** Google for Developers — Google Chat quickstart  
**URL:** https://developers.google.com/workspace/chat/quickstart/gcf-app  
**Last updated:** 2026-04-20 UTC

---

## Overview

This guide explains how to build a basic **HTTP Google Chat app** using a **Cloud Run function**. The app responds to user messages in Google Chat with a **card message** that displays the sender’s **display name** and **avatar image**.

> “This page explains how to create an HTTP Chat app.”

The quickstart uses Google Cloud, but the same HTTP architecture can work with:

- Cloud Run
- App Engine
- Other cloud services
- On-premises web servers

The app is implemented as a web service that receives HTTP requests from Google Chat and returns HTTP responses.

---

## What the App Does

The sample app:

- Receives a message from Google Chat.
- Runs a Cloud Run function.
- Responds with:
  - Text: `Here's your avatar`
  - A card titled `Hello <displayName>!`
  - The user’s avatar image
- Supports example app commands:
  - `/about`
  - `Help`

For commands, it replies privately:

```text
The Avatar app replies to Google Chat messages.
```

---

## HTTP Chat App Architecture

A user interaction follows this flow:

1. A user sends a message to the Chat app:
   - In a direct message
   - Or in a Chat space
2. Google Chat sends an **HTTP request** to a web server containing the app logic.
3. The app logic can optionally integrate with:
   - Google Workspace services, such as Calendar and Sheets
   - Google services, such as Maps, YouTube, and Vertex AI
   - External services, such as project management or ticketing tools
4. The web server sends an **HTTP response** back to Google Chat.
5. Google Chat delivers the response to the user.
6. Optionally, the Chat app can call the **Chat API** asynchronously to:
   - Post messages
   - Perform other Chat operations

Key advantage:

> “This architecture provides you the flexibility to use existing libraries and components that already exist in your system because these Chat apps can be designed using different programming languages.”

---

## Objectives

By the end of the guide, you will:

- Set up your Google Cloud environment.
- Create and deploy a Cloud Run function.
- Publish the app to Google Chat.
- Test the app in Google Chat.

---

## Prerequisites

You need:

- A **Business or Enterprise Google Workspace account** with access to Google Chat.
- A **Google Cloud project with billing enabled**.

Useful references:

- Verify billing status:  
  https://cloud.google.com/billing/docs/how-to/verify-billing-enabled
- Create a Google Cloud project:  
  https://developers.google.com/workspace/guides/create-project

---

## Set Up the Environment

Before using Google APIs, enable the required APIs in your Google Cloud project.

Enable these APIs:

- Google Chat API
- Cloud Build API
- Cloud Functions API
- Cloud Pub/Sub API
- Cloud Logging API
- Artifact Registry API
- Cloud Run API

Direct enablement link:

https://console.developers.google.com/flows/enableapi?apiid=chat.googleapis.com,cloudbuild.googleapis.com,cloudfunctions.googleapis.com,pubsub.googleapis.com,logging.googleapis.com,artifactregistry.googleapis.com,run.googleapis.com

---

# Create and Deploy a Cloud Run Function

The function generates a Google Chat card showing the sender’s name and avatar.

Go to Cloud Run:

https://console.developers.google.com/run

Make sure the correct Google Cloud project is selected.

---

## Common Cloud Run Function Setup

For all runtimes:

1. Open the **Cloud Run** page.
2. Click **Write a function**.
3. On the **Create service** page:
   - **Service name:** `quickstartchatapp`
   - **Region:** Select a region
   - **Runtime:** Choose Node.js, Python, or Java
   - **Authentication:** Select **Require authentication**
4. Click **Create**.
5. Wait for Cloud Run to create the service.
6. The console redirects to the **Source** tab.
7. Set the correct entry point for your runtime.
8. Replace the sample source code.
9. Click **Save and redeploy**.

---

## Node.js Implementation

### Entry Point

```text
avatarApp
```

### File

```text
index.js
```

### GitHub Source

https://github.com/googleworkspace/google-chat-samples/blob/main/node/avatar-app/index.js

### Key Node.js Code

```js
const functions = require('@google-cloud/functions-framework');

// Command IDs (configure these in Google Chat API)
const ABOUT_COMMAND_ID = 1; // ID for the "/about" slash command
const HELP_COMMAND_ID = 2; // ID for the "Help" quick command

/**
 * Google Cloud Function that handles HTTP requests from Google Chat.
 *
 * @param {Object} req - The HTTP request object sent from Google Chat.
 * @param {Object} res - The HTTP response object.
 */
functions.http('avatarApp', (req, res) => {
  const event = req.body;

  if (event.appCommandMetadata) {
    handleAppCommands(event, res);
  } else {
    handleRegularMessage(event, res);
  }
});
```

### Command Handli

[... summary truncated for context management ...]
