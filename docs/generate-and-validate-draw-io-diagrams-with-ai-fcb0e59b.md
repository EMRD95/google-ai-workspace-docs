---
title: "Generate and validate draw.io diagrams with AI"
source_url: "https://www.drawio.com/docs/reference/diagram-generation/"
product_area: "external_drawio"
retrieved_at: "2026-06-15T00:00:00Z"
extraction_method: "web_extract"
---

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
