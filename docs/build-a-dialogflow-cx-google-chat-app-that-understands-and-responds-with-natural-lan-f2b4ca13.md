---
title: "Build a Dialogflow CX Google Chat app that understands and responds with natural language  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/build-dialogflow-chat-app-natural-language"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:09:18Z"
extraction_method: "web_extract"
---

# Build a Dialogflow CX Google Chat App That Understands and Responds with Natural Language

**Source:** Google for Developers — Google Workspace Chat  
**URL:** https://developers.google.com/workspace/chat/build-dialogflow-chat-app-natural-language  
**Last updated:** 2026-04-20 UTC

---

## Overview

This guide explains how to build a **Google Chat app** that uses **Dialogflow CX** to understand and respond to users in natural language.

Dialogflow CX has a **direct integration with Google Chat**, letting users message a Chat app while Dialogflow handles conversation logic, intent detection, parameter extraction, and responses.

> This page explains how to build a Google Chat app that can both understand and respond with natural language using Dialogflow.

A typical use case is a **car rental assistant**:

> A user might write, "I'd like to rent a car". The Chat app might respond with a question like "Where would you like to pick up the vehicle?"

Dialogflow Chat apps are useful for natural-language workflows such as:

- Booking flights
- Scheduling doctor appointments
- Ordering food delivery
- Answering retail product catalog questions, such as whether items are available in other colors

Dialogflow provides **prebuilt agents** to help you start quickly, including the guide’s example agent: **Travel: car rental**.

---

## Objectives

By the end of the guide, you can:

- Set up the required Google Cloud environment.
- Create and deploy a **Dialogflow CX agent**.
- Create and deploy a **Google Chat app** powered by that agent.
- Test the Chat app in Google Chat.

---

## Prerequisites

You need:

- A **Business or Enterprise Google Workspace account** with access to **Google Chat**.
- A **Google Cloud project with billing enabled**.

Useful references:

- Verify billing status of projects
- Create a Google Cloud project

---

## Architecture

A Dialogflow-powered Google Chat app follows this flow:

1. A user sends a message to the Chat app in:
   - A direct message, or
   - A Chat space
2. A **Dialogflow virtual agent** in Google Cloud receives and processes the message.
3. Optionally, the Dialogflow agent uses a **Dialogflow webhook** to interact with external systems, such as:
   - Project management tools
   - Ticketing systems
   - Other third-party services
4. Dialogflow sends a response back to the Chat app service.
5. The response is delivered to the Chat space.

Key architectural point:

> The Dialogflow agent and the Chat app must be set up in the same Google Cloud project when using the direct Dialogflow CX integration with Chat.

If they must be in different projects, use an intermediate server. Google provides a GitHub example: **Chat integration for Dialogflow CX**.

---

## Set Up the Environment

Before using the app, enable the required APIs in your Google Cloud project:

- **Google Chat API**
- **Dialogflow API**

Steps:

1. Open the API enablement flow in Google Cloud Console.
2. Confirm the correct Cloud project.
3. Confirm the APIs.
4. Click **Enable**.

---

## Create a Dialogflow CX Agent

A **Dialogflow CX agent** is a virtual agent that handles conversations with end users.

Key concept:

> Dialogflow translates end-user text during a conversation to structured data that your apps and services can understand.

Dialogflow agents are trained like human call center agents: they are designed to handle expected conversation scenarios without requiring every user phrase to be explicitly scripted.

---

### Agent Creation Options

You can either:

1. Use a **prebuilt agent**, recommended for quick testing.
2. Create your own agent.

For this guide, Google recommends selecting the prebuilt agent:

> **Travel: car rental**

Prebuilt agents are rated:

- Beginner
- Intermediate
- Advanced

Advanced or intermediate agents may require extra configuration, features, or API enablement.

---

### Create a Prebuilt Agent

Steps:

1. Open the **Dialogflow CX Console**.
2. Select your Google Cloud project.
3. Click **Use prebuilt agents**.
4. Select **Travel: car rental**.
5. Click **Import as agent**.

---

### Create Your Own Agent

Steps:

1. Click **Create agent**.
2. Choose one of:
   - **Auto-generate** to create a **data store agent**
   - **Build your own** to create other agent types

Basic settings:

- **Display name**
- **Location**
- **Time zone**
- **Default language**

Important constraint:

> You can't change the default language for an agent after creation.

Click **Create**. Dialogflow CX creates the agent and displays its **default start flow**.

---

### Test the Dialogflow CX Agent

Recommended best practice: test the agent before connecting it to Chat.

Steps:

1. Click **Test agent**.
2. Select **Test agent in environment**.
3. Set:
   - **Environment:** `Draft`
   - **Flow:** `Default Start Flow`
   - **Page:** `Start Page`
4. In the **Talk to agent** compose bar, type:

```text
Hello
```

5. Press **Enter**.
6. The agent should introduce itself.
7. Continue with the sample t

[... summary truncated for context management ...]
