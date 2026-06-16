---
title: "Combined source: apps-script-ai"
product_area: "apps-script-ai"
source_count: 11
generated_at: "2026-06-16T08:47:02Z"
source_type: "coverage_merged_official_extracts"
---

# Combined source: apps-script-ai

This file merges 11 official extracted source document(s) from coverage area `apps-script-ai` for NotebookLM import limits.
No synthetic documentation is added; each section preserves the source URL and extracted Markdown body.

## Source index

1. AddOns manifest resource  |  Apps Script  |  Google for Developers — https://developers.google.com/apps-script/manifest/addons
2. Advanced Chat Service  |  Apps Script  |  Google for Developers — https://developers.google.com/apps-script/advanced/chat
3. Advanced Google services  |  Apps Script  |  Google for Developers — https://developers.google.com/apps-script/guides/services/advanced
4. Build a Google Chat app with Google Apps Script  |  Google for Developers — https://developers.google.com/apps-script/quickstart/chat-app
5. Class ChatActionResponse  |  Apps Script  |  Google for Developers — https://developers.google.com/apps-script/reference/card-service/chat-action-response
6. Class ChatResponse  |  Apps Script  |  Google for Developers — https://developers.google.com/apps-script/reference/card-service/chat-response
7. Class ChatSpaceDataSource  |  Apps Script  |  Google for Developers — https://developers.google.com/apps-script/reference/card-service/chat-space-data-source
8. Enum ResponseType  |  Apps Script  |  Google for Developers — https://developers.google.com/apps-script/reference/card-service/response-type
9. Fact-check statements with an ADK AI agent and Gemini model  |  Apps Script  |  Google for Developers — https://developers.google.com/apps-script/samples/custom-functions/fact-check
10. Quickstart: Generate text using Agent Platform  |  Apps Script  |  Google for Developers — https://developers.google.com/apps-script/quickstart/vertex-ai
11. Vertex AI Service  |  Apps Script  |  Google for Developers — https://developers.google.com/apps-script/advanced/vertex-ai

---

## Source 1: AddOns manifest resource  |  Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/apps-script/manifest/addons
- Original file: `docs/addons-manifest-resource-apps-script-google-for-developers-cba6cab3.md`
- Product area: `apps-script-ai`

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

---

## Source 2: Advanced Chat Service  |  Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/apps-script/advanced/chat
- Original file: `docs/advanced-chat-service-apps-script-google-for-developers-549b3688.md`
- Product area: `apps-script-ai`

# Advanced Chat Service for Apps Script — Summary

**Source:** https://developers.google.com/apps-script/advanced/chat  
**Last updated:** 2026-05-04 UTC

## Overview

The **Advanced Chat service** lets Google Apps Script projects use the **Google Chat API**.

It enables scripts to:

- Find, create, and modify Google Chat spaces
- Add or remove members from spaces
- Read or post messages
- Work with message content such as:
  - Text
  - Cards
  - Attachments
  - Reactions

