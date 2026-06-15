---
title: "Manage projects with Google Chat, Vertex AI, and Firestore  |  Google Workspace add-ons  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/tutorial-project-management"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:09:18Z"
extraction_method: "web_extract"
---

# Manage Projects with Google Chat, Vertex AI, and Firestore — Summary

**Source:** Google for Developers — Google Workspace add-ons  
**URL:** https://developers.google.com/workspace/chat/tutorial-project-management  
**Last updated:** 2026-04-20 UTC

---

## Overview

This tutorial explains how to build a **Google Chat app** that helps teams manage agile software projects in real time.

The app lets users create and manage **user stories** directly from Google Chat. It uses:

- **Google Chat API** to receive messages, mentions, slash commands, and card interactions.
- **Vertex AI** to generate, expand, regenerate, and correct user story descriptions.
- **Firestore** to persist spaces, users, and user stories.
- **Cloud Functions** to host the app’s HTTP endpoint and business logic.

The app supports collaboration in Chat spaces by letting users:

- Create user stories.
- Edit story details.
- Assign stories.
- Set story status, priority, and size.
- Manage all user stories in a space.
- Delete user stories.

---

## Example User Flow

The tutorial illustrates the app with the following flow:

1. A user mentions the project management Chat app in a Chat space.
2. The app offers help.
3. The user runs:

```text
/createUserStory
```

4. Vertex AI generates a story title and description.
5. The story is shared in the Chat space as a card.
6. The user clicks **Edit** to finalize details.
7. The user can click **Expand** to have Vertex AI add requirements to the description.
8. The user assigns the story, sets status, priority, and size, then clicks **Save**.
9. At any time, users can manage stories with:

```text
/manageUserStories
```

---

## Prerequisites

You need:

- A **Business or Enterprise Google Workspace account** with access to **Google Chat**.
- Access to Google Cloud services that allow you to:
  - Create a Google Cloud project.
  - Link a Cloud Billing account.
  - Use unauthenticated Google Cloud Function invocations.
- If using the Google Cloud CLI:
  - A Node.js development environment configured to work with `gcloud`.

If needed, ask a Google Cloud administrator for access or permissions.

---

## Objectives

By completing the tutorial, you build a Chat app that can:

- Manage agile software projects.
- Use Vertex AI for AI-assisted user story writing:
  - Generate story descriptions.
  - Regenerate story descriptions.
  - Expand notes into complete requirements.
  - Correct grammar and typos.
- Read and write project data in Firestore.
- Let users create, edit, assign, start, and manage stories directly from Chat conversations.

---

## Products Used

### Google Workspace / Google Cloud Services

| Product | Role in the App |
|---|---|
| **Chat API** | Receives and responds to Chat interaction events such as messages, mentions, slash commands, and card clicks. Also configures app name, avatar, visibility, and commands. |
| **Vertex AI API** | Generates user story titles and descriptions. |
| **Firestore** | Stores spaces, users, and user stories. |
| **Cloud Functions** | Hosts the HTTP endpoint that receives Chat events and runs app logic. |

### Cloud Functions Dependencies

Cloud Functions uses:

- **Cloud Build** — builds and deploys functions.
- **Pub/Sub** — asynchronous messaging used by Cloud Functions infrastructure.
- **Cloud Run Admin API** — manages containerized function runtime resources.

---

## Architecture

The app receives Chat interaction events through an HTTP endpoint hosted by Cloud Functions.

### Flow

1. A user invokes the Chat app by:
   - Direct messaging it.
   - Mentioning it in a space.
   - Entering a slash command.
2. Google Chat sends a synchronous HTTP request to the Cloud Function endpoint.
3. The app processes the request:
   - Vertex AI writes or updates a user story.
   - Firestore stores, retrieves, updates, or deletes user story data.
4. Cloud Functions returns an HTTP response to Google Chat.
5. Chat displays the response as a message, card, dialog, or other interaction.

---

## Prepare the Environment

You must create and configure a Google Cloud project.

---

## Create a Google Cloud Project

### Using Google API Console

1. Go to **IAM & Admin > Create a Project**.
2. Enter a project name.
3. Optionally edit the project ID.
   - The project ID cannot be changed after project creation.
4. Choose a location.
5. Click **Create**.

### Using `gcloud`

```bash
gcloud projects create PROJECT_ID
```

Replace `PROJECT_ID` with the desired project ID.

---

## Enable Billing

### Using Google API Console

1. Go to **Billing > My Projects**.
2. Select the organization.
3. In the project row, open **Actions > Change billing**.
4. Choose a Cloud Billing account.
5. Click **Set account**.

### Using `gcloud`

List billing accounts:

```bash
gcloud billing accounts list
```

Link a billing account:

```bash
gcloud billing projects link PROJECT_ID --billing-account=BILLING_ACCOUNT_ID
```

Replace:

- `PROJECT_ID` — your Google Cloud project ID.
- `BILLING_ACC

[... summary truncated for context management ...]
