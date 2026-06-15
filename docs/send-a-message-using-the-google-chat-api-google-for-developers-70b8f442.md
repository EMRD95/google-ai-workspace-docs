---
title: "Send a message using the Google Chat API  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/create-messages"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:14:37Z"
extraction_method: "web_extract"
---

# Send a Message Using the Google Chat API — Comprehensive Summary

**Source:** Google for Developers — Google Chat API  
**URL:** https://developers.google.com/workspace/chat/create-messages  
**Last updated:** 2026-05-08 UTC

---

## Overview

The Google Chat API lets developers use the [`create()` / `CreateMessage()`](https://developers.google.com/workspace/chat/api/reference/rpc/google.chat.v1#google.chat.v1.ChatService.CreateMessage) method on the `Message` resource to create messages in Google Chat.

You can use it to:

- Send messages containing:
  - Plain text
  - Rich text
  - Cards
  - Interactive widgets
- Send private messages visible only to a specific user.
- Start or reply to message threads.
- Assign custom IDs to messages for later retrieval, update, or deletion.
- Quote existing messages.
- Send messages as:
  - A **Chat app**
  - A **Chat app on behalf of a user**

> **Maximum message size:**  
> The maximum message size, including text and cards, is **32,000 bytes**.  
> If a message exceeds this size, the Chat app must send multiple messages.

Chat apps can also send messages synchronously in response to user interactions without calling the Chat API, such as posting a welcome message when added to a space.

---

## How Google Chat Displays API-Created Messages

The way Chat displays and attributes a message depends on the authentication type.

### App Authentication

When using **app authentication**, the Chat app sends the message directly.

- Chat displays `App` next to the sender name.
- The message is attributed to the Chat app.
- Supports rich message features:
  - Text
  - Cards
  - Interactive widgets
  - Accessory widgets
  - Private messages
  - Forced notifications
  - Silent messages

> With app authentication, the Chat app sends the message. To note that the sender isn't a person, Chat displays `App` next to its name.

### User Authentication

When using **user authentication**, the Chat app sends the message on behalf of the user.

- Chat displays the user as the sender.
- Chat also displays the Chat app name next to the user’s name.
- Generally supports **text messages only**.
- In **Developer Preview**, user-authenticated messages can also include cards.

> With user authentication, the user sends the message, and Chat displays the Chat app name next to the user's name.

---

## Prerequisites

To use the examples in the guide, you need:

- A **Business or Enterprise Google Workspace account** with access to Google Chat.
- A Google Cloud project.
- OAuth consent screen configured.
- Google Chat API enabled and configured with:
  - Chat app name
  - Icon
  - Description
- A Google Chat space where:
  - The authenticated user is a member, or
  - The calling Chat app is a member.
- Appropriate credentials depending on authentication type:
  - **User authentication:** OAuth client ID credentials saved as `credentials.json`
  - **App authentication:** Service account credentials saved as `credentials.json`
- Appropriate authorization scopes.
- Language-specific setup:
  - Node.js Cloud Client Library
  - Python Cloud Client Library
  - Java Cloud Client Library
  - Apps Script project with Advanced Chat Service enabled

For app authentication, the Chat app must be added to the space.

---

## Authentication Scopes

Common scopes mentioned:

### App Authentication

```text
https://www.googleapis.com/auth/chat.bot
```

### User Authentication

```text
https://www.googleapis.com/auth/chat.messages.create
```

---

## Sending a Message as the Chat App

Using app authentication, a Chat app can send messages with rich content, including text, cards, and interactive accessory widgets.

Required request fields:

- `chat.bot` authorization scope
- `parent`: the target `Space` resource, such as `spaces/SPACE_NAME`
- `message`: the `Message` resource to create

Message content can include:

- `text`
- `cardsV2`
- Both `text` and `cardsV2`

Optional fields include:

- `accessoryWidgets`
- `privateMessageViewer`
- `messageId`
- `thread.threadKey`
- `messageReplyOption`

### Representative Node.js Example

```js
import {createClientWithAppCredentials} from './authentication-utils.js';

// This sample shows how to create message with app credential
async function main() {
  // Create a client
  const chatClient = createClientWithAppCredentials();

  // Initialize request argument(s)
  const request = {
    // Replace SPACE_NAME here.
    parent: 'spaces/SPACE_NAME',
    message: {
      text:
        '👋🌎 Hello world! I created this message by calling ' +
        "the Chat API's `messages.create()` method.",
      cardsV2: [
        {
          card: {
            header: {
              title: 'About this message',
              imageUrl:
                'https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/info/default/24px.svg',
            },
            sections: [
              {
                header: 'Contents',
                widgets: [
                  {
               

[... summary truncated for context management ...]
