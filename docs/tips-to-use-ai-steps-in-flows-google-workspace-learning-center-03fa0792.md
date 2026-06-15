---
title: "Tips to use AI steps in flows - Google Workspace Learning Center"
source_url: "https://support.google.com/a/users/answer/16431105"
product_area: "workspace-studio"
retrieved_at: "2026-06-15T17:30:23Z"
extraction_method: "web_extract"
---

# Tips to Use AI Steps in Flows — Google Workspace Studio

**Source:** Google Workspace Learning Center  
**URL:** https://support.google.com/a/users/answer/16431105

## Overview

Google Workspace Studio lets you incorporate **Gemini** into flows so AI can automatically:

- Analyze information
- Write content
- Research topics
- Decide whether a flow should run

The article explains which AI step to use depending on your use case, covering:

- How to use AI steps effectively
- General AI steps
- AI action steps
- Source/privacy controls

---

## Account Type Requirements

### Personal Accounts

- If you have a **Google AI Pro** or **Ultra** plan, you can use flows in Workspace Studio.
- You **can’t share flows** with others.

### School Accounts

- If you use a school account and are **under 18**, AI features in Workspace Studio are unavailable.
- If someone shares a flow containing AI steps with you, those AI steps are **removed when you open the flow**.

---

## Key Excerpts

> “One of the most powerful features of Google Workspace Studio is that you can easily incorporate Gemini into your flows.”

> “Gemini doesn’t know about the other steps in your flow. Prompts like ‘Write a professional reply to the email’ won’t work because Gemini doesn’t know which email you mean.”

> “The response from Gemini or a Gem is available as a variable associated with the AI-powered step.”

> “Though you can use Ask Gemini for almost all types of requests, Workspace Studio has AI steps that are optimized for certain actions, such as extracting information from text, summarizing ideas and insights, or writing text for specific scenarios.”

> “By default, Gemini is allowed to use the web, as well as any Workspace and connected integration data that you can access.”

---

## How to Use AI Steps Effectively

The article highlights **4 keys to success** when using AI steps in flows.

### 1. Provide Context in Your Request

Gemini does **not automatically know** what happened in earlier steps of your flow.

Avoid vague prompts such as:

> “Write a professional reply to the email”

Instead, include enough context so Gemini knows what to work with.

#### Ways to Add Context

- Reference variables from earlier flow steps
- Link to specific Google Drive files
- Include links to relevant websites
- Provide explicit instructions in open-prompt AI steps such as:
  - **Ask Gemini**
  - **Decide**

#### Data Source Control

By default, Gemini can reference:

- The web
- Google Workspace content you can access
- Connected integrations

To restrict Gemini from using personal or organizational data, choose:

> **Web only**

---

### 2. Use Gemini’s Response as a Variable

Responses from Gemini or a Gem can be accessed later in the flow as variables.

You can use these AI-generated variables in:

- Messages
- Documents
- Sheets
- Later Gemini requests
- Other flow steps

This allows AI output from one step to become input for another step.

---

### 3. Use Multiple AI Steps in One Flow

You can combine several AI steps and pass information between them using variables.

Example workflow:

1. Use the **Sales pitch ideator** Gem in **Ask a Gem** to analyze a form response.
2. Use an **Extract** step to find questions in an open-ended response.
3. Use **Ask Gemini** to draft an email using:
   - The Gem response
   - Extracted questions
   - Additional context
4. Use another **Ask Gemini** step to create a subject line.

This lets you chain specialized AI capabilities together.

---

### 4. Use AI Action Steps When Appropriate

While **Ask Gemini** can handle many requests, AI action steps are optimized for specific tasks, including:

- Extracting information from text
- Summarizing ideas and insights
- Writing text for specific scenarios
- Making subjective or complex decisions

Use these specialized steps when they match the task, rather than writing a detailed prompt from scratch.

---

## General AI Steps

General AI steps work similarly to Gemini in Workspace and are best for flexible, agentic tasks.

| AI Step | Best For | Examples |
|---|---|---|
| **Ask Gemini** | General inquiries or text generation | Web search on a company, project summaries, creative writing |
| **Ask a Gem** | Using the specialized expertise of a pre-built or custom Gem | Sales pitch ideation, file-grounded custom content generation |

---

### Ask Gemini

Use **Ask Gemini** for broad or flexible tasks, including:

- Quick web research
- Drafting content
- Summarizing project status
- Generating creative writing

Examples from the article:

- Do a quick web search on the company of a person who submitted a form or contacted you.
- Summarize the state of a project based on the latest meeting notes and tracking spreadsheet.
- Write a poem about the importance of updating a meeting agenda to send to attendees.

**Tip:** For common drafting, summarizing, and extracting tasks, use AI action steps to avoid spending time crafting prompts.

---

### Ask a Gem

Use **Ask a 

[... summary truncated for context management ...]
