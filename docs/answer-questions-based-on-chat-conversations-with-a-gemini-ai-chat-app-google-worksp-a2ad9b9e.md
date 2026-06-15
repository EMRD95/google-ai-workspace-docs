---
title: "Answer questions based on Chat conversations with a Gemini AI Chat app  |  Google Workspace add-ons  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/tutorial-ai-knowledge-assistant"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:09:18Z"
extraction_method: "web_extract"
---

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
