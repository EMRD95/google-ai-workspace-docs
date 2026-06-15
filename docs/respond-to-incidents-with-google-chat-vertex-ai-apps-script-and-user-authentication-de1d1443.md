---
title: "Respond to incidents with Google Chat, Vertex AI, Apps Script, and user authentication  |  Google Workspace add-ons  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/tutorial-incident-response"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:09:18Z"
extraction_method: "web_extract"
---

# Respond to Incidents with Google Chat, Vertex AI, Apps Script, and User Authentication

**Source:** Google Developers — Google Workspace add-ons  
**URL:** https://developers.google.com/workspace/chat/tutorial-incident-response  
**Last updated:** 2026-05-29 UTC

---

## Overview

This tutorial shows how to build a **Google Chat incident response app** using:

- **Google Chat API**
- **Vertex AI**
- **Google Apps Script**
- **Google Docs**
- **Admin SDK Directory API**
- **User authentication**

The app helps teams respond to incidents in real time by:

- Creating a dedicated Google Chat space for an incident.
- Adding responders to the space.
- Posting incident details.
- Supporting a `Close incident` quick command.
- Opening a dialog to capture resolution details.
- Reading the Chat conversation.
- Summarizing the response with **Vertex AI Gemini**.
- Creating a Google Docs post-mortem.
- Sharing the generated document back into the Chat space.

> An _incident_ is an event that requires the immediate attention of a team of people to resolve.

Examples include:

- A time-sensitive CRM case requiring service-team collaboration.
- A system outage requiring SRE response.
- A high-magnitude earthquake requiring emergency coordination.

For the tutorial, an incident starts when a user submits a form on a web page with:

- Incident title
- Incident description / initial message
- Email addresses of responders

---

## What the App Does

The incident management app workflow:

1. A user opens an Apps Script-hosted web page.
2. The user submits incident details.
3. The app creates a Google Chat space.
4. The app adds responders and itself to the space.
5. The app posts the initial incident message.
6. Responders discuss the incident.
7. A responder uses the quick command **Close incident**.
8. The app opens a dialog asking for resolution details.
9. The app retrieves up to the first 100 Chat messages.
10. Vertex AI summarizes the conversation.
11. The app creates a Google Docs post-mortem.
12. The app posts the document link in the Chat space.

---

## Prerequisites

If needed, ask a Google Workspace administrator to enable these:

- A **Business or Enterprise Google Workspace account** with access to **Google Chat**.
- **Directory / contact sharing** enabled for Google Workspace.

Important notes:

- Incident responders must be users with a Google Chat account in the same Google Workspace organization.
- The app uses the Directory API to look up responder contact information such as names and email addresses.

---

## Objectives

The tutorial’s goals are to build a Chat app that can:

- Respond to incidents.
- Create incident-response Chat spaces.
- Post incident and response messages.
- Support interactive Chat app features such as:
  - Messages
  - Button clicks
  - Quick commands
  - Dialogs
- Summarize conversations and resolutions with **Vertex AI**.

---

## Architecture

The app uses Google Workspace and Google Cloud resources:

1. A user starts an incident from an external Apps Script-hosted website.
2. The website sends an asynchronous HTTP request to the Chat app, also hosted on Apps Script.
3. The Chat app:
   - Uses Apps Script Admin SDK service to get team member information.
   - Uses Apps Script Advanced Chat service / Chat API to:
     - Create a Chat space.
     - Add team members.
     - Send a message.
4. Team members discuss the incident in the Chat space.
5. A team member invokes the `Close incident` quick command.
6. The app:
   - Lists messages in the Chat space.
   - Sends the conversation to Vertex AI for summarization.
   - Creates a Google Docs document using `DocumentApp`.
   - Posts a Chat message linking to the document.

---

# Environment Setup

## 1. Create a Google Cloud Project

### Using Google API Console

Go to:

```text
Menu > IAM & Admin > Create a Project
```

Then:

1. Enter a descriptive project name.
2. Optionally edit the project ID.
   - The project ID cannot be changed after creation.
3. Select a location.
4. Click **Create**.

### Using gcloud CLI

```bash
gcloud projects create PROJECT_ID
```

Replace `PROJECT_ID` with your desired Google Cloud project ID.

---

## 2. Enable Billing

### Using Google API Console

Go to:

```text
Menu > Billing > My Projects
```

Then:

1. Select the organization.
2. Open the project row’s **Actions** menu.
3. Click **Change billing**.
4. Select the Cloud Billing account.
5. Click **Set account**.

### Using gcloud CLI

List billing accounts:

```bash
gcloud billing accounts list
```

Link billing to the project:

```bash
gcloud billing projects link PROJECT_ID --billing-account=BILLING_ACCOUNT_ID
```

Replace:

- `PROJECT_ID` — your Cloud project ID.
- `BILLING_ACCOUNT_ID` — your billing account ID.

---

## 3. Enable APIs

Required APIs:

- Google Chat API
- Google Docs API
- Admin SDK API
- Vertex AI API

### Using gcloud CLI

Set the current project:

```bash
gcloud config set project PROJECT_ID
```

Enable APIs:

```bash
gclou

[... summary truncated for context management ...]