> The Advanced Chat service lets you use the [Google Chat API](https://developers.google.com/chat/api/guides) in Google Apps Script.

This is an **advanced Apps Script service**, so it must be explicitly enabled before use.

---

## Key Requirements

### Prerequisites

To use the Advanced Chat service, you need:

- An **Apps Script Google Chat app** configured in the **Google Cloud console** on the Chat API configuration page.
- The Apps Script project must use a **standard Google Cloud project**, not the default project automatically created by Apps Script.
- Authentication configured for the Chat app.

Authentication depends on how the API action is performed:

| Action type | Required authentication |
|---|---|
| Perform an action on behalf of a user | User authentication |
| Perform an action as the Chat app | App authentication with a service account |

Relevant references:

- [Build a Google Chat app with Google Apps Script](https://developers.google.com/workspace/add-ons/chat/quickstart-apps-script)
- [User authentication](https://developers.google.com/chat/api/guides/auth/users)
- [App authentication with a service account](https://developers.google.com/chat/api/guides/auth/service-accounts)
- [Types of required authentication for Google Chat API calls](https://developers.google.com/chat/api/guides/auth#asynchronous-chat-calls)
- [Turn on advanced services](https://developers.google.com/apps-script/guides/services/advanced)

---

## Reference Behavior

The Advanced Chat service follows the same objects, methods, and parameters as the public **Google Chat API**.

> Like all advanced services in Apps Script, the Chat service uses the same objects, methods, and parameters as the public API.

Main reference:

- [Chat API REST reference](https://developers.google.com/chat/api/reference/rest)

---

# Sample Code

The page provides examples for common Chat API actions using the Apps Script advanced service.

---

## Post a Message with User Credentials

Posts a message to a Chat space **on behalf of the user**.

### Required scope

Add this to the Apps Script project’s `appsscript.json` file:

```json
"oauthScopes": [
     "https://www.googleapis.com/auth/chat.messages.create"
]
```

### Apps Script function

```javascript
/**
    * Posts a new message to the specified space on behalf of the user.
    * @param {string} spaceName The resource name of the space.
    */
function postMessageWithUserCredentials(spaceName) {
     try {
       const message = { text: "Hello world!" };
       Chat.Spaces.Messages.create(message, spaceName);
     } catch (err) {
       // TODO (developer) - Handle exception
       console.log("Failed to create message with error %s", err.message);
     }
}
```

---

## Post a Message with App Credentials

Posts a message to a Chat space **on behalf of the app**.

Important note:

> Using the advanced Chat service with a service account doesn't require you to specify authorization scopes in `appsscript.json`.

This requires app authentication with a service account.

Reference:

- [Authenticate as a Google Chat app](https://developers.google.com/chat/api/guides/auth/service-accounts)

### Apps Script function

```javascript
/**
 * Posts a new message to the specified space on behalf of the app.
 * @param {string} spaceName The resource name of the space.
 */
function postMessageWithAppCredentials(spaceName) {
  try {
    // See https://developers.google.com/chat/api/guides/auth/service-accounts
    // for details on how to obtain a service account OAuth token.
    const appToken = getToken_();
    const message = { text: "Hello world!" };
    Chat.Spaces.Messages.create(
      message,
      spaceName,
      {},
      // Authenticate with the service account token.
      { Authorization: `Bearer ${appToken}` },
    );
  } catch (err) {
    // TODO (developer) - Handle exception
    console.log("Failed to create message with error %s", err.message);
  }
}
```

---

## Get a Space

Gets information about a Chat space.

### Required scope

Add this to `appsscript.json`:

```json
"oauthScopes": [
     "https://www.googleapis.com/auth/chat.spaces.readonly"
]
```

### Apps Script function

```javascript
/**
    * Gets information about a Chat space.
    * @param {string} spaceName The resource name of the space.
    */
function getSpace(spaceName) {
     try {
       const space = Chat.Spaces.get(spaceName);
       console.log("Space display name: %s", space.displayName);
       console.log("Space type: %s", space.space

[... summary truncated for context management ...]

---

## Source 3: Advanced Google services  |  Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/apps-script/guides/services/advanced
- Original file: `docs/advanced-google-services-apps-script-google-for-developers-dafeec53.md`
- Product area: `apps-script-ai`

# Advanced Google Services in Apps Script — Summary

**Source:** Google Developers — Apps Script Guide  
**URL:** https://developers.google.com/apps-script/guides/services/advanced  
**Last updated:** 2026-04-20 UTC

---

## Overview

Advanced Google services in Apps Script let developers connect to certain public Google APIs with less setup than using raw HTTP requests.

> Advanced services are thin wrappers around those Google APIs.

They behave similarly to Apps Script’s built-in services:

- Provide **autocomplete** in the Apps Script editor
- Let Apps Script handle the **authorization flow automatically**
- Use objects, methods, and parameters similar to the underlying public Google APIs
- Must be **explicitly enabled** before use

Advanced services are recommended whenever available, but direct HTTP access through `UrlFetchApp` can be used when an advanced service is unavailable or lacks required functionality.

---

## Key Takeaways

- Advanced services simplify access to supported public Google APIs.
- They must be enabled in the Apps Script project.
- If the script uses a **standard Google Cloud project**, the corresponding API must also be enabled in Google Cloud Console.
- If the script uses the default Apps Script-created Cloud project, the API is enabled automatically when the service is added.
- Advanced services offer easier authorization and autocomplete but may expose only a subset of the full API.
- `UrlFetchApp` provides full API access but requires manually handling authorization, headers, request construction, response parsing, and OAuth scopes.

---

# Enabling Advanced Services

To use an advanced Google service, two enablement steps may be required.

---

## Step 1: Enable the Advanced Service

You can enable an advanced service either through the Apps Script editor or by editing the project manifest.

---

## Method A: Enable Using the Apps Script Editor

1. Open the Apps Script project.
2. In the left sidebar, click **Editor**.
3. Next to **Services**, click **Add a service**.
4. Select an advanced Google service.
5. Click **Add**.

After enabling, the service becomes available in autocomplete.

---

## Method B: Enable Using the Manifest

Advanced services can also be enabled by editing the Apps Script manifest file.

Example: enabling the **Google Drive advanced service**:

```json
{
  "timeZone": "America/Denver",
  "dependencies": {
    "enabledAdvancedServices": [
      {
        "userSymbol": "Drive",
        "version": "v3",
        "serviceId": "drive"
      }
    ]
  },
  "exceptionLogging": "STACKDRIVER",
  "runtimeVersion": "V8"
}
```

Important manifest fields:

- `userSymbol`: The name used in Apps Script code, such as `Drive`
- `version`: API version, such as `v3`
- `serviceId`: Google API service identifier, such as `drive`

---

## Step 2: Enable the Google Cloud API

This step depends on the type of Google Cloud project associated with the Apps Script project.

### If Using the Default Apps Script Cloud Project

Skip this step.

> The API is enabled automatically when you add the service in Step 1.

### If Using a Standard Google Cloud Project

You must manually enable the corresponding API.

Steps:

1. Open the Cloud project associated with your script in the **Google Cloud console**.
2. Use the search bar to search for the API by name, such as `"Calendar"`.
3. Select the API from the results.
4. Click **Enable API**.
5. Return to the Apps Script editor.

---

# How Advanced Service Method Signatures Work

Advanced services generally follow the same:

- Objects
- Method names
- Parameters

as the corresponding public Google APIs.

However, method signatures are translated for Apps Script.

The editor’s autocomplete usually provides enough information to determine how to call a method.

---

## Method Signature Argument Order

Google API requests may include:

- Path parameters
- Query parameters
- Request body
- Media upload attachments
- Specific HTTP request headers

In Apps Script, advanced service method signatures use this order:

1. **Request body**, usually a resource, as a JavaScript object
2. **Path or required parameters**, as individual arguments  
   - If multiple path parameters are required, they appear in the order listed in the API endpoint URL
3. **Media upload attachment**, as a `Blob`
4. **Optional parameters**, typically query parameters, as a JavaScript object
5. **HTTP request headers**, as a JavaScript object

If a method has no item in one of these categories, that part of the signature is omitted.

---

## Important Exceptions

- For methods that accept media uploads, the `uploadType` parameter is set automatically.
- Methods named `delete` in the Google API are renamed to `remove` in Apps Script because `delete` is a reserved JavaScript word.
- If an advanced service accepts HTTP request headers and you set a headers object, you must also set the optional parameters object.
  - If you do not need optional parameters, pass an empty object 

[... summary truncated for context management ...]

---

## Source 4: Build a Google Chat app with Google Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/apps-script/quickstart/chat-app
- Original file: `docs/build-a-google-chat-app-with-google-apps-script-google-for-developers-17092387.md`
- Product area: `apps-script-ai`

# Build a Google Chat App with Google Apps Script — Summary

**Source:** https://developers.google.com/apps-script/quickstart/chat-app  
**Last updated:** 2026-04-20 UTC  
**Goal:** Create a Google Chat app using **Google Apps Script** that can receive direct messages or messages in Chat spaces and respond by echoing user messages.

---

## Page Summary

> Create a Google Chat app that you can directly message and that responds by echoing your messages.

The guide walks through how to:

- Set up a Google Cloud environment.
- Enable the Google Chat API.
- Configure the OAuth consent screen.
- Create an Apps Script project from a Chat App template.
- Create a test deployment and copy its deployment ID.
- Configure the Chat app in the Google Chat API console.
- Test the app in Google Chat.
- Troubleshoot errors and clean up Cloud resources.

---

## Architecture and Message Flow

The app is implemented with **Apps Script**, hosted in **Google Cloud**, and connected to Google Chat.

### Message flow

1. A user sends a message to the Chat app:
   - In a direct message, or
   - In a Chat space.
2. The Chat app logic, implemented in **Apps Script**, receives and processes the message.
3. Optionally, the app can integrate with:
   - Google Workspace services such as **Calendar** or **Sheets**
   - Other Google services such as **Google Maps** or **YouTube**
4. The Apps Script logic sends a response back to the Chat app service.
5. Google Chat delivers the response to the user.

---

## Objectives

By the end of the guide, you should be able to:

- Set up your environment.
- Set up the script.
- Configure the Chat app.
- Test the Chat app.

---

## Prerequisites

You need:

- A **Business or Enterprise Google Workspace account** with access to **Google Chat**.
- A **Google Cloud project**.

Relevant links:

- [Google Workspace account information](https://support.google.com/a/answer/6043576)
- [Google Chat](https://workspace.google.com/products/chat/)
- [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project)

---

# Setup Instructions

## 1. Open Your Cloud Project

If your intended Cloud project is not already open:

1. Go to the **Select a project** page in the Google Cloud console.
2. Select the project you want to use.

Alternatively:

- Click **Create project**.
- Follow the on-screen instructions.
- If required, enable billing for the project.

Links:

- [Select a Cloud project](https://console.cloud.google.com/projectselector2)
- [Enable billing for a project](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)

---

## 2. Enable the Google Chat API

Before using Google APIs, you must enable them in a Google Cloud project.

Action:

- In the Google Cloud console, enable the **Google Chat API**.

Link:

- [Enable the Google Chat API](https://console.cloud.google.com/flows/enableapi?apiid=chat.googleapis.com)

---

## 3. Configure the OAuth Consent Screen

All apps using OAuth 2.0 require a consent screen configuration. This defines what users and app reviewers see and registers the app so it can be published later.

### Open OAuth Branding

1. In the Google API Console, go to:

   **Menu > Google Auth platform > Branding**

2. If the Google Auth platform is already configured, update settings in:
   - **Branding**
   - **Audience**
   - **Data Access**

3. If you see:

> **Google Auth platform not configured yet**

Click **Get Started**.

Link:

- [Go to Branding](https://console.developers.google.com/auth/branding)

### OAuth Consent Setup Steps

1. Under **App Information**, in **App name**, enter a name for the app.
2. In **User support email**, choose a support email address.
3. Click **Next**.
4. Under **Audience**, select **Internal**.
5. Click **Next**.
6. Under **Contact Information**, enter an **Email address** for project notifications.
7. Click **Next**.
8. Under **Finish**, review the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy).
9. If you agree, select:

> **I agree to the Google API Services: User Data Policy**

10. Click **Continue**.
11. Click **Create**.

### Scopes Note

For this quickstart:

- You can skip adding scopes.

For future apps used outside your Google Workspace organization:

- Change **User type** to **External**.
- Add the authorization scopes required by your app.

Reference:

- [Configure OAuth consent](https://developers.google.com/workspace/guides/configure-oauth-consent)

---

# Set Up the Apps Script Project

## 4. Create the Script from the Template

Use the Apps Script Chat App template.

Steps:

1. Go to the [Apps Script Getting Started page](https://script.google.com/home/start).
2. Click the **Chat App** template at the top of the page.
3. Click **Untitled project**.
4. Rename it to:

```text
Quickstart app
```

5. Click **Rename**.

### Cloud Project Association Note

For this guide, you **don’t need** to associate your Cloud proje

[... summary truncated for context management ...]

---

## Source 5: Class ChatActionResponse  |  Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/apps-script/reference/card-service/chat-action-response
- Original file: `docs/class-chatactionresponse-apps-script-google-for-developers-f864351f.md`
- Product area: `apps-script-ai`

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

---

## Source 6: Class ChatResponse  |  Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/apps-script/reference/card-service/chat-response
- Original file: `docs/class-chatresponse-apps-script-google-for-developers-d78c2723.md`
- Product area: `apps-script-ai`

[Skip to main content](https://developers.google.com/apps-script/reference/card-service/chat-response#main-content)

[![Google Workspace](https://www.gstatic.com/images/branding/productlogos/googleg_gradient/v1/16px.svg)](https://developers.google.com/workspace)

- [GoogleWorkspace](https://developers.google.com/workspace)

`/`

- English
- Deutsch
- Español
- Español – América Latina
- Français
- Indonesia
- Italiano
- Polski
- Português – Brasil
- Tiếng Việt
- Türkçe
- Русский
- עברית
- العربيّة
- فارسی
- हिंदी
- বাংলা
- ภาษาไทย
- 中文 – 简体
- 中文 – 繁體
- 日本語
- 한국어

Sign in

- [Apps Script](https://developers.google.com/apps-script)

- [Home](https://developers.google.com/)
- [Google Workspace](https://developers.google.com/workspace)
- [Apps Script](https://developers.google.com/apps-script)
- [Reference](https://developers.google.com/apps-script/reference)



 Send feedback



# Class ChatResponse    Stay organized with collections      Save and categorize content based on your preferences.

![Spark icon](https://developers.google.com/_static/images/icons/spark.svg)

## Page Summary

outlined\_flag

- ChatResponse is the response object for a card message in Google Chat, available only for Google Chat apps.

- You can create a ChatResponse using `CardService.newChatResponseBuilder()`, adding text and cards using `setText()` and `addCardsV2()`.

- The `printJson()` method is available for debugging and prints the JSON representation of the ChatResponse object.


ChatResponse

The response object for a card message in Google Chat.

Only available for Google Chat apps. Not available for Google Workspace add-ons.

```
// Creates a card message in Chat.
const cardHeader = CardService.newCardHeader()
                       .setTitle('Card Header Title')
                       .setSubtitle('Card Header Subtitle');

const card = CardService.newCardBuilder().setHeader(cardHeader).build();

const chatResponse =
    CardService.newChatResponseBuilder()
        .setText('Example text')
        .addCardsV2(
            CardService.newCardWithId().setCardId('card_id').setCard(card))
        .build();

console.log(chatResponse.printJson());
```

### Methods

| Method | Return type | Brief description |
| --- | --- | --- |
| `printJson()` | `String` | Prints the JSON representation of this object. |

## Detailed documentation

### `printJson()`

Prints the JSON representation of this object. This is for debugging only.

#### Return

`String`



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-13 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-04-13 UTC."\],\[\],\["The \`ChatResponse\` object, exclusive to Google Chat apps, facilitates the creation of card messages. It is not for Google Workspace add-ons. You can build card messages using methods like \`newCardHeader()\` and \`newCardBuilder()\`. \`newChatResponseBuilder()\` builds the ChatResponse by adding text and cards. \`printJson()\` outputs the JSON representation of the constructed \`ChatResponse\` object, for debugging purposes.\\n"\]\]

---

## Source 7: Class ChatSpaceDataSource  |  Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/apps-script/reference/card-service/chat-space-data-source
- Original file: `docs/class-chatspacedatasource-apps-script-google-for-developers-8f5f9c87.md`
- Product area: `apps-script-ai`

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

---

## Source 8: Enum ResponseType  |  Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/apps-script/reference/card-service/response-type
- Original file: `docs/enum-responsetype-apps-script-google-for-developers-d28114c8.md`
- Product area: `apps-script-ai`

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

---

## Source 9: Fact-check statements with an ADK AI agent and Gemini model  |  Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/apps-script/samples/custom-functions/fact-check
- Original file: `docs/fact-check-statements-with-an-adk-ai-agent-and-gemini-model-apps-script-google-for-d-37d81ba6.md`
- Product area: `apps-script-ai`

# Fact-check statements with an ADK AI agent and Gemini model — Markdown Summary

**Source:** Google for Developers — Apps Script sample  
**URL:** https://developers.google.com/apps-script/samples/custom-functions/fact-check  
**Last updated:** 2026-04-20 UTC  
**Coding level:** Advanced  
**Duration:** 30 minutes  
**Project type:** [Custom function](https://developers.google.com/apps-script/guides/sheets/functions)

---

## Overview

This guide shows how to create a **Google Sheets custom function** named `FACT_CHECK` using a **container-bound Google Apps Script project**, powered by:

- A **Vertex AI Agent Engine ADK agent** for reasoning.
- A **Gemini model from Vertex AI** for output formatting and text generation.

The function lets users fact-check statements directly in Google Sheets.

> “A fact-check custom function for Google Sheets to be used as a bound Google Apps Script project powered by a Vertex AI agent and Gemini model.”

The sample demonstrates two AI capabilities inside Sheets:

1. **AI agents** for sophisticated, multi-tool, multi-step reasoning using ADK agents deployed in Vertex AI Agent Engine.
2. **AI models** for advanced understanding, generation, and summarization using Gemini models from Vertex AI.

---

## What the Solution Does

The custom function analyzes a statement, grounds the response using recent web information, and returns the result in the requested format.

### Function Name

```text
FACT_CHECK
```

### Usage

```text
=FACT_CHECK("Your statement here")
```

Returns a concise, summarized fact-check result.

```text
=FACT_CHECK("Your statement here", "Your output formatting instructions here")
```

Returns a fact-check result formatted according to the second argument.

### AI Components

- **Reasoning:** [LLM Auditor ADK AI Agent — Python sample](https://github.com/google/adk-samples/tree/main/python/agents/llm-auditor)
- **Output formatting:** [Gemini model](https://cloud.google.com/vertex-ai/generative-ai/docs/models)

### API Access

The Apps Script custom function calls Vertex AI REST APIs using:

```text
UrlFetchApp
```

Reference: [UrlFetchApp](https://developers.google.com/apps-script/reference/url-fetch/url-fetch-app)

---

## Objectives

By following the guide, you learn how to:

- Understand what the solution does.
- Understand how the solution is implemented.
- Deploy the Vertex AI agent.
- Set up the Apps Script project.
- Run and test the custom function in Google Sheets.

---

## Architecture

The solution uses both **Google Workspace** and **Google Cloud** resources.

At a high level:

- Google Sheets hosts the custom function.
- Apps Script executes the custom function logic.
- Apps Script calls Vertex AI REST APIs.
- Vertex AI Agent Engine hosts the deployed **LLM Auditor ADK agent**.
- Gemini formats and summarizes the final response.
- A Google Cloud service account authenticates API access.

Architecture image referenced in the guide:

```text
https://developers.google.com/static/apps-script/samples/images/fact-check-flow.png
```

---

## Prerequisites

You need:

- A Google Account.
  - Google Workspace accounts may require administrator approval.
- A web browser with internet access.
- Prerequisites for the LLM Auditor ADK agent:
  - **Python 3.11+**
  - **Python Poetry**
  - **Google Cloud CLI**

Relevant setup links:

- Python: https://docs.python.org/3/using/index.html
- Poetry: https://python-poetry.org/docs/
- Google Cloud CLI: https://cloud.google.com/sdk/docs/install

---

# Environment Preparation

The environment setup includes:

1. Creating a Google Cloud project.
2. Enabling billing.
3. Enabling Vertex AI API.
4. Creating a service account.
5. Creating a private key.

---

## 1. Create a Google Cloud Project

### Using Google Cloud Console

1. Go to **IAM & Admin > Create a Project**.
2. Enter a descriptive project name.
3. Optionally edit the **Project ID**.
   - The project ID cannot be changed after creation.
4. Choose a project location.
5. Click **Create**.

Direct link:

```text
https://console.cloud.google.com/projectcreate
```

### Using gcloud CLI

Use Cloud Shell or a local shell with Google Cloud CLI installed and initialized.

```bash
gcloud projects create PROJECT_ID
```

Replace:

- `PROJECT_ID` with the desired Cloud project ID.

---

## 2. Enable Billing for the Cloud Project

### Using Google Cloud Console

1. Go to **Billing > My Projects**.
2. Select the organization associated with the project.
3. In the project row, open **Actions > Change billing**.
4. Choose the Cloud Billing account.
5. Click **Set account**.

Direct link:

```text
https://console.cloud.google.com/billing/projects
```

### Using gcloud CLI

List available billing accounts:

```bash
gcloud billing accounts list
```

Link a billing account to the project:

```bash
gcloud billing projects link PROJECT_ID --billing-account=BILLING_ACCOUNT_ID
```

Replace:

- `PROJECT_ID` with the Cloud project ID.
- `BILLING_ACCOUNT_ID` with the billing account ID.

[... summary truncated for context management ...]

---

## Source 10: Quickstart: Generate text using Agent Platform  |  Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/apps-script/quickstart/vertex-ai
- Original file: `docs/quickstart-generate-text-using-agent-platform-apps-script-google-for-developers-a59a63bb.md`
- Product area: `apps-script-ai`

# Quickstart: Generate Text Using Agent Platform in Apps Script

**Source:** [Google Developers — Apps Script Quickstart: Vertex AI / Agent Platform](https://developers.google.com/apps-script/quickstart/vertex-ai)  
**Last updated:** 2026-05-27 UTC  
**Topic:** Using Google Apps Script’s **Vertex AI advanced service** to call the **Agent Platform API** and generate text with **Gemini 2.5 Flash**.

---

## Overview

This quickstart shows how to use **Google Apps Script** with the **Vertex AI advanced service**, which connects to the **Agent Platform API**, to prompt the **Gemini 2.5 Flash** model and generate text.

> This page explains how to use Google Apps Script's Vertex AI advanced service (which connects to the Agent Platform API) to prompt the Gemini 2.5 Flash model to generate text.

The guide includes:

- Enabling the required Google Cloud API.
- Creating an Apps Script project.
- Adding the Vertex AI advanced service.
- Calling Gemini from Apps Script.
- Viewing the generated response in the Apps Script execution log.
- Cleaning up Cloud resources to avoid charges.

---

## Objectives

By completing the quickstart, you will:

- Set up your environment.
- Create an Apps Script project that uses the **Vertex AI advanced service** to connect to the **Agent Platform**.
- Run a script that generates text using Gemini.

---

## Prerequisite

You need:

- A **Google Cloud project with billing enabled**.

Helpful links from the guide:

- [Verify the billing status of your projects](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled)
- [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project)

---

## Set Up Your Environment

The setup involves configuration in both:

- **Google Cloud Console**
- **Apps Script editor**

---

## Enable the Agent Platform API

The required API is the **Agent Platform API**, formerly known as the **Vertex AI API**.

### Steps

1. Open your Google Cloud project in the Google Cloud Console.
2. Enable the Agent Platform API:

   [Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com)

3. Confirm you are enabling the API in the correct Cloud project.
4. Click **Next**.
5. Confirm the correct API is selected.
6. Click **Enable**.

---

## Create and Set Up the Apps Script Project

### Create the Project

1. Go to [script.google.com](https://script.google.com/home).
2. Click **New project**.
3. In the top-left, click **Untitled project**.
4. Rename the project:

   ```text
   Agent Platform quickstart
   ```

5. Click **Rename**.

---

## Add the Vertex AI Advanced Service

The Apps Script project must enable the **Vertex AI API advanced service**, which wraps the Agent Platform API.

### Steps

1. In the Apps Script editor, open **Services**.
2. Click **Add a service**.
3. Select:

   ```text
   Vertex AI API
   ```

4. Click **Add**.
5. Open `Code.gs`.
6. Replace the file contents with the provided code.
7. Replace:

   ```text
   GOOGLE_CLOUD_PROJECT_ID
   ```

   with your actual Google Cloud **project ID**.

Reference: [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)

8. Click **Save**.

---

## Code Sample

```javascript
/**
    * Main entry point to test the Agent Platform integration.
    */
function main() {
     const prompt = 'What is Apps Script in one sentence?';

     try {
       const response = callVertexAI(prompt);
       console.log(`Response: ${response}`);
     } catch (error) {
       console.error(`Failed to call Agent Platform: ${error.message}`);
     }
}

/**
    * Calls the Gemini model on Agent Platform.
    *
    * @param {string} prompt - The user's input prompt.
    * @return {string} The text generated by the model.
    */
function callVertexAI(prompt) {
     // Configuration
     const projectId = 'GOOGLE_CLOUD_PROJECT_ID';
     const region = 'us-central1';
     const modelName = 'gemini-2.5-flash';

     const model = `projects/${projectId}/locations/${region}/publishers/google/models/${modelName}`;

     const payload = {
       contents: [{\
         role: 'user',\
         parts: [{\
           text: prompt\
         }]\
       }],
       generationConfig: {
         temperature: 0.1,
         maxOutputTokens: 2048
       }
     };

     // Execute the request using the Vertex AI Advanced Service (which wraps the Agent Platform API)
     const response = VertexAI.Endpoints.generateContent(payload, model);

     // Use optional chaining for safe property access
     return response?.candidates?.[0]?.content?.parts?.[0]?.text || 'No response generated.';
}
```

---

## Important Code Details

### Prompt

The script sends this prompt to Gemini:

```javascript
const prompt = 'What is Apps Script in one sentence?';
```

### Model Configuration

The sample uses:

```javascript
const region = 'us-central1';
const modelName = 'gemini-2.5-flash';
```

The model resource path is built a

[... summary truncated for context management ...]

---

## Source 11: Vertex AI Service  |  Apps Script  |  Google for Developers

- Source URL: https://developers.google.com/apps-script/advanced/vertex-ai
- Original file: `docs/vertex-ai-service-apps-script-google-for-developers-2d9e69eb.md`
- Product area: `apps-script-ai`

# Vertex AI Service for Google Apps Script — Summary

**Source:** [Google Developers: Vertex AI Service | Apps Script](https://developers.google.com/apps-script/advanced/vertex-ai)  
**Last updated:** 2026-05-27 UTC

---

## Overview

The **Vertex AI advanced service** in Google Apps Script lets Apps Script projects use the **Agent Platform API** — formerly called the **Vertex AI API**.

> “The Vertex AI service lets you use the Agent Platform API (formerly the Vertex AI API) in Google Apps Script.”

This API provides access to **Gemini** and other **generative AI models**, including capabilities for:

- Text generation
- Image generation
- Other generative AI tasks

To get started, Google recommends using the Vertex AI Apps Script quickstart:

- [Vertex AI Apps Script quickstart](https://developers.google.com/apps-script/quickstart/vertex-ai)

---

## Prerequisites

Before using the Vertex AI service in Apps Script, you need:

### 1. Google Cloud Project with Billing Enabled

You must have a **Google Cloud project** with billing enabled.

Helpful links:

- [Verify billing status of projects](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled)
- [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project)

### 2. Enable the Agent Platform API

In the Google Cloud console, enable the **Agent Platform API**, formerly the **Vertex AI API**:

- [Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com)

### 3. Enable the Vertex AI Advanced Service in Apps Script

In your Apps Script project, turn on the **Vertex AI service**.

Reference:

- [Advanced Google services](https://developers.google.com/apps-script/guides/services/advanced#enable)

---

## API Reference

The Apps Script Vertex AI service uses the same:

- Objects
- Methods
- Parameters

as the public Agent Platform API.

> “Like all advanced services in Apps Script, the Vertex AI service uses the same objects, methods, and parameters as the public API.”

Reference documentation:

- [Agent Platform API reference documentation](https://docs.cloud.google.com/vertex-ai/docs/reference/rest)

The sample code on the page uses:

- [Version 1 of the Agent Platform API](https://docs.cloud.google.com/vertex-ai/docs/reference#versions)

---

## Sample: Generate Text with Gemini 2.5 Flash

This example prompts the **Gemini 2.5 Flash** model to generate text and logs the output to the Apps Script execution log.

Model referenced:

- [Gemini 2.5 Flash model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions#latest-stable)

Apps Script logging reference:

- [Execution log](https://developers.google.com/apps-script/guides/logging)

### Key Details

- Prompt: `'What is Apps Script in one sentence?'`
- Region: `us-central1`
- Model name: `gemini-2.5-flash`
- Temperature: `0.1`
- Max output tokens: `2048`
- Uses `VertexAI.Endpoints.generateContent(payload, model)`
- Replace `GOOGLE_CLOUD_PROJECT_ID` with your actual Google Cloud project ID.

Project ID reference:

- [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)

### Code

```javascript
/**
 * Main entry point to test the Vertex AI integration.
 */
function main() {
  const prompt = 'What is Apps Script in one sentence?';

  try {
    const response = callVertexAI(prompt);
    console.log(`Response: ${response}`);
  } catch (error) {
    console.error(`Failed to call Vertex AI: ${error.message}`);
  }
}

/**
 * Calls the Vertex AI Gemini model.
 *
 * @param {string} prompt - The user's input prompt.
 * @return {string} The text generated by the model.
 */
function callVertexAI(prompt) {
  // Configuration
  const projectId = 'GOOGLE_CLOUD_PROJECT_ID';
  const region = 'us-central1';
  const modelName = 'gemini-2.5-flash';

  const model = `projects/${projectId}/locations/${region}/publishers/google/models/${modelName}`;

  const payload = {
    contents: [{\
      role: 'user',\
      parts: [{\
        text: prompt\
      }]\
    }],
    generationConfig: {
      temperature: 0.1,
      maxOutputTokens: 2048
    }
  };

  // Execute the request using the Vertex AI Advanced Service
  const response = VertexAI.Endpoints.generateContent(payload, model);

  // Use optional chaining for safe property access
  return response?.candidates?.[0]?.content?.parts?.[0]?.text || 'No response generated.';
}
```

---

## Sample: Generate Text Using a Service Account

The page also provides an example for generating text by authenticating as an Apps Script project using a **service account**.

Reference:

- [Authenticate as an Apps Script project using a service account](https://developers.google.com/apps-script/guides/service-account)

### Key Details

This version:

- Retrieves a service account key from Apps Script script properties.
- Expects the key to be stored under:

```javascript
SERVICE_ACCOUNT_KEY
```

- Parses the service account

[... summary truncated for context management ...]

---
