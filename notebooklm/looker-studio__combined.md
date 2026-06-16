---
title: "Combined source: looker-studio"
product_area: "looker-studio"
source_count: 5
generated_at: "2026-06-16T08:47:02Z"
source_type: "coverage_merged_official_extracts"
---

# Combined source: looker-studio

This file merges 5 official extracted source document(s) from coverage area `looker-studio` for NotebookLM import limits.
No synthetic documentation is added; each section preserves the source URL and extracted Markdown body.

## Source index

1. Add Data Studio content to your Google Slides presentation using Gemini assistance  |  Google Cloud Documentation — https://cloud.google.com/looker/docs/studio/add-looker-studio-slides-gemini
2. Converse with Data Studio data  |  Google Cloud Documentation — https://cloud.google.com/looker/docs/studio/conversational-analytics-looker-studio
3. Create calculated fields with Gemini assistance  |  Data Studio  |  Google Cloud Documentation — https://cloud.google.com/looker/docs/studio/create-calculated-fields-gemini
4. Data agents in Data Studio  |  Google Cloud Documentation — https://cloud.google.com/looker/docs/studio/conversational-data-agents?hl=en
5. Enable and use the Code Interpreter  |  Data Studio  |  Google Cloud Documentation — https://cloud.google.com/looker/docs/studio/conversational-analytics-code-interpreter?hl=en

---

## Source 1: Add Data Studio content to your Google Slides presentation using Gemini assistance  |  Google Cloud Documentation

- Source URL: https://cloud.google.com/looker/docs/studio/add-looker-studio-slides-gemini
- Original file: `docs/add-data-studio-content-to-your-google-slides-presentation-using-gemini-assistance-google--c1dc5ba4.md`
- Product area: `looker-studio`

# Add Data Studio Content to Google Slides Using Gemini Assistance — Summary

**Source:** Google Cloud Documentation  
**Product note:** *Looker Studio is now called Data Studio.*  
**Last updated:** 2026-06-11 UTC

## Overview

This page explains how to use **Gemini in Data Studio** to generate or enhance **Google Slides presentations** from **Data Studio reports**.

Gemini can:

- Insert Data Studio report charts into Google Slides **as images**
- Generate a **textual summary for each chart**
- Insert those summaries as **text elements**
- Create a full Google Slides deck from:
  - All report visualizations
  - Selected report visualizations
  - Data Studio content imported into an existing Slides presentation

> Gemini in Data Studio is part of the **Gemini for Google Cloud** portfolio and provides generative AI-powered assistance for analyzing and gaining insights from data.

Relevant data governance information:  
[How and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance)

---

## Key Requirements Before You Begin

To use this feature, all applicable requirements must be met:

- You must be under a **Data Studio Pro subscription**.
  - Data Studio Pro licenses are available at no cost to Looker users.
- **Gemini in Data Studio** must be enabled for your Data Studio project.
- The **Gemini for Google Cloud API** must be enabled in your Google Cloud project.
- You must be a **viewer or editor** of the Data Studio report.
- If you are only a viewer, the sharing option **Disable viewers from generating Google Slides with Gemini in Data Studio** must **not** be selected.
- You must be an **editor** of the Google Slides presentation you want to import content into.
- To add Data Studio content to an existing Google Slides presentation, you must install the **Data Studio add-on for Google Workspace**.

Important API:

```text
cloudaicompanion.googleapis.com
```

---

## Generate a Google Slides Presentation from All Visualizations

Use this option to create a deck containing every visualization in a Data Studio report.

### Steps

1. Open a Data Studio report in **view mode** or **edit mode**.
2. In the panel manager, select the **Gemini** panel.
3. Select **Generate Slides**.
4. Select **All visualizations**.
5. Data Studio generates a Google Slides presentation and saves it to your **Google Drive**.

### Generated Presentation Includes

- A **title slide** with:
  - Data Studio report title
  - Your name
  - Date generated
  - Link to the Data Studio report
- One slide for every chart, including:
  - Chart title, if available
  - Textual chart summary
- A **closing slide**

### Important Limitation

