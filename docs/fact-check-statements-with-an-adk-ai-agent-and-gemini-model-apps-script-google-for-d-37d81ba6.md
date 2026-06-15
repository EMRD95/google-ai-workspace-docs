---
title: "Fact-check statements with an ADK AI agent and Gemini model  |  Apps Script  |  Google for Developers"
source_url: "https://developers.google.com/apps-script/samples/custom-functions/fact-check"
product_area: "apps-script-ai"
retrieved_at: "2026-06-15T18:20:14Z"
extraction_method: "web_extract"
---

# Fact-check statements with an ADK AI agent and Gemini model — Markdown Summary

**Source:** Google for Developers — Apps Script sample  
**URL:** https://developers.google.com/apps-script/samples/custom-functions/fact-check  
**Last updated:** 2026-04-20 UTC  
**Coding level:** Advanced  
**Duration:** 30 minutes  
**Project type:** [Custom function](https://developers.google.com/apps-script/guides/sheets/functions)

---

## Overview

This guide shows how to create a **Google Sheets custom function** named `FACT_CHECK` using a **container-bound Google Apps Script project**, powered by:

- A **Vertex AI Agent Engine ADK agent** for reasoning.
- A **Gemini model from Vertex AI** for output formatting and text generation.

The function lets users fact-check statements directly in Google Sheets.

> “A fact-check custom function for Google Sheets to be used as a bound Google Apps Script project powered by a Vertex AI agent and Gemini model.”

The sample demonstrates two AI capabilities inside Sheets:

1. **AI agents** for sophisticated, multi-tool, multi-step reasoning using ADK agents deployed in Vertex AI Agent Engine.
2. **AI models** for advanced understanding, generation, and summarization using Gemini models from Vertex AI.

---

## What the Solution Does

The custom function analyzes a statement, grounds the response using recent web information, and returns the result in the requested format.

### Function Name

```text
FACT_CHECK
```

### Usage

```text
=FACT_CHECK("Your statement here")
```

Returns a concise, summarized fact-check result.

```text
=FACT_CHECK("Your statement here", "Your output formatting instructions here")
```

Returns a fact-check result formatted according to the second argument.

### AI Components

- **Reasoning:** [LLM Auditor ADK AI Agent — Python sample](https://github.com/google/adk-samples/tree/main/python/agents/llm-auditor)
- **Output formatting:** [Gemini model](https://cloud.google.com/vertex-ai/generative-ai/docs/models)

### API Access

The Apps Script custom function calls Vertex AI REST APIs using:

```text
UrlFetchApp
```

Reference: [UrlFetchApp](https://developers.google.com/apps-script/reference/url-fetch/url-fetch-app)

---

## Objectives

By following the guide, you learn how to:

- Understand what the solution does.
- Understand how the solution is implemented.
- Deploy the Vertex AI agent.
- Set up the Apps Script project.
- Run and test the custom function in Google Sheets.

---

## Architecture

The solution uses both **Google Workspace** and **Google Cloud** resources.

At a high level:

- Google Sheets hosts the custom function.
- Apps Script executes the custom function logic.
- Apps Script calls Vertex AI REST APIs.
- Vertex AI Agent Engine hosts the deployed **LLM Auditor ADK agent**.
- Gemini formats and summarizes the final response.
- A Google Cloud service account authenticates API access.

Architecture image referenced in the guide:

```text
https://developers.google.com/static/apps-script/samples/images/fact-check-flow.png
```

---

## Prerequisites

You need:

- A Google Account.
  - Google Workspace accounts may require administrator approval.
- A web browser with internet access.
- Prerequisites for the LLM Auditor ADK agent:
  - **Python 3.11+**
  - **Python Poetry**
  - **Google Cloud CLI**

Relevant setup links:

- Python: https://docs.python.org/3/using/index.html
- Poetry: https://python-poetry.org/docs/
- Google Cloud CLI: https://cloud.google.com/sdk/docs/install

---

# Environment Preparation

The environment setup includes:

1. Creating a Google Cloud project.
2. Enabling billing.
3. Enabling Vertex AI API.
4. Creating a service account.
5. Creating a private key.

---

## 1. Create a Google Cloud Project

### Using Google Cloud Console

1. Go to **IAM & Admin > Create a Project**.
2. Enter a descriptive project name.
3. Optionally edit the **Project ID**.
   - The project ID cannot be changed after creation.
4. Choose a project location.
5. Click **Create**.

Direct link:

```text
https://console.cloud.google.com/projectcreate
```

### Using gcloud CLI

Use Cloud Shell or a local shell with Google Cloud CLI installed and initialized.

```bash
gcloud projects create PROJECT_ID
```

Replace:

- `PROJECT_ID` with the desired Cloud project ID.

---

## 2. Enable Billing for the Cloud Project

### Using Google Cloud Console

1. Go to **Billing > My Projects**.
2. Select the organization associated with the project.
3. In the project row, open **Actions > Change billing**.
4. Choose the Cloud Billing account.
5. Click **Set account**.

Direct link:

```text
https://console.cloud.google.com/billing/projects
```

### Using gcloud CLI

List available billing accounts:

```bash
gcloud billing accounts list
```

Link a billing account to the project:

```bash
gcloud billing projects link PROJECT_ID --billing-account=BILLING_ACCOUNT_ID
```

Replace:

- `PROJECT_ID` with the Cloud project ID.
- `BILLING_ACCOUNT_ID` with the billing account ID.

[... summary truncated for context management ...]
