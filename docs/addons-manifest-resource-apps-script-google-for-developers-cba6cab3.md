---
title: "AddOns manifest resource  |  Apps Script  |  Google for Developers"
source_url: "https://developers.google.com/apps-script/manifest/addons"
product_area: "apps-script-ai"
retrieved_at: "2026-06-15T18:21:14Z"
extraction_method: "web_extract"
---

# AddOns Manifest Resource — Google Apps Script / Google Workspace Add-ons

**Source:** https://developers.google.com/apps-script/manifest/addons  
**Last updated:** 2026-04-20 UTC

## Overview

The **`AddOns` manifest resource** defines the **content and behavior** of a **Google Workspace add-on** in Apps Script.

> “The resource configuration that is used to define Google Workspace add-on content and behavior. add-on manifests must include all components marked as **Required**.”

A Google Workspace add-on manifest can include configuration for multiple host applications:

- Google Calendar
- Google Chat
- Google Drive
- Gmail
- Google Docs
- Google Sheets
- Google Slides
- Google Meet

The manifest contains:

- A required `common` section for shared/default configuration.
- Optional host-specific sections, required only if the add-on extends that host.
- UI and behavior settings such as:
  - Homepage trigger
  - Toolbar name and logo
  - Layout colors
  - Allowed outbound link prefixes
  - Universal actions
  - Locale/timezone event behavior

---

## Top-Level `AddOns` Configuration

The `AddOns` object is the top-level manifest configuration for a Google Workspace add-on.

### JSON Representation

```json
{
  "common": {
    object (Common)
  },
  "calendar": {
    object (Calendar)
  },
  "chat": {
    object (Chat)
  },
  "drive": {
    object (Drive)
  },
  "gmail": {
    object (Gmail)
  },
  "docs": {
    object (Docs)
  },
  "sheets": {
    object (Sheets)
  },
  "slides": {
    object (Slides)
  },
  "meet": {
    object (Meet)
  }
}
```

---

## `AddOns` Fields

### `common`

**Type:** `object (Common)`  
**Required.**

Defines values common to every host application.

> “Values defined here serve as defaults when specific values for a particular host are omitted.”

---

### `calendar`

**Type:** `object (Calendar)`  
**Required if the add-on extends Calendar.**

Defines appearance and behavior in Google Calendar.

If omitted, the add-on is disabled in Calendar.

---

### `chat`

**Type:** `object ()`  
**Required if the add-on extends Chat.**

Configures Google Chat app support.

Important requirement:

> “The `addOns.chat` object must be empty.”

To configure Chat behavior and appearance, use the separate Google Chat app configuration.

If omitted, the add-on is disabled in Google Chat.

---

### `drive`

**Type:** `object (Drive)`  
**Required if the add-on extends Drive.**

Defines appearance and behavior in Google Drive.

If omitted, the add-on is disabled in Drive.

---

### `gmail`

**Type:** `object (Gmail)`  
**Required if the add-on extends Gmail.**

Defines appearance and behavior in Gmail.

If omitted, the add-on is disabled in Gmail.

---

### `docs`

**Type:** `object (Docs)`  
**Required if the add-on extends Docs.**

Defines appearance and behavior in Google Docs.

If omitted, the add-on is disabled in Docs.

---

### `sheets`

**Type:** `object (Sheets)`  
**Required if the add-on extends Sheets.**

Defines appearance and behavior in Google Sheets.

If omitted, the add-on is disabled in Sheets.

---

### `slides`

**Type:** `object (Slides)`  
**Required if the add-on extends Slides.**

Defines appearance and behavior in Google Slides.

If omitted, the add-on is disabled in Slides.

---

### `meet`

**Type:** `object (Meet)`  
**Required if the add-on extends Meet.**

Defines appearance and behavior in Google Meet.

If omitted, the add-on is disabled in Meet.

---

## `Common` Configuration

The `Common` object defines manifest parameters shared across all host applications.

> “Values defined here serve as defaults when specific values for a host are omitted.”

### JSON Representation

```json
{
  "homepageTrigger": {
    object (HomepageTrigger)
  },
  "layoutProperties": {
    object (LayoutProperties)
  },
  "logoUrl": string,
  "name": string,
  "openLinkUrlPrefixes": [
    string
  ],
  "universalActions": [
    {
      object (UniversalAction)
    }
  ],
  "useLocaleFromApp": boolean
}
```

---

## `Common` Fields

### `homepageTrigger`

**Type:** `object (HomepageTrigger)`

Defines the default trigger function for the add-on homepage.

Used when a host-specific homepage trigger is not defined.

If omitted:

> “a generic homepage card is used.”

---

### `layoutProperties`

**Type:** `object (LayoutProperties)`

Configures colors used in the add-on toolbar and buttons.

---

### `logoUrl`

**Type:** `string`  
**Required.**

The public URL of the toolbar image.

---

### `name`

**Type:** `string`  
**Required.**

The add-on name shown in the toolbar.

---

### `openLinkUrlPrefixes[]`

**Type:** `string`  
**Conditionally required.**

Required if the add-on displays outbound links using:

- An [`OpenLink`](https://developers.google.com/apps-script/reference/card-service/open-link)
- HTML anchor tags in a text widget

Purpose:

> “To protect user data, links rendered by the add-on must match a prefix in this list.”

Requirements:

- Must be a list of **HTTPS URL prefixes**.

[... summary truncated for context management ...]
