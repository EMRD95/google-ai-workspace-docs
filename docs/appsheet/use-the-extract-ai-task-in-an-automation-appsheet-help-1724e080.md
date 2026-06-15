---
title: "Use the Extract AI task in an automation - AppSheet Help"
source_url: "https://support.google.com/appsheet/answer/15969430?hl=en"
product_area: "appsheet"
retrieved_at: "2026-06-15T09:15:22Z"
extraction_method: "web_extract"
---

# Use the Extract AI Task in an Automation — AppSheet Help Summary

**Source:** https://support.google.com/appsheet/answer/15969430?hl=en  
**Feature availability:** **AppSheet Enterprise Plus accounts only**

> This feature is available to **AppSheet Enterprise Plus** accounts only.

## Purpose

The **Extract AI** task lets you use AI in an AppSheet automation to extract information from:

- Uploaded images, such as photos
- Files, specifically PDFs
- Text inputs, such as descriptions stored as `Text` or `LongText`

The extracted data can be saved back to an AppSheet table or returned for use in later automation steps.

## Example Use Cases

Extract AI can be used to automatically pull structured information from unstructured inputs, such as:

- Technicians taking photos of equipment to extract:
  - Serial numbers
  - Model numbers
  - Meter readings
- Processing uploaded purchase orders or shipping labels to extract:
  - PO numbers
  - Company names
  - Tracking numbers
  - Addresses
- Extracting key details from incident reports, such as:
  - Location
  - Date
  - Names

## Getting Started Resources

AppSheet recommends starting with:

- A quick tour video
- A quick start walkthrough
- An app template

Related AppSheet documentation includes:

- **Best practices for using AI in automations**
- **Limitations with AI in automations**

## How to Add and Configure the Extract AI Task

To extract data using AI:

1. Add the **Extract AI** task to a bot.
2. Configure the task using the settings below.
3. Save the app.

## Extract AI Task Settings

| Setting | Description |
|---|---|
| **Task type** | Select **AI task**. |
| **Table** | The table defined in the automation event and used by the task. |
| **AI task** | Select **Extract**. |
| **Input column** | The column used as input to the AI task. Must be one of: `Drawing`, `File`, `Image`, `LongText`, `Text`, or `Thumbnail`. |
| **Output** | Choose whether to save extracted results to the table or return them for later automation steps. |
| **Additional instructions** | Optional but recommended. Provide detailed extraction guidance, fallback values, and formatting/type expectations. Supports up to **2000 characters**. |

## Supported Input Column Types

For the Extract task, the input column must use one of the following types:

```text
Drawing
File
Image
LongText
Text
Thumbnail
```

## Output Options

### Save to Table

Select **Save to table** to save extracted information directly into your data source table.

### Return Value

Select **Return value** to guide AI responses without storing results in your data source.

Returned values can be used in later automation steps with this format:

```text
[AI-step].[column]
```

When configuring output, select one or more columns to define the information to extract.

**Limit:**

> Maximum of **12** columns.

Click **Add** to add more output columns.

## Supported Output Column Types

The following output column types are supported:

- Boolean / Yes-No
- Numeric
- Date and time
- Text
- `Enum` columns using one of the supported subtypes above

Important limitation:

> Barcode and QR code scanning isn't supported at this time.

## Additional Instructions Guidance

The **Additional instructions** field is recommended for improving extraction quality.

Use it to:

- Describe in more detail what information should be extracted.
- Indicate what values to use when results are unknown.
- Ensure recommended fallback values match the target column type and format.

Character limit:

```text
2000 characters
```

Example instructions from the article:

```text
If not sure of Make, Model, or Year, make best guess
If not sure of Color, set to "Other"
For Description, add 2 to 3 sentences
```

## Important Notes and Best Practices

- Extract AI is available only for **AppSheet Enterprise Plus**.
- The task is configured as an **AI task** inside an automation bot.
- Input data can come from image, file, drawing, thumbnail, or text-based columns.
- Output can either be stored in the table or passed as a return value to later automation steps.
- Up to **12 extraction output columns** can be defined.
- Use detailed additional instructions for better AI results.
- When saving content back to table rows, AppSheet recommends following best practices for managing row updates by multiple bots.
- Barcode and QR code scanning are **not currently supported**.
