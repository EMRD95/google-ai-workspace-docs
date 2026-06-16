---
title: "Combined source: external_drawio"
product_area: "external_drawio"
source_count: 3
generated_at: "2026-06-16T08:47:02Z"
source_type: "coverage_merged_official_extracts"
---

# Combined source: external_drawio

This file merges 3 official extracted source document(s) from coverage area `external_drawio` for NotebookLM import limits.
No synthetic documentation is added; each section preserves the source URL and extracted Markdown body.

## Source index

1. Customise LLM backends for diagram generation in draw.io — https://www.drawio.com/doc/faq/configure-ai-options
2. Generate and validate draw.io diagrams with AI — https://www.drawio.com/docs/reference/diagram-generation/
3. Manually edit the XML source of your draw.io diagram — https://www.drawio.com/docs/manual/advanced/diagram-source-edit/

---

## Source 1: Customise LLM backends for diagram generation in draw.io

- Source URL: https://www.drawio.com/doc/faq/configure-ai-options
- Original file: `docs/customise-llm-backends-for-diagram-generation-in-draw-io-94f9d0dd.md`
- Product area: `external_drawio`

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

---

## Source 2: Generate and validate draw.io diagrams with AI

- Source URL: https://www.drawio.com/docs/reference/diagram-generation/
- Original file: `docs/generate-and-validate-draw-io-diagrams-with-ai-fcb0e59b.md`
- Product area: `external_drawio`

# Generate and validate draw.io diagrams with AI

Source: https://www.drawio.com/docs/reference/diagram-generation/

## Overview

draw.io diagram files (`.drawio`) use a well-defined XML format that AI systems can generate and validate programmatically. Two reference documents are provided to help AI models produce correct diagram files.

- **draw.io Style Reference** — Comprehensive guide covering `.drawio` file structure, style properties, shape types, edge routing, colors, HTML labels, layers, groups, and examples.
- **mxfile.xsd** — XML Schema Definition for validating `.drawio` file structure.

## draw.io MCP Server Integration Options

Four approaches provided by the draw.io MCP server, all sharing a common XML generation reference:

| Approach | What it does | Production endpoint |
|----------|--------------|---------------------|
| MCP App Server | Renders diagrams inline in AI chat as an interactive viewer | mcp.draw.io/mcp |
| MCP Tool Server | Opens diagrams in the draw.io editor in browser; supports XML, CSV, and Mermaid | @drawio/mcp on npm |
| Skill + CLI | Generates native .drawio files with optional PNG/SVG/PDF export via draw.io Desktop CLI | Copy skill file to Claude Code |
| Project Instructions | Claude generates draw.io URLs via Python; no installation required | Paste into Claude Project |

All approaches share the same XML generation rules via shared/xml-reference.md covering edge routing, containers, layers, tags, metadata, dark mode, and style properties.

## File Format Overview

A full `.drawio` file is XML:

```
<mxfile>
  <diagram id="page-1" name="Page-1">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- Diagram elements go here with parent="1" -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

### Core Concepts

- Diagram elements are `mxCell` elements
- Shapes use `vertex="1"`
- Connectors use `edge="1"`
- Visual appearance via `style` attribute (semicolon-separated `key=value` pairs)
- Example: `rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;`

## Simplified Format: mxGraphModel Only

AI may generate only the `<mxGraphModel>` element without `<mxfile>` and `<diagram>` wrappers:

```
<mxGraphModel adaptiveColors="auto">
  <root>
    <mxCell id="0" />
    <mxCell id="1" parent="0" />
    <mxCell id="2" value="Hello" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
      <mxGeometry x="100" y="100" width="120" height="60" as="geometry" />
    </mxCell>
  </root>
</mxGraphModel>
```

- draw.io accepts both formats; it auto-wraps bare `<mxGraphModel>`
- Recommended for AI when multi-page diagrams are not needed

## File-Level Variables

`<mxfile>` supports a `vars` attribute with JSON key-value pairs. Variables are referenced in labels/tooltips using `%variableName%`. Set `placeholders="1"` on `UserObject` or as a style property for substitution.

## Key Rules for AI Generation

1. Always include the two structural cells — `id="0"` (root container) and `id="1" parent="0"` (default layer)
2. Use uncompressed XML — AI should generate plain XML, not compressed/Base64
3. All IDs must be unique within a diagram
4. Vertices need `vertex="1"`, edges need `edge="1"` — mutually exclusive

## URL Encoding for Draw.io Editor

To open an AI-generated diagram directly in draw.io, compress the XML and pass it via URL hash using `#create` parameter.

## Inline Viewer

To display a diagram inline in a web page without the full editor, use the draw.io viewer library: load `viewer-static.min.js` from CDN, then use `<div class="mxgraph">` with diagram config in `data-mxgraph` attribute.

---

## Source 3: Manually edit the XML source of your draw.io diagram

- Source URL: https://www.drawio.com/docs/manual/advanced/diagram-source-edit/
- Original file: `docs/manually-edit-the-xml-source-of-your-draw-io-diagram-4fc58f94.md`
- Product area: `external_drawio`

# Manually edit the XML source of your draw.io diagram

Source: https://www.drawio.com/docs/manual/advanced/diagram-source-edit/

## Overview

The shapes, connectors, styles, and metadata in your diagram, and even which shape libraries are currently displayed, are all described in XML code. In draw.io, you can view the XML source of each page in a multi-page diagram, and edit it directly.

## Edit the Diagram Source Code

1. Select **Extras > Edit Diagram** from the draw.io menu to see the XML source of your diagram, which starts and ends with the `<mxGraphModel>` tags.

2. Edit the diagram source to add or remove elements, restyle shapes and connectors, modify layers, edit shape metadata, set global diagram options, and more. You may find it easier to copy all of the XML code into an appropriate editor with contextual highlighting.

3. When finished, select how you want the changes saved from the drop-down list:
   - **Replace existing drawing**
   - **Open in New Window**
   - **Add to Existing Drawing** (similar to import)

4. Click **OK** to save (or **Cancel** to discard).

---