After generating the presentation this way, you **cannot edit it further in Data Studio**. To view or edit it, click the link in the **Gemini** panel.

---

## Generate a Presentation from Selected Visualizations

Use this option to choose specific report components for the generated Slides deck.

### Steps

1. Open a Data Studio report in **view mode** or **edit mode**.
2. In the panel manager, select the **Gemini** panel.
3. Select **Generate Slides**.
4. Select **Let me choose**.
5. Click the component or components to add.
   - To select multiple components:
     - **Shift-click** each component, or
     - Drag a selection area over the canvas.
   - Charts, titles, and filters are separate components.
   - Gemini only generates text summaries for **visualizations**.
6. Choose whether to add the selected components to:
   - A new slide, or
   - The current slide.
7. Click **Done** in the top banner.
8. Data Studio adds the selected components to the **Gemini** panel.
   - To disable a textual summary, click the **Summary on** icon.
   - To remove a visualization, click the **Delete** icon.
9. Repeat the selection process to add more components.
10. When finished, select **Generate Slides** in the **Gemini** panel.
11. Data Studio generates the presentation and saves it to your **Google Drive**.

### Generated Presentation Includes

- A title slide with:
  - Report title
  - Your name
  - Generation date
  - Link to the Data Studio report
- The slides you created from selected components
- A closing slide

### Important Limitation

After generation, the presentation **cannot be further edited in Data Studio**. Use the link in the **Gemini** panel to open it in Google Slides.

---

## Add Data Studio Content to an Existing Google Slides Presentation

This workflow uses the **Data Studio add-on for Google Workspace**.

### Requirement

Install the add-on:

