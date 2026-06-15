---
title: "Advanced Google services  |  Apps Script  |  Google for Developers"
source_url: "https://developers.google.com/apps-script/guides/services/advanced"
product_area: "apps-script-ai"
retrieved_at: "2026-06-15T18:21:14Z"
extraction_method: "web_extract"
---

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
