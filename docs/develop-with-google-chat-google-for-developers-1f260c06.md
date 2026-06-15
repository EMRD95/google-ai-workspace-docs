---
title: "Develop with Google Chat  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/overview"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:14:37Z"
extraction_method: "web_extract"
---

# Develop with Google Chat — Summary

**Source:** Google for Developers — Google Chat  
**URL:** https://developers.google.com/workspace/chat/overview  
**Last updated:** 2026-04-20 UTC

---

## Page Purpose

This page introduces the **Google Chat API** and explains how developers can build **Google Chat apps** that integrate services, workflows, and resources directly into Google Chat conversations.

---

## Key Excerpts

> Google Chat apps integrate services directly into chats, enabling users to access information and take action without leaving the conversation.

> The Chat API consists of gRPC services or REST resources and methods that grant access to Chat, including spaces, space members, messages, message reactions, message attachments, space events, and user read states.

> Calling the Chat API requires authentication.

> The recommended way for most developers to call the Google Chat API is with our officially supported Cloud Client Libraries for your preferred language, like Python, Java, or Node.js.

> The Chat API lets you build Google Chat apps that bring your services and resources right into Google Chat.

---

## Google Chat API Overview

The **Google Chat API** provides access to Google Chat through:

- **gRPC services**
- **REST resources and methods**

It lets developers work with core Google Chat entities such as:

- Spaces
- Space members
- Messages
- Message reactions
- Message attachments
- Space events
- User read states
- User notification settings
- Custom emoji
- Sections

A video introduction is available:

- **Introduction to Google Chat API** — Google Workspace Developers  
  https://www.youtube.com/watch?v=cPHUsVvonjE

---

## Core Google Chat API Concepts

### Spaces

**Spaces** are places where people and apps converse and share files.

Types of spaces include:

- **Direct messages (DMs):** 1:1 conversations between two users or between a user and a Chat app.
- **Group chats:** Conversations between three or more users and Chat apps.
- **Named spaces:** Persistent collaboration areas where people send messages, share files, and work together.

**Resource references:**

- RPC: `google.chat.v1.Space`
- REST: `v1/spaces`

**Example operations:**

- Create a space
- Set up a space
- Get a space
- List spaces
- Update a space
- Delete a space
- Find a direct message

---

### Members

**Members** are users and Chat apps that have joined or been invited to a space.

**Resource references:**

- RPC: `google.chat.v1.Membership`
- REST: `v1/spaces.members`

**Example operations:**

- Create a membership
- Get a membership
- List memberships
- Update a membership
- Delete a membership

---

### Messages

**Messages** include:

- Text communications
- Card-based communications
- File attachments

Users can also react to messages with emoji.

**Resource references:**

- RPC: `google.chat.v1.Message`
- REST: `v1/spaces.messages`
- Cards: `v1/cards`

**Example operations:**

- Create a message
- Get a message
- List messages
- Update a message
- Delete a message

---

### Reactions

**Reactions** represent emoji responses to messages.

Examples include:

> 👍, 🚲, and 🌞

**Resource references:**

- RPC: `google.chat.v1.Reaction`
- REST: `v1/spaces.messages.reactions`

**Example operations:**

- Create a reaction
- List reactions
- Delete a reaction

---

### Custom Emoji

**Custom emoji** are emoji created and shared within an organization in Google Chat.

They can be:

- Included in message content
- Used as reactions to messages

**Resource references:**

- RPC: `google.chat.v1.CustomEmoji`
- REST: `v1/customEmojis`

**Example operations:**

- Create a custom emoji
- Delete a custom emoji
- Get details about a custom emoji
- List custom emojis in an organization

---

### Sections

**Sections** let users group conversations and customize the list of spaces shown in the Google Chat navigation panel.

Types include:

- Predefined system sections
- User-defined custom sections

**Resource references:**

- RPC: `google.chat.v1.Section`
- REST: `v1/users.sections`

**Example operations:**

- Create a section
- Update a section
- Delete a section
- Change the position of a section
- List sections
- List spaces in a section
- Move a space to a different section

---

### Media and Attachments

**Media** represents files uploaded to Google Chat, including:

- Images
- Videos
- Documents

**Media resource reference:**

- REST: `v1/media`
- RPC: Unavailable

**Attachments** are instances of media attached to messages.

**Attachment resource references:**

- RPC: `google.chat.v1.Attachment`
- REST: `v1/spaces.messages.attachments`

**Example operations:**

- Upload media as an attachment
- Download media as an attachment
- Get an attachment

---

### Space Events

**Space events** represent changes to a space or its child resources, including:

- Members
- Messages
- Reactions

**Resource references:**

- RPC: `google.chat.v1.SpaceEvent`
- REST: `v1/spaces.spaceEvents`

**Example related operations 

[... summary truncated for context management ...]
