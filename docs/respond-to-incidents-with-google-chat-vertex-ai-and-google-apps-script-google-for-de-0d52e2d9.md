---
title: "Respond to incidents with Google Chat, Vertex AI, and Google Apps Script  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/tutorial-incident-response-app-auth"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:09:18Z"
extraction_method: "web_extract"
---

# Respond to Incidents with Google Chat, Vertex AI, and Google Apps Script — Summary

**Source:** Google for Developers — Google Chat tutorial  
**URL:** https://developers.google.com/workspace/chat/tutorial-incident-response-app-auth  
**Last updated:** 2026-04-20 UTC

---

## Overview

This tutorial explains how to build a **Google Chat incident response app** using:

- **Google Chat API**
- **Vertex AI**
- **Google Apps Script**
- **Google Docs API**
- **Admin SDK Directory API**
- **Google Workspace Marketplace SDK**

The app responds to incidents in real time by:

- Creating a dedicated Google Chat space for an incident.
- Adding incident responders to the space.
- Posting an initial incident summary.
- Supporting collaboration using Chat messages, slash commands, and dialogs.
- Using **Vertex AI** to summarize the incident discussion.
- Creating a **Google Docs post-mortem** containing the resolution, summary, and full Chat history.
- Sharing the generated document back into the Chat space.

> This tutorial uses authorization scopes that begins with  
> `https://www.googleapis.com/auth/chat.app.*`.  
> For the Chat app to use those scopes, you must get a one-time administrator approval.

---

## Incident Definition and Example Scenarios

An **incident** is an event requiring immediate team attention.

Examples include:

- A time-sensitive CRM case requiring service team collaboration.
- A system outage requiring SREs to coordinate recovery.
- A high-magnitude earthquake requiring emergency response coordination.

For this tutorial, incidents are initiated from a simulated external web page where users enter:

- Incident title
- Incident description / initial message
- Email addresses of responders

---

## App Flow

The tutorial demonstrates the app through these UI stages:

1. Website where someone reports an incident.
2. Notification that the incident Chat space is created.
3. Incident response Chat space.
4. Resolving the incident with a slash command.
5. Incident resolution dialog.
6. Google Docs post-mortem shared in the space.
7. AI-generated incident summary in the Google Doc.

---

## Prerequisites

If these are not enabled, a Google Workspace administrator must enable them.

### Required Account and Services

- A **Business or Enterprise Google Workspace account**
- Access to **Google Chat**
- **Directory/contact sharing** enabled for Google Workspace

### User Requirements

Incident responders must:

- Be users in the same Google Workspace organization.
- Have Google Chat accounts.

The app uses the Directory API to look up responder information such as:

- Name
- Email address
- User ID

---

## Objectives

The tutorial’s goals are to build a Chat app that:

- Responds to incidents.
- Creates incident response spaces.
- Posts incident and response messages.
- Uses interactive Chat app features.
- Summarizes conversations and resolutions with **Vertex AI**.

---

## Architecture

The app uses both Google Workspace and Google Cloud resources.

### High-Level Architecture Flow

1. A user starts an incident from an external website hosted on Apps Script.
2. The website sends an asynchronous HTTP request to the Chat app, also hosted on Apps Script.
3. The Chat app processes the request:
   - Uses Apps Script Admin SDK service to get team member info.
   - Uses Chat API through Apps Script Advanced Chat service to:
     - Create a Chat space.
     - Add team members.
     - Send an incident message.
4. Team members discuss the incident in the Chat space.
5. A team member invokes the `/closeIncident` slash command.
6. The app:
   - Lists all Chat messages in the space.
   - Sends the messages to Vertex AI.
   - Generates a summary.
   - Creates a Google Docs document using Apps Script `DocumentApp`.
   - Posts the document link back to the Chat space.

---

## Prepare the Environment

### 1. Create a Google Cloud Project

You can create the project using either the Google API Console or `gcloud`.

#### Using `gcloud`

```bash
gcloud projects create PROJECT_ID
```

Replace `PROJECT_ID` with the desired project ID.

---

### 2. Enable Billing

#### List billing accounts

```bash
gcloud billing accounts list
```

#### Link billing account to project

```bash
gcloud billing projects link PROJECT_ID --billing-account=BILLING_ACCOUNT_ID
```

Replace:

- `PROJECT_ID` — your Google Cloud project ID.
- `BILLING_ACCOUNT_ID` — the billing account ID to link.

---

### 3. Enable Required APIs

Enable the following APIs:

- Google Chat API
- Google Docs API
- Admin SDK API
- Google Workspace Marketplace SDK
- Vertex AI API

#### Using `gcloud`

Set current project:

```bash
gcloud config set project PROJECT_ID
```

Enable APIs:

```bash
gcloud services enable chat.googleapis.com docs.googleapis.com admin.googleapis.com aiplatform.googleapis.com appsmarket-component.googleapis.com
```

---

## Authentication and Authorization

The app uses different credentials depending on the API:

| API / Service | Credentia

[... summary truncated for context management ...]
