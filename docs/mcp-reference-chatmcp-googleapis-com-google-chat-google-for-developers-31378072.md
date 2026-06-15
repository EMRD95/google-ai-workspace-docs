---
title: "MCP Reference: chatmcp.googleapis.com  |  Google Chat  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/api/reference/mcp"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:18:54Z"
extraction_method: "web_extract"
---

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
