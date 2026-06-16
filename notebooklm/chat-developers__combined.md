---
title: "Combined source: chat-developers"
product_area: "chat-developers"
source_count: 26
generated_at: "2026-06-16T08:47:02Z"
source_type: "coverage_merged_official_extracts"
---

# Combined source: chat-developers

This file merges 26 official extracted source document(s) from coverage area `chat-developers` for NotebookLM import limits.
No synthetic documentation is added; each section preserves the source URL and extracted Markdown body.

## Source index

1. Answer questions based on Chat conversations with a Gemini AI Chat app  |  Google Workspace add-ons  |  Google for Developers — https://developers.google.com/workspace/chat/tutorial-ai-knowledge-assistant
2. Authenticate and authorize Chat apps and Google Chat API requests  |  Google for Developers — https://developers.google.com/workspace/chat/authenticate-authorize
3. Authenticate as a Google Chat app  |  Google for Developers — https://developers.google.com/workspace/chat/authenticate-authorize-chat-app
4. Build a Dialogflow CX Google Chat app that understands and responds with natural language  |  Google for Developers — https://developers.google.com/workspace/chat/build-dialogflow-chat-app-natural-language
5. Build a Google Chat app as a webhook  |  Google for Developers — https://developers.google.com/workspace/chat/quickstart/webhooks
6. Build a Google Chat app behind a firewall with Pub/Sub  |  Google for Developers — https://developers.google.com/workspace/chat/quickstart/pub-sub
7. Build a Google Chat app with Google Apps Script  |  Google for Developers — https://developers.google.com/workspace/chat/quickstart/apps-script-app
8. Build an HTTP Google Chat app  |  Google for Developers — https://developers.google.com/workspace/chat/quickstart/gcf-app
9. Build an interactive Google Chat app  |  Google for Developers — https://developers.google.com/workspace/chat/interact-users-overview
10. Choose a Google Chat app architecture  |  Google for Developers — https://developers.google.com/workspace/chat/structure
11. Configure the Chat MCP server  |  Google Chat  |  Google for Developers — https://developers.google.com/workspace/chat/api/guides/configure-mcp-server
12. Develop with Google Chat  |  Google for Developers — https://developers.google.com/workspace/chat/overview
13. Google Apps Script quickstart  |  Google Chat  |  Google for Developers — https://developers.google.com/workspace/chat/api/guides/quickstart/apps-script
14. Google Chat app samples  |  Google for Developers — https://developers.google.com/workspace/chat/samples
15. Manage projects with Google Chat, Vertex AI, and Firestore  |  Google Workspace add-ons  |  Google for Developers — https://developers.google.com/workspace/chat/tutorial-project-management
16. MCP Reference: chatmcp.googleapis.com  |  Google Chat  |  Google for Developers — https://developers.google.com/workspace/chat/api/reference/mcp
17. Method: spaces.messages.create  |  Google Chat  |  Google for Developers — https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages/create
18. Receive and respond to interaction events  |  Google Chat  |  Google for Developers — https://developers.google.com/workspace/chat/interaction-events
19. Receive and respond to interaction events  |  Google Chat  |  Google for Developers — https://developers.google.com/workspace/chat/receive-respond-interactions
20. Respond to Google Chat app commands  |  Google for Developers — https://developers.google.com/workspace/chat/commands
21. Respond to Google Chat app commands  |  Google for Developers — https://developers.google.com/workspace/chat/slash-commands
22. Respond to incidents with Google Chat, Vertex AI, and Google Apps Script  |  Google for Developers — https://developers.google.com/workspace/chat/tutorial-incident-response-app-auth
23. Respond to incidents with Google Chat, Vertex AI, Apps Script, and user authentication  |  Google Workspace add-ons  |  Google for Developers — https://developers.google.com/workspace/chat/tutorial-incident-response
24. Send a message using the Google Chat API  |  Google for Developers — https://developers.google.com/workspace/chat/create-messages
25. Usage limits  |  Google Chat  |  Google for Developers — https://developers.google.com/workspace/chat/limits
26. Verify requests from Google Chat  |  Google for Developers — https://developers.google.com/workspace/chat/verify-requests-from-chat

---

## Source 1: Answer questions based on Chat conversations with a Gemini AI Chat app  |  Google Workspace add-ons  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/tutorial-ai-knowledge-assistant
- Original file: `docs/answer-questions-based-on-chat-conversations-with-a-gemini-ai-chat-app-google-worksp-a2ad9b9e.md`
- Product area: `chat-developers`

# Summary: Answer Questions Based on Chat Conversations with a Gemini AI Chat App

**Source:** Google Developers — Google Workspace add-ons  
**URL:** https://developers.google.com/workspace/chat/tutorial-ai-knowledge-assistant  
**Last updated:** 2026-05-29 UTC

---

## Overview

This tutorial explains how to build a **Google Chat app** called **AI knowledge assistant** that uses **Vertex AI with Gemini** to answer questions based on the conversation history of Google Chat spaces.

The app:

- Uses **Chat space messages as a knowledge base**.
- Detects questions posted in spaces **in real time**, even when the app is **not mentioned**.
- Uses **Gemini via Vertex AI** to decide whether a message is a question and answer it from prior space history.
- Stores and retrieves messages using **Firestore**.
- Uses the **Google Workspace Events API** and **Pub/Sub** to receive live Chat events.
- Uses **Cloud Functions** to run the app logic.

> “The Chat app uses all the messages sent in the space as a data source and knowledge base: when someone asks a question, the Chat app checks for previously shared answers and then shares one.”

If Gemini cannot find an answer in the space history, the app posts that it can’t answer.

---

## Example Scenario

In an employee onboarding/support Chat space:

1. A user adds the **AI knowledge assistant** Chat app to the space.
2. Another user asks a question, such as whether the company offers public speaking training.
3. The Chat app prompts **Vertex AI with Gemini** using the space’s conversation history.
4. The app posts an answer back into the space.

---

## Prerequisites

You need:

- A **Business or Enterprise Google Workspace account** with access to **Google Chat**.
- Access to Google Cloud services to:
  - Create a Google Cloud project.
  - Link a Cloud Billing account.
  - Use **unauthenticated Google Cloud Function invocations**.
- If using the Google Cloud CLI:
  - A Node.js development environment configured for `gcloud`.

If permissions are missing, ask a Google Cloud administrator for access.

---

## Objectives

By the end of the tutorial, you build a Chat app that can:

- Use generative AI to answer questions from Chat space conversations.
- Detect and answer employee questions.
- Continuously learn from ongoing Chat conversations.
- Listen and respond to Chat messages in real time, even without direct mentions.
- Persist Chat messages in Firestore.
- Mention or involve space managers when no answer is found.

---

## Architecture

The app uses both **Google Workspace** and **Google Cloud** services.

### Main Flow: App Added to a Space

When a user adds the app to a Chat space:

1. The app prompts the user to configure authentication and authorization.
2. The app calls the Chat API method:

   ```text
   spaces.messages.list
   ```

   to fetch existing space messages.
3. The app stores fetched messages in Firestore.
4. The app calls the Google Workspace Events API method:

   ```text
   subscriptions.create
   ```

   to subscribe to space events.
5. The subscription sends notifications to a Pub/Sub topic.
6. Eventarc forwards Pub/Sub events to the app.
7. The app posts an introduction message to the Chat space.

### Main Flow: User Posts a Message

When a message is posted:

1. The app receives the message in real time from Pub/Sub.
2. The message is added to Firestore.
3. If a message is edited or deleted, Firestore is updated accordingly.
4. The app sends the message and space history to **Vertex AI with Gemini**.
5. Gemini determines whether the message includes a question.
6. If it is a question:
   - Gemini tries to answer using the Firestore conversation history.
   - The app posts the answer using:

     ```text
     spaces.messages.create
     ```

7. If Gemini cannot answer, the app posts that it can’t find an answer in the space history.
8. If the message is not a question, the app does not respond.

### Subscription Lifecycle

When the Google Workspace Events API subscription is near expiration:

- The app renews it using:

  ```text
  subscriptions.patch
  ```

When the app is removed from a Chat space:

1. The app deletes the subscription using:

   ```text
   subscriptions.delete
   ```

2. The app deletes that space’s data from Firestore.

---

## Products and Services Used

### Vertex AI API with Gemini

Used to:

- Recognize questions.
- Understand message context.
- Generate answers from Chat history.

### Google Chat API

Used to:

- Receive and respond to Chat interaction events.
- List messages in a space.
- Post responses.
- Configure app metadata such as name and avatar.

### Google Workspace Events API

Used to:

- Subscribe to Chat space events.
- Receive message events even when the app is not mentioned.

### Firestore

Used to:

- Store Chat space messages.
- Retrieve conversation history for Gemini prompts.

### Pub/Sub

Used as the notification endpoint for Workspace Events API subscriptions.

### Eventarc

Used to route Pub/Sub

[... summary truncated for context management ...]

---

## Source 2: Authenticate and authorize Chat apps and Google Chat API requests  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/authenticate-authorize
- Original file: `docs/authenticate-and-authorize-chat-apps-and-google-chat-api-requests-google-for-develop-698eead9.md`
- Product area: `chat-developers`

# Authenticate and authorize Chat apps and Google Chat API requests — Summary

**Source:** Google for Developers — Google Chat  
**URL:** https://developers.google.com/workspace/chat/authenticate-authorize  
**Last updated:** 2026-06-03 UTC

---

## Core idea

Google Chat apps use **authentication** to verify identity and **authorization** to determine access to Google Chat resources.

Chat apps can authenticate in two main ways:

- **User authentication** — the app acts on behalf of a user and usually requires OAuth consent.
- **App authentication** — the app acts as itself using a **service account**.

> Google Chat apps can use either user or app authentication to interact with the Chat API.

---

## Authentication & authorization process overview

High-level flow for Google Chat API access:

1. **Configure a Google Cloud project**
   - Create a Google Cloud project.
   - Enable the **Google Chat API**.
   - Configure the Chat app.
   - Set up authentication.

2. **Call the Chat API**
   - The app sends credentials with API requests.
   - Service account credentials are included by the app.
   - User authentication may prompt the user to sign in.

3. **Request resources**
   - The app requests access using OAuth **scopes**.

4. **Ask for consent**
   - For user authentication, Google shows an OAuth consent screen.
   - Service account authentication doesn’t require end-user consent.

5. **Send approved request**
   - Credentials and approved scopes are sent to Google’s authorization server.

6. **Receive access token**
   - Google returns an access token containing granted scopes.
   - If fewer scopes are granted than requested, the app should disable features requiring missing scopes.

7. **Access resources**
   - The app uses the access token to call the Chat API.

8. **Optional refresh token**
   - Apps needing access beyond one access token lifetime can request a refresh token.

9. **Request more resources later**
   - If more access is needed, request additional scopes and repeat consent/token flow.

---

## When Chat apps require authentication

Chat apps can send messages:

- **Synchronously**, in direct response to user interaction.
- **Asynchronously**, by making Chat API calls independently.

### No authentication required: synchronous interaction responses

Chat apps **don’t need authentication** to receive and respond synchronously to interaction events, unless they call the Chat API or another Google API while processing the response.

Interaction events include:

- A user sends a message to a Chat app.
- A user `@mentions` a Chat app.
- A user invokes one of the app’s commands.

Typical sequence:

1. User sends a message to the Chat app.
2. Google Chat forwards the message to the app.
3. The app processes it and returns a response.
4. Google Chat renders the response.

> Google Chat apps don't need to authenticate as a user or Chat app to receive and respond synchronously to interaction events.

### Authentication required: asynchronous messages and tasks

Asynchronous operations require authentication and authorization because they call the Chat API.

Examples:

- Create a Chat space for an incident.
- Add people to a Chat space.
- Post a message to a Chat space.
- Access or modify Chat resources on a user’s behalf.

Example asynchronous flow:

1. Chat app calls `spaces.messages.create`.
2. The request includes user or service account credentials.
3. Google Chat authenticates the request.
4. Google Chat renders the app’s message in the target space.

---

## OAuth scopes

OAuth scopes define:

- Which Google Workspace app is accessed.
- What data is accessed.
- What level of access is granted.

> An authorization scope is an OAuth 2.0 URI string that contains the Google Workspace app name, what kind of data it accesses, and the level of access.

Apps should configure the OAuth consent screen and choose scopes before publication.

---

## Scope sensitivity levels

### Non-sensitive scopes

Require only basic app verification.

| Scope | Description |
|---|---|
| `https://www.googleapis.com/auth/chat.bot` | Lets Chat apps view chats and send messages. Supports **app authentication only** with service accounts. Cannot be used with user credentials or domain-wide delegation. |

---

### Sensitive scopes

Sensitive scopes provide access to specific user Google data and require additional app verification.

