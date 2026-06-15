---
title: "Connect flows to other services with webhooks - Workspace Studio Help"
source_url: "https://support.google.com/workspace-studio/answer/16521900"
product_area: "workspace-studio"
retrieved_at: "2026-06-15T17:49:09Z"
extraction_method: "web_extract"
---

# Connect flows to other services with webhooks — Workspace Studio Help

**Source:** https://support.google.com/workspace-studio/answer/16521900  
**Status:** _This feature is in limited preview._

## Overview

Workspace Studio flows can send information to external services using a **webhook step**. A webhook sends an **HTTP request** to a specific URL you provide.

Example use case: posting a message to a Slack channel.

> **Important:** When you add variables to third-party integration steps or add-on steps, they might contain your Google Account data, such as the contents of a message in Gmail or Chat, or event information from Calendar. The flow can then share your Google Account data with a third-party service. Make sure you trust the third-party service.

---

## Add a webhook step

To add a webhook to a flow:

1. Go to [https://studio.workspace.google.com](https://studio.workspace.google.com/) and create a flow.
2. In the flow, click **Add step**.
3. Click **Send a webhook**.
4. Configure the webhook step.
5. Optionally add later steps that use the webhook response.
6. Optionally run a test.
7. When ready, click **Turn on**.

---

## Webhook configuration options

### 1. Webhook or API URL — required

Enter the full destination URL, including:

```text
http://
```

or

```text
https://
```

Key details:

- The URL must be **static**.
- Variables are **not allowed** in the URL for security reasons.
- The URL is stored securely.

---

### 2. Method — required

Choose the HTTP method for the request. The default is **POST**.

| Method | Purpose |
|---|---|
| **GET** | Retrieve data from a URL. |
| **POST** | Send data to create something, like a message or record. |
| **PUT** | Send data to replace existing data. |
| **PATCH** | Send data to do a partial update. |
| **DELETE** | Remove data. |

---

### 3. Payload — optional

The payload is the request body content.

Key details:

- Payloads are ignored for **GET** requests.
- Payloads are sent as **plain text**.
- Any format can be used, but Google recommends **JSON** for web services.
- If variables are inserted into the payload, ensure their content does **not break the payload format**.

> **Note:** Payload is sent as plain text. You can use any format, but we recommend using JSON format to easily send data to web services. If you use a variable to add content to the payload, make sure the variable’s content doesn't break the payload’s format.

---

## Using the webhook response

After the webhook runs, the webhook step outputs the response as **plain text** in a variable.

You can use this variable in later steps, including:

- Adding the raw response to another step
- Using an **AI-powered step** to clean up the response
- Extracting specific content from the response

---

## Test runs

You can test the flow before turning it on:

1. Click **Test run**.
2. Select the starting conditions.
3. Click **Start**.

Important behavior:

- A test run runs the flow **once**.
- It takes **real actions**, so you can verify the actual outcome.

---

## Example payloads

| **Method** | **Example payload** |
|---|---|
| POST | `{`<br>` "text": "Hello world!"`<br>` }` |
| GET | `payload is ignored for GET requests` |
| PUT | `{`<br>` "contactId": " _<variable>_",`<br>` "email": "dana@example.com"`<br>` }` |
| DELETE | `{`<br>` "recordId": " _<variable>_",`<br>` }` |
| PATCH | `{`<br>` "recordId": " _<variable>_",`<br>` }` |

---

## Monitor webhook activity

After a flow runs, check the **Activity** tab to review webhook activity.

If the webhook worked, you can see:

- The data that was sent
- The response that was returned

If the webhook had issues, you can see:

- An error message
- The full error code
- The response from the destination URL

This information can help troubleshoot problems with the webhook destination or request.
