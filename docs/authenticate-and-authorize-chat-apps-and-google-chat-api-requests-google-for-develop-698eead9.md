---
title: "Authenticate and authorize Chat apps and Google Chat API requests  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/authenticate-authorize"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:10:59Z"
extraction_method: "web_extract"
---

# Authenticate and authorize Chat apps and Google Chat API requests — Summary

**Source:** Google for Developers — Google Chat  
**URL:** https://developers.google.com/workspace/chat/authenticate-authorize  
**Last updated:** 2026-06-03 UTC

---

## Core idea

Google Chat apps use **authentication** to verify identity and **authorization** to determine access to Google Chat resources.

Chat apps can authenticate in two main ways:

- **User authentication** — the app acts on behalf of a user and usually requires OAuth consent.
- **App authentication** — the app acts as itself using a **service account**.

> Google Chat apps can use either user or app authentication to interact with the Chat API.

---

## Authentication & authorization process overview

High-level flow for Google Chat API access:

1. **Configure a Google Cloud project**
   - Create a Google Cloud project.
   - Enable the **Google Chat API**.
   - Configure the Chat app.
   - Set up authentication.

2. **Call the Chat API**
   - The app sends credentials with API requests.
   - Service account credentials are included by the app.
   - User authentication may prompt the user to sign in.

3. **Request resources**
   - The app requests access using OAuth **scopes**.

4. **Ask for consent**
   - For user authentication, Google shows an OAuth consent screen.
   - Service account authentication doesn’t require end-user consent.

5. **Send approved request**
   - Credentials and approved scopes are sent to Google’s authorization server.

6. **Receive access token**
   - Google returns an access token containing granted scopes.
   - If fewer scopes are granted than requested, the app should disable features requiring missing scopes.

7. **Access resources**
   - The app uses the access token to call the Chat API.

8. **Optional refresh token**
   - Apps needing access beyond one access token lifetime can request a refresh token.

9. **Request more resources later**
   - If more access is needed, request additional scopes and repeat consent/token flow.

---

## When Chat apps require authentication

Chat apps can send messages:

- **Synchronously**, in direct response to user interaction.
- **Asynchronously**, by making Chat API calls independently.

### No authentication required: synchronous interaction responses

Chat apps **don’t need authentication** to receive and respond synchronously to interaction events, unless they call the Chat API or another Google API while processing the response.

Interaction events include:

- A user sends a message to a Chat app.
- A user `@mentions` a Chat app.
- A user invokes one of the app’s commands.

Typical sequence:

1. User sends a message to the Chat app.
2. Google Chat forwards the message to the app.
3. The app processes it and returns a response.
4. Google Chat renders the response.

> Google Chat apps don't need to authenticate as a user or Chat app to receive and respond synchronously to interaction events.

### Authentication required: asynchronous messages and tasks

Asynchronous operations require authentication and authorization because they call the Chat API.

Examples:

- Create a Chat space for an incident.
- Add people to a Chat space.
- Post a message to a Chat space.
- Access or modify Chat resources on a user’s behalf.

Example asynchronous flow:

1. Chat app calls `spaces.messages.create`.
2. The request includes user or service account credentials.
3. Google Chat authenticates the request.
4. Google Chat renders the app’s message in the target space.

---

## OAuth scopes

OAuth scopes define:

- Which Google Workspace app is accessed.
- What data is accessed.
- What level of access is granted.

> An authorization scope is an OAuth 2.0 URI string that contains the Google Workspace app name, what kind of data it accesses, and the level of access.

Apps should configure the OAuth consent screen and choose scopes before publication.

---

## Scope sensitivity levels

### Non-sensitive scopes

Require only basic app verification.

| Scope | Description |
|---|---|
| `https://www.googleapis.com/auth/chat.bot` | Lets Chat apps view chats and send messages. Supports **app authentication only** with service accounts. Cannot be used with user credentials or domain-wide delegation. |

---

### Sensitive scopes

Sensitive scopes provide access to specific user Google data and require additional app verification.

| Scope | Description |
|---|---|
| `https://www.googleapis.com/auth/chat.spaces` | Create conversations and spaces and see or edit metadata, including history and access settings. |
| `https://www.googleapis.com/auth/chat.spaces.create` | Create new conversations in Chat. |
| `https://www.googleapis.com/auth/chat.spaces.readonly` | View chat and spaces. |
| `https://www.googleapis.com/auth/chat.memberships` | View, add, update, and remove members from Chat conversations. |
| `https://www.googleapis.com/auth/chat.memberships.app` | Add and remove itself from conversations. |
| `https://www.go

[... summary truncated for context management ...]
