---
title: "Authenticate as a Google Chat app  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/authenticate-authorize-chat-app"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:16:12Z"
extraction_method: "web_extract"
---

# Authenticate as a Google Chat App — Markdown Summary

**Source:** Google for Developers — Google Chat  
**URL:** https://developers.google.com/workspace/chat/authenticate-authorize-chat-app  
**Last updated:** 2026-04-20 UTC

---

## Purpose

This guide explains how to authenticate a **Google Chat app** using a **service account** so the app can access the **Google Chat API** and perform app-level actions, such as posting a message to a Chat space.

> A service account acts as the Chat app's identity for authentication and interaction with the Google Chat API, requiring a private key for secure access.

The guide walks through:

1. Creating a service account.
2. Generating a private key.
3. Getting administrator approval when required.
4. Installing client libraries.
5. Writing sample code in Java, Python, Node.js, or Apps Script.
6. Running the example.
7. Troubleshooting common errors.

---

## Core Concepts

### Service Account Authentication

A Google Chat app can authenticate to the Chat API using a **service account**. When authenticated this way, the app acts as itself—not as a user.

Important implications:

- The Chat app must be a **member of a Chat space** to access data or perform actions in that space.
- Examples of actions requiring membership:
  - Listing members of a space.
  - Creating a message in a space.
- Exception:
  - If the Chat app creates a space using app authentication, it automatically becomes a member.

### Authorization Scopes

Google Chat API methods support different app authorization scopes.

#### Scope requiring no admin approval

```text
https://www.googleapis.com/auth/chat.bot
```

- Does **not** require additional administrator approval.
- Used by the examples in this guide.

#### Scopes requiring one-time administrator approval

```text
https://www.googleapis.com/auth/chat.app.*
```

- Any scope beginning with this prefix requires one-time Google Workspace administrator approval.

---

## When to Authenticate as a User Instead

If the Chat app needs to:

- Access user data.
- Perform actions on behalf of a user.

Then it should use **user authentication** instead of service account authentication.

For domain administrators, Google supports **domain-wide delegation**, allowing a service account to access users’ data without each user consenting individually.

Related guides:

- Authenticate as a user.
- Authenticate and authorize using domain-wide delegation.
- Types of required authentication in the Chat API authentication overview.

---

## Prerequisites

Prerequisites vary by language.

### Common Prerequisites

For all implementations:

- A Google Chat app that receives and responds to **interaction events**.
- The Chat app must be added to a Chat space.

To create an interactive Chat app:

- For HTTP service apps, complete the Google Chat quickstart.
- For Apps Script apps, complete the Apps Script Chat app quickstart.

To test/add the app:

- Use the guide for testing interactive features for Google Chat apps.

---

### Java Prerequisites

- JDK 1.7 or greater.
- Maven.
- An initialized Maven project.

Create a Maven project:

```bash
mvn archetype:generate -DgroupId=com.google.chat.app.authsample -DartifactId=auth-sample-app -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false
```

---

### Python Prerequisites

- Python 3.6 or greater.
- `pip`.

---

### Node.js Prerequisites

- Node.js 14 or greater.
- `npm`.
- An initialized Node.js project.

Initialize a Node.js project:

```bash
npm init
```

---

### Apps Script Prerequisites

- A Google Chat app built in Apps Script.
- The app added to a Chat space.

---

## Step 1: Create a Service Account

Create a service account that the Chat app can use to access Google APIs.

---

### Option A: Google Cloud Console

1. In Google Cloud Console, go to:

   **IAM & Admin > Service Accounts**

2. Click **Create service account**.
3. Fill in service account details.
4. Click **Create and continue**.
5. Optional: assign roles to grant access to Google Cloud project resources.
6. Click **Continue**.
7. Optional: enter users or groups that can manage or perform actions with this service account.
8. Click **Done**.
9. Save the service account email address.

---

### Option B: gcloud CLI

Create the service account:

```bash
gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
     --display-name="SERVICE_ACCOUNT_NAME"
```

Optional: assign roles to grant access to Google Cloud project resources.

---

## Step 1b: Create a Private Key

After creating the service account, generate a JSON private key.

Steps:

1. In Google Cloud Console, go to:

   **IAM & Admin > Service Accounts**

2. Select the service account.
3. Click:

   **Keys > Add key > Create new key**

4. Select **JSON**.
5. Click **Create**.
6. Save the downloaded JSON file as:

```text
credentials.json
```

7. Place it in your working directory.

Important security note:

> This file is the only copy of this key.


[... summary truncated for context management ...]