| Scope | Description |
|---|---|
| `https://www.googleapis.com/auth/chat.spaces` | Create conversations and spaces and see or edit metadata, including history and access settings. |
| `https://www.googleapis.com/auth/chat.spaces.create` | Create new conversations in Chat. |
| `https://www.googleapis.com/auth/chat.spaces.readonly` | View chat and spaces. |
| `https://www.googleapis.com/auth/chat.memberships` | View, add, update, and remove members from Chat conversations. |
| `https://www.googleapis.com/auth/chat.memberships.app` | Add and remove itself from conversations. |
| `https://www.go

[... summary truncated for context management ...]

---

## Source 3: Authenticate as a Google Chat app  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/authenticate-authorize-chat-app
- Original file: `docs/authenticate-as-a-google-chat-app-google-for-developers-dbf2c861.md`
- Product area: `chat-developers`

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

---

## Source 4: Build a Dialogflow CX Google Chat app that understands and responds with natural language  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/build-dialogflow-chat-app-natural-language
- Original file: `docs/build-a-dialogflow-cx-google-chat-app-that-understands-and-responds-with-natural-lan-f2b4ca13.md`
- Product area: `chat-developers`

# Build a Dialogflow CX Google Chat App That Understands and Responds with Natural Language

**Source:** Google for Developers — Google Workspace Chat  
**URL:** https://developers.google.com/workspace/chat/build-dialogflow-chat-app-natural-language  
**Last updated:** 2026-04-20 UTC

---

## Overview

This guide explains how to build a **Google Chat app** that uses **Dialogflow CX** to understand and respond to users in natural language.

Dialogflow CX has a **direct integration with Google Chat**, letting users message a Chat app while Dialogflow handles conversation logic, intent detection, parameter extraction, and responses.

> This page explains how to build a Google Chat app that can both understand and respond with natural language using Dialogflow.

A typical use case is a **car rental assistant**:

> A user might write, "I'd like to rent a car". The Chat app might respond with a question like "Where would you like to pick up the vehicle?"

Dialogflow Chat apps are useful for natural-language workflows such as:

- Booking flights
- Scheduling doctor appointments
- Ordering food delivery
- Answering retail product catalog questions, such as whether items are available in other colors

Dialogflow provides **prebuilt agents** to help you start quickly, including the guide’s example agent: **Travel: car rental**.

---

## Objectives

By the end of the guide, you can:

- Set up the required Google Cloud environment.
- Create and deploy a **Dialogflow CX agent**.
- Create and deploy a **Google Chat app** powered by that agent.
- Test the Chat app in Google Chat.

---

## Prerequisites

You need:

- A **Business or Enterprise Google Workspace account** with access to **Google Chat**.
- A **Google Cloud project with billing enabled**.

Useful references:

- Verify billing status of projects
- Create a Google Cloud project

---

## Architecture

A Dialogflow-powered Google Chat app follows this flow:

1. A user sends a message to the Chat app in:
   - A direct message, or
   - A Chat space
2. A **Dialogflow virtual agent** in Google Cloud receives and processes the message.
3. Optionally, the Dialogflow agent uses a **Dialogflow webhook** to interact with external systems, such as:
   - Project management tools
   - Ticketing systems
   - Other third-party services
4. Dialogflow sends a response back to the Chat app service.
5. The response is delivered to the Chat space.

Key architectural point:

> The Dialogflow agent and the Chat app must be set up in the same Google Cloud project when using the direct Dialogflow CX integration with Chat.

If they must be in different projects, use an intermediate server. Google provides a GitHub example: **Chat integration for Dialogflow CX**.

---

## Set Up the Environment

Before using the app, enable the required APIs in your Google Cloud project:

- **Google Chat API**
- **Dialogflow API**

Steps:

1. Open the API enablement flow in Google Cloud Console.
2. Confirm the correct Cloud project.
3. Confirm the APIs.
4. Click **Enable**.

---

## Create a Dialogflow CX Agent

A **Dialogflow CX agent** is a virtual agent that handles conversations with end users.

Key concept:

> Dialogflow translates end-user text during a conversation to structured data that your apps and services can understand.

Dialogflow agents are trained like human call center agents: they are designed to handle expected conversation scenarios without requiring every user phrase to be explicitly scripted.

---

### Agent Creation Options

You can either:

1. Use a **prebuilt agent**, recommended for quick testing.
2. Create your own agent.

For this guide, Google recommends selecting the prebuilt agent:

> **Travel: car rental**

Prebuilt agents are rated:

- Beginner
- Intermediate
- Advanced

Advanced or intermediate agents may require extra configuration, features, or API enablement.

---

### Create a Prebuilt Agent

Steps:

1. Open the **Dialogflow CX Console**.
2. Select your Google Cloud project.
3. Click **Use prebuilt agents**.
4. Select **Travel: car rental**.
5. Click **Import as agent**.

---

### Create Your Own Agent

Steps:

1. Click **Create agent**.
2. Choose one of:
   - **Auto-generate** to create a **data store agent**
   - **Build your own** to create other agent types

Basic settings:

- **Display name**
- **Location**
- **Time zone**
- **Default language**

Important constraint:

> You can't change the default language for an agent after creation.

Click **Create**. Dialogflow CX creates the agent and displays its **default start flow**.

---

### Test the Dialogflow CX Agent

Recommended best practice: test the agent before connecting it to Chat.

Steps:

1. Click **Test agent**.
2. Select **Test agent in environment**.
3. Set:
   - **Environment:** `Draft`
   - **Flow:** `Default Start Flow`
   - **Page:** `Start Page`
4. In the **Talk to agent** compose bar, type:

```text
Hello
```

5. Press **Enter**.
6. The agent should introduce itself.
7. Continue with the sample t

[... summary truncated for context management ...]

---

## Source 5: Build a Google Chat app as a webhook  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/quickstart/webhooks
- Original file: `docs/build-a-google-chat-app-as-a-webhook-google-for-developers-f2d523bb.md`
- Product area: `chat-developers`

# Build a Google Chat App as a Webhook — Comprehensive Summary

**Source:** Google for Developers — <https://developers.google.com/workspace/chat/quickstart/webhooks>  
**Last updated:** 2026-04-20 UTC

---

## Overview

Incoming webhooks let external services send **asynchronous, one-way notifications** into a specific Google Chat space using standard HTTP requests.

> “Webhooks provide a way for external services to send asynchronous, one-way notifications to Google Chat spaces.”

Typical use case:

- A monitoring system detects a server outage.
- It sends a `POST` request to a Google Chat webhook URL.
- A message appears in a Chat space for on-call staff.

For synchronous or interactive Chat apps, use the Google Chat API guide to [Send a message](https://developers.google.com/workspace/chat/api/guides/v1/messages/create) or build a full [Chat app](https://developers.google.com/workspace/chat/quickstart/gcf-app).

---

## Important Characteristics

Webhooks are **not conversational**.

They:

- Send messages into Chat spaces.
- Use standard HTTP `POST` requests.
- Work only in the Chat space where they’re registered.
- Can start or reply to message threads using `threadKey`.
- Can work in direct messages only when all users have Chat apps enabled.

They **cannot**:

- Receive messages from users.
- Respond to user messages.
- Receive Chat app interaction events.
- Be published to the Google Workspace Marketplace.

> “With this type of architecture design, users can't interact with the webhook or the connected external application because communication is one-way.”

> “Webhooks aren't conversational. They can't respond to or receive messages from users or Chat app interaction events.”

---

## Architecture Flow

A webhook-based Chat app follows this flow:

1. External third-party service triggers logic, such as:
   - Project management system
   - Ticketing tool
   - Monitoring application
2. Hosted app logic runs in:
   - Cloud infrastructure, or
   - On-premises systems
3. The app sends a message using a webhook URL to a specific Chat space.
4. Users receive the message in that Chat space but cannot interact with the webhook app.

---

## Prerequisites

Common prerequisites for all implementations:

- A **Business or Enterprise Google Workspace account** with access to Google Chat.
- The Google Workspace organization must allow users to **add and use incoming webhooks**.
- A Google Chat space.
  - Can be created via the Google Chat API or directly in Chat.

Language-specific prerequisites:

### Node.js

- Node.js 14 or greater
- npm

### Python

- Python 3.6 or greater
- pip
- `httplib2` library

Install `httplib2`:

```bash
pip install httplib2
```

### Java

- Java 11 or greater
- Maven

### Apps Script

- A standalone Apps Script project
- Advanced Chat Service enabled

---

# Creating a Webhook

Creating a webhook involves two main steps:

1. Register the incoming webhook in a Chat space.
2. Write and run a script that sends a message to the webhook URL.

---

## Register the Incoming Webhook

1. Open [Google Chat](https://chat.google.com/) in a browser.
   - Webhooks are **not configurable from the Chat mobile app**.
2. Go to the space where you want to add the webhook.
3. Next to the space title, click the expand arrow.
4. Click **Apps & integrations**.
5. Click **Add webhooks**.
6. In the **Name** field, enter:

```text
Quickstart Webhook
```

7. In the **Avatar URL** field, enter:

```text
https://developers.google.com/chat/images/chat-product-icon.png
```

8. Click **Save**.
9. To copy the webhook URL:
   - Click **More**
   - Click **Copy link**

---

## Webhook URL Security

The webhook URL contains two important parameters:

- `key` — a common value shared between webhooks.
- `token` — a unique secret value.

> “The webhook URL contains two parameters: `key`, a common value shared between webhooks, and `token` which is a unique value that must be kept secret to preserve the security of your webhook.”

Keep the webhook URL private.

---

# Sending a Message with a Webhook

The webhook script sends a `POST` request to the webhook URL.

The request:

- Uses `Content-Type: application/json; charset=UTF-8`
- Sends a JSON body containing the Chat message
- Receives a Google Chat API `Message` response

---

## Basic Node.js Example

```javascript
/**
    * Sends asynchronous message to Google Chat
    * @return {Object} response
    */
async function webhook() {
     const url = "https://chat.googleapis.com/v1/spaces/SPACE_ID/messages?key=KEY&token=TOKEN"
     const res = await fetch(url, {
       method: "POST",
       headers: {"Content-Type": "application/json; charset=UTF-8"},
       body: JSON.stringify({
         text: "Hello from a Node script!"
       })
     });
     return await res.json();
}

webhook().then(res => console.log(res));
```

Replace the `url` value with the copied webhook URL.

Run:

```bash
node index.js
```

---

## Basic Python Example

```python
from json import dumps
fr

[... summary truncated for context management ...]

---

## Source 6: Build a Google Chat app behind a firewall with Pub/Sub  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/quickstart/pub-sub
- Original file: `docs/build-a-google-chat-app-behind-a-firewall-with-pub-sub-google-for-developers-81060285.md`
- Product area: `chat-developers`

# Build a Google Chat App Behind a Firewall with Pub/Sub — Summary

**Source:** Google for Developers — Google Chat quickstart  
**URL:** https://developers.google.com/workspace/chat/quickstart/pub-sub  
**Last updated:** 2026-05-06 UTC

---

## Purpose

This guide explains how to build a **Google Chat app that communicates asynchronously through Google Cloud Pub/Sub**.

This architecture is useful when:

- Your organization has a **firewall** that prevents Google Chat from sending direct HTTP requests to your app.
- Your Chat app uses the **Google Workspace Events API**.
- You want an application server, either cloud-hosted or on-premises, to pull Chat events from Pub/Sub.

---

## Key Architecture

A Pub/Sub-based Chat app works as follows:

1. A user sends a message to the Chat app in:
   - A direct message
   - A Chat space
   - A Chat space where the app has an active subscription

2. Google Chat publishes the event to a **Pub/Sub topic**.

3. Your application server subscribes to the Pub/Sub topic using a **pull subscription**.

4. Your app processes the event and can optionally call the **Google Chat API** to respond asynchronously.

> “This type of architecture for a Chat app is useful if your organization has a firewall, which can prevent Chat from sending messages to your Chat app, or if the Chat app uses the Google Workspace Events API.”

---

## Important Limitations

Because Pub/Sub Chat apps only support **asynchronous messages**, they have these limitations:

- **Dialogs are not supported.**
  - Use a **card message** instead.

- **Individual cards can’t be updated with synchronous responses.**
  - To update content, patch the entire message using the Chat API `patch` method.

> “Can't use dialogs in messages. Instead, use a card message.”

> “Can't update individual cards with a synchronous response. Instead, update the entire message by calling the `patch` method.”

---

## Prerequisites

### Required for All Languages

- A **Business or Enterprise Google Workspace account** with access to Google Chat.
- A **Google Cloud project with billing enabled**.
- The **Google Chat API** and **Pub/Sub API** enabled.
- A service account for your Chat app.
- A Pub/Sub topic and pull subscription.
- The Chat app must **not** be configured as a Google Workspace add-on.

> When configuring the Chat API, clear **Build this Chat app as a Google Workspace add-on**.

### Language-Specific Requirements

#### Node.js

- Node.js 14 or greater
- npm
- Initialized Node.js project:

```bash
npm init
```

#### Python

- Python 3.6 or greater
- pip

#### Java

- Java 11 or greater
- Maven

---

## Set Up the Environment

Enable these APIs in your Google Cloud project:

- **Google Chat API**
- **Pub/Sub API**

Google provides a console shortcut:

```text
https://console.cloud.google.com/flows/enableapi?apiid=chat.googleapis.com,pubsub.googleapis.com
```

---

## Set Up Pub/Sub

Complete these Pub/Sub setup steps:

1. **Create a Pub/Sub topic**
   - Recommended: use **one topic per Chat app**.

2. **Grant Google Chat permission to publish to the topic**
   - Assign the **Pub/Sub Publisher** role to this service account:

```text
chat-api-push@system.gserviceaccount.com
```

3. **Create a service account** for the Chat app.
   - This account authorizes access to Pub/Sub and Google Chat.
   - Save the private key file to your working directory.

4. **Create a pull subscription** to the topic.

5. Assign the **Pub/Sub Subscriber** role on the subscription to the service account you created.

---

## Required Environment Variables

