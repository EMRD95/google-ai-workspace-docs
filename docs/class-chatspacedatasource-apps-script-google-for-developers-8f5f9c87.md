---
title: "Class ChatSpaceDataSource  |  Apps Script  |  Google for Developers"
source_url: "https://developers.google.com/apps-script/reference/card-service/chat-space-data-source"
product_area: "apps-script-ai"
retrieved_at: "2026-06-15T18:21:14Z"
extraction_method: "web_extract"
---

# Google Apps Script Card Service: `ChatSpaceDataSource`

**Source:** [Google Developers — Class ChatSpaceDataSource](https://developers.google.com/apps-script/reference/card-service/chat-space-data-source)  
**Last updated:** 2026-04-13 UTC

## Overview

`ChatSpaceDataSource` is an Apps Script Card Service class used to populate a **multiselect menu** with **Google Chat spaces**.

Key behavior:

- Populates selection items with Google Chat spaces.
- Only includes spaces that the current user is a member of.
- Available **only for Google Chat apps**.
- **Not available** for Google Workspace add-ons.

## Key Excerpt

> A data source that populates Google Chat spaces as selection items for a multiselect menu. Only populates spaces that the user is a member of.

## Example Usage

```javascript
const chatSpaceDataSource =
    CardService.newChatSpaceDataSource().setDefaultToCurrentSpace(true);
```

## Availability

> Only available for Google Chat apps. Not available for Google Workspace add-ons.

## Methods

| Method | Return type | Description |
|---|---:|---|
| `setDefaultToCurrentSpace(defaultToCurrentSpace)` | `ChatSpaceDataSource` | If set to `true`, the multiselect menu selects the current Google Chat space as an item by default. |

## `setDefaultToCurrentSpace(defaultToCurrentSpace)`

Configures whether the current Google Chat space should be selected by default in the multiselect menu.

### Key Excerpt

> If set to `true`, the multi select menu selects the current Google Chat space as an item by default.

### Example

```javascript
const chatSpaceDataSource =
    CardService.newChatSpaceDataSource().setDefaultToCurrentSpace(true);
```

### Parameters

| Name | Type | Description |
|---|---:|---|
| `defaultToCurrentSpace` | `Boolean` | The boolean value to be set. |

### Return Value

```text
ChatSpaceDataSource — This object, for chaining.
```

## Practical Notes

- Use `CardService.newChatSpaceDataSource()` to create a new `ChatSpaceDataSource`.
- Use `.setDefaultToCurrentSpace(true)` when you want the current Chat space preselected.
- The method supports chaining because it returns the same `ChatSpaceDataSource` object.
- This class is specifically intended for Google Chat app card interfaces that use multiselect menus.
