# Converse with Data Studio data  |  Google Cloud Documentation

**Product Area:** looker-studio
**Source:** https://cloud.google.com/looker/docs/studio/conversational-analytics-looker-studio

# Converse with Data Studio Data — Comprehensive Summary

**Source:** Google Cloud Documentation — Data Studio  
**URL:** https://cloud.google.com/looker/docs/studio/conversational-analytics-looker-studio  
**Last updated:** 2026-06-11 UTC  
**Note:** Looker Studio is now called **Data Studio**.

---

## Overview

This documentation explains how to use **Conversational Analytics in Data Studio** to ask natural-language questions about connected data sources, manage conversations, understand generated results, and work within known limitations.

Conversational Analytics lets users interact with data through chat-style conversations. Responses may include text explanations, tables, visualizations, SQL, reasoning traces, and suggested follow-up insights.

For setup and connection instructions, see:

- **Set up Conversational Analytics in Data Studio**
- **Conversational Analytics overview**
- **Create and converse with data agents**
- **Enable advanced analytics with the Code Interpreter**

Google also links to guidance on **how and when Gemini for Google Cloud uses your data**.

---

## Key Excerpts & Important Original Text

### Query cancellation message

When a query is stopped, Conversational Analytics displays:

```text
The query was cancelled.
```

### Example question rephrasing

Conversational Analytics may rephrase user questions:

> Conversational Analytics might rephrase the question "What is the mean of user ages?" to "What is the average user age?"

### Example Fast mode mapping

A natural-language query such as:

> "What was our total revenue last month?"

Can be translated into a query that selects:

```text
total_revenue
```

and filters for the previous month.

### Sample conversation prompt

Example user question:

> "Can you plot monthly sales of hot drinks versus smoothies for 2023, and highlight the top selling month for each type of drink?"

Conversational Analytics responds with a line graph showing monthly sales for hot drinks and smoothies in 2023, highlighting **July** as the top-selling month for both categories.

### Example Insights output

For the prompt:

> "How many users are in each state?"

Conversational Analytics might return insights such as:

- "California, Texas, and Ohio are key states for business operations based on the data provided."
- "England and specific regions in China, namely Anhui and Guangdong, show significant business activity."
- "Some states, including Mie, Akita, and Iwate, have minimal presence based on the data."
- "The data indicates varying operational scales across different locations."

---

## Accessing Conversational Analytics

You can access Conversational Analytics in Data Studio in several ways:

- Go directly to **Conversational Analytics**:
  - https://datastudio.google.com/conversation
- Select **Conversational Analytics** from the Data Studio navigation panel.
- In a **Sandbox** workspace, choose **Conversations** from the **Create** menu.
- If **data agents** exist for your instance:
  - Select **Data source** from the **Create** menu.
  - Choose **Chat with my data** on the **Get started** page.

---

## Conversations: Core Concept

A **conversation** is a set of questions asked about a dataset or data agent.

Using multiple conversations is helpful for organizing different lines of inquiry.

The conversation experience differs between:

- **New Conversational Analytics**
- **Legacy Conversational Analytics**

The documentation contains separate guidance for each experience.

---

## Starting a Conversation

### New Conversational Analytics

All conversations happen with a **data agent** that was:

1. Built in **BigQuery**
2. Published to **Data Studio**

To start:

1. Go to the **Chat with your data** page.
2. Select the data agent you want to use.
   - Use the **Search agents** bar if needed.
3. Enter your question and press:
   - **Return** on Mac
   - **Enter** on PC

To chat with a different data agent, select:

```text
+ New conversation
```

### Permissions for Data Agents

If you lack required permissions:

- The agent appears on the **Chat with your data** page.
- The agent is inactive.
- Clicking the agent card shows a message explaining which IAM role or permission is needed for the agent’s Google Cloud project.

---

### Legacy Conversational Analytics

To create a new conversation:

1. Click **+ Create conversation** in Conversational Analytics.
2. Select either:
   - **Data source**
   - **Data agent**
3. Enter your question and press:
   - **Return** on Mac
   - **Enter** on PC

#### Data Source Option

To use an existing data source:

1. Select the **Data source** panel.
2. Choose a data source.

To create a new data source:

- Select **Connect to data**.

#### Data Agent Option

To use an existing data agent:

1. Select **Agents**.
2. Choose a data agent.

To create a new data agent:

- Select **+ Create agent**.

You can return to prior conversations from the **Recent** section.

---

## Conversing with Looker Data Sou

[... summary truncated for context management ...]
