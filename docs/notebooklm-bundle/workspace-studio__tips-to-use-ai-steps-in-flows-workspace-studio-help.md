# Tips to use AI steps in flows - Workspace Studio Help

**Product Area:** workspace-studio
**Source:** https://support.google.com/workspace-studio/answer/16431105?hl=en

# Tips to Use AI Steps in Flows — Google Workspace Studio

**Source:** [Workspace Studio Help](https://support.google.com/workspace-studio/answer/16431105?hl=en)  
**Topic:** How to incorporate Gemini and AI-powered steps into Workspace Studio flows.

---

## Overview

Google Workspace Studio lets you incorporate **Gemini** into automated flows. Gemini can help flows:

- Analyze content
- Write or draft text
- Research information
- Determine whether a flow should run
- Summarize, extract, or recap information

The article explains when to use different types of AI steps:

- **General AI steps**
  - Ask Gemini
  - Ask a Gem
- **AI action steps**
  - Decide
  - Extract
  - Summarize
  - Recap unread emails

---

## Account Type Requirements

### Personal Accounts

> **Personal accounts:** If you have a Google AI Pro or Ultra plan, you can use flows in Workspace Studio. You can't share flows with others.

### School Accounts

> **School accounts:** If you use a school account and are under 18, you can't get AI features in Workspace Studio. If someone shares a flow with AI steps with you, those steps are removed when you open the flow.

---

## How to Use AI Steps Successfully

The article identifies **4 keys to success** when using any AI step.

---

### 1. Provide Context in Your Request

Gemini does **not** automatically know what happened in earlier steps of your flow.

> Gemini doesn’t know about the other steps in your flow. Prompts like “Write a professional reply to the email” won’t work because Gemini doesn’t know which email you mean.

#### Actionable Tips

- Reference data from earlier flow steps.
- Include variables from previous steps.
- Link to specific Google Drive files.
- Link to relevant websites.
- Add enough context for Gemini to understand the request.

#### For Open Prompt AI Steps

For steps such as **Ask Gemini** and **Decide**, add context directly into the prompt for better results.

> **Reference data from earlier steps and specific files**: For AI steps with open prompts, such as 'Ask Gemini' and 'Decide', add context to your prompt to get better results.

---

### 2. Control Data Sources Gemini Can Use

By default, Gemini can use:

- The web
- Workspace content you can access
- Connected integrations you can access

To limit access, choose **Web only**.

> **Allow Google Workspace data sources**: By default, Gemini can reference the web, as well as all content that you can access in Google Workspace and connected integrations. To prevent Gemini from accessing your personal or organization's data, choose **Web only**.

---

### 3. Use Gemini’s Response as a Variable Later

Gemini’s response becomes a variable tied to the AI step.

> **Access Gemini’s response by adding a variable in a later step**. The response from Gemini or a Gem is available as a variable associated with the AI-powered step.

You can reuse that output in later steps, such as:

- A message
- A document
- A spreadsheet
- Another Gemini request

---

### 4. Use Multiple AI Steps in One Flow

You can chain AI steps together by passing variables from one step to another.

Example workflow from the article:

> You could use the **Sales pitch ideator** Gem in **Ask a Gem** to analyze a form response, use an **Extract** step find any questions in an open-ended response, use a **Ask Gemini** step draft an email message using the Gem response and extracted questions for additional context, and use an **Ask Gemini** step to create a subject line for your message.

---

### 5. Use AI Action Steps When Appropriate

Although **Ask Gemini** can handle many requests, Workspace Studio includes specialized AI action steps optimized for common tasks.

> Though you can use Ask Gemini for almost all types of requests, Workspace Studio has AI steps that are optimized for certain actions, such as extracting information from text, summarizing ideas and insights, or writing text for specific scenarios.

---

## General AI Steps

General AI steps are used similarly to Gemini in Workspace.

| Step | Best For | Examples / Notes |
|---|---|---|
| **Ask Gemini** | General inquiries or text generation | Web research, summarizing project status, creative writing |
| **Ask a Gem** | Using the agentic expertise of a pre-built or custom Gem | Sales pitch ideation, custom file-grounded content generation |

---

### Ask Gemini

Best for **general inquiries** or **text generation** needs.

Examples:

- Do a quick web search on the company of a person who submitted a form or contacted you.
- Summarize the state of a project based on the latest meeting notes and tracking spreadsheet.
- Write a poem about the importance of updating a meeting agenda to send to attendees.

Important tip:

> **Tip:** For common drafting, summarizing, and extracting tasks, you can save time crafting prompts by using AI action steps instead.

---

### Ask a Gem

Use **Ask a Gem** when you need the expertise of a specific Gem, either pre-built or custom.

Examples:

- Have t

[... summary truncated for context management ...]
