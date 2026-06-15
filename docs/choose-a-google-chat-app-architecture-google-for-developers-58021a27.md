---
title: "Choose a Google Chat app architecture  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/structure"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:10:59Z"
extraction_method: "web_extract"
---

# Choose a Google Chat App Architecture — Summary

**Source:** Google for Developers — <https://developers.google.com/workspace/chat/structure>  
**Last updated:** 2026-04-20 UTC

---

## Page Purpose

This guide explains common service architectures for building **Google Chat apps** and helps developers choose the right one based on:

- Target audience: **team**, **organization**, or **public**
- Messaging needs: synchronous, asynchronous, event-driven, or one-way
- User interaction style
- Integration requirements
- Development model: no-code, low-code, or full-code
- DevOps and CI/CD needs
- Whether the app runs behind a firewall

> If you have an existing app that you want to integrate into Google Chat, you can use or adapt your existing implementation.

---

## Key Takeaways

- Google Chat apps can be built with several architectures:
  - **Web or HTTP service**
  - **Pub/Sub**
  - **Webhooks**
  - **Apps Script**
  - **AppSheet**
  - **Dialogflow**
  - **Command-line application or script**
- **Web/HTTP services** provide the most flexibility and are the most common option for public or complex apps.
- **Pub/Sub** is best when the app is behind a firewall or needs event subscriptions.
- **Webhooks** are simple but limited to sending messages into a single Chat space.
- **Apps Script** is low-code and integrates well with Google Workspace services.
- **AppSheet** enables no-code Chat apps.
- **Dialogflow** is best for natural language and conversational bots.
- **Command-line apps/scripts** are suitable for non-interactive asynchronous operations.
- Chat apps can handle user interactions through:
  - Command parsing
  - Dialogs
  - Natural language processing
- Chat apps can also proactively send messages or perform actions using the **Chat API**.

---

## Architecture Selection Overview

Google identifies architecture fit using two levels:

- **Recommended / verified**: Best fit for the use case.
- **Possible / check_circle_outline**: Possible, but not as strong a fit.

### By Intended Audience

| Audience | Best-fit architectures |
|---|---|
| **Your team** | Webhooks, Apps Script, AppSheet |
| **Your organization** | Web/HTTP service, Pub/Sub, Apps Script |
| **The public** | Web/HTTP service |

Other possible fits include Web/HTTP service, Pub/Sub, Dialogflow, script, and Apps Script depending on the case.

---

### By User Interactivity

| Capability | Best-fit architecture |
|---|---|
| **Natural language processing** | Dialogflow |

NLP can also be implemented with Web/HTTP service, Pub/Sub, or Apps Script, but Dialogflow is the recommended option.

---

### By Messaging Pattern

| Messaging need | Best-fit architectures |
|---|---|
| **Send and receive synchronous messages** | Web/HTTP service, Apps Script, AppSheet, Dialogflow |
| **Synchronous + asynchronous messages** | Web/HTTP service, Apps Script, AppSheet |
| **Asynchronous messages only** | Web/HTTP service, Apps Script, script |
| **Send messages from an external system to a single Chat space** | Web/HTTP service, Webhooks, Apps Script, AppSheet |

---

### By Integration / System Access

| Requirement | Best-fit architecture |
|---|---|
| **Integrate with other Google services** | Apps Script, AppSheet |
| **Communicate behind a firewall** | Pub/Sub |
| **Query or subscribe to Chat events** | Pub/Sub |

---

### By Development and Deployment Style

| Requirement | Best-fit architecture |
|---|---|
| **No-code development** | AppSheet |
| **Low-code development** | Webhooks, Apps Script |
| **Programming language of your choice** | Web/HTTP service, Pub/Sub, script |
| **Simplified DevOps** | Apps Script, AppSheet |
| **Complete DevOps and CI/CD management** | Web/HTTP service, Pub/Sub |

---

# Service Architecture Styles

---

## 1. Web or HTTP Service

A **web or HTTP service** is the most commonly deployed architecture.

> A _web or HTTP service_ is the most commonly deployed architecture because it provides the most flexibility for developers to build public Chat apps.

### Recommended Use Cases

Use this architecture when:

- The Chat app is deployed publicly on the **Google Workspace Marketplace**.
- The app needs all messaging patterns:
  - Send and receive synchronous messages
  - Send asynchronous messages
  - Send messages from an external system
- The app is developed in **any programming language**.
- The app requires full **DevOps and CI/CD** control.
- The service runs in cloud or on-premises servers.

### Flow

1. User sends a message in a Chat space to the Chat app.
2. Chat sends an HTTP request to a cloud or on-premises web server.
3. The app logic can optionally interact with third-party services, such as:
   - Project management systems
   - Ticketing tools
4. The web server sends an HTTP response back to Chat.
5. Chat delivers the response to the user.
6. Optionally, the app calls the **Chat API** to post asynchronous messages or perform other operations.

### Implementation Notes

- Supports existing libraries and

[... summary truncated for context management ...]
