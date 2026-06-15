---
title: "Build a Google Chat app as a webhook  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/quickstart/webhooks"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:10:59Z"
extraction_method: "web_extract"
---

# Build a Google Chat App as a Webhook — Comprehensive Summary

**Source:** Google for Developers — <https://developers.google.com/workspace/chat/quickstart/webhooks>  
**Last updated:** 2026-04-20 UTC

---

## Overview

Incoming webhooks let external services send **asynchronous, one-way notifications** into a specific Google Chat space using standard HTTP requests.

> “Webhooks provide a way for external services to send asynchronous, one-way notifications to Google Chat spaces.”

Typical use case:

- A monitoring system detects a server outage.
- It sends a `POST` request to a Google Chat webhook URL.
- A message appears in a Chat space for on-call staff.

For synchronous or interactive Chat apps, use the Google Chat API guide to [Send a message](https://developers.google.com/workspace/chat/api/guides/v1/messages/create) or build a full [Chat app](https://developers.google.com/workspace/chat/quickstart/gcf-app).

---

## Important Characteristics

Webhooks are **not conversational**.

They:

- Send messages into Chat spaces.
- Use standard HTTP `POST` requests.
- Work only in the Chat space where they’re registered.
- Can start or reply to message threads using `threadKey`.
- Can work in direct messages only when all users have Chat apps enabled.

They **cannot**:

- Receive messages from users.
- Respond to user messages.
- Receive Chat app interaction events.
- Be published to the Google Workspace Marketplace.

> “With this type of architecture design, users can't interact with the webhook or the connected external application because communication is one-way.”

> “Webhooks aren't conversational. They can't respond to or receive messages from users or Chat app interaction events.”

---

## Architecture Flow

A webhook-based Chat app follows this flow:

1. External third-party service triggers logic, such as:
   - Project management system
   - Ticketing tool
   - Monitoring application
2. Hosted app logic runs in:
   - Cloud infrastructure, or
   - On-premises systems
3. The app sends a message using a webhook URL to a specific Chat space.
4. Users receive the message in that Chat space but cannot interact with the webhook app.

---

## Prerequisites

Common prerequisites for all implementations:

- A **Business or Enterprise Google Workspace account** with access to Google Chat.
- The Google Workspace organization must allow users to **add and use incoming webhooks**.
- A Google Chat space.
  - Can be created via the Google Chat API or directly in Chat.

Language-specific prerequisites:

### Node.js

- Node.js 14 or greater
- npm

### Python

- Python 3.6 or greater
- pip
- `httplib2` library

Install `httplib2`:

```bash
pip install httplib2
```

### Java

- Java 11 or greater
- Maven

### Apps Script

- A standalone Apps Script project
- Advanced Chat Service enabled

---

# Creating a Webhook

Creating a webhook involves two main steps:

1. Register the incoming webhook in a Chat space.
2. Write and run a script that sends a message to the webhook URL.

---

## Register the Incoming Webhook

1. Open [Google Chat](https://chat.google.com/) in a browser.
   - Webhooks are **not configurable from the Chat mobile app**.
2. Go to the space where you want to add the webhook.
3. Next to the space title, click the expand arrow.
4. Click **Apps & integrations**.
5. Click **Add webhooks**.
6. In the **Name** field, enter:

```text
Quickstart Webhook
```

7. In the **Avatar URL** field, enter:

```text
https://developers.google.com/chat/images/chat-product-icon.png
```

8. Click **Save**.
9. To copy the webhook URL:
   - Click **More**
   - Click **Copy link**

---

## Webhook URL Security

The webhook URL contains two important parameters:

- `key` — a common value shared between webhooks.
- `token` — a unique secret value.

> “The webhook URL contains two parameters: `key`, a common value shared between webhooks, and `token` which is a unique value that must be kept secret to preserve the security of your webhook.”

Keep the webhook URL private.

---

# Sending a Message with a Webhook

The webhook script sends a `POST` request to the webhook URL.

The request:

- Uses `Content-Type: application/json; charset=UTF-8`
- Sends a JSON body containing the Chat message
- Receives a Google Chat API `Message` response

---

## Basic Node.js Example

```javascript
/**
    * Sends asynchronous message to Google Chat
    * @return {Object} response
    */
async function webhook() {
     const url = "https://chat.googleapis.com/v1/spaces/SPACE_ID/messages?key=KEY&token=TOKEN"
     const res = await fetch(url, {
       method: "POST",
       headers: {"Content-Type": "application/json; charset=UTF-8"},
       body: JSON.stringify({
         text: "Hello from a Node script!"
       })
     });
     return await res.json();
}

webhook().then(res => console.log(res));
```

Replace the `url` value with the copied webhook URL.

Run:

```bash
node index.js
```

---

## Basic Python Example

```python
from json import dumps
fr

[... summary truncated for context management ...]
