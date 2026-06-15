---
title: "Build an interactive Google Chat app  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/interact-users-overview"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:17:54Z"
extraction_method: "web_extract"
---

# Build an Interactive Google Chat App — Summary

**Source:** [Google for Developers: Build an interactive Google Chat app](https://developers.google.com/workspace/chat/interact-users-overview)  
**Last updated:** 2026-04-20 UTC  
**Page purpose:** Provides an overview of frameworks for building an **interactive Google Chat app**.

---

## Core Overview

This page explains how to build Google Chat apps that interact with users, including how users discover them, which development frameworks are available, and where to find configuration, quickstart, and feature-building documentation.

> “This page provides an overview of the frameworks that you can use to build an interactive Google Chat app.”

Related video: [What are Google Chat apps?](https://www.youtube.com/watch?v=lzQ0z3OBTO0) by Google Workspace Developers.

---

## What Interactive Chat Apps Can Do

Interactive Google Chat apps let users:

- Add Chat apps to **Chat spaces** or **direct messages**.
- Send messages to or receive messages from Chat apps.
- Prompt Chat apps with a **command**.
- Preview links from an external service or system.
- Submit information to Chat apps, such as entering text into a **dialog** or **card message**.

---

## How Users Discover and Use Chat Apps

Users can discover and use Chat apps published to the **Google Workspace Marketplace** in several ways:

- Search for and install Chat apps from **Google Chat** or the **Marketplace**.
- Interact with a Chat app that has been added to a Chat space.
- Discover the Chat app in their **direct messages panel** after a Google Workspace administrator installs it on their behalf.

To start using a Chat app, users can:

- Start a direct message with the Chat app.
- Add the Chat app to a space.
- Add the Chat app by **@mentioning** it.

For user-facing instructions, see: [Use Chat apps](https://support.google.com/chat/answer/7655820).

Example described on the page:

> A user can @mention a Chat app to add it to a space.

---

## Choose a Framework for an Interactive Chat App

Google provides two main frameworks for building Chat apps that interact with users.

### 1. Google Workspace Add-on

Use this when you want to extend Google Workspace apps and list your Chat app alongside other app types in the Google Workspace Marketplace.

> **Google Workspace add-on**: Lets you extend other Google Workspace applications and list your Chat app with other types of apps on the Google Workspace Marketplace.

Documentation: [Extend Google Chat](https://developers.google.com/workspace/add-ons/chat)

### 2. Chat API Interaction Event

Use this when you want to build Chat-specific interactive features, including capabilities such as a Chat app homepage.

> **Chat API interaction event**: Lets you build additional features such as a Chat app homepage.

Documentation: [Receive and respond to interaction events](https://developers.google.com/workspace/chat/receive-respond-interactions)

---

## Configure an Interactive Chat App

The page links to framework-specific setup and quickstart documentation for different [Google Chat app architectures](https://developers.google.com/workspace/chat/structure).

| Configuration / Quickstart | Google Workspace Add-on | Chat API Interaction Events |
|---|---|---|
| Configure the Chat API | [Documentation](https://developers.google.com/workspace/add-ons/chat/configure) | [Documentation](https://developers.google.com/workspace/chat/configure-chat-api) |
| Apps Script quickstart | [Documentation](https://developers.google.com/workspace/add-ons/chat/quickstart-apps-script) | [Documentation](https://developers.google.com/workspace/chat/quickstart/apps-script-app) |
| HTTP service quickstart | [Documentation](https://developers.google.com/workspace/add-ons/chat/quickstart-http) | [Documentation](https://developers.google.com/workspace/chat/quickstart/gcf-app) |
| Dialogflow CX quickstart | [Documentation](https://developers.google.com/workspace/add-ons/chat/quickstart-dialogflow-cx) | [Documentation](https://developers.google.com/workspace/chat/build-dialogflow-chat-app-natural-language) |
| Pub/Sub quickstart | [Documentation](https://developers.google.com/workspace/add-ons/chat/quickstart-pubsub) | [Documentation](https://developers.google.com/workspace/chat/quickstart/pub-sub) |

---

## Build Interactive Features

The page maps common Chat app features to the appropriate documentation for each framework.

| Feature | Google Workspace Add-on | Chat API Interaction Events |
|---|---|---|
| Send messages | [Documentation](https://developers.google.com/workspace/add-ons/chat/send-messages) | — |
| Respond to commands | [Documentation](https://developers.google.com/workspace/add-ons/chat/commands) | [Documentation](https://developers.google.com/workspace/chat/commands) |
| Build interactive dialogs | [Documentation](https://developers.google.com/workspace/add-ons/chat/dialogs) | [Documentation](https://developers.google.com/workspace/chat/dialogs) |
| Collect and proce

[... summary truncated for context management ...]
