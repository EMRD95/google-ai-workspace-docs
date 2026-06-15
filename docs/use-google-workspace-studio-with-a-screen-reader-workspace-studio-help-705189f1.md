---
title: "Use Google Workspace Studio with a screen reader - Workspace Studio Help"
source_url: "https://support.google.com/workspace-studio/answer/17119624"
product_area: "workspace-studio"
retrieved_at: "2026-06-15T17:46:37Z"
extraction_method: "web_extract"
---

# Use Google Workspace Studio with a Screen Reader — Summary

**Source:** Google Workspace Studio Help  
**URL:** https://support.google.com/workspace-studio/answer/17119624  
**Page title:** *Use Google Workspace Studio with a screen reader*

---

## Overview

Google Workspace Studio is a web-based automation tool for Google Workspace. It lets users create automated workflows, called **flows**, using Gemini, without programming.

> **Note**: A supported Workspace edition is required. Learn more about [access to Workspace Studio](https://support.google.com/workspace-studio/answer/16782648).

Workspace Studio supports:

- **Keyboard-only focus navigation**
- **Screen reader navigation**
- Web structure optimized for screen reader context
- Creating, editing, sharing, testing, reviewing, and managing flows

---

## Key Terms

### Flows

In Workspace Studio, automated tasks are called **flows**.

A flow has 3 main parts:

- **Starter**: The event or schedule that starts the flow.
  - Example: receiving an email from specific people
  - Example: every Monday at 9 AM
- **Steps**: Actions the flow performs after it starts.
  - Example: ask Gemini to extract action items
  - Example: draft a reply
  - Example: add content to a document
- **Variables**: Dynamic placeholders for information from earlier steps.
  - Example: Gemini’s response
  - Example: email sender
  - Example: form response

> Variables let you use information from one step in later steps.

---

## Before You Start: Screen Reader Mode Tips

Workspace Studio works best when screen readers are set to focus-oriented editing modes.

### ChromeVox

> Ensure sticky mode is turned off. To turn off, press the Search key twice until you hear “Sticky mode disabled.”

### JAWS

> For editing content, ensure that JAWS Virtual PC cursor is off. To turn off, press JAWS + z until you hear "Use virtual PC cursor off."

Additional note:

- Depending on Forms mode configuration, you may need to do this more than once.

### NVDA

> Focus mode generally provides a better experience for editing content than browse mode. To switch between focus and browse modes: Press NVDA + space.

### VoiceOver

- Turn off Quick Nav:

> Press the Left arrow and Right arrow keys at the same time until you hear “Quick Nav off.”

- If focus is not placed correctly, such as after a dialog opens:

> Press Escape to return your focus to the editing area.

- To return to the editing area:

> Press VoiceOver + Shift + Down arrow.

---

# Navigate the Workspace Studio UI

Go to:

```text
https://studio.workspace.google.com/
```

If the UI does not match the described layout, you may not have access to Workspace Studio.

> **Note:** the title of the main page is: “Discover - Google Workspace Studio”.

---

## Screen Reader Web Navigation Structure

Starting from the top in screen reader **web navigation mode**, users should find:

- **Heading / Banner landmark**
  - Link: “Workspace studio”
  - Button: “Send Feedback”
  - Button: “Help”
  - Button collapsed: “Google apps”
  - Button collapsed: “Google Account: <name>”
- Button: “New flow”
- “Flows Left navigation” navigation landmark, vertical menu bar
  - Menu item: “Discover”
  - Menu item: “My flows”
- Heading: “Automate your work with Gemini”
- Heading: “Streamline and manage tasks across Workspace”
- Edit field:
  - “prompt input field”
  - read-only
  - multiline
  - prompt: “Describe a task for Gemini”
- Button: “Create”

### Example Workflow Cards

Example 1 may include:

- Static text: “Streamline my follow-up”
- Static text: “Send me summaries & action items after meetings”
- Static text:

```text
Start after your meetings Have Gemini summarize the meeting and action items Get the summaries in Chat
```

- Graphics:
  - “Calendar”
  - “Gemini”
  - “Gemini”
  - “Chat”
- Static text: “+1”
- Button: “Turn on Workflow”

Other examples may include:

- Static text: “Review quickly”
- Button: “More details about this workflow”
- Static text: “Get prepared”
- Button: “More details about this workflow”

### Filter Toolbar

The toolbar can filter remaining examples:

- Toggle button not pressed: “Email boosters”
- Toggle button not pressed: “Better meetings”
- Toggle button not pressed: “Tasks and action items”

Additional headings and examples may include:

- “Email boosters”
- “Better meetings”
- “Tasks and action items”

---

## Keyboard Focus Navigation

Using screen reader **focus navigation mode**, tab order from the top includes:

1. Link: “Workspace studio”
2. Button: “Send Feedback”
3. Button: “Help”
4. Button collapsed: “Google apps”
5. Button collapsed: “Google Account: <name>”

Initial focus is on:

- “New flow” button

Then:

- Tab to “Flows Left navigation” vertical menu bar
  - Menu item current page: “Discover”
    - Activating it returns to initial focus
  - Down arrow to: “My flows”

Next tab opens a dialog:

- Initial focus is on:
  - “prompt input field” edit field
- If text is typed, focus moves to:
  - Create button
  - Ex

[... summary truncated for context management ...]