For Node.js, Python, and Java examples, set the following environment variables:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=SERVICE_ACCOUNT_FILE_PATH
```

```bash
export PROJECT_ID=PROJECT_ID
```

```bash
export SUBSCRIPTION_ID=SUBSCRIPTION_ID
```

Where:

- `GOOGLE_APPLICATION_CREDENTIALS` is the path to the service account key file.
- `PROJECT_ID` is your Google Cloud project ID.
- `SUBSCRIPTION_ID` is the Pub/Sub pull subscription ID.

---

## Application Behavior

The sample app listens for Pub/Sub messages and handles Chat events based on their type.

### Event Handling Logic

| Event type | Behavior |
|---|---|
| `MESSAGE` | Responds in the same thread with `You said: <message>` |
| `ADDED_TO_SPACE` with no message | Posts `Thank you for adding me!` |
| `ADDED_TO_SPACE` from an @mention | Falls through to message response behavior |
| `REMOVED_FROM_SPACE` | Does not respond |

Key response text used by the samples:

```text
Thank you for adding me!
```

```text
You said: `<user message>`
```

---

## Node.js Implementation Summary

### `package.json`

Create `package.json` with dependencies for Google Chat and Pub/Sub:

```json
{
     "name": "pub-sub-app",
     "version": "1.0.0",
     "description": "Google Chat App that listens for messages via Cloud Pub/Sub",
     "main": "index.js",
     "scripts": {
       "start": "node index.js",
       "test": "echo \"Error: no test specified\

[... summary truncated for context management ...]

---

## Source 7: Build a Google Chat app with Google Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/quickstart/apps-script-app
- Original file: `docs/build-a-google-chat-app-with-google-apps-script-google-for-developers-e461c690.md`
- Product area: `chat-developers`

# Build a Google Chat App with Google Apps Script — Summary

**Source:** https://developers.google.com/workspace/chat/quickstart/apps-script-app  
**Last updated:** 2026-04-20 UTC  
**Goal:** Create a Google Chat app using **Google Apps Script** that can receive direct messages and echo user messages back.

---

## Key Purpose

This quickstart shows how to build a simple Google Chat app that:

- Can be directly messaged in Google Chat.
- Responds by echoing the user’s message.
- Is implemented with **Google Apps Script**.
- Runs using Google Cloud infrastructure.
- Can optionally integrate with Google Workspace and Google services.

> Create a Google Chat app that you can directly message and that responds by echoing your messages.

---

## Architecture & Message Flow

The app follows this interaction pattern:

1. A user sends a message to the Chat app, either in a direct message or in a Chat space.
2. The Chat app logic, implemented in Apps Script and hosted in Google Cloud, receives and processes the message.
3. Optionally, the app logic can integrate with:
   - Google Workspace services, such as Calendar or Sheets.
   - Other Google services, such as Google Maps or YouTube.
4. The app logic sends a response back to the Chat app service.
5. Google Chat delivers the response to the user.

---

## Objectives

By the end of the guide, you will:

- Set up your environment.
- Set up the Apps Script project.
- Configure the Chat app.
- Test the Chat app.

---

## Prerequisites

You need:

- A **Business or Enterprise Google Workspace account** with access to [Google Chat](https://workspace.google.com/products/chat/).
- A **Google Cloud project**.

Reference:

- [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project)

---

# Setup Steps

---

## 1. Set Up Your Environment

### Open Your Cloud Project

If you already have a Google Cloud project:

1. Go to the **Select a project** page in the Google Cloud console.
2. Select the project you want to use.

If you don’t have one:

1. Click **Create project**.
2. Follow the on-screen instructions.
3. If required, enable billing for the project.

Useful link:

- [Select a Cloud project](https://console.cloud.google.com/projectselector2)

---

### Enable the Google Chat API

Before using Google APIs, enable them in your Google Cloud project.

Action:

- Enable the **Google Chat API** in the Google Cloud console.

Useful link:

- [Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=chat.googleapis.com)

---

## 2. Configure the OAuth Consent Screen

All apps using OAuth 2.0 require a consent screen configuration.

The consent screen:

- Defines what users and app reviewers see.
- Registers the app so it can be published later.

Go to:

- **Google API Console > Google Auth platform > Branding**

Useful link:

- [Go to Branding](https://console.developers.google.com/auth/branding)

---

### OAuth Consent Configuration Steps

If the Google Auth platform is not configured yet, click **Get Started**.

Then configure:

1. Under **App Information**:
   - In **App name**, enter a name for the app.
   - In **User support email**, choose a support email address.

2. Click **Next**.

3. Under **Audience**:
   - Select **Internal**.

4. Click **Next**.

5. Under **Contact Information**:
   - Enter an **Email address** for project notifications.

6. Click **Next**.

7. Under **Finish**:
   - Review the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy).
   - If you agree, select:

> I agree to the Google API Services: User Data Policy

8. Click **Continue**.

9. Click **Create**.

---

### Notes About Scopes and External Apps

For this quickstart, you can skip adding scopes.

Important future consideration:

> In the future, when you create an app for use outside of your Google Workspace organization, you must change the **User type** to **External**. Then add the authorization scopes that your app requires.

Reference:

- [Configure OAuth consent](https://developers.google.com/workspace/guides/configure-oauth-consent)

---

# Set Up the Apps Script Project

---

## Create the Script from the Template

1. Go to the [Apps Script Getting Started page](https://script.google.com/home/start).
2. Click the **Chat App** template.
3. Click **Untitled project**.
4. Rename it:

```text
Quickstart app
```

5. Click **Rename**.

---

### Cloud Project Association Note

For this guide, you **don’t need** to associate your Apps Script project with your Google Cloud project.

However, in the future, you must associate them if you want to:

- Use certain Google APIs.
- Publish your app.

Reference:

- [Google Cloud projects guide](https://developers.google.com/apps-script/guides/cloud-platform-projects)

---

## Create a Test Deployment

You need a deployment ID for the Apps Script project.

Steps:

1. In the Apps Script project, click:

```text
Deploy > Test deployments
```

2. Copy the *

[... summary truncated for context management ...]

---

## Source 8: Build an HTTP Google Chat app  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/quickstart/gcf-app
- Original file: `docs/build-an-http-google-chat-app-google-for-developers-7893fd2b.md`
- Product area: `chat-developers`

# Build an HTTP Google Chat App — Comprehensive Summary

**Source:** Google for Developers — Google Chat quickstart  
**URL:** https://developers.google.com/workspace/chat/quickstart/gcf-app  
**Last updated:** 2026-04-20 UTC

---

## Overview

This guide explains how to build a basic **HTTP Google Chat app** using a **Cloud Run function**. The app responds to user messages in Google Chat with a **card message** that displays the sender’s **display name** and **avatar image**.

> “This page explains how to create an HTTP Chat app.”

The quickstart uses Google Cloud, but the same HTTP architecture can work with:

- Cloud Run
- App Engine
- Other cloud services
- On-premises web servers

The app is implemented as a web service that receives HTTP requests from Google Chat and returns HTTP responses.

---

## What the App Does

The sample app:

- Receives a message from Google Chat.
- Runs a Cloud Run function.
- Responds with:
  - Text: `Here's your avatar`
  - A card titled `Hello <displayName>!`
  - The user’s avatar image
- Supports example app commands:
  - `/about`
  - `Help`

For commands, it replies privately:

```text
The Avatar app replies to Google Chat messages.
```

---

## HTTP Chat App Architecture

A user interaction follows this flow:

1. A user sends a message to the Chat app:
   - In a direct message
   - Or in a Chat space
2. Google Chat sends an **HTTP request** to a web server containing the app logic.
3. The app logic can optionally integrate with:
   - Google Workspace services, such as Calendar and Sheets
   - Google services, such as Maps, YouTube, and Vertex AI
   - External services, such as project management or ticketing tools
4. The web server sends an **HTTP response** back to Google Chat.
5. Google Chat delivers the response to the user.
6. Optionally, the Chat app can call the **Chat API** asynchronously to:
   - Post messages
   - Perform other Chat operations

Key advantage:

> “This architecture provides you the flexibility to use existing libraries and components that already exist in your system because these Chat apps can be designed using different programming languages.”

---

## Objectives

By the end of the guide, you will:

- Set up your Google Cloud environment.
- Create and deploy a Cloud Run function.
- Publish the app to Google Chat.
- Test the app in Google Chat.

---

## Prerequisites

You need:

- A **Business or Enterprise Google Workspace account** with access to Google Chat.
- A **Google Cloud project with billing enabled**.

Useful references:

- Verify billing status:  
  https://cloud.google.com/billing/docs/how-to/verify-billing-enabled
- Create a Google Cloud project:  
  https://developers.google.com/workspace/guides/create-project

---

## Set Up the Environment

Before using Google APIs, enable the required APIs in your Google Cloud project.

Enable these APIs:

- Google Chat API
- Cloud Build API
- Cloud Functions API
- Cloud Pub/Sub API
- Cloud Logging API
- Artifact Registry API
- Cloud Run API

Direct enablement link:

https://console.developers.google.com/flows/enableapi?apiid=chat.googleapis.com,cloudbuild.googleapis.com,cloudfunctions.googleapis.com,pubsub.googleapis.com,logging.googleapis.com,artifactregistry.googleapis.com,run.googleapis.com

---

# Create and Deploy a Cloud Run Function

The function generates a Google Chat card showing the sender’s name and avatar.

Go to Cloud Run:

https://console.developers.google.com/run

Make sure the correct Google Cloud project is selected.

---

## Common Cloud Run Function Setup

For all runtimes:

1. Open the **Cloud Run** page.
2. Click **Write a function**.
3. On the **Create service** page:
   - **Service name:** `quickstartchatapp`
   - **Region:** Select a region
   - **Runtime:** Choose Node.js, Python, or Java
   - **Authentication:** Select **Require authentication**
4. Click **Create**.
5. Wait for Cloud Run to create the service.
6. The console redirects to the **Source** tab.
7. Set the correct entry point for your runtime.
8. Replace the sample source code.
9. Click **Save and redeploy**.

---

## Node.js Implementation

### Entry Point

```text
avatarApp
```

### File

```text
index.js
```

### GitHub Source

https://github.com/googleworkspace/google-chat-samples/blob/main/node/avatar-app/index.js

### Key Node.js Code

```js
const functions = require('@google-cloud/functions-framework');

// Command IDs (configure these in Google Chat API)
const ABOUT_COMMAND_ID = 1; // ID for the "/about" slash command
const HELP_COMMAND_ID = 2; // ID for the "Help" quick command

/**
 * Google Cloud Function that handles HTTP requests from Google Chat.
 *
 * @param {Object} req - The HTTP request object sent from Google Chat.
 * @param {Object} res - The HTTP response object.
 */
functions.http('avatarApp', (req, res) => {
  const event = req.body;

  if (event.appCommandMetadata) {
    handleAppCommands(event, res);
  } else {
    handleRegularMessage(event, res);
  }
});
```

### Command Handli

[... summary truncated for context management ...]

---

## Source 9: Build an interactive Google Chat app  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/interact-users-overview
- Original file: `docs/build-an-interactive-google-chat-app-google-for-developers-1c4d5256.md`
- Product area: `chat-developers`

# Build an Interactive Google Chat App — Summary

**Source:** [Google for Developers: Build an interactive Google Chat app](https://developers.google.com/workspace/chat/interact-users-overview)  
**Last updated:** 2026-04-20 UTC  
**Page purpose:** Provides an overview of frameworks for building an **interactive Google Chat app**.

---

## Core Overview

This page explains how to build Google Chat apps that interact with users, including how users discover them, which development frameworks are available, and where to find configuration, quickstart, and feature-building documentation.

> “This page provides an overview of the frameworks that you can use to build an interactive Google Chat app.”

Related video: [What are Google Chat apps?](https://www.youtube.com/watch?v=lzQ0z3OBTO0) by Google Workspace Developers.

---

## What Interactive Chat Apps Can Do

Interactive Google Chat apps let users:

- Add Chat apps to **Chat spaces** or **direct messages**.
- Send messages to or receive messages from Chat apps.
- Prompt Chat apps with a **command**.
- Preview links from an external service or system.
- Submit information to Chat apps, such as entering text into a **dialog** or **card message**.

---

## How Users Discover and Use Chat Apps

Users can discover and use Chat apps published to the **Google Workspace Marketplace** in several ways:

- Search for and install Chat apps from **Google Chat** or the **Marketplace**.
- Interact with a Chat app that has been added to a Chat space.
- Discover the Chat app in their **direct messages panel** after a Google Workspace administrator installs it on their behalf.

To start using a Chat app, users can:

- Start a direct message with the Chat app.
- Add the Chat app to a space.
- Add the Chat app by **@mentioning** it.

For user-facing instructions, see: [Use Chat apps](https://support.google.com/chat/answer/7655820).

Example described on the page:

> A user can @mention a Chat app to add it to a space.

---

## Choose a Framework for an Interactive Chat App

Google provides two main frameworks for building Chat apps that interact with users.

### 1. Google Workspace Add-on

Use this when you want to extend Google Workspace apps and list your Chat app alongside other app types in the Google Workspace Marketplace.

> **Google Workspace add-on**: Lets you extend other Google Workspace applications and list your Chat app with other types of apps on the Google Workspace Marketplace.

Documentation: [Extend Google Chat](https://developers.google.com/workspace/add-ons/chat)

### 2. Chat API Interaction Event

Use this when you want to build Chat-specific interactive features, including capabilities such as a Chat app homepage.

> **Chat API interaction event**: Lets you build additional features such as a Chat app homepage.

Documentation: [Receive and respond to interaction events](https://developers.google.com/workspace/chat/receive-respond-interactions)

---

## Configure an Interactive Chat App

The page links to framework-specific setup and quickstart documentation for different [Google Chat app architectures](https://developers.google.com/workspace/chat/structure).

| Configuration / Quickstart | Google Workspace Add-on | Chat API Interaction Events |
|---|---|---|
| Configure the Chat API | [Documentation](https://developers.google.com/workspace/add-ons/chat/configure) | [Documentation](https://developers.google.com/workspace/chat/configure-chat-api) |
| Apps Script quickstart | [Documentation](https://developers.google.com/workspace/add-ons/chat/quickstart-apps-script) | [Documentation](https://developers.google.com/workspace/chat/quickstart/apps-script-app) |
| HTTP service quickstart | [Documentation](https://developers.google.com/workspace/add-ons/chat/quickstart-http) | [Documentation](https://developers.google.com/workspace/chat/quickstart/gcf-app) |
| Dialogflow CX quickstart | [Documentation](https://developers.google.com/workspace/add-ons/chat/quickstart-dialogflow-cx) | [Documentation](https://developers.google.com/workspace/chat/build-dialogflow-chat-app-natural-language) |
| Pub/Sub quickstart | [Documentation](https://developers.google.com/workspace/add-ons/chat/quickstart-pubsub) | [Documentation](https://developers.google.com/workspace/chat/quickstart/pub-sub) |

---

## Build Interactive Features

The page maps common Chat app features to the appropriate documentation for each framework.

| Feature | Google Workspace Add-on | Chat API Interaction Events |
|---|---|---|
| Send messages | [Documentation](https://developers.google.com/workspace/add-ons/chat/send-messages) | — |
| Respond to commands | [Documentation](https://developers.google.com/workspace/add-ons/chat/commands) | [Documentation](https://developers.google.com/workspace/chat/commands) |
| Build interactive dialogs | [Documentation](https://developers.google.com/workspace/add-ons/chat/dialogs) | [Documentation](https://developers.google.com/workspace/chat/dialogs) |
| Collect and proce

[... summary truncated for context management ...]

---

## Source 10: Choose a Google Chat app architecture  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/structure
- Original file: `docs/choose-a-google-chat-app-architecture-google-for-developers-58021a27.md`
- Product area: `chat-developers`

# Choose a Google Chat App Architecture — Summary

**Source:** Google for Developers — <https://developers.google.com/workspace/chat/structure>  
**Last updated:** 2026-04-20 UTC

---

## Page Purpose

This guide explains common service architectures for building **Google Chat apps** and helps developers choose the right one based on:

- Target audience: **team**, **organization**, or **public**
- Messaging needs: synchronous, asynchronous, event-driven, or one-way
- User interaction style
- Integration requirements
- Development model: no-code, low-code, or full-code
- DevOps and CI/CD needs
- Whether the app runs behind a firewall

> If you have an existing app that you want to integrate into Google Chat, you can use or adapt your existing implementation.

---

## Key Takeaways

- Google Chat apps can be built with several architectures:
  - **Web or HTTP service**
  - **Pub/Sub**
  - **Webhooks**
  - **Apps Script**
  - **AppSheet**
  - **Dialogflow**
  - **Command-line application or script**
- **Web/HTTP services** provide the most flexibility and are the most common option for public or complex apps.
- **Pub/Sub** is best when the app is behind a firewall or needs event subscriptions.
- **Webhooks** are simple but limited to sending messages into a single Chat space.
- **Apps Script** is low-code and integrates well with Google Workspace services.
- **AppSheet** enables no-code Chat apps.
- **Dialogflow** is best for natural language and conversational bots.
- **Command-line apps/scripts** are suitable for non-interactive asynchronous operations.
- Chat apps can handle user interactions through:
  - Command parsing
  - Dialogs
  - Natural language processing
- Chat apps can also proactively send messages or perform actions using the **Chat API**.

---

## Architecture Selection Overview

Google identifies architecture fit using two levels:

- **Recommended / verified**: Best fit for the use case.
- **Possible / check_circle_outline**: Possible, but not as strong a fit.

### By Intended Audience

| Audience | Best-fit architectures |
|---|---|
| **Your team** | Webhooks, Apps Script, AppSheet |
| **Your organization** | Web/HTTP service, Pub/Sub, Apps Script |
| **The public** | Web/HTTP service |

Other possible fits include Web/HTTP service, Pub/Sub, Dialogflow, script, and Apps Script depending on the case.

---

### By User Interactivity

| Capability | Best-fit architecture |
|---|---|
| **Natural language processing** | Dialogflow |

NLP can also be implemented with Web/HTTP service, Pub/Sub, or Apps Script, but Dialogflow is the recommended option.

---

### By Messaging Pattern

| Messaging need | Best-fit architectures |
|---|---|
| **Send and receive synchronous messages** | Web/HTTP service, Apps Script, AppSheet, Dialogflow |
| **Synchronous + asynchronous messages** | Web/HTTP service, Apps Script, AppSheet |
| **Asynchronous messages only** | Web/HTTP service, Apps Script, script |
| **Send messages from an external system to a single Chat space** | Web/HTTP service, Webhooks, Apps Script, AppSheet |

---

### By Integration / System Access

| Requirement | Best-fit architecture |
|---|---|
| **Integrate with other Google services** | Apps Script, AppSheet |
| **Communicate behind a firewall** | Pub/Sub |
| **Query or subscribe to Chat events** | Pub/Sub |

---

### By Development and Deployment Style

| Requirement | Best-fit architecture |
|---|---|
| **No-code development** | AppSheet |
| **Low-code development** | Webhooks, Apps Script |
| **Programming language of your choice** | Web/HTTP service, Pub/Sub, script |
| **Simplified DevOps** | Apps Script, AppSheet |
| **Complete DevOps and CI/CD management** | Web/HTTP service, Pub/Sub |

---

# Service Architecture Styles

---

## 1. Web or HTTP Service

A **web or HTTP service** is the most commonly deployed architecture.

> A _web or HTTP service_ is the most commonly deployed architecture because it provides the most flexibility for developers to build public Chat apps.

### Recommended Use Cases

Use this architecture when:

- The Chat app is deployed publicly on the **Google Workspace Marketplace**.
- The app needs all messaging patterns:
  - Send and receive synchronous messages
  - Send asynchronous messages
  - Send messages from an external system
- The app is developed in **any programming language**.
- The app requires full **DevOps and CI/CD** control.
- The service runs in cloud or on-premises servers.

### Flow

1. User sends a message in a Chat space to the Chat app.
2. Chat sends an HTTP request to a cloud or on-premises web server.
3. The app logic can optionally interact with third-party services, such as:
   - Project management systems
   - Ticketing tools
4. The web server sends an HTTP response back to Chat.
5. Chat delivers the response to the user.
6. Optionally, the app calls the **Chat API** to post asynchronous messages or perform other operations.

### Implementation Notes

- Supports existing libraries and

[... summary truncated for context management ...]

---

## Source 11: Configure the Chat MCP server  |  Google Chat  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/api/guides/configure-mcp-server
- Original file: `docs/configure-the-chat-mcp-server-google-chat-google-for-developers-8746e948.md`
- Product area: `chat-developers`

# Configure the Google Chat MCP Server — Summary

**Source:** Google Developers — Google Chat API  
**URL:** https://developers.google.com/workspace/chat/api/guides/configure-mcp-server  
**Last updated:** 2026-06-05 UTC

---

## Overview

Google Chat provides a remote **Model Context Protocol (MCP)** server that lets AI agents securely interact with Google Chat data.

By configuring the Google Chat MCP server, AI applications such as **Google Antigravity** and **Claude** can perform actions in Google Chat.

The MCP server enables AI agents to:

- **Read data:** List and search conversations, and read messages.
- **Respect security:** Inherit the same permissions and data governance controls as the user.

---

## Prerequisites

You need:

- A **Google Cloud project**
  - See: [Create a project](https://developers.google.com/workspace/guides/create-project)
- An **MCP client**, such as [Google Antigravity](https://antigravity.google/)
- The **gcloud CLI** set up in a local development environment

### gcloud CLI setup

1. Install the Google Cloud CLI:  
   https://cloud.google.com/sdk/docs/install
2. If already installed, update it:

```bash
gcloud components update
```

3. If using an external identity provider, sign in with your federated identity.
4. Initialize the gcloud CLI:  
   https://docs.cloud.google.com/sdk/docs/initializing

---

## Configure the Google Chat MCP Server

To use the Google Chat MCP server:

1. Enable required APIs in your Google Cloud project.
2. Enable MCP services.
3. Configure a Google Chat app.
4. Set up OAuth consent.
5. Configure your MCP client.

---

## 1. Enable the Google Chat API

Enable the **Google Chat API** in your Google Cloud project.

### CLI

```bash
gcloud services enable chat.googleapis.com --project=PROJECT_ID
```

Replace:

- `PROJECT_ID` — your Google Cloud project ID

### Console

Use the Google Cloud Console flow:

- [Enable the APIs](https://console.cloud.google.com/flows/enableapi?apiid=chat.googleapis.com)

---

## 2. Enable the Google Chat MCP API

Enable the MCP components by enabling the **Google Chat MCP API**.

### CLI

```bash
gcloud services enable chatmcp.googleapis.com --project=PROJECT_ID
```

Replace:

- `PROJECT_ID` — your Google Cloud project ID

### Console

Use the Google Cloud Console flow:

- [Enable the MCP services](https://console.cloud.google.com/flows/enableapi?apiid=chatmcp.googleapis.com)

---

## 3. Configure the Chat App

You must configure a Chat app in your Google Cloud project.

### Steps

1. In Google Cloud Console, search for **Google Chat API**.
2. Go to:

   **Google Chat API > Manage > Configuration**

   Or use:  
   [Go to Google Chat API](https://console.cloud.google.com/apis/api/chat.googleapis.com/hangouts-chat)

3. Configure the Chat app:

| Field / Setting | Value |
|---|---|
| **App name** | `Chat MCP` |
| **Avatar URL** | `https://developers.google.com/chat/images/quickstart-app-avatar.png` |
| **Description** | `Chat MCP server` |
| **Functionality** | Turn off interactive features by toggling **Enable interactive features** off |
| **Logs** | Select **Log errors to Logging** |

4. Click **Save**.

Reference:

- [Choose a Google Chat app architecture](https://developers.google.com/workspace/chat/structure)

---

## 4. Set Up the OAuth Consent Screen

The Google Chat MCP server uses **OAuth 2.0** for authentication and authorization. You must configure OAuth consent before creating an OAuth client ID.

### Start OAuth Branding Setup

Go to:

- **Google Auth Platform > Branding**

Or use:  
[Go to Branding](https://console.cloud.google.com/auth/branding)

If **Google Auth Platform** is already configured, update settings in:

- [Branding](https://console.cloud.google.com/auth/branding)
- [Audience](https://console.cloud.google.com/auth/audience)
- [Data Access](https://console.cloud.google.com/auth/scopes)

If you see **Google Auth Platform not configured yet**, click **Get Started**.

### OAuth Consent Screen Setup

1. Under **App Information**:
   - **App name:** `Chat MCP Server`
   - **User support email:** Select your email address or an appropriate Google group
2. Click **Next**.
3. Under **Audience**:
   - Select **Internal**
   - If **Internal** is unavailable, select **External**
4. Click **Next**.
5. Under **Contact Information**:
   - Enter an email address for project notifications
6. Click **Next**.
7. Under **Finish**:
   - Review the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy)
   - If you agree, select **I agree to the Google API Services: User Data Policy**
8. Click **Continue**.
9. Click **Create**.

### If You Selected External

Add test users:

1. Click **Audience**.
2. Under **Test users**, click **Add users**.
3. Enter your email address and any other authorized test users.
4. Click **Save**.

---

## OAuth Scopes Required

Go to:

**Data Access > Add or Remove Scopes**

Under **Manually add scopes**, paste these scopes:

```text


[... summary truncated for context management ...]

---

## Source 12: Develop with Google Chat  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/overview
- Original file: `docs/develop-with-google-chat-google-for-developers-1f260c06.md`
- Product area: `chat-developers`

# Develop with Google Chat — Summary

**Source:** Google for Developers — Google Chat  
**URL:** https://developers.google.com/workspace/chat/overview  
**Last updated:** 2026-04-20 UTC

---

## Page Purpose

This page introduces the **Google Chat API** and explains how developers can build **Google Chat apps** that integrate services, workflows, and resources directly into Google Chat conversations.

---

## Key Excerpts

> Google Chat apps integrate services directly into chats, enabling users to access information and take action without leaving the conversation.

> The Chat API consists of gRPC services or REST resources and methods that grant access to Chat, including spaces, space members, messages, message reactions, message attachments, space events, and user read states.

> Calling the Chat API requires authentication.

> The recommended way for most developers to call the Google Chat API is with our officially supported Cloud Client Libraries for your preferred language, like Python, Java, or Node.js.

> The Chat API lets you build Google Chat apps that bring your services and resources right into Google Chat.

---

## Google Chat API Overview

The **Google Chat API** provides access to Google Chat through:

- **gRPC services**
- **REST resources and methods**

It lets developers work with core Google Chat entities such as:

- Spaces
- Space members
- Messages
- Message reactions
- Message attachments
- Space events
- User read states
- User notification settings
- Custom emoji
- Sections

A video introduction is available:

- **Introduction to Google Chat API** — Google Workspace Developers  
  https://www.youtube.com/watch?v=cPHUsVvonjE

---

## Core Google Chat API Concepts

### Spaces

**Spaces** are places where people and apps converse and share files.

Types of spaces include:

- **Direct messages (DMs):** 1:1 conversations between two users or between a user and a Chat app.
- **Group chats:** Conversations between three or more users and Chat apps.
- **Named spaces:** Persistent collaboration areas where people send messages, share files, and work together.

**Resource references:**

- RPC: `google.chat.v1.Space`
- REST: `v1/spaces`

**Example operations:**

- Create a space
- Set up a space
- Get a space
- List spaces
- Update a space
- Delete a space
- Find a direct message

---

### Members

**Members** are users and Chat apps that have joined or been invited to a space.

**Resource references:**

- RPC: `google.chat.v1.Membership`
- REST: `v1/spaces.members`

**Example operations:**

- Create a membership
- Get a membership
- List memberships
- Update a membership
- Delete a membership

---

### Messages

**Messages** include:

- Text communications
- Card-based communications
- File attachments

Users can also react to messages with emoji.

**Resource references:**

- RPC: `google.chat.v1.Message`
- REST: `v1/spaces.messages`
- Cards: `v1/cards`

**Example operations:**

- Create a message
- Get a message
- List messages
- Update a message
- Delete a message

---

### Reactions

**Reactions** represent emoji responses to messages.

Examples include:

> 👍, 🚲, and 🌞

**Resource references:**

- RPC: `google.chat.v1.Reaction`
- REST: `v1/spaces.messages.reactions`

**Example operations:**

- Create a reaction
- List reactions
- Delete a reaction

---

### Custom Emoji

**Custom emoji** are emoji created and shared within an organization in Google Chat.

They can be:

- Included in message content
- Used as reactions to messages

**Resource references:**

- RPC: `google.chat.v1.CustomEmoji`
- REST: `v1/customEmojis`

**Example operations:**

- Create a custom emoji
- Delete a custom emoji
- Get details about a custom emoji
- List custom emojis in an organization

---

### Sections

**Sections** let users group conversations and customize the list of spaces shown in the Google Chat navigation panel.

Types include:

- Predefined system sections
- User-defined custom sections

**Resource references:**

- RPC: `google.chat.v1.Section`
- REST: `v1/users.sections`

**Example operations:**

- Create a section
- Update a section
- Delete a section
- Change the position of a section
- List sections
- List spaces in a section
- Move a space to a different section

---

### Media and Attachments

**Media** represents files uploaded to Google Chat, including:

- Images
- Videos
- Documents

**Media resource reference:**

- REST: `v1/media`
- RPC: Unavailable

**Attachments** are instances of media attached to messages.

**Attachment resource references:**

- RPC: `google.chat.v1.Attachment`
- REST: `v1/spaces.messages.attachments`

**Example operations:**

- Upload media as an attachment
- Download media as an attachment
- Get an attachment

---

### Space Events

**Space events** represent changes to a space or its child resources, including:

- Members
- Messages
- Reactions

**Resource references:**

- RPC: `google.chat.v1.SpaceEvent`
- REST: `v1/spaces.spaceEvents`

**Example related operations 

[... summary truncated for context management ...]

---

## Source 13: Google Apps Script quickstart  |  Google Chat  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/api/guides/quickstart/apps-script
- Original file: `docs/google-apps-script-quickstart-google-chat-google-for-developers-bba2c4e2.md`
- Product area: `chat-developers`

# Google Apps Script Quickstart for Google Chat API — Summary

**Source:** Google Developers — Google Chat API  
**URL:** https://developers.google.com/workspace/chat/api/guides/quickstart/apps-script  
**Last updated:** 2026-04-20 UTC

---

## Purpose

This quickstart shows how to create a **Google Apps Script** that calls the **Google Chat API** to **list Chat spaces**.

It demonstrates how to:

- Configure a Google Cloud project.
- Enable the Google Chat API.
- Configure OAuth consent.
- Configure a Google Chat app.
- Create and configure an Apps Script project.
- Link Apps Script to the Cloud project.
- Use an Advanced Google service to call the Chat API.
- Run and authorize the sample script.

> Quickstarts explain how to set up and run an app that calls a Google Workspace API.

The guide uses a **simplified authentication approach** intended for testing.

> This quickstart uses a simplified authentication approach that is appropriate for a testing environment.

For production apps, Google recommends learning about authentication and authorization before choosing credentials.

---

## Key Concepts

### Apps Script + Google Workspace APIs

In Apps Script, Google Workspace quickstarts use **Advanced Google services** to call Google Workspace APIs.

> In Apps Script, Google Workspace quickstarts use Advanced Google services to call Google Workspace APIs and handle some details of the authentication and authorization flow.

### Google Chat app configuration is required

To call the Google Chat API, you must configure a **Google Chat app**. For write requests, Google Chat uses the app’s configured identity in the Chat UI.

---

## Objectives

- Configure the environment.
- Create and configure the script.
- Run the script.

---

## Prerequisites

You need:

- A **Google Cloud project**.
- A **Business or Enterprise Google Workspace account** with access to **Google Chat**.

---

# Setup Workflow

## 1. Configure Your Google Cloud Project

If using a new Cloud project, configure it and add yourself as a test user. If already configured, skip ahead.

---

## 2. Open or Create a Cloud Project

In the Google Cloud console:

1. Go to **Select a project**.
2. Select an existing Google Cloud project, or click **Create project**.
3. If creating a new project, you might need to enable billing.

Link:

- [Select a Cloud project](https://console.cloud.google.com/projectselector2)

---

## 3. Enable the Google Chat API

Before using Google APIs, enable them in a Cloud project.

Action:

- Enable the **Google Chat API** in the Google Cloud console.

Link:

- [Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=chat.googleapis.com)

---

## 4. Configure the OAuth Consent Screen

In the Google API Console:

1. Go to **Menu > Google Auth platform > Branding**.
2. If the Google Auth platform is not configured, click **Get Started**.
3. Configure the following:

### App Information

- **App name:** enter a name for the app.
- **User support email:** choose an address users can contact for consent questions.

### Audience

- Select **Internal**.

### Contact Information

- Enter an email address to receive project change notifications.

### Finish

- Review the **Google API Services User Data Policy**.
- If you agree, select:

> I agree to the Google API Services: User Data Policy

Then click:

- **Continue**
- **Create**

### Scopes

For this quickstart:

- You can skip adding scopes for now.

Important production note:

> In the future, when you create an app for use outside of your Google Workspace organization, you must change the User type to External. Then add the authorization scopes that your app requires.

Reference:

- [Configure OAuth consent](https://developers.google.com/workspace/guides/configure-oauth-consent)

---

## 5. Configure the Google Chat App

To call the Google Chat API, configure a Chat app.

Open:

- [Chat API Configuration page](https://console.developers.google.com/apis/api/chat.googleapis.com/hangouts-chat)

Under **Application info**, enter:

| Field | Value |
|---|---|
| **App name** | `Chat API quickstart app` |
| **Avatar URL** | `https://developers.google.com/chat/images/quickstart-app-avatar.png` |
| **Description** | `Quickstart for calling the Chat API` |

Then:

1. Under **Interactive features**, turn **Enable interactive features** off.
2. Click **Save**.

---

# Create the Apps Script Project

## 1. Create a New Script

Go to:

- [script.google.com/create](https://script.google.com/create)

## 2. Add the Sample Code

Replace the contents of the script editor with:

```javascript
/**
 * This quickstart sample shows how to list spaces with user credential
 *
 * It relies on the OAuth2 scope 'https://www.googleapis.com/auth/chat.spaces.readonly'
 * referenced in the manifest file (appsscript.json).
 */
function listSpaces() {
  // Initialize request argument(s)
  // Filter spaces by space type (SPACE or GROUP_CHAT or DIRECT_MESSAGE)
  const filter = 'space_type = "SPACE

[... summary truncated for context management ...]

---

## Source 14: Google Chat app samples  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/samples
- Original file: `docs/google-chat-app-samples-google-for-developers-af5dc587.md`
- Product area: `chat-developers`

# Google Chat App Samples — Summary

**Source:** [Google Chat app samples | Google for Developers](https://developers.google.com/workspace/chat/samples)  
**Last updated:** 2026-04-20 UTC  
**Product area:** Google Workspace → Google Chat → Samples

---

## Key Excerpts

> Explore samples that show you how to build and deploy different kinds of Google Chat apps.

> If you've never built a Chat app, you can get started by completing a _quickstart_. Quickstarts explain how to set up and run a basic sample.

> API quickstarts use user authentication to call the Chat API, which means they perform an action as an authenticated Chat user.

> Unlike the interactive quickstarts, you don't need to install or interact with the Chat app in Chat spaces.

> You can also find Chat app samples on GitHub. You can fork these repositories and use the code as a reference for your own projects.

---

## Page Purpose

This Google Developers page collects resources for **building and deploying Google Chat apps**, including:

- Quickstarts for beginners
- Interactive app setup guides
- Tutorials and codelabs
- GitHub sample repositories
- Related Google Workspace developer videos
- Next-step planning resources for designing Chat apps

The page is intended to help developers choose a starting point based on their desired app type, programming language, Google product integrations, and preferred learning format.

---

# Get Started with a Quickstart

Quickstarts help developers set up and run a basic Google Chat app or Chat API integration.

There are **two main quickstart paths**:

## 1. API Quickstarts

API quickstarts are for calling the **Google Chat API programmatically**.

They use **user authentication**, meaning the app performs actions as the authenticated Chat user.

Typical actions include:

- Sending a message
- Returning a list of spaces the authenticated user belongs to
- Performing Chat API operations on behalf of the user

Important distinction:

- API quickstarts **do not require installing or interacting with a Chat app inside Chat spaces**.
- They are focused on using the Chat API as the authenticated user.

### API Quickstart Languages

API quickstarts are available for:

- [Apps Script](https://developers.google.com/workspace/chat/api/guides/quickstart/apps-script)
- [Python](https://developers.google.com/workspace/chat/api/guides/quickstart/python)
- [Node.js](https://developers.google.com/workspace/chat/api/guides/quickstart/nodejs)
- [Java](https://developers.google.com/workspace/chat/api/guides/quickstart/java)

For other programming languages, developers should use the Google Workspace [client libraries](https://developers.google.com/workspace/chat/libraries).

---

## 2. Interactive Quickstarts

Interactive quickstarts help developers configure the Chat API and create a basic Chat app that can be:

- Added to Chat spaces
- Messaged by users
- Used interactively inside Google Chat

### Interactive Quickstart Options

Developers can choose based on their preferred build environment or architecture:

- [Google Apps Script](https://developers.google.com/workspace/chat/quickstart/apps-script-app)  
  A cloud-based, low-code JavaScript development platform.

- [HTTP service with Google Cloud Functions](https://developers.google.com/workspace/chat/quickstart/gcf-app)  
  For building Chat apps backed by an HTTP endpoint.

- [Google Cloud Dialogflow CX](https://developers.google.com/workspace/chat/build-dialogflow-chat-app-natural-language)  
  A natural language platform for automated conversations and dynamic responses.

- [Google Cloud Pub/Sub](https://developers.google.com/workspace/chat/quickstart/pub-sub)  
  A real-time messaging service useful for building apps behind a firewall.

- [AppSheet](https://support.google.com/appsheet/answer/12923581)  
  A no-code development platform for building apps in Google Workspace organizations.

---

# Explore Google Chat App Samples

The page provides sample apps that can be filtered by:

## Products

- Firestore
- Gemini
- Google Admin console
- Google Calendar
- Google Cloud Functions
- Google Cloud Run
- Google Docs
- Pub/Sub
- Vertex AI

## Languages

- Apps Script
- Node.js
- Java
- Python

## Sample Types

- Quickstart
- Tutorial
- Codelab
- GitHub

---

## Featured Samples Listed on the Page

### Build a Google Chat Add-on with Dialogflow ES

**Link:** [Build a Google Chat add-on with Dialogflow ES](https://developers.google.com/workspace/add-ons/chat/quickstart-dialogflow-es?hl=en&authuser=5)

Explains how to build a Google Chat app as a **Google Workspace Add-on** that uses **Dialogflow ES** to understand and respond to natural language.

The page also notes that **Dialogflow CX** has a direct integration with Google Chat.

**Tags / technologies:**

- Google Chat
- Google Workspace add-ons
- Google Workspace
- Dialogflow

---

### Schedule Meetings from Google Chat — Workspace Add-on Sample

**Link:** [Schedule meetings from Google Chat](https://developers.g

[... summary truncated for context management ...]

---

## Source 15: Manage projects with Google Chat, Vertex AI, and Firestore  |  Google Workspace add-ons  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/tutorial-project-management
- Original file: `docs/manage-projects-with-google-chat-vertex-ai-and-firestore-google-workspace-add-ons-go-82389d2e.md`
- Product area: `chat-developers`

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

---

## Source 16: MCP Reference: chatmcp.googleapis.com  |  Google Chat  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/api/reference/mcp
- Original file: `docs/mcp-reference-chatmcp-googleapis-com-google-chat-google-for-developers-31378072.md`
- Product area: `chat-developers`

# MCP Reference: `chatmcp.googleapis.com` — Google Chat

**Source:** https://developers.google.com/workspace/chat/api/reference/mcp  
**Product:** Google Workspace → Google Chat → MCP server  
**Last updated:** **2026-05-08 UTC**

---

## Overview

The **Chat MCP API** provides **remote MCP access for Google Chat features**.

> Chat MCP API provides remote MCP for Google Chat features.

A **Model Context Protocol (MCP) server** acts as a proxy between an AI application/LLM and external systems such as Google Chat. It lets an LLM request context, call tools, or access resources in a standardized way.

> A Model Context Protocol (MCP) server acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application.

---

## Server Setup

Before using the Chat MCP server, you must configure it.

**Required setup:**

- Configure the Chat MCP server before use.
- For broader context, see the Google Cloud MCP servers overview.

Relevant links:

- [Configure the Chat MCP server](https://developers.google.com/workspace/chat/api/guides/configure-mcp-server)
- [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview)

---

## Server Endpoints

An MCP service endpoint is the network address, usually a URL, that an AI application uses to connect securely to the MCP server.

> It is the point of contact for the LLM to request context, call a tool, or access a resource.

Google MCP endpoints may be **global** or **regional**.

### Global MCP Endpoint

The Chat MCP API server has the following global MCP endpoint:

```text
https://chatmcp.googleapis.com/mcp/v1
```

### MCP Toolset Endpoint

The Chat MCP API server offers the following MCP toolset endpoint:

```text
https://chatmcp.googleapis.com/mcp/v1
```

---

## MCP Tools

An **MCP tool** is a function or executable capability exposed by the MCP server to an LLM or AI application.

> An MCP tool is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

**Toolsets** are groups of tools useful for a specific task. They can improve agent performance by reducing the number of available tools the agent must consider.

---

## Available Toolset

The `chatmcp.googleapis.com` MCP server provides a Google Chat toolset.

| Endpoint | Description | Tools |
|---|---|---|
| `/mcp/v1` | Tools for Google Chat. | `list_messages`<br>`search_conversations`<br>`search_messages`<br>`send_message` |

### Available Tools

- `list_messages`
- `search_conversations`
- `search_messages`
- `send_message`

---

## Get MCP Tool Specifications

To retrieve specifications for all available tools in the MCP server, use the `tools/list` method.

### Curl Request

```bash
curl --location 'https://chatmcp.googleapis.com/mcp/v1' \
--header 'content-type: application/json' \
--header 'accept: application/json, text/event-stream' \
--data '{
    "method": "tools/list",
    "jsonrpc": "2.0",
    "id": 1
}'
```

This request lists all tools and their specifications currently available within the Chat MCP server.

---

## Licensing

Unless otherwise noted:

- Page content is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/).
- Code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
- Java is a registered trademark of Oracle and/or its affiliates.

See also: [Google Developers Site Policies](https://developers.google.com/site-policies).

---

## Source 17: Method: spaces.messages.create  |  Google Chat  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages/create
- Original file: `docs/method-spaces-messages-create-google-chat-google-for-developers-00e948af.md`
- Product area: `chat-developers`

# Google Chat API: `spaces.messages.create` — Summary

**Source:** <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages/create>  
**Last updated:** 2026-05-07 UTC

## Purpose

Creates a message in a Google Chat space.

> Creates a message in a Google Chat space. For an example, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

Messages can be created using either **app authentication** or **user authentication**, with different sender attribution and message content capabilities.

---

## Key Capabilities & Constraints

- Creates messages in Google Chat spaces.
- Supports **text**, **cards**, and **accessory widgets** when using **app authentication**.
- Supports **text only** when using **user authentication**.
- Can start a new thread or reply to an existing thread.
- Supports idempotent message creation using `requestId`.
- Supports custom message IDs using `messageId`.
- Supports notification behavior controls, including forced or silent notifications.
- Maximum message size:

> The maximum message size, including the message contents, is 32,000 bytes.

- For webhook requests:

> For [webhook](https://developers.google.com/workspace/chat/quickstart/webhooks) requests, the response doesn't contain the full message. The response only populates the `name` and `thread.name` fields in addition to the information that was in the request.

---

## Authentication Behavior

Google Chat attributes the message sender differently depending on the authentication type.

### App Authentication

Required scope:

```text
https://www.googleapis.com/auth/chat.bot
```

With app authentication:

- Chat displays the **Chat app** as the sender.
- Message content can include:
  - `text`
  - `cardsV2`
  - `accessoryWidgets`

### User Authentication

Supported scopes:

```text
https://www.googleapis.com/auth/chat.messages.create
https://www.googleapis.com/auth/chat.messages
https://www.googleapis.com/auth/chat.import
```

Notes:

- `chat.import` applies to **import mode spaces only**.
- Chat displays the **user** as the sender.
- The Chat app is attributed by displaying its name.
- Message content can only contain:

```text
text
```

---

## HTTP Request

```http
POST https://chat.googleapis.com/v1/{parent=spaces/*}/messages
```

The URL uses **gRPC Transcoding** syntax.

---

## Path Parameters

| Parameter | Type | Required | Description |
|---|---:|:---:|---|
| `parent` | `string` | Yes | Resource name of the space where the message is created. Format: `spaces/{space}` |

Example format:

```text
spaces/{space}
```

---

## Query Parameters

| Parameter | Type | Required | Description |
|---|---:|:---:|---|
| `threadKey` | `string` | No | **Deprecated.** Use `thread.thread_key` instead. ID for the thread. Supports up to **4000 characters**. Used to start or add to a thread. |
| `requestId` | `string` | No | Unique request ID for the message. If an existing request ID is reused, Chat returns the message created with that ID instead of creating a duplicate. |
| `messageReplyOption` | `enum (MessageReplyOption)` | No | Specifies whether the message starts a thread or replies to one. Only supported in named spaces. Ignored when responding to user interactions. |
| `messageId` | `string` | No | Custom ID for the message. Lets Chat apps get, update, or delete a message without storing the system-assigned ID. |
| `createMessageNotificationOptions` | `object (CreateMessageNotificationOptions)` | No | Controls notification behavior when the message is posted. |

---

## `messageId` Custom ID Requirements

`messageId` lets a Chat app assign a custom ID to a message so it can later retrieve, update, or delete the message without storing the system-generated `name`.

Requirements:

- Must begin with:

```text
client-
```

- Example of a valid ID:

```text
client-custom-name
```

- Example of an invalid ID:

```text
custom-name
```

- Must contain **up to 63 characters**.
- May contain only:
  - lowercase letters
  - numbers
  - hyphens
- Must be **unique within a space**.
- A Chat app can’t use the same custom ID for different messages.

---

## Request Body

The request body contains an instance of:

```text
Message
```

---

## Response Body

If successful, the response body contains a newly created instance of:

```text
Message
```

---

## Required OAuth Scopes

Requires one of the following OAuth scopes:

```text
https://www.googleapis.com/auth/chat.bot
https://www.googleapis.com/auth/chat.import
https://www.googleapis.com/auth/chat.messages
https://www.googleapis.com/auth/chat.messages.create
```

---

# `MessageReplyOption`

Specifies how to reply to a message.

> More states might be added in the future.

| Enum | Description |
|---|---|
| `MESSAGE_REPLY_OPTION_UNSPECIFIED` | Default. Starts a new thread. Ignores any included `thread ID` or `threadKey`. |
| `REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD` | Creates the message as a reply to the specified `thread ID` or `thre

[... summary truncated for context management ...]

---

## Source 18: Receive and respond to interaction events  |  Google Chat  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/interaction-events
- Original file: `docs/receive-and-respond-to-interaction-events-google-chat-google-for-developers-388b4ea4.md`
- Product area: `chat-developers`

# Receive and Respond to Google Chat Interaction Events — Summary

**Source:** Google Developers — Google Chat  
**URL:** https://developers.google.com/workspace/chat/interaction-events  
**Last updated:** 2026-04-20 UTC

---

## Core Concept

Google Chat apps can receive and respond to **user interaction events**, which occur when users interact with the app in Chat.

Examples include:

- @mentioning the app
- Sending a slash command
- Adding or removing the app from a space
- Clicking a card button
- Opening the app homepage
- Submitting a form
- Interacting with dialogs

Interaction events are represented by the Chat API [`Event`](https://developers.google.com/workspace/chat/api/reference/rest/v1/Event) type and identified by an [`eventType`](https://developers.google.com/workspace/chat/api/reference/rest/v1/EventType).

> A _Google Chat app interaction event_ represents any action that a user takes to invoke or interact with a Chat app, such as @mentioning a Chat app or adding it to a space.

---

## What This Page Covers

The guide explains how to:

- Configure a Chat app to receive interaction events.
- Process interaction events on your infrastructure.
- Respond to interaction events when appropriate.

---

## Prerequisites

To build an interactive Google Chat app, you need:

- A Business or Enterprise [Google Workspace](https://support.google.com/a/answer/6043576) account with access to [Google Chat](https://workspace.google.com/products/chat/).
- A [Google Cloud project](https://developers.google.com/workspace/guides/create-project).
- A configured [OAuth consent screen](https://developers.google.com/workspace/guides/configure-oauth-consent).
- The [Google Chat API enabled](https://developers.google.com/workspace/guides/enable-apis).

---

## Types of Interaction Events

Google Chat sends different interaction event types depending on the user action. The app can process each event type differently and optionally respond with a message or another UI action.

### Common Interaction Events

| User interaction | `eventType` | Typical response from a Chat app |
|---|---|---|
| A user messages a Chat app, such as @mentioning it or using a slash command. | `MESSAGE` | Responds based on the message content. For example, `/about` can return a message explaining what the app does. |
| A user adds a Chat app to a space. | `ADDED_TO_SPACE` | Sends an onboarding or welcome message explaining what the app does and how users can interact with it. |
| A user removes a Chat app from a space. | `REMOVED_FROM_SPACE` | Removes incoming notifications configured for the space, such as deleting a webhook, and clears internal storage. |
| A user clicks a button on a card from a message, dialog, or homepage. | `CARD_CLICKED` | Processes and stores submitted data, or returns another card. |
| A user opens the app homepage by clicking the **Home** tab in a 1:1 message. | `APP_HOME` | Returns a static or interactive homepage card. |
| A user submits a form from the app homepage. | `SUBMIT_FORM` | Processes and stores submitted data, or returns another card. |
| A user invokes a quick command. | `APP_COMMAND` | Responds based on the invoked command, such as replying to an **About** command. |

For all supported events, see the [`EventType` reference documentation](https://developers.google.com/workspace/chat/api/reference/rest/v1/EventType).

---

## Dialog Interaction Events

If a Chat app opens [dialogs](https://developers.google.com/workspace/chat/dialogs), the interaction event includes additional dialog-specific information:

- `isDialogEvent` is set to `true`.
- [`DialogEventType`](https://developers.google.com/workspace/chat/api/reference/rest/v1/DialogEventType) clarifies whether the event:
  - Opens a dialog
  - Submits dialog information
  - Cancels or closes a dialog

### Common Dialog Events

| User interaction with a dialog | Dialog event type | Typical response |
|---|---|---|
| A user triggers a dialog request, such as by using a slash command or clicking a button. | `REQUEST_DIALOG` | The Chat app opens the dialog. |
| A user submits information in the dialog by clicking a button. | `SUBMIT_DIALOG` | The Chat app navigates to another dialog or closes the dialog to complete the interaction. |
| A user exits or closes the dialog before submitting information. | `CANCEL_DIALOG` | Optionally, the Chat app sends a new message or updates the message/card that opened the dialog. |

Related guide: [Open interactive dialogs](https://developers.google.com/workspace/chat/dialogs)

---

## Configure a Chat App to Receive Interaction Events

Not all Chat apps are interactive. For example:

> Incoming webhooks can only send outgoing messages and can't respond to users.

To build an interactive app, choose an endpoint that can receive, process, and respond to interaction events.

Configuration is done in the **Google Cloud console**:

1. Go to the Chat API page.
2. Open the **Configuration** page:  
   [Go to Chat API Config

[... summary truncated for context management ...]

---

## Source 19: Receive and respond to interaction events  |  Google Chat  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/receive-respond-interactions
- Original file: `docs/receive-and-respond-to-interaction-events-google-chat-google-for-developers-b6ab42ec.md`
- Product area: `chat-developers`

# Google Chat: Receive and Respond to Interaction Events — Summary

**Source:** https://developers.google.com/workspace/chat/receive-respond-interactions  
**Last updated:** 2026-04-20 UTC

## Overview

This guide explains how **Google Chat apps** receive and respond to user interactions, also called **Google Chat app interaction events**.

Interaction events occur when users interact with a Chat app, such as:

- @mentioning the app
- Using a slash command or quick command
- Adding or removing the app from a space
- Clicking a button on a card
- Opening the app homepage
- Submitting a form
- Opening, submitting, or canceling a dialog

Chat apps can process these events and optionally respond with messages, cards, dialogs, or asynchronous API calls.

> “This page describes how your Google Chat app can receive and respond to user interactions, also known as _Google Chat app interaction events_.”

The page covers how to:

- Configure a Chat app to receive interaction events.
- Process interaction events on your infrastructure.
- Respond to interaction events when appropriate.

---

## Prerequisites

To build an interactive Google Chat app, you need:

- A **Business or Enterprise Google Workspace account** with access to Google Chat.
- A **Google Cloud project**.
- An OAuth consent screen configured.
- The **Google Chat API enabled**.

---

## Core Concepts

A **Google Chat app interaction event** represents an action a user takes to invoke or interact with a Chat app.

When a user interacts with a Chat app:

1. Google Chat sends the app an event.
2. The event is represented as an [`Event`](https://developers.google.com/workspace/chat/api/reference/rest/v1/Event) type in the Chat API.
3. The app processes the event.
4. The app may optionally respond.

Each event includes an `eventType`, represented by the [`EventType`](https://developers.google.com/workspace/chat/api/reference/rest/v1/EventType) object.

Example:

- When a user adds a Chat app to a space, Google Chat sends an `ADDED_TO_SPACE` event.
- The app can respond with an onboarding or welcome message.

> “For each type of user interaction, Google Chat sends a different type of interaction event which helps your Chat app handle each event type accordingly.”

---

## Common Interaction Event Types

| User interaction | `eventType` | Typical Chat app response |
|---|---|---|
| User messages the Chat app, such as by @mentioning it or using a slash command. | `MESSAGE` | Responds based on message content. For example, `/about` can return a description of what the app does. |
| User adds the Chat app to a space. | `ADDED_TO_SPACE` | Sends an onboarding message explaining what the app does and how users can interact with it. |
| User removes the Chat app from a space. | `REMOVED_FROM_SPACE` | Removes incoming notifications configured for the space, such as webhooks, and clears internal storage. |
| User clicks a button on a card from a message, dialog, or homepage. | `CARD_CLICKED` | Processes and stores submitted data, or returns another card. |
| User opens the app homepage by clicking the **Home** tab in a 1:1 message. | `APP_HOME` | Returns a static or interactive homepage card. |
| User submits a form from the app homepage. | `SUBMIT_FORM` | Processes and stores submitted data, or returns another card. |
| User invokes a quick command. | `APP_COMMAND` | Responds based on the invoked command. For example, an **About** command can describe the app’s capabilities. |

For the complete list, see the [`EventType` reference documentation](https://developers.google.com/workspace/chat/api/reference/rest/v1/EventType).

---

## Dialog Interaction Events

If a Chat app opens dialogs, interaction events include extra dialog-related information:

- `isDialogEvent` is set to `true`.
- [`DialogEventType`](https://developers.google.com/workspace/chat/api/reference/rest/v1/DialogEventType) indicates whether the interaction opens, submits, or cancels a dialog.

### Common Dialog Event Types

| User interaction with a dialog | Dialog event type | Typical response |
|---|---|---|
| User triggers a dialog request, such as by using a slash command or clicking a button. | `REQUEST_DIALOG` | The Chat app opens the dialog. |
| User submits information in a dialog by clicking a button. | `SUBMIT_DIALOG` | The Chat app either navigates to another dialog or closes the dialog to complete the interaction. |
| User exits or closes the dialog before submitting. | `CANCEL_DIALOG` | Optionally sends a new message, or updates the message/card from which the dialog was opened. |

Related guide: [Open interactive dialogs](https://developers.google.com/workspace/chat/dialogs)

---

## Receiving Interaction Events

Not all Chat apps are interactive.

For example:

- **Incoming webhooks** can only send outgoing messages.
- They **can’t respond to users**.

To build an interactive Chat app, you must configure an endpoint that can receive, process, and respond to events.

---

## Configure a Chat

[... summary truncated for context management ...]

---

## Source 20: Respond to Google Chat app commands  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/commands
- Original file: `docs/respond-to-google-chat-app-commands-google-for-developers-2f843fbf.md`
- Product area: `chat-developers`

# Respond to Google Chat App Commands — Summary

**Source:** Google Developers — <https://developers.google.com/workspace/chat/commands>  
**Last updated:** 2026-04-20 UTC

## Purpose

This guide explains how to **set up and respond to commands** in a Google Chat app.

> Commands help users discover and use key features of a Chat app. Only Chat apps can see the content of a command. For example, if a user sends a message with a slash command, the message is only visible to the user and the Chat app.

Google recommends using commands as part of designing user journeys for Chat apps.

---

## Types of Google Chat App Commands

Google Chat apps can define three command types:

| Command type | How users invoke it | Best used when |
|---|---|---|
| **Slash command** | Type `/` followed by predefined text, such as `/about`, or select from the command menu | The app needs additional user input |
| **Quick command** | Open the command menu from the reply area, click **Add**, then select a command | The app can respond immediately without extra input |
| **Message action** | Hover over a message, open the three-dot menu, and select an action | The app performs an action based on a specific message |

### Slash Commands

Users type a slash command such as:

```text
/about
/search receipts
```

Use slash commands when the app needs argument text from the user.

Example:

> Create a slash command called `/search` that runs after the user enters a phrase to search for, like `/search receipts`.

---

### Quick Commands

Users select quick commands from the command menu in the message reply area.

Use quick commands when the app can respond immediately.

Example:

> Create a quick command called **Random image** that responds immediately with an image.

---

### Message Actions

> **Developer Preview**

Users invoke message actions from the message context menu.

Use message actions when the app can act on the context of a message.

Example:

> Create a message action if your Chat app can perform actions based on the context of a message.

---

## Prerequisites

You need a **Google Chat app that receives and responds to interaction events**.

Google provides quickstarts depending on implementation language/platform:

- **Node.js**
- **Apps Script**
- **Python**
- **Java**

For HTTP-service apps, Google points to the Google Cloud Functions Chat app quickstart.  
For Apps Script apps, Google points to the Apps Script Chat app quickstart.

---

# Set Up a Command

Setting up a command involves two main steps:

1. **Create a name and description**
2. **Configure the command in the Google Cloud console**

---

## Naming and Describing Commands

The command name is what users type or select to invoke the Chat app. A short description appears below the command name to help users understand how to use it.

### Naming Recommendations

Use names that are:

- **Short**
- **Descriptive**
- **Actionable**
- Easy for users to understand

Example recommendation:

```text
Use "Remind me" instead of "Create a reminder"
```

Additional guidance:

- Use common names for common interactions, such as:
  - `Settings`
  - `Feedback`
- Use unique names when possible to avoid confusion with commands from other Chat apps.
- If multiple apps use the same command name, users may need to filter through similar commands.

---

### Description Recommendations

Descriptions should be:

- Short
- Clear
- Explicit about expected behavior

Include formatting requirements when relevant.

Example:

```text
Remind me to do [something] at [time]
```

Also clarify whether the app responds:

- Publicly to everyone in the space
- Privately to the user who invoked the command

Example:

```text
Learn about this app (Only visible to you)
```

---

# Configure a Command in Google Cloud Console

To create a **slash command**, **quick command**, or **message action**, configure it in the Google Chat API settings for your app.

## Steps

1. In Google Cloud console, go to:

   ```text
   Menu > APIs & Services > Enabled APIs & Services > Google Chat API
   ```

   Google Chat API page: <https://console.cloud.google.com/apis/api/chat.googleapis.com>

2. Click **Configuration**.

3. Under **Commands**, click **Add a command**.

4. Enter command details:

   | Field | Details |
   |---|---|
   | **Command ID** | A number from `1` to `1000`; used by the Chat app to recognize the command and return a response |
   | **Description** | Up to 50 characters; can include special characters |
   | **Command type** | Choose **Quick command**, **Slash command**, or **Message action** |
   | **Command name** | Depends on the command type |

---

## Command Name Rules by Type

### Quick Command Name

- Display name users select from the menu
- Up to 50 characters
- Can include special characters

Example:

```text
Remind me
```

---

### Slash Command Name

- Text users type in a message
- Must start with `/`
- Must contain only text
- Up to 50 characters

Example:

```text
/remindMe

[... summary truncated for context management ...]

---

## Source 21: Respond to Google Chat app commands  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/slash-commands
- Original file: `docs/respond-to-google-chat-app-commands-google-for-developers-592b1c9f.md`
- Product area: `chat-developers`

# Respond to Google Chat App Commands — Markdown Summary

**Source:** Google Developers — Google Chat  
**URL:** https://developers.google.com/workspace/chat/slash-commands  
**Last updated:** 2026-04-20 UTC

---

## Overview

Google Chat app commands help users discover and use key features of a Chat app. Commands are visible only to the user and the Chat app, not to everyone in the space.

> “Only Chat apps can see the content of a command. For example, if a user sends a message with a slash command, the message is only visible to the user and the Chat app.”

Before building commands, Google recommends designing the user journey first: [Define all user journeys](https://developers.google.com/workspace/chat/journeys).

---

## Types of Google Chat App Commands

Google Chat apps support three command types:

| Command type | How users invoke it | Best used when |
|---|---|---|
| **Slash commands** | Type `/` plus predefined text, such as `/about`, or select from the command menu | The app needs additional user input |
| **Quick commands** | Open the command menu from the message reply area, click **Add**, and select a command | The app can respond immediately without more input |
| **Message actions** | Hover over a message, open the three-dot menu, and select an action | The app acts on the context of an existing message |

---

### Slash Commands

Users invoke slash commands by typing a slash (`/`) followed by predefined text, such as:

```text
/about
/search receipts
```

Use slash commands when your app needs arguments or additional input.

Example use case:

> Create a slash command called `/search` that runs after the user enters a phrase to search for, like `/search receipts`.

---

### Quick Commands

Users invoke quick commands from the Chat message reply area command menu.

Use quick commands when the app can respond immediately.

Example:

> Create a quick command called **Random image** that responds immediately with an image.

---

### Message Actions

> **Developer Preview**

Users invoke message actions from the three-dot menu on a specific message.

Use message actions when the app performs an action based on the context of a message.

Example:

> A message context menu can contain a **“Remind me”** message action.

---

## Prerequisites

You need a Google Chat app that receives and responds to [interaction events](https://developers.google.com/workspace/chat/receive-respond-interactions).

Supported implementation paths:

- **Node.js**
  - Create an interactive Chat app using an HTTP service with the [Google Cloud Functions quickstart](https://developers.google.com/workspace/chat/quickstart/gcf-app).
- **Apps Script**
  - Create an interactive Chat app using the [Apps Script quickstart](https://developers.google.com/workspace/chat/quickstart/apps-script-app).
- **Python**
  - Create an interactive Chat app using an HTTP service with the [Google Cloud Functions quickstart](https://developers.google.com/workspace/chat/quickstart/gcf-app).
- **Java**
  - Create an interactive Chat app using an HTTP service with the [Google Cloud Functions quickstart](https://developers.google.com/workspace/chat/quickstart/gcf-app).

---

# Set Up a Command

Setting up a command involves:

1. Creating a command **name and description**
2. Configuring the command in the **Google Cloud console**

---

## Name and Describe the Command

The command name is what users type or select to invoke the Chat app. A short description appears below the command name to help users understand how to use it.

---

### Command Naming Recommendations

Use names that are:

- **Short**
- **Descriptive**
- **Actionable**

Example:

```text
Remind me
```

Instead of:

```text
Create a reminder
```

Additional guidance:

- Use common names for familiar features, such as:
  - `Settings`
  - `Feedback`
- Use unique names when possible to avoid confusion with similar commands from other Chat apps.

> If your command name is the same as a command from another Chat app, users must filter through similar commands to find yours.

---

### Command Description Recommendations

Descriptions should be short and clear.

They should explain:

- What the command does
- Whether formatting is required
- Whether the response is visible to everyone or only the invoking user

Example for a slash command requiring arguments:

```text
Remind me to do [something] at [time]
```

Example for a private quick command:

```text
Learn about this app (Only visible to you)
```

---

## Configure the Command in Google Cloud Console

To configure slash commands, quick commands, or message actions:

1. In the Google Cloud console, go to:

   ```text
   Menu > APIs & Services > Enabled APIs & Services > Google Chat API
   ```

   Or open: [Google Chat API page](https://console.cloud.google.com/apis/api/chat.googleapis.com)

2. Click **Configuration**.

3. Under **Commands**, click **Add a command**.

4. Enter the command details:

   - **Command ID**
     - A number fr

[... summary truncated for context management ...]

---

## Source 22: Respond to incidents with Google Chat, Vertex AI, and Google Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/tutorial-incident-response-app-auth
- Original file: `docs/respond-to-incidents-with-google-chat-vertex-ai-and-google-apps-script-google-for-de-0d52e2d9.md`
- Product area: `chat-developers`

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

---

## Source 23: Respond to incidents with Google Chat, Vertex AI, Apps Script, and user authentication  |  Google Workspace add-ons  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/tutorial-incident-response
- Original file: `docs/respond-to-incidents-with-google-chat-vertex-ai-apps-script-and-user-authentication-de1d1443.md`
- Product area: `chat-developers`

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

---

## Source 24: Send a message using the Google Chat API  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/create-messages
- Original file: `docs/send-a-message-using-the-google-chat-api-google-for-developers-70b8f442.md`
- Product area: `chat-developers`

# Send a Message Using the Google Chat API — Comprehensive Summary

**Source:** Google for Developers — Google Chat API  
**URL:** https://developers.google.com/workspace/chat/create-messages  
**Last updated:** 2026-05-08 UTC

---

## Overview

The Google Chat API lets developers use the [`create()` / `CreateMessage()`](https://developers.google.com/workspace/chat/api/reference/rpc/google.chat.v1#google.chat.v1.ChatService.CreateMessage) method on the `Message` resource to create messages in Google Chat.

You can use it to:

- Send messages containing:
  - Plain text
  - Rich text
  - Cards
  - Interactive widgets
- Send private messages visible only to a specific user.
- Start or reply to message threads.
- Assign custom IDs to messages for later retrieval, update, or deletion.
- Quote existing messages.
- Send messages as:
  - A **Chat app**
  - A **Chat app on behalf of a user**

> **Maximum message size:**  
> The maximum message size, including text and cards, is **32,000 bytes**.  
> If a message exceeds this size, the Chat app must send multiple messages.

Chat apps can also send messages synchronously in response to user interactions without calling the Chat API, such as posting a welcome message when added to a space.

---

## How Google Chat Displays API-Created Messages

The way Chat displays and attributes a message depends on the authentication type.

### App Authentication

When using **app authentication**, the Chat app sends the message directly.

- Chat displays `App` next to the sender name.
- The message is attributed to the Chat app.
- Supports rich message features:
  - Text
  - Cards
  - Interactive widgets
  - Accessory widgets
  - Private messages
  - Forced notifications
  - Silent messages

> With app authentication, the Chat app sends the message. To note that the sender isn't a person, Chat displays `App` next to its name.

### User Authentication

When using **user authentication**, the Chat app sends the message on behalf of the user.

- Chat displays the user as the sender.
- Chat also displays the Chat app name next to the user’s name.
- Generally supports **text messages only**.
- In **Developer Preview**, user-authenticated messages can also include cards.

> With user authentication, the user sends the message, and Chat displays the Chat app name next to the user's name.

---

## Prerequisites

To use the examples in the guide, you need:

- A **Business or Enterprise Google Workspace account** with access to Google Chat.
- A Google Cloud project.
- OAuth consent screen configured.
- Google Chat API enabled and configured with:
  - Chat app name
  - Icon
  - Description
- A Google Chat space where:
  - The authenticated user is a member, or
  - The calling Chat app is a member.
- Appropriate credentials depending on authentication type:
  - **User authentication:** OAuth client ID credentials saved as `credentials.json`
  - **App authentication:** Service account credentials saved as `credentials.json`
- Appropriate authorization scopes.
- Language-specific setup:
  - Node.js Cloud Client Library
  - Python Cloud Client Library
  - Java Cloud Client Library
  - Apps Script project with Advanced Chat Service enabled

For app authentication, the Chat app must be added to the space.

---

## Authentication Scopes

Common scopes mentioned:

### App Authentication

```text
https://www.googleapis.com/auth/chat.bot
```

### User Authentication

```text
https://www.googleapis.com/auth/chat.messages.create
```

---

## Sending a Message as the Chat App

Using app authentication, a Chat app can send messages with rich content, including text, cards, and interactive accessory widgets.

Required request fields:

- `chat.bot` authorization scope
- `parent`: the target `Space` resource, such as `spaces/SPACE_NAME`
- `message`: the `Message` resource to create

Message content can include:

- `text`
- `cardsV2`
- Both `text` and `cardsV2`

Optional fields include:

- `accessoryWidgets`
- `privateMessageViewer`
- `messageId`
- `thread.threadKey`
- `messageReplyOption`

### Representative Node.js Example

```js
import {createClientWithAppCredentials} from './authentication-utils.js';

// This sample shows how to create message with app credential
async function main() {
  // Create a client
  const chatClient = createClientWithAppCredentials();

  // Initialize request argument(s)
  const request = {
    // Replace SPACE_NAME here.
    parent: 'spaces/SPACE_NAME',
    message: {
      text:
        '👋🌎 Hello world! I created this message by calling ' +
        "the Chat API's `messages.create()` method.",
      cardsV2: [
        {
          card: {
            header: {
              title: 'About this message',
              imageUrl:
                'https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/info/default/24px.svg',
            },
            sections: [
              {
                header: 'Contents',
                widgets: [
                  {
               

[... summary truncated for context management ...]

---

## Source 25: Usage limits  |  Google Chat  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/limits
- Original file: `docs/usage-limits-google-chat-google-for-developers-75b4339d.md`
- Product area: `chat-developers`

# Google Chat API Usage Limits — Summary

**Source:** Google for Developers — Google Chat API Usage Limits  
**Last updated:** **2026-05-01 UTC**

## Overview

Google Chat API enforces quotas and limits to ensure **fair usage** and protect **Google Workspace performance**.

> Because the Google Chat API is a shared service, we apply quotas and limitations to make sure that it's used fairly by all users and to protect the overall performance of Google Workspace.

If a quota is exceeded, the API returns:

```http
429: Too many requests
```

Google notes that additional backend rate-limit checks can also produce the same error.

**Recommended response:** use a **truncated exponential backoff** algorithm and retry later.

> As long as you stay within the per-minute quotas listed in the following tables, there's no limit to the number of requests you can make per day.

Multiple quota types can apply to a Chat API method:

- **Per-project quotas** — apply to a Google Cloud project / single Chat app.
- **Per-space quotas** — apply within a given Chat space and are shared by all Chat apps acting in that space.
- **Per-user quotas** — apply across all Chat apps calling API methods on behalf of a user using user authentication.

---

## Per-Project Quotas

Per-project quotas limit query rates for a **Google Cloud project**, typically applying to a single Chat app calling the listed Chat API methods.

These limits are also visible in the Google Cloud Console on the **Quotas** page.

| Per-project quota | Chat API methods | Limit |
|---|---|---:|
| **Message writes per minute** | `spaces.messages.create`<br>`spaces.messages.patch`<br>`spaces.messages.delete` | **3000 / 60 sec** |
| **Message reads per minute** | `spaces.messages.get`<br>`spaces.messages.list` | **3000 / 60 sec** |
| **Membership writes per minute** | `spaces.members.create`<br>`spaces.members.delete` | **300 / 60 sec** |
| **Membership reads per minute** | `spaces.members.get`<br>`spaces.members.list` | **3000 / 60 sec** |
| **Space writes per minute** | `spaces.setup`<br>`spaces.create`<br>`spaces.patch`<br>`spaces.delete` | **60 / 60 sec** |
| **Space reads per minute** | `spaces.get`<br>`spaces.list`<br>`spaces.findDirectMessage` | **3000 / 60 sec** |
| **Attachment writes per minute** | `media.upload` | **600 / 60 sec** |
| **Attachment reads per minute** | `spaces.messages.attachments.get`<br>`media.download` | **3000 / 60 sec** |
| **Reaction writes per minute** | `spaces.messages.reactions.create`<br>`spaces.messages.reactions.delete` | **600 / 60 sec** |
| **Reaction reads per minute** | `spaces.messages.reactions.list` | **3000 / 60 sec** |
| **CustomEmoji writes per minute** | `customEmojis.create`<br>`customEmojis.delete` | **600 / 60 sec** |
| **CustomEmoji reads per minute** | `customEmojis.get`<br>`customEmojis.list` | **3000 / 60 sec** |
| **Section writes per minute** | `users.sections.create`<br>`users.sections.delete`<br>`users.sections.patch`<br>`users.sections.position`<br>`users.sections.items.move` | **600 / 60 sec** |
| **Section reads per minute** | `users.sections.list`<br>`users.sections.items.list` | **3000 / 60 sec** |

---

## Per-Space Quotas

Per-space quotas limit query rates **inside a specific Chat space**.

These quotas are **shared among all Chat apps** acting in that space.

| Per-space quota | Chat API methods | Limit |
|---|---|---:|
| **Reads per second** | `media.download`<br>`spaces.get`<br>`spaces.members.get`<br>`spaces.members.list`<br>`spaces.messages.get`<br>`spaces.messages.list`<br>`spaces.messages.attachments.get`<br>`spaces.messages.reactions.list` | **15 / sec** |
| **Writes per second** | `media.upload`<br>`spaces.delete`<br>`spaces.patch`<br>`spaces.messages.create`<br>`spaces.messages.delete`<br>`spaces.messages.patch`<br>`spaces.messages.reactions.delete` | **1 / sec** |
| **Create Reaction writes per second** | `spaces.messages.reactions.create` | **5 / sec** |
| **Message writes per second while importing data to Google Chat** | `spaces.messages.create` | **10 / sec** |

**Important note:** additional limits apply to **incoming webhooks** for `spaces.messages.create`.

---

## Per-User Quotas

Per-user quotas limit query rates for a **Google Chat user**.

They apply to all Chat apps that call Chat API methods **on behalf of a user** using **user authentication**.

| Per-user quota | Chat API methods | Limit |
|---|---|---:|
| **CustomEmoji writes per second** | `customEmojis.create`<br>`customEmojis.delete` | **1 / sec** |
| **CustomEmoji reads per second** | `customEmojis.get`<br>`customEmojis.list` | **15 / sec** |
| **Section writes per second** | `users.sections.create`<br>`users.sections.delete`<br>`users.sections.patch`<br>`users.sections.position`<br>`users.sections.items.move` | **1 / sec** |
| **Section reads per second** | `users.sections.list`<br>`users.sections.items.list` | **15 / sec** |

---

## Additional Usage Limits

High traffic directed at the same Chat space can trigger **ad

[... summary truncated for context management ...]

---

## Source 26: Verify requests from Google Chat  |  Google for Developers

- Source URL: https://developers.google.com/workspace/chat/verify-requests-from-chat
- Original file: `docs/verify-requests-from-google-chat-google-for-developers-e27839ac.md`
- Product area: `chat-developers`

# Verify Requests from Google Chat — Markdown Summary

**Source:** https://developers.google.com/workspace/chat/verify-requests-from-chat  
**Last updated:** 2026-04-20 UTC

---

## Core Purpose

For Google Chat apps built with **HTTP endpoints**, you must verify that incoming HTTPS requests actually originate from **Google Chat**.

Google Chat includes a **bearer token** in the `Authorization` header of every HTTPS request sent to your app endpoint.

```http
POST
Host: yourappurl.com
Authorization: Bearer AbCdEf123456
Content-Type: application/json
User-Agent: Google-Dynamite
```

The bearer token is a **cryptographic token produced by Google**. Its type and `audience` value depend on the **Authentication Audience** setting configured for the Chat app.

---

## Key Facts

- Google Chat sends a bearer token in the `Authorization` header of HTTPS requests.
- The token verifies that the request originated from Google Chat.
- If verification fails, your service should return:

```http
401 Unauthorized
```

- For **Cloud Run functions / Cloud Run**, Google Cloud IAM can handle token verification automatically.
- For apps with their own HTTP server, verify the bearer token using:
  - A Google API client library
  - Or direct validation of the ID token / JWT
- The token format depends on the Chat app’s **Authentication Audience**:
  - **HTTP endpoint URL** → Google-signed **OIDC ID token**
  - **Project Number** → self-signed **JWT**

---

## Google Chat Service Account

Requests from Chat are associated with this service account:

```text
chat@system.gserviceaccount.com
```

This value is used as the expected issuer/email when verifying tokens.

---

## Recommended Google API Client Libraries

For self-managed HTTP servers, Google recommends using open source Google API client libraries:

- **Java:** https://github.com/google/google-api-java-client
- **Python:** https://github.com/google/google-api-python-client
- **Node.js:** https://github.com/google/google-api-nodejs-client
- **.NET:** https://github.com/google/google-api-dotnet-client

---

# Authentication with Cloud Run Functions

If your Chat app is implemented using **Cloud Run functions**, Cloud IAM handles token verification automatically.

## Required Chat App Configuration

In the Chat app connection settings:

- Set **Authentication Audience** to:

```text
HTTP endpoint URL
```

- Ensure the configured HTTP endpoint URL matches the Cloud Run function endpoint URL.

## Required IAM Configuration

Authorize the Google Chat service account as an invoker:

```text
chat@system.gserviceaccount.com
```

---

## Grant Invoker Permission Using Google Cloud Console

After deploying your function or service:

1. Open the Cloud Run page in Google Cloud Console.
2. In the Cloud Run services list, select the checkbox next to the receiving function.
   - Do **not** click the function itself.
3. Click **Permissions**.
4. Click **Add principal**.
5. In **New principals**, enter:

```text
chat@system.gserviceaccount.com
```

6. Select the role:

```text
Cloud Run > Cloud Run Invoker
```

7. Click **Save**.

---

## Grant Invoker Permission Using `gcloud`

Use:

```bash
gcloud functions add-invoker-policy-binding RECEIVING_FUNCTION \
  --member='serviceAccount:chat@system.gserviceaccount.com'
```

Replace:

```text
RECEIVING_FUNCTION
```

with the name of your Chat app’s function.

---

# Authentication with an ID Token

Use this method when the Chat app’s **Authentication Audience** is set to:

```text
HTTP endpoint URL
```

## Token Characteristics

When using an HTTP endpoint URL as the audience:

- The bearer token is a Google-signed OpenID Connect **ID token**.
- The `email` field is:

```text
chat@system.gserviceaccount.com
```

- The token audience is the endpoint URL configured for the Chat app.

Example:

If the configured endpoint is:

```text
https://example.com/app/
```

then the ID token audience is:

```text
https://example.com/app/
```

## Recommendation

This is the **recommended authentication method** if your HTTP endpoint is not hosted on a service that supports IAM-based authentication, such as Cloud Run.

Benefits:

- Your service only needs to know its endpoint URL.
- It does **not** need to know the Google Cloud project number.

---

## ID Token Verification Examples

### Java

Source: `java/basic-app/src/main/java/com/google/chat/app/basic/App.java`

```java
String CHAT_ISSUER = "chat@system.gserviceaccount.com";
JsonFactory factory = JacksonFactory.getDefaultInstance();

GoogleIdTokenVerifier verifier =
    new GoogleIdTokenVerifier.Builder(new ApacheHttpTransport(), factory)
        .setAudience(Collections.singletonList(AUDIENCE))
        .build();

GoogleIdToken idToken = GoogleIdToken.parse(factory, bearer);
return idToken != null
    && verifier.verify(idToken)
    && idToken.getPayload().getEmailVerified()
    && idToken.getPayload().getEmail().equals(CHAT_ISSUER);
```

### Python

Source: `python/basic-app/main.py`

```python
# Bearer T

[... summary truncated for context management ...]

---
