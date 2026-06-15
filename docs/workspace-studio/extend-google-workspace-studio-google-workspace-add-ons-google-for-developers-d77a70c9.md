---
title: "Extend Google Workspace Studio  |  Google Workspace add-ons  |  Google for Developers"
source_url: "https://developers.google.com/workspace/add-ons/studio"
product_area: "workspace-studio"
retrieved_at: "2026-06-15T09:29:57Z"
extraction_method: "web_extract"
---

# Extend Google Workspace Studio — Summary

**Source:** Google for Developers — Google Workspace add-ons  
**URL:** https://developers.google.com/workspace/add-ons/studio  
**Last updated:** 2026-04-20 UTC  
**License:** Content under Creative Commons Attribution 4.0; code samples under Apache 2.0.

---

## Purpose of the Guide

These guides explain how developers can **extend Google Workspace Studio** by building **custom steps** that can be run inside Workspace Studio flows.

> “These guides explain how to extend the functionality of Google Workspace Studio by building custom steps that flows can run.”

### Recommended starting point

To begin, Google recommends the quickstart:

- [Build a calculator step with Apps Script](https://developers.google.com/workspace/add-ons/studio/quickstart-calculator)
- “Try the quickstart” link points to the same guide.

---

## What Workspace Studio Flows Do

**Flows** let Google Workspace users automate tasks across services by combining steps **without writing code**.

> “Flows let Google Workspace users automate tasks across services by combining a series of steps without writing any code.”

Developers can extend flows by exposing their app’s functionality as flow steps:

> “By extending flows, you let users add your app's functions as steps.”

---

## Example Flow: Customer Question Triage

A sample flow for handling customer emails:

1. Starts when an email from a customer is received.
2. Prompts Gemini to triage the email.
3. Creates a task for follow-up with the sales or support team.

The page includes a figure showing a user configuring a flow that triages customer questions with Gemini.

> **Figure 1:** A user configures a flow that triages customer questions with Gemini.

---

## Workspace Studio Concepts

### Flows

Users build **flows** in Workspace Studio to automate tasks in Google Workspace and beyond.

Key traits:

- Deep system integration
- Contextual awareness
- Can optionally use AI

> “Flows have deep system integration, contextual awareness, and can optionally use AI.”

---

### Step

A **step** is a single task in a flow’s automated process.

Important details:

- Represents one task in a sequence.
- Follows a starting event.
- Runs **synchronously**:
  - Each step completes before the next step begins.
- Users determine the order of steps.
- Steps can have inputs and outputs, but they are not required.

Examples of steps:

- “send an email”
- “post in a Chat space”
- “ask Gemini”
- Tasks outside Google Workspace, such as creating a CRM lead

> “Each step runs synchronously, meaning it completes its operation before the next step in the sequence begins.”

---

### Input Variable

An **input variable** is received by a step.

Key points:

- Set by the user on a step’s configuration card.
- Used while configuring the step.
- Examples:
  - Email address
  - Datetime
  - Gemini prompt

> “Input variables are received by steps.”

---

### Output Variable

An **output variable** is returned by a step and can be passed to another step.

Example use case:

- A step outputs an email address.
- Another step uses that email address as the recipient of an email.

> “Output variables are returned by steps, and can be sent to another step.”

---

### Dynamic Variable

A **dynamic variable** is a variable whose data can only be determined when the user configures the flow.

Example:

- Google Forms can have varying questions and answers.
- The number and content of those questions and answers are unknown until a specific Form starts a flow.

> “Dynamic variables account for this case.”

---

### Custom Resource

A **custom resource** is a custom data structure used to group multiple variables together.

Example:

- To create a CRM lead, pass a custom resource containing:
  - Email address
  - Street address
  - Name

> “A custom data structure that you can define to group multiple variables together.”

---

### Card

A **card** is a building block for user interfaces in add-ons.

Cards support:

- Defined layouts
- Interactive UI elements, such as buttons
- Rich media, such as images

Cards include special features for building flows:

- `IncludeVariables`: A property that enables dynamic variable inclusion.
- `Type`: Defines the type of data that input variables expect.

---

### Activity Log

An **activity log** describes what happens when a flow runs.

By default:

- Activity logs include the name of the starter or step.
- These names are statically defined in the manifest.

Developers can also provide customized activity logs.

> “Describes what happens when an flow runs.”

---

## What You Can Build

Workspace Studio flows are built on the **Google Workspace add-ons platform**.

If you already have an existing add-on:

- You can extend it to include flows.
- This is done by updating the add-on manifest to include a flow-specific section.

> “If you already have an existing add-on, you can extend its functionality to include Flows by updating its manifest to 

[... summary truncated for context management ...]
