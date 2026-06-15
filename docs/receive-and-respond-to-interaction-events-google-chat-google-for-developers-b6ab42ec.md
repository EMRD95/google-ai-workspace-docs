---
title: "Receive and respond to interaction events  |  Google Chat  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/receive-respond-interactions"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:10:59Z"
extraction_method: "web_extract"
---

# Google Chat: Receive and Respond to Interaction Events — Summary

**Source:** https://developers.google.com/workspace/chat/receive-respond-interactions  
**Last updated:** 2026-04-20 UTC

## Overview

This guide explains how **Google Chat apps** receive and respond to user interactions, also called **Google Chat app interaction events**.

Interaction events occur when users interact with a Chat app, such as:

- @mentioning the app
- Using a slash command or quick command
- Adding or removing the app from a space
- Clicking a button on a card
- Opening the app homepage
- Submitting a form
- Opening, submitting, or canceling a dialog

Chat apps can process these events and optionally respond with messages, cards, dialogs, or asynchronous API calls.

> “This page describes how your Google Chat app can receive and respond to user interactions, also known as _Google Chat app interaction events_.”

The page covers how to:

- Configure a Chat app to receive interaction events.
- Process interaction events on your infrastructure.
- Respond to interaction events when appropriate.

---

## Prerequisites

To build an interactive Google Chat app, you need:

- A **Business or Enterprise Google Workspace account** with access to Google Chat.
- A **Google Cloud project**.
- An OAuth consent screen configured.
- The **Google Chat API enabled**.

---

## Core Concepts

A **Google Chat app interaction event** represents an action a user takes to invoke or interact with a Chat app.

When a user interacts with a Chat app:

1. Google Chat sends the app an event.
2. The event is represented as an [`Event`](https://developers.google.com/workspace/chat/api/reference/rest/v1/Event) type in the Chat API.
3. The app processes the event.
4. The app may optionally respond.

Each event includes an `eventType`, represented by the [`EventType`](https://developers.google.com/workspace/chat/api/reference/rest/v1/EventType) object.

Example:

- When a user adds a Chat app to a space, Google Chat sends an `ADDED_TO_SPACE` event.
- The app can respond with an onboarding or welcome message.

> “For each type of user interaction, Google Chat sends a different type of interaction event which helps your Chat app handle each event type accordingly.”

---

## Common Interaction Event Types

| User interaction | `eventType` | Typical Chat app response |
|---|---|---|
| User messages the Chat app, such as by @mentioning it or using a slash command. | `MESSAGE` | Responds based on message content. For example, `/about` can return a description of what the app does. |
| User adds the Chat app to a space. | `ADDED_TO_SPACE` | Sends an onboarding message explaining what the app does and how users can interact with it. |
| User removes the Chat app from a space. | `REMOVED_FROM_SPACE` | Removes incoming notifications configured for the space, such as webhooks, and clears internal storage. |
| User clicks a button on a card from a message, dialog, or homepage. | `CARD_CLICKED` | Processes and stores submitted data, or returns another card. |
| User opens the app homepage by clicking the **Home** tab in a 1:1 message. | `APP_HOME` | Returns a static or interactive homepage card. |
| User submits a form from the app homepage. | `SUBMIT_FORM` | Processes and stores submitted data, or returns another card. |
| User invokes a quick command. | `APP_COMMAND` | Responds based on the invoked command. For example, an **About** command can describe the app’s capabilities. |

For the complete list, see the [`EventType` reference documentation](https://developers.google.com/workspace/chat/api/reference/rest/v1/EventType).

---

## Dialog Interaction Events

If a Chat app opens dialogs, interaction events include extra dialog-related information:

- `isDialogEvent` is set to `true`.
- [`DialogEventType`](https://developers.google.com/workspace/chat/api/reference/rest/v1/DialogEventType) indicates whether the interaction opens, submits, or cancels a dialog.

### Common Dialog Event Types

| User interaction with a dialog | Dialog event type | Typical response |
|---|---|---|
| User triggers a dialog request, such as by using a slash command or clicking a button. | `REQUEST_DIALOG` | The Chat app opens the dialog. |
| User submits information in a dialog by clicking a button. | `SUBMIT_DIALOG` | The Chat app either navigates to another dialog or closes the dialog to complete the interaction. |
| User exits or closes the dialog before submitting. | `CANCEL_DIALOG` | Optionally sends a new message, or updates the message/card from which the dialog was opened. |

Related guide: [Open interactive dialogs](https://developers.google.com/workspace/chat/dialogs)

---

## Receiving Interaction Events

Not all Chat apps are interactive.

For example:

- **Incoming webhooks** can only send outgoing messages.
- They **can’t respond to users**.

To build an interactive Chat app, you must configure an endpoint that can receive, process, and respond to events.

---

## Configure a Chat

[... summary truncated for context management ...]
