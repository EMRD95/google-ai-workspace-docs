---
title: "Data agents in Data Studio  |  Google Cloud Documentation"
source_url: "https://cloud.google.com/looker/docs/studio/conversational-data-agents?hl=en"
product_area: "looker-studio"
retrieved_at: "2026-06-15T09:34:34Z"
extraction_method: "web_extract"
---

# Data Agents in Data Studio — Summary

**Source:** Google Cloud Documentation — Data Studio  
**URL:** https://cloud.google.com/looker/docs/studio/conversational-data-agents?hl=en  
**Last updated:** 2026-06-11 UTC

> Looker Studio is now called Data Studio.

## Overview

**Data agents** let users curate the **Conversational Analytics** experience for specific datasets and use cases. They help analysts provide the system with context and instructions so it can answer data questions more effectively.

Data agents can be used to:

- Map business terms to specific fields
- Specify preferred fields for filtering and grouping
- Define custom calculations or concepts
- Provide contextual instructions for more accurate responses

The experience differs between:

- **New Conversational Analytics**
- **Legacy Conversational Analytics**

---

# New Conversational Analytics Experience

In the new experience, **data agents are created and managed in BigQuery**, then made available in Data Studio after being shared with users.

## Key Behavior

> Conversational Analytics data agents become available in Data Studio after they are first created in BigQuery and shared with Data Studio users.

Once a data agent is **published in BigQuery**, it automatically appears in the list of agents on the **Chat with your data** page in Data Studio.

---

## Create and Share a Data Agent

To create and share a data agent:

1. Create the agent in **BigQuery**.
2. Grant users access to chat with it in BigQuery and Data Studio.
3. Publish the agent.
4. The agent appears automatically in Data Studio under **Chat with your data**.

You can also copy a Data Studio link from BigQuery:

- From the agent card:
  1. Select **Open actions**
  2. Select **Copy link**
  3. Select **Data Studio**

- From the **Details** panel:
  1. Select **Copy agent link**
  2. Select **Data Studio**

Pasting the link in a browser opens a new conversation with the agent.

---

## Edit a Data Agent

Data agents in the new experience are edited in **BigQuery**.

Options:

- Edit directly in BigQuery
- From Data Studio, open the agent **Details** panel and select **Edit in BigQuery**

From BigQuery, you can also:

- Revoke access
- Delete the agent

---

## Start a Conversation with an Agent

To start a conversation:

1. Navigate to the **Chat with your data** page.
2. Select the data agent you want to use.
   - Use the **Search agents** bar if needed.
3. Enter your question.
4. Press **Return** on Mac or **Enter** on PC.

To chat with another agent:

- Select **+ New conversation** from the main navigation.

You can return to previous conversations from the **Recent** section.

---

## Agent Metadata

Data Studio shows data agent information in two places:

1. **Agent card**
2. **Details panel**

---

### Agent Card

The agent card appears on the **Chat with your data** page.

It includes:

- **Agent**: Name of the agent, as written by the creator
- **Description**: Description written by the creator
- **Updated**: Timestamp of when the agent was last published from BigQuery
- **Open actions** menu with:
  - **Details**: Opens the Details panel
  - **Edit in BigQuery**: Opens the agent configuration in BigQuery
  - **Copy link**: Copies the link to the agent
  - **Send Feedback**: Opens a feedback panel

---

### Agent Details Panel

The **Details** panel appears while chatting with a data agent.

It includes:

- **Agent**: Agent name
- **Description**: Agent description
- Link to edit the agent in BigQuery
- Link to copy the agent URL
- **Knowledge sources**:
  - BigQuery tables
  - BigQuery views
  - BigQuery user-defined functions, or UDFs
- **Project**: Google Cloud project containing the data agent
- **Labels**: Labels assigned to the BigQuery resources, if any
- **Last published**: Timestamp of last publication from BigQuery
- **Created**: Timestamp of creation in BigQuery

---

# Legacy Conversational Analytics Experience

In the legacy experience, data agents are created, edited, shared, deleted, and restored directly in **Conversational Analytics** within Data Studio.

---

## Create and Edit Data Agents

### Create a New Data Agent

To create a new data agent:

1. In Conversational Analytics, go to the **Chat with your data** page.
2. Select the **Agents** tab.
3. Select **+ Create agent**.

Alternatively:

1. In the left navigation panel, select **Manage agents**.
2. Select **+ Create agent**.

On the **New agent** page, provide:

### Required Agent Information

#### Agent Name

Enter a unique and descriptive name.

#### Description

Briefly describe:

- What the agent can do
- What data it uses
- How users should use it

Users see this description when selecting or receiving the shared agent, so it should clearly explain the agent’s purpose.

#### Data

Connect to a new or existing data source:

1. In the **Data** field, click **Select data**.
2. In the **Select data for Agent** window, click the data source name.
3. Click **Select**.

Alternatively, se

[... summary truncated for context management ...]
