---
title: "Receive and respond to interaction events  |  Google Chat  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/interaction-events"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:10:59Z"
extraction_method: "web_extract"
---

# Receive and Respond to Google Chat Interaction Events — Summary

**Source:** Google Developers — Google Chat  
**URL:** https://developers.google.com/workspace/chat/interaction-events  
**Last updated:** 2026-04-20 UTC

---

## Core Concept

Google Chat apps can receive and respond to **user interaction events**, which occur when users interact with the app in Chat.

Examples include:

- @mentioning the app
- Sending a slash command
- Adding or removing the app from a space
- Clicking a card button
- Opening the app homepage
- Submitting a form
- Interacting with dialogs

Interaction events are represented by the Chat API [`Event`](https://developers.google.com/workspace/chat/api/reference/rest/v1/Event) type and identified by an [`eventType`](https://developers.google.com/workspace/chat/api/reference/rest/v1/EventType).

> A _Google Chat app interaction event_ represents any action that a user takes to invoke or interact with a Chat app, such as @mentioning a Chat app or adding it to a space.

---

## What This Page Covers

The guide explains how to:

- Configure a Chat app to receive interaction events.
- Process interaction events on your infrastructure.
- Respond to interaction events when appropriate.

---

## Prerequisites

To build an interactive Google Chat app, you need:

- A Business or Enterprise [Google Workspace](https://support.google.com/a/answer/6043576) account with access to [Google Chat](https://workspace.google.com/products/chat/).
- A [Google Cloud project](https://developers.google.com/workspace/guides/create-project).
- A configured [OAuth consent screen](https://developers.google.com/workspace/guides/configure-oauth-consent).
- The [Google Chat API enabled](https://developers.google.com/workspace/guides/enable-apis).

---

## Types of Interaction Events

Google Chat sends different interaction event types depending on the user action. The app can process each event type differently and optionally respond with a message or another UI action.

### Common Interaction Events

| User interaction | `eventType` | Typical response from a Chat app |
|---|---|---|
| A user messages a Chat app, such as @mentioning it or using a slash command. | `MESSAGE` | Responds based on the message content. For example, `/about` can return a message explaining what the app does. |
| A user adds a Chat app to a space. | `ADDED_TO_SPACE` | Sends an onboarding or welcome message explaining what the app does and how users can interact with it. |
| A user removes a Chat app from a space. | `REMOVED_FROM_SPACE` | Removes incoming notifications configured for the space, such as deleting a webhook, and clears internal storage. |
| A user clicks a button on a card from a message, dialog, or homepage. | `CARD_CLICKED` | Processes and stores submitted data, or returns another card. |
| A user opens the app homepage by clicking the **Home** tab in a 1:1 message. | `APP_HOME` | Returns a static or interactive homepage card. |
| A user submits a form from the app homepage. | `SUBMIT_FORM` | Processes and stores submitted data, or returns another card. |
| A user invokes a quick command. | `APP_COMMAND` | Responds based on the invoked command, such as replying to an **About** command. |

For all supported events, see the [`EventType` reference documentation](https://developers.google.com/workspace/chat/api/reference/rest/v1/EventType).

---

## Dialog Interaction Events

If a Chat app opens [dialogs](https://developers.google.com/workspace/chat/dialogs), the interaction event includes additional dialog-specific information:

- `isDialogEvent` is set to `true`.
- [`DialogEventType`](https://developers.google.com/workspace/chat/api/reference/rest/v1/DialogEventType) clarifies whether the event:
  - Opens a dialog
  - Submits dialog information
  - Cancels or closes a dialog

### Common Dialog Events

| User interaction with a dialog | Dialog event type | Typical response |
|---|---|---|
| A user triggers a dialog request, such as by using a slash command or clicking a button. | `REQUEST_DIALOG` | The Chat app opens the dialog. |
| A user submits information in the dialog by clicking a button. | `SUBMIT_DIALOG` | The Chat app navigates to another dialog or closes the dialog to complete the interaction. |
| A user exits or closes the dialog before submitting information. | `CANCEL_DIALOG` | Optionally, the Chat app sends a new message or updates the message/card that opened the dialog. |

Related guide: [Open interactive dialogs](https://developers.google.com/workspace/chat/dialogs)

---

## Configure a Chat App to Receive Interaction Events

Not all Chat apps are interactive. For example:

> Incoming webhooks can only send outgoing messages and can't respond to users.

To build an interactive app, choose an endpoint that can receive, process, and respond to interaction events.

Configuration is done in the **Google Cloud console**:

1. Go to the Chat API page.
2. Open the **Configuration** page:  
   [Go to Chat API Config

[... summary truncated for context management ...]