- [Data Studio add-on for Google Workspace](https://workspace.google.com/marketplace/app/looker_studio/771955699012)

The add-on only works if:

- You are a **Data Studio Pro user**
- Gemini in Data Studio is enabled for your Data Studio project

### Steps

1. In Google Slides, click the **Data Studio** icon on the right-hand toolbar to open the **Data Studio** panel.
2. Click **Import**.
3. Data S

[... summary truncated for context management ...]

---

## Source 2: Converse with Data Studio data  |  Google Cloud Documentation

- Source URL: https://cloud.google.com/looker/docs/studio/conversational-analytics-looker-studio
- Original file: `docs/converse-with-data-studio-data-google-cloud-documentation-255c363a.md`
- Product area: `looker-studio`

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

---

## Source 3: Create calculated fields with Gemini assistance  |  Data Studio  |  Google Cloud Documentation

- Source URL: https://cloud.google.com/looker/docs/studio/create-calculated-fields-gemini
- Original file: `docs/create-calculated-fields-with-gemini-assistance-data-studio-google-cloud-documentation-9374845c.md`
- Product area: `looker-studio`

# Create Calculated Fields with Gemini Assistance — Data Studio

**Source:** Google Cloud Documentation — Data Studio  
**Page:** “Create calculated fields with Gemini assistance”  
**Last updated:** 2026-06-11 UTC  
**Audience:** Report editors in Data Studio

> Looker Studio is now called **Data Studio**.

---

## Overview

This documentation explains how to use **Gemini in Data Studio** to help create **calculated fields** by describing the field you want in natural language.

Data Studio uses Gemini to suggest a formula for a calculated field based on:

- Your prompt or description
- Fields from your data source
- Data Studio functions and operators

Gemini in Data Studio is part of the **Gemini for Google Cloud** portfolio and provides generative AI-powered assistance to help users analyze data and gain insights.

Relevant resources mentioned:

- [Gemini in Data Studio](https://docs.cloud.google.com/data-studio/gemini-overview)
- [Calculated fields in Data Studio](https://docs.cloud.google.com/data-studio/about-calculated-fields)
- [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview)
- [How and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance)

---

## Requirements Before You Begin

To use Gemini assistance for calculated fields, all of the following must be true:

- You must be a user under a **Data Studio Pro subscription**.
  - Data Studio Pro licenses are available at no cost to Looker users.
- To create **chart-specific calculated fields**, you must be an **editor of the report**.
- **Field Editing in Reports** must be enabled in the data source.
- **Gemini in Data Studio** must be enabled for your **Data Studio Pro project**.

---

## How to Create a Calculated Field with Gemini Assistance

Follow these steps:

1. While writing a calculated field, click the **Help me write a calculated field** icon in the bottom-right corner of the field editor.

2. If you have **not** started writing a calculated field:
   - Data Studio prompts you to either:
     - Select a suggested prompt, or
     - Describe the kind of calculated field you want to create.
   - To use a suggested prompt, click it.
   - To write your own prompt, enter a description and click **Create**.

3. If you have **already started** writing a calculated field:
   - Data Studio uses your existing formula as context.
   - Describe how you want to change the calculated field.
   - Click **Create**.

   Additional options while refining:
   - To edit your original prompt:
     - Hover over the prompt.
     - Click the **Edit** icon.
     - Update the prompt.
     - Click **Update**.
   - To remove the previous formula from Data Studio’s context:
     - Hover over the formula.
     - Click the **Reset** icon.
   - To refine the formula:
     - Click **Refine**.
     - Provide more details, such as:
       - Adding or removing a bucket
       - Adding another field to a concatenation
     - Click **Create**.

4. To add the generated formula to the calculated field definition, click **Apply**.

5. To save the field definition, click **Save**.

### Exiting Without Saving

To exit the formula generation dialog without saving changes:

- Click the **X** in the top-right corner, or
- Click outside the dialog.

---

## Limitations

Gemini assistance for calculated fields has these limitations:

- Gemini can only help create calculated fields that meet Data Studio’s standard criteria for what calculated fields can do.
- Data Studio will **not** suggest:
  - Parameters
  - `NATIVE_DIMENSION`
- The **Looker connector** supports only some calculated-field functions.

---

## Information Used by Gemini in Data Studio

When generating formulas, Data Studio uses:

- The prompt you write to create or edit a field
- The formula definition for any field you change or refine
- The schema of the underlying data source

---

## Sample Prompts and Generated Formulas

### Example 1: Merge City and State

Prompt:

```text
Merge city and state like City, State
```

Data Studio may return:

```sql
CONCAT(Users City, ", ", Users State)
```

---

### Example 2: Bucket Sale Price in Groups of 20

Prompt:

```text
bucket sale price in groups of 20
```

Data Studio may return:

```sql
CASE
      WHEN Order Items Sale Price < 20 THEN "0-20"
      WHEN Order Items Sale Price < 40 THEN "20-40"
      WHEN Order Items Sale Price < 60 THEN "40-60"
      WHEN Order Items Sale Price < 80 THEN "60-80"
      WHEN Order Items Sale Price < 100 THEN "80-100"
      WHEN Order Items Sale Price < 120 THEN "100-120"
      WHEN Order Items Sale Price < 140 THEN "120-140"
      WHEN Order Items Sale Price < 160 THEN "140-160"
      WHEN Order Items Sale Price < 180 THEN "160-180"
      WHEN Order Items Sale Price < 200 THEN "180-200"
      ELSE "200+"
END
```

---

## Troubleshooting

If an error occurs while creating a calculated field, verify that your request is asking for something achievabl

[... summary truncated for context management ...]

---

## Source 4: Data agents in Data Studio  |  Google Cloud Documentation

- Source URL: https://cloud.google.com/looker/docs/studio/conversational-data-agents?hl=en
- Original file: `docs/data-agents-in-data-studio-google-cloud-documentation-ec1946bf.md`
- Product area: `looker-studio`

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

---

## Source 5: Enable and use the Code Interpreter  |  Data Studio  |  Google Cloud Documentation

- Source URL: https://cloud.google.com/looker/docs/studio/conversational-analytics-code-interpreter?hl=en
- Original file: `docs/enable-and-use-the-code-interpreter-data-studio-google-cloud-documentation-031cb36c.md`
- Product area: `looker-studio`

# Enable and Use the Code Interpreter — Data Studio / Conversational Analytics

**Source:** Google Cloud Documentation  
**URL:** <https://cloud.google.com/looker/docs/studio/conversational-analytics-code-interpreter?hl=en>  
**Last updated:** 2026-06-11 UTC

---

## Overview

The **Code Interpreter** is a feature of **Conversational Analytics** in **Data Studio** that converts natural language questions into **Python code** to perform advanced analytics and generate visualizations.

It extends standard SQL-powered BI capabilities by supporting more flexible and advanced analysis, including:

- Basic computations
- Charting and visualizations
- Advanced analytics
- Time series forecasting
- Statistical or coding-based analysis that would otherwise require specialized expertise

> The Code Interpreter is available for Conversational Analytics as part of a **Data Studio Pro subscription**.

It uses **the engine that powers Gemini chat** to translate user questions into Python code and execute that code.

Google also provides information on data usage here:  
[How and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance)

---

## Prerequisites

To use the Code Interpreter, you must meet the requirements for Conversational Analytics in Data Studio:

- You must be a user under a **Data Studio Pro subscription**.
- **Gemini in Data Studio** and the **Code Interpreter** setting must be enabled for the Google Cloud project associated with your Data Studio Pro subscription.

Relevant setup documentation:

- [Conversational Analytics setup and requirements](https://docs.cloud.google.com/data-studio/conversational-analytics-setup#setup_and_requirements)
- [Enable and disable Gemini in Data Studio](https://docs.cloud.google.com/data-studio/enable-and-disable-gemini-in-data-studio)

---

## Enable the Code Interpreter for Agents

To enable the Code Interpreter for all conversations and data agents:

1. In the left navigation panel within **Conversational Analytics**, click the **Advanced analytics** toggle to enable the Code Interpreter.
2. After enabling it, use Conversational Analytics normally to start conversations and ask questions of your data.

Once enabled, the Code Interpreter translates natural language prompts into Python code and executes that code to provide answers, analysis, and visualizations.

---

## Known Limitations

The Code Interpreter has several important limitations:

- It uses **Python** to solve problems. Because Python is more flexible than structured query languages, results may show **more variability** than responses from the core Conversational Analytics experience.
- For **Looker data**, Conversational Analytics can return a maximum of **5,000 rows per query**.
- The Code Interpreter supports only a specific set of Python libraries.
- The following visualization chart type is **not supported** in Code Interpreter responses:
  - Maps

> This feature is in Pre-GA. For support with errors, unexpected results, feedback, or to request support for additional Python libraries, send an email to [conversational-analytics-feedback@google.com](mailto:conversational-analytics-feedback@google.com).

For broader limitations, see:  
[Known limitations in Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics-data#known-limitations)

---

## Supported Python Libraries

The Code Interpreter supports the following Python libraries:

```text
altair
attrs
chess
contourpy
cycler
entrypoints
fonttools
fpdf
geopandas
imageio
jinja2
joblib
jsonschema
jsonschema-specifications
kiwisolver
lxml
markupsafe
matplotlib
mpmath
numexpr
numpy
opencv-python
openpyxl
packaging
pandas
patsy
pdfminer-six
pillow
plotly
protobuf
pylatex
pyparsing
PyPDF2
python-dateutil
python-docx
python-pptx
pytz
referencing
reportlab
rpds-py
scikit-image
scikit-learn
scipy
seaborn
six
statsmodels
striprtf
sympy
tabulate
tensorflow
threadpoolctl
toolz
torch
tzdata
xlrd
```

---

## Suggested Questions and Use Cases

When enabled, the Code Interpreter expands the range of questions Conversational Analytics can answer beyond standard supported question types.

Example prompts include:

- Can you explain the key drivers for sales based on my data?
- What is the lifetime value for each of my customer segments, taking into account the average purchase frequency and the average order value?
- How do sales this year compare to sales last year?
- Identify outliers in my sales data to help identify products or regions that are performing particularly well or particularly poorly.
- Perform a cohort analysis to understand customer retention.
- Are my highest margin products also the most popular products? Use this answer to provide a suggestion on how to optimize my product mix.
- What is the compound annual growth rate, or CAGR, for sales by product category for the last 3 years?
- Show the CAGR as a bar chart with product category on the x-axis and CAGR o

[... summary truncated for context management ...]

---
