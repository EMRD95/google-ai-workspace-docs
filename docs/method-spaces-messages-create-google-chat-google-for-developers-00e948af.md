---
title: "Method: spaces.messages.create  |  Google Chat  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages/create"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:14:37Z"
extraction_method: "web_extract"
---

# Google Chat API: `spaces.messages.create` — Summary

**Source:** <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages/create>  
**Last updated:** 2026-05-07 UTC

## Purpose

Creates a message in a Google Chat space.

> Creates a message in a Google Chat space. For an example, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

Messages can be created using either **app authentication** or **user authentication**, with different sender attribution and message content capabilities.

---

## Key Capabilities & Constraints

- Creates messages in Google Chat spaces.
- Supports **text**, **cards**, and **accessory widgets** when using **app authentication**.
- Supports **text only** when using **user authentication**.
- Can start a new thread or reply to an existing thread.
- Supports idempotent message creation using `requestId`.
- Supports custom message IDs using `messageId`.
- Supports notification behavior controls, including forced or silent notifications.
- Maximum message size:

> The maximum message size, including the message contents, is 32,000 bytes.

- For webhook requests:

> For [webhook](https://developers.google.com/workspace/chat/quickstart/webhooks) requests, the response doesn't contain the full message. The response only populates the `name` and `thread.name` fields in addition to the information that was in the request.

---

## Authentication Behavior

Google Chat attributes the message sender differently depending on the authentication type.

### App Authentication

Required scope:

```text
https://www.googleapis.com/auth/chat.bot
```

With app authentication:

- Chat displays the **Chat app** as the sender.
- Message content can include:
  - `text`
  - `cardsV2`
  - `accessoryWidgets`

### User Authentication

Supported scopes:

```text
https://www.googleapis.com/auth/chat.messages.create
https://www.googleapis.com/auth/chat.messages
https://www.googleapis.com/auth/chat.import
```

Notes:

- `chat.import` applies to **import mode spaces only**.
- Chat displays the **user** as the sender.
- The Chat app is attributed by displaying its name.
- Message content can only contain:

```text
text
```

---

## HTTP Request

```http
POST https://chat.googleapis.com/v1/{parent=spaces/*}/messages
```

The URL uses **gRPC Transcoding** syntax.

---

## Path Parameters

| Parameter | Type | Required | Description |
|---|---:|:---:|---|
| `parent` | `string` | Yes | Resource name of the space where the message is created. Format: `spaces/{space}` |

Example format:

```text
spaces/{space}
```

---

## Query Parameters

| Parameter | Type | Required | Description |
|---|---:|:---:|---|
| `threadKey` | `string` | No | **Deprecated.** Use `thread.thread_key` instead. ID for the thread. Supports up to **4000 characters**. Used to start or add to a thread. |
| `requestId` | `string` | No | Unique request ID for the message. If an existing request ID is reused, Chat returns the message created with that ID instead of creating a duplicate. |
| `messageReplyOption` | `enum (MessageReplyOption)` | No | Specifies whether the message starts a thread or replies to one. Only supported in named spaces. Ignored when responding to user interactions. |
| `messageId` | `string` | No | Custom ID for the message. Lets Chat apps get, update, or delete a message without storing the system-assigned ID. |
| `createMessageNotificationOptions` | `object (CreateMessageNotificationOptions)` | No | Controls notification behavior when the message is posted. |

---

## `messageId` Custom ID Requirements

`messageId` lets a Chat app assign a custom ID to a message so it can later retrieve, update, or delete the message without storing the system-generated `name`.

Requirements:

- Must begin with:

```text
client-
```

- Example of a valid ID:

```text
client-custom-name
```

- Example of an invalid ID:

```text
custom-name
```

- Must contain **up to 63 characters**.
- May contain only:
  - lowercase letters
  - numbers
  - hyphens
- Must be **unique within a space**.
- A Chat app can’t use the same custom ID for different messages.

---

## Request Body

The request body contains an instance of:

```text
Message
```

---

## Response Body

If successful, the response body contains a newly created instance of:

```text
Message
```

---

## Required OAuth Scopes

Requires one of the following OAuth scopes:

```text
https://www.googleapis.com/auth/chat.bot
https://www.googleapis.com/auth/chat.import
https://www.googleapis.com/auth/chat.messages
https://www.googleapis.com/auth/chat.messages.create
```

---

# `MessageReplyOption`

Specifies how to reply to a message.

> More states might be added in the future.

| Enum | Description |
|---|---|
| `MESSAGE_REPLY_OPTION_UNSPECIFIED` | Default. Starts a new thread. Ignores any included `thread ID` or `threadKey`. |
| `REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD` | Creates the message as a reply to the specified `thread ID` or `thre

[... summary truncated for context management ...]
