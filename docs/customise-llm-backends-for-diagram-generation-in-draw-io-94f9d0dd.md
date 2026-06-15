---
title: "Customise LLM backends for diagram generation in draw.io"
source_url: "https://www.drawio.com/doc/faq/configure-ai-options"
product_area: "external_drawio"
retrieved_at: "2026-06-15T00:00:00Z"
extraction_method: "web_extract"
---

# Customise LLM Backends for Diagram Generation in draw.io

Source: https://www.drawio.com/doc/faq/configure-ai-options

## Overview

draw.io supports configuring custom LLM backends for AI-powered diagram generation. Users can bring their own API keys, custom endpoints, self-hosted LLMs, custom models, and customized system prompts.

## Important Limitation

Custom AI backends **do not work** in the Forge version of draw.io for Confluence Cloud or Jira Cloud — Atlassian's Content Security Policy blocks browser requests to third-party AI endpoints.

## Use Cases

1. **Private API Keys** — Use your own keys instead of draw.io's public backend (ChatGPT, Gemini, Claude)
2. **Custom Models** — Add support for new or custom AI models
3. **Self-Hosted LLMs** — Point to your own compatible LLM infrastructure
4. **Custom Prompts** — Tailor AI behavior to your workflow
5. **Enterprise Deployment** — Align with organizational AI policies

## Core Configuration Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `enableAi` | Enables AI diagram generation in templates, menus, toolbar, search | `true` (only on app.diagrams.net) |
| `gptApiKey` | ChatGPT API key | `null` |
| `gptUrl` | API endpoint for ChatGPT | `https://api.openai.com/v1/chat/completions` |
| `geminiApiKey` | Gemini API key | `null` |
| `claudeApiKey` | Claude API key | `null` |

## AI Actions

Selectable actions in the Generate dialog dropdown. Default: `['createPublic', 'create', 'update', 'assist']`

| Action Key | Dropdown Label | Description |
|------------|----------------|-------------|
| `createPublic` | Create Diagram (draw.io) | Uses public AI backend; diagram data cached on backend |
| `create` | Create Diagram | Generates new diagrams from prompts using your configured LLM |
| `update` | Prompt with Diagram / Prompt with Selection | Sends diagram/selection data with the prompt |
| `assist` | Prompt Only | Sends only the prompt, no diagram context |

## Clipboard Actions (No AI Config Required)

These actions allow use of an external AI tool to modify diagrams via XML copy/paste:

| Action | Behavior | Enable Condition |
|--------|----------|------------------|
| Copy diagram to clipboard | Copies full `mxGraphModel` XML with all cell IDs | Diagram not empty |
| Copy selection to clipboard | Copies XML of selected cells only | Cells selected |
| Update diagram from clipboard | Reads XML from clipboard, computes diff, applies changes | Clipboard has valid `mxGraphModel` XML |
| Insert diagram from clipboard | Inserts clipboard XML as new cells (no modification of existing) | Clipboard has valid `mxGraphModel` XML |

### Typical External AI Workflow

1. Select **Copy diagram to clipboard** (or **Copy selection to clipboard**)
2. Paste the XML into your preferred AI tool and describe the changes you want
3. Copy the AI's modified XML response
4. Select **Update diagram from clipboard** to apply changes, or **Insert diagram from clipboard** to add as new cells

## Global Placeholders & System Prompts (`aiGlobals`)

`aiGlobals` defines global placeholders for AI requests. The `{data}` placeholder contains the diagram/selection XML. Default includes API key references and system instructions for `create`, `update`, and `assist` actions.

## Custom AI Models (`aiConfigs` / `aiModels`)

- **`aiModels`** — Array of selectable AI models. Each references a key in `aiConfigs`.
- **`aiConfigs`** — Object mapping model names to their configuration (API key, endpoint, request/response formatting, system prompts).

Supports placeholders: `{data}`, `{model}`, `{apiKey}`, `{prompt}`, and custom keys from `aiGlobals`.

### Gemini Configuration Example

```
geminiApiKey: "YOUR_API_KEY"
aiModels: [{name: "Gemini 2.5", model: "gemini-2.5-flash", config: "gemini"}]
aiConfigs:
  gemini:
    apiKey: "geminiApiKey"
    endpoint: "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    requestHeaders:
      X-Goog-Api-Key: "{apiKey}"
    request:
      contents: [{parts: [{text: "{prompt}"}]}]
    responsePath: "$.candidates[0].content.parts[0].text"
```

### Claude Configuration Example

```
claudeApiKey: "YOUR_API_KEY"
aiModels: [{name: "Claude", model: "claude-sonnet-4-20250514", config: "claude"}]
aiConfigs:
  claude:
    apiKey: "claudeApiKey"
    endpoint: "https://api.anthropic.com/v1/messages"
    requestHeaders:
      X-API-Key: "{apiKey}"
      Anthropic-Version: "2023-06-01"
      Anthropic-Dangerous-Direct-Browser-Access: "true"
    request:
      max_tokens: 8192
      model: "{model}"
      messages:
        - {role: "assistant", content: "{action}"}
        - {role: "user", content: "{prompt}"}
    responsePath: "$.content[0].text"
```
