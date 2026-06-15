---
title: "Build a Google Chat app behind a firewall with Pub/Sub  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/quickstart/pub-sub"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:16:12Z"
extraction_method: "web_extract"
---

# Build a Google Chat App Behind a Firewall with Pub/Sub — Summary

**Source:** Google for Developers — Google Chat quickstart  
**URL:** https://developers.google.com/workspace/chat/quickstart/pub-sub  
**Last updated:** 2026-05-06 UTC

---

## Purpose

This guide explains how to build a **Google Chat app that communicates asynchronously through Google Cloud Pub/Sub**.

This architecture is useful when:

- Your organization has a **firewall** that prevents Google Chat from sending direct HTTP requests to your app.
- Your Chat app uses the **Google Workspace Events API**.
- You want an application server, either cloud-hosted or on-premises, to pull Chat events from Pub/Sub.

---

## Key Architecture

A Pub/Sub-based Chat app works as follows:

1. A user sends a message to the Chat app in:
   - A direct message
   - A Chat space
   - A Chat space where the app has an active subscription

2. Google Chat publishes the event to a **Pub/Sub topic**.

3. Your application server subscribes to the Pub/Sub topic using a **pull subscription**.

4. Your app processes the event and can optionally call the **Google Chat API** to respond asynchronously.

> “This type of architecture for a Chat app is useful if your organization has a firewall, which can prevent Chat from sending messages to your Chat app, or if the Chat app uses the Google Workspace Events API.”

---

## Important Limitations

Because Pub/Sub Chat apps only support **asynchronous messages**, they have these limitations:

- **Dialogs are not supported.**
  - Use a **card message** instead.

- **Individual cards can’t be updated with synchronous responses.**
  - To update content, patch the entire message using the Chat API `patch` method.

> “Can't use dialogs in messages. Instead, use a card message.”

> “Can't update individual cards with a synchronous response. Instead, update the entire message by calling the `patch` method.”

---

## Prerequisites

### Required for All Languages

- A **Business or Enterprise Google Workspace account** with access to Google Chat.
- A **Google Cloud project with billing enabled**.
- The **Google Chat API** and **Pub/Sub API** enabled.
- A service account for your Chat app.
- A Pub/Sub topic and pull subscription.
- The Chat app must **not** be configured as a Google Workspace add-on.

> When configuring the Chat API, clear **Build this Chat app as a Google Workspace add-on**.

### Language-Specific Requirements

#### Node.js

- Node.js 14 or greater
- npm
- Initialized Node.js project:

```bash
npm init
```

#### Python

- Python 3.6 or greater
- pip

#### Java

- Java 11 or greater
- Maven

---

## Set Up the Environment

Enable these APIs in your Google Cloud project:

- **Google Chat API**
- **Pub/Sub API**

Google provides a console shortcut:

```text
https://console.cloud.google.com/flows/enableapi?apiid=chat.googleapis.com,pubsub.googleapis.com
```

---

## Set Up Pub/Sub

Complete these Pub/Sub setup steps:

1. **Create a Pub/Sub topic**
   - Recommended: use **one topic per Chat app**.

2. **Grant Google Chat permission to publish to the topic**
   - Assign the **Pub/Sub Publisher** role to this service account:

```text
chat-api-push@system.gserviceaccount.com
```

3. **Create a service account** for the Chat app.
   - This account authorizes access to Pub/Sub and Google Chat.
   - Save the private key file to your working directory.

4. **Create a pull subscription** to the topic.

5. Assign the **Pub/Sub Subscriber** role on the subscription to the service account you created.

---

## Required Environment Variables

For Node.js, Python, and Java examples, set the following environment variables:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=SERVICE_ACCOUNT_FILE_PATH
```

```bash
export PROJECT_ID=PROJECT_ID
```

```bash
export SUBSCRIPTION_ID=SUBSCRIPTION_ID
```

Where:

- `GOOGLE_APPLICATION_CREDENTIALS` is the path to the service account key file.
- `PROJECT_ID` is your Google Cloud project ID.
- `SUBSCRIPTION_ID` is the Pub/Sub pull subscription ID.

---

## Application Behavior

The sample app listens for Pub/Sub messages and handles Chat events based on their type.

### Event Handling Logic

| Event type | Behavior |
|---|---|
| `MESSAGE` | Responds in the same thread with `You said: <message>` |
| `ADDED_TO_SPACE` with no message | Posts `Thank you for adding me!` |
| `ADDED_TO_SPACE` from an @mention | Falls through to message response behavior |
| `REMOVED_FROM_SPACE` | Does not respond |

Key response text used by the samples:

```text
Thank you for adding me!
```

```text
You said: `<user message>`
```

---

## Node.js Implementation Summary

### `package.json`

Create `package.json` with dependencies for Google Chat and Pub/Sub:

```json
{
     "name": "pub-sub-app",
     "version": "1.0.0",
     "description": "Google Chat App that listens for messages via Cloud Pub/Sub",
     "main": "index.js",
     "scripts": {
       "start": "node index.js",
       "test": "echo \"Error: no test specified\

[... summary truncated for context management ...]
