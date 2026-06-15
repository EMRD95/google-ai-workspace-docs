---
title: "Respond to Google Chat app commands  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/slash-commands"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:17:54Z"
extraction_method: "web_extract"
---

# Respond to Google Chat App Commands — Markdown Summary

**Source:** Google Developers — Google Chat  
**URL:** https://developers.google.com/workspace/chat/slash-commands  
**Last updated:** 2026-04-20 UTC

---

## Overview

Google Chat app commands help users discover and use key features of a Chat app. Commands are visible only to the user and the Chat app, not to everyone in the space.

> “Only Chat apps can see the content of a command. For example, if a user sends a message with a slash command, the message is only visible to the user and the Chat app.”

Before building commands, Google recommends designing the user journey first: [Define all user journeys](https://developers.google.com/workspace/chat/journeys).

---

## Types of Google Chat App Commands

Google Chat apps support three command types:

| Command type | How users invoke it | Best used when |
|---|---|---|
| **Slash commands** | Type `/` plus predefined text, such as `/about`, or select from the command menu | The app needs additional user input |
| **Quick commands** | Open the command menu from the message reply area, click **Add**, and select a command | The app can respond immediately without more input |
| **Message actions** | Hover over a message, open the three-dot menu, and select an action | The app acts on the context of an existing message |

---

### Slash Commands

Users invoke slash commands by typing a slash (`/`) followed by predefined text, such as:

```text
/about
/search receipts
```

Use slash commands when your app needs arguments or additional input.

Example use case:

> Create a slash command called `/search` that runs after the user enters a phrase to search for, like `/search receipts`.

---

### Quick Commands

Users invoke quick commands from the Chat message reply area command menu.

Use quick commands when the app can respond immediately.

Example:

> Create a quick command called **Random image** that responds immediately with an image.

---

### Message Actions

> **Developer Preview**

Users invoke message actions from the three-dot menu on a specific message.

Use message actions when the app performs an action based on the context of a message.

Example:

> A message context menu can contain a **“Remind me”** message action.

---

## Prerequisites

You need a Google Chat app that receives and responds to [interaction events](https://developers.google.com/workspace/chat/receive-respond-interactions).

Supported implementation paths:

- **Node.js**
  - Create an interactive Chat app using an HTTP service with the [Google Cloud Functions quickstart](https://developers.google.com/workspace/chat/quickstart/gcf-app).
- **Apps Script**
  - Create an interactive Chat app using the [Apps Script quickstart](https://developers.google.com/workspace/chat/quickstart/apps-script-app).
- **Python**
  - Create an interactive Chat app using an HTTP service with the [Google Cloud Functions quickstart](https://developers.google.com/workspace/chat/quickstart/gcf-app).
- **Java**
  - Create an interactive Chat app using an HTTP service with the [Google Cloud Functions quickstart](https://developers.google.com/workspace/chat/quickstart/gcf-app).

---

# Set Up a Command

Setting up a command involves:

1. Creating a command **name and description**
2. Configuring the command in the **Google Cloud console**

---

## Name and Describe the Command

The command name is what users type or select to invoke the Chat app. A short description appears below the command name to help users understand how to use it.

---

### Command Naming Recommendations

Use names that are:

- **Short**
- **Descriptive**
- **Actionable**

Example:

```text
Remind me
```

Instead of:

```text
Create a reminder
```

Additional guidance:

- Use common names for familiar features, such as:
  - `Settings`
  - `Feedback`
- Use unique names when possible to avoid confusion with similar commands from other Chat apps.

> If your command name is the same as a command from another Chat app, users must filter through similar commands to find yours.

---

### Command Description Recommendations

Descriptions should be short and clear.

They should explain:

- What the command does
- Whether formatting is required
- Whether the response is visible to everyone or only the invoking user

Example for a slash command requiring arguments:

```text
Remind me to do [something] at [time]
```

Example for a private quick command:

```text
Learn about this app (Only visible to you)
```

---

## Configure the Command in Google Cloud Console

To configure slash commands, quick commands, or message actions:

1. In the Google Cloud console, go to:

   ```text
   Menu > APIs & Services > Enabled APIs & Services > Google Chat API
   ```

   Or open: [Google Chat API page](https://console.cloud.google.com/apis/api/chat.googleapis.com)

2. Click **Configuration**.

3. Under **Commands**, click **Add a command**.

4. Enter the command details:

   - **Command ID**
     - A number fr

[... summary truncated for context management ...]
