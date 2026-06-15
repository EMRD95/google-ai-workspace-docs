---
title: "Advanced Chat Service  |  Apps Script  |  Google for Developers"
source_url: "https://developers.google.com/apps-script/advanced/chat"
product_area: "apps-script-ai"
retrieved_at: "2026-06-15T18:18:54Z"
extraction_method: "web_extract"
---

# Advanced Chat Service for Apps Script — Summary

**Source:** https://developers.google.com/apps-script/advanced/chat  
**Last updated:** 2026-05-04 UTC

## Overview

The **Advanced Chat service** lets Google Apps Script projects use the **Google Chat API**.

It enables scripts to:

- Find, create, and modify Google Chat spaces
- Add or remove members from spaces
- Read or post messages
- Work with message content such as:
  - Text
  - Cards
  - Attachments
  - Reactions

> The Advanced Chat service lets you use the [Google Chat API](https://developers.google.com/chat/api/guides) in Google Apps Script.

This is an **advanced Apps Script service**, so it must be explicitly enabled before use.

---

## Key Requirements

### Prerequisites

To use the Advanced Chat service, you need:

- An **Apps Script Google Chat app** configured in the **Google Cloud console** on the Chat API configuration page.
- The Apps Script project must use a **standard Google Cloud project**, not the default project automatically created by Apps Script.
- Authentication configured for the Chat app.

Authentication depends on how the API action is performed:

| Action type | Required authentication |
|---|---|
| Perform an action on behalf of a user | User authentication |
| Perform an action as the Chat app | App authentication with a service account |

Relevant references:

- [Build a Google Chat app with Google Apps Script](https://developers.google.com/workspace/add-ons/chat/quickstart-apps-script)
- [User authentication](https://developers.google.com/chat/api/guides/auth/users)
- [App authentication with a service account](https://developers.google.com/chat/api/guides/auth/service-accounts)
- [Types of required authentication for Google Chat API calls](https://developers.google.com/chat/api/guides/auth#asynchronous-chat-calls)
- [Turn on advanced services](https://developers.google.com/apps-script/guides/services/advanced)

---

## Reference Behavior

The Advanced Chat service follows the same objects, methods, and parameters as the public **Google Chat API**.

> Like all advanced services in Apps Script, the Chat service uses the same objects, methods, and parameters as the public API.

Main reference:

- [Chat API REST reference](https://developers.google.com/chat/api/reference/rest)

---

# Sample Code

The page provides examples for common Chat API actions using the Apps Script advanced service.

---

## Post a Message with User Credentials

Posts a message to a Chat space **on behalf of the user**.

### Required scope

Add this to the Apps Script project’s `appsscript.json` file:

```json
"oauthScopes": [
     "https://www.googleapis.com/auth/chat.messages.create"
]
```

### Apps Script function

```javascript
/**
    * Posts a new message to the specified space on behalf of the user.
    * @param {string} spaceName The resource name of the space.
    */
function postMessageWithUserCredentials(spaceName) {
     try {
       const message = { text: "Hello world!" };
       Chat.Spaces.Messages.create(message, spaceName);
     } catch (err) {
       // TODO (developer) - Handle exception
       console.log("Failed to create message with error %s", err.message);
     }
}
```

---

## Post a Message with App Credentials

Posts a message to a Chat space **on behalf of the app**.

Important note:

> Using the advanced Chat service with a service account doesn't require you to specify authorization scopes in `appsscript.json`.

This requires app authentication with a service account.

Reference:

- [Authenticate as a Google Chat app](https://developers.google.com/chat/api/guides/auth/service-accounts)

### Apps Script function

```javascript
/**
 * Posts a new message to the specified space on behalf of the app.
 * @param {string} spaceName The resource name of the space.
 */
function postMessageWithAppCredentials(spaceName) {
  try {
    // See https://developers.google.com/chat/api/guides/auth/service-accounts
    // for details on how to obtain a service account OAuth token.
    const appToken = getToken_();
    const message = { text: "Hello world!" };
    Chat.Spaces.Messages.create(
      message,
      spaceName,
      {},
      // Authenticate with the service account token.
      { Authorization: `Bearer ${appToken}` },
    );
  } catch (err) {
    // TODO (developer) - Handle exception
    console.log("Failed to create message with error %s", err.message);
  }
}
```

---

## Get a Space

Gets information about a Chat space.

### Required scope

Add this to `appsscript.json`:

```json
"oauthScopes": [
     "https://www.googleapis.com/auth/chat.spaces.readonly"
]
```

### Apps Script function

```javascript
/**
    * Gets information about a Chat space.
    * @param {string} spaceName The resource name of the space.
    */
function getSpace(spaceName) {
     try {
       const space = Chat.Spaces.get(spaceName);
       console.log("Space display name: %s", space.displayName);
       console.log("Space type: %s", space.space

[... summary truncated for context management ...]
