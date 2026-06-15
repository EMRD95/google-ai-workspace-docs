---
title: "Class ChatActionResponse  |  Apps Script  |  Google for Developers"
source_url: "https://developers.google.com/apps-script/reference/card-service/chat-action-response"
product_area: "apps-script-ai"
retrieved_at: "2026-06-15T18:20:14Z"
extraction_method: "web_extract"
---

# Class `ChatActionResponse` — Apps Script Card Service

**Source:** https://developers.google.com/apps-script/reference/card-service/chat-action-response  
**Last updated:** 2026-04-13 UTC  
**Product area:** Google Workspace → Apps Script → Card Service → Google Chat apps

---

## Overview

`ChatActionResponse` represents the parameters a **Google Chat app** can use to configure how its response is posted.

> A class that represents the parameters that a Chat app can use to configure how its response is posted.

**Availability:**

- ✅ Available for **Google Chat apps**
- ❌ Not available for **Google Workspace add-ons**

This class is commonly used to:

- Open or interact with a **dialog**
- Set the **response type** for a Chat app response
- Provide **autocomplete options** by updating a widget
- Send users to a URL for **authentication or configuration**

Each method returns the same `ChatActionResponse` object, enabling **method chaining**.

---

## Basic Example: Open a Dialog

```javascript
const card = CardService.newCardBuilder()
                 .setHeader(CardService.newCardHeader().setTitle('Card title'))
                 .build();
const dialog = CardService.newDialog().setBody(card);

const dialogAction = CardService.newDialogAction().setDialog(dialog);

const chatActionResponse = CardService.newChatActionResponse()
                               .setResponseType(CardService.Type.DIALOG)
                               .setDialogAction(dialogAction);
```

This creates a card, wraps it in a dialog, creates a dialog action, and configures a Chat action response to show the dialog.

---

## Methods Summary

| Method | Return type | Description |
|---|---:|---|
| `setDialogAction(dialogAction)` | `ChatActionResponse` | Sets the dialog action to an event related to a dialog. |
| `setResponseType(responseType)` | `ChatActionResponse` | Sets the type of Chat app response. |
| `setUpdatedWidget(updatedWidget)` | `ChatActionResponse` | Sets an updated widget, typically used to provide autocomplete options. |
| `setUrl(url)` | `ChatActionResponse` | Sets a URL for users to authenticate or configure. Used with `REQUEST_CONFIG`. |

---

## Detailed Method Reference

### `setDialogAction(dialogAction)`

Sets the dialog action to an event related to a dialog.

```javascript
const card = CardService.newCardBuilder()
                 .setHeader(CardService.newCardHeader().setTitle('Card title'))
                 .build();
const dialog = CardService.newDialog().setBody(card);

const dialogAction = CardService.newDialogAction().setDialog(dialog);

const chatActionResponse = CardService.newChatActionResponse()
                               .setResponseType(CardService.Type.DIALOG)
                               .setDialogAction(dialogAction);
```

#### Parameter

| Name | Type | Description |
|---|---|---|
| `dialogAction` | `DialogAction` | The dialog action to set. |

#### Return

`ChatActionResponse` — This object, for chaining.

---

### `setResponseType(responseType)`

Sets the type of Chat app response.

```javascript
const chatActionResponse = CardService.newChatActionResponse().setResponseType(
    CardService.Type.DIALOG,
);
```

#### Parameter

| Name | Type | Description |
|---|---|---|
| `responseType` | `ResponseType` | The response type. |

#### Return

`ChatActionResponse` — This object, for chaining.

---

### `setUpdatedWidget(updatedWidget)`

Sets the updated widget, used to provide autocomplete options for a widget.

**Availability:**

- ✅ Google Chat apps only
- ❌ Not available for Google Workspace add-ons

```javascript
const updatedWidget =
    CardService.newUpdatedWidget()
        .addItem(
            'Contact 1',
            'contact-1',
            false,
            'https://www.gstatic.com/images/branding/product/2x/contacts_48dp.png',
            'Contact one description',
            )
        .addItem(
            'Contact 2',
            'contact-2',
            false,
            'https://www.gstatic.com/images/branding/product/2x/contacts_48dp.png',
            'Contact two description',
            )
        .addItem(
            'Contact 3',
            'contact-3',
            false,
            'https://www.gstatic.com/images/branding/product/2x/contacts_48dp.png',
            'Contact three description',
            )
        .addItem(
            'Contact 4',
            'contact-4',
            false,
            'https://www.gstatic.com/images/branding/product/2x/contacts_48dp.png',
            'Contact four description',
            )
        .addItem(
            'Contact 5',
            'contact-5',
            false,
            'https://www.gstatic.com/images/branding/product/2x/contacts_48dp.png',
            'Contact five description',
        );

const actionResponse =
    CardService.newChatActionResponse()
        .setUpdatedWidget(updatedWidget)
        .setResponseType(CardService.ResponseType.UPDATE_WIDGET);
```

#### Parameter

| Name | Type | Description |


[... summary truncated for context management ...]
