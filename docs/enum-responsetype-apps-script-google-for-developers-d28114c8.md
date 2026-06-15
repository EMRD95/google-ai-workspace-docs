---
title: "Enum ResponseType  |  Apps Script  |  Google for Developers"
source_url: "https://developers.google.com/apps-script/reference/card-service/response-type"
product_area: "apps-script-ai"
retrieved_at: "2026-06-15T18:20:14Z"
extraction_method: "web_extract"
---

# Google Apps Script Card Service: `ResponseType` Enum

**Source:** Google Developers — Apps Script Reference  
**Page:** `Enum ResponseType`  
**URL:** https://developers.google.com/apps-script/reference/card-service/response-type  
**Last updated:** **2026-04-13 UTC**

---

## Overview

`ResponseType` is an enum in Apps Script’s **Card Service** that defines the type of response a **Google Chat app** returns.

> An enum that represents the type of Chat app response.

**Availability:**

- **Only available for Google Chat apps**
- **Not available for Google Workspace add-ons**

---

## How to Reference the Enum

To use an enum value, reference its parent class, enum name, and property.

```js
CardService.Type.DIALOG
```

> To call an enum, you call its parent class, name, and property. For example, `CardService.Type.DIALOG`.

---

## `ResponseType` Properties

| Property | Type | Description |
|---|---:|---|
| `TYPE_UNSPECIFIED` | `Enum` | Default type that's handled as `NEW_MESSAGE`. |
| `NEW_MESSAGE` | `Enum` | Post as a new message in the topic. |
| `UPDATE_MESSAGE` | `Enum` | Update the Chat app's message. This is only permitted on a `CARD_CLICKED` event where the message sender type is `BOT`. |
| `UPDATE_USER_MESSAGE_CARDS` | `Enum` | Update the cards on a user's message. This is only permitted as a response to a `MESSAGE` event with a matched URL, or a `CARD_CLICKED` event where the message sender type is `HUMAN`. Text is ignored. |
| `REQUEST_CONFIG` | `Enum` | Privately ask the user for additional authentication or configuration. |
| `DIALOG` | `Enum` | Presents a dialog. |
| `UPDATE_WIDGET` | `Enum` | Widget text autocomplete options query. |

---

## Usage Notes & Constraints

- `TYPE_UNSPECIFIED` behaves the same as `NEW_MESSAGE`.
- `NEW_MESSAGE` posts a new message in the current Chat topic.
- `UPDATE_MESSAGE` can only update a Chat app’s own message when:
  - The event is `CARD_CLICKED`
  - The message sender type is `BOT`
- `UPDATE_USER_MESSAGE_CARDS` updates cards attached to a user’s message and is only allowed:
  - In response to a `MESSAGE` event with a matched URL, or
  - In response to a `CARD_CLICKED` event where the message sender type is `HUMAN`
  - Any text in the response is ignored.
- `REQUEST_CONFIG` is used to privately request authentication or configuration from the user.
- `DIALOG` presents a dialog to the user.
- `UPDATE_WIDGET` is used for widget text autocomplete option queries.

---

## Licensing

- Page content is licensed under the **Creative Commons Attribution 4.0 License**.
- Code samples are licensed under the **Apache 2.0 License**.
- Java is a registered trademark of Oracle and/or its affiliates.
