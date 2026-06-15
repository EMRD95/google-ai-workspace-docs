---
title: "Respond to Google Chat app commands  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/commands"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:17:54Z"
extraction_method: "web_extract"
---

# Respond to Google Chat App Commands — Summary

**Source:** Google Developers — <https://developers.google.com/workspace/chat/commands>  
**Last updated:** 2026-04-20 UTC

## Purpose

This guide explains how to **set up and respond to commands** in a Google Chat app.

> Commands help users discover and use key features of a Chat app. Only Chat apps can see the content of a command. For example, if a user sends a message with a slash command, the message is only visible to the user and the Chat app.

Google recommends using commands as part of designing user journeys for Chat apps.

---

## Types of Google Chat App Commands

Google Chat apps can define three command types:

| Command type | How users invoke it | Best used when |
|---|---|---|
| **Slash command** | Type `/` followed by predefined text, such as `/about`, or select from the command menu | The app needs additional user input |
| **Quick command** | Open the command menu from the reply area, click **Add**, then select a command | The app can respond immediately without extra input |
| **Message action** | Hover over a message, open the three-dot menu, and select an action | The app performs an action based on a specific message |

### Slash Commands

Users type a slash command such as:

```text
/about
/search receipts
```

Use slash commands when the app needs argument text from the user.

Example:

> Create a slash command called `/search` that runs after the user enters a phrase to search for, like `/search receipts`.

---

### Quick Commands

Users select quick commands from the command menu in the message reply area.

Use quick commands when the app can respond immediately.

Example:

> Create a quick command called **Random image** that responds immediately with an image.

---

### Message Actions

> **Developer Preview**

Users invoke message actions from the message context menu.

Use message actions when the app can act on the context of a message.

Example:

> Create a message action if your Chat app can perform actions based on the context of a message.

---

## Prerequisites

You need a **Google Chat app that receives and responds to interaction events**.

Google provides quickstarts depending on implementation language/platform:

- **Node.js**
- **Apps Script**
- **Python**
- **Java**

For HTTP-service apps, Google points to the Google Cloud Functions Chat app quickstart.  
For Apps Script apps, Google points to the Apps Script Chat app quickstart.

---

# Set Up a Command

Setting up a command involves two main steps:

1. **Create a name and description**
2. **Configure the command in the Google Cloud console**

---

## Naming and Describing Commands

The command name is what users type or select to invoke the Chat app. A short description appears below the command name to help users understand how to use it.

### Naming Recommendations

Use names that are:

- **Short**
- **Descriptive**
- **Actionable**
- Easy for users to understand

Example recommendation:

```text
Use "Remind me" instead of "Create a reminder"
```

Additional guidance:

- Use common names for common interactions, such as:
  - `Settings`
  - `Feedback`
- Use unique names when possible to avoid confusion with commands from other Chat apps.
- If multiple apps use the same command name, users may need to filter through similar commands.

---

### Description Recommendations

Descriptions should be:

- Short
- Clear
- Explicit about expected behavior

Include formatting requirements when relevant.

Example:

```text
Remind me to do [something] at [time]
```

Also clarify whether the app responds:

- Publicly to everyone in the space
- Privately to the user who invoked the command

Example:

```text
Learn about this app (Only visible to you)
```

---

# Configure a Command in Google Cloud Console

To create a **slash command**, **quick command**, or **message action**, configure it in the Google Chat API settings for your app.

## Steps

1. In Google Cloud console, go to:

   ```text
   Menu > APIs & Services > Enabled APIs & Services > Google Chat API
   ```

   Google Chat API page: <https://console.cloud.google.com/apis/api/chat.googleapis.com>

2. Click **Configuration**.

3. Under **Commands**, click **Add a command**.

4. Enter command details:

   | Field | Details |
   |---|---|
   | **Command ID** | A number from `1` to `1000`; used by the Chat app to recognize the command and return a response |
   | **Description** | Up to 50 characters; can include special characters |
   | **Command type** | Choose **Quick command**, **Slash command**, or **Message action** |
   | **Command name** | Depends on the command type |

---

## Command Name Rules by Type

### Quick Command Name

- Display name users select from the menu
- Up to 50 characters
- Can include special characters

Example:

```text
Remind me
```

---

### Slash Command Name

- Text users type in a message
- Must start with `/`
- Must contain only text
- Up to 50 characters

Example:

```text
/remindMe

[... summary truncated for context management ...]
