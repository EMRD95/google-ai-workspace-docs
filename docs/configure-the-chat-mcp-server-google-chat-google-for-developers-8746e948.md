---
title: "Configure the Chat MCP server  |  Google Chat  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/api/guides/configure-mcp-server"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:17:54Z"
extraction_method: "web_extract"
---

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
