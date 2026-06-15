# Overview of AI in automations - AppSheet Help

**Product Area:** appsheet
**Source:** https://support.google.com/appsheet/answer/16045284?hl=en

# Overview of AI in Automations — AppSheet Help

**Source:** https://support.google.com/appsheet/answer/16045284?hl=en  
**Product area:** AppSheet Automations / Gemini in AppSheet Solutions

---

## Key Excerpts

> This feature is available to **AppSheet Enterprise Plus** accounts only.

> With Gemini in AppSheet Solutions, you can use AI in automations to extract information from an image, PDF document, or text; and categorize information.

> When you use Gemini in AppSheet Solutions, you consume _credits_ based on the number and complexity of the AI tasks that are run by users of the apps owned by creators in your organization.

---

## What AI in AppSheet Automations Does

AppSheet supports Gemini-powered AI tasks inside automations. These tasks can help apps:

- **Extract information** from:
  - Images, such as photos
  - PDF files
  - Text
- **Categorize information** into defined categories
- **Extract rows** from images or PDFs into existing tables
- **Summarize long text** into shorter summaries

The feature is intended to simplify workflows where users provide unstructured input, such as photos or documents, and AppSheet converts that input into structured app data.

---

## Availability

AI in automations is available only for:

- **AppSheet Enterprise Plus** accounts

Related reference:

- [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

---

## Example Use Case: Car Dealership Inventory

A car dealership owner needs to frequently update sales inventory.

End-user workflow:

1. Take a photo of a new car on a mobile device.
2. Upload the image to the AppSheet app.
3. AppSheet uses AI to extract data from the photo, such as:
   - Car make
   - Model
   - Color
   - Year
   - Description

This extracted data can then be used to update the dealership’s sales inventory.

---

## Important Considerations

Before using AI in automations:

- Review [limits and limitations with AI in automations](https://support.google.com/appsheet/answer/15999115).
- AppSheet admins should understand credit usage and governance controls.

### Admin Considerations

AppSheet admins should note:

- Gemini in AppSheet Solutions uses **credits**.
- Credit usage is based on:
  - The number of AI tasks run
  - The complexity of those AI tasks
  - Usage by users of apps owned by creators in the organization
- Admins can define governance policies to control which app creators can use AI in automations.

Related resources:

- [About credits and quotas with Gemini in AppSheet Solutions](https://support.google.com/appsheet/answer/16622530)
- [Control which app creators can use AI in automations](https://support.google.com/appsheet/answer/16052764)

---

## Supported AI Tasks

Additional AI tasks may be supported in the future.

| AI Task | Description | Example |
|---|---|---|
| **Categorize** | AI categorizes information into defined categories. You select the columns to evaluate and the column that defines the allowed category values. | Categorize a support request |
| **Extract** | AI extracts information from an image, such as a photo, a PDF file, or text. You select the information to extract and save to your data source. | Upload a photo to add a car to sales inventory |
| **Extract rows** | AI extracts information from an uploaded image, such as a photo, or PDF file and saves it to rows in an existing table. | Upload a PDF file, extract receipt items above fifty dollars, and save them to an expenses table |
| **Summarize** | AI summarizes long textual data into a shorter summary. | Summarize information for a specific customer, highlighting the main points of concern |

### Task-Specific Help Links

- [Use the Categorize AI task in an automation](https://support.google.com/appsheet/answer/15983005)
- [Use the Extract AI task in an automation](https://support.google.com/appsheet/answer/15969430)
- [Use the Extract rows AI task in an automation](https://support.google.com/appsheet/answer/16411323)
- [Use the Summarize AI task in an automation](https://support.google.com/appsheet/answer/16468184)

---

## Getting Started

AppSheet recommends three ways to get started with AI in automations:

1. Watch a quick tour video
2. Step through a quick start
3. Explore an app template

---

## Quick Tour Video

Video:

- **Quick tour: Gemini in AppSheet Solutions**
- YouTube link: https://www.youtube.com/watch?v=Ktz2_bFcdfc
- Channel: AppSheet

---

## Quick Starts

| Quick Start | Description | AI Task |
|---|---|---|
| [Quick start: Extract information from an image using AI](https://support.google.com/appsheet/answer/15985259) | Build an automation using AI to extract information from a car photo and use it to update a car sales inventory. | **Extract AI — image** |
| [Quick start: Categorize information using AI](https://support.google.com/appsheet/answer/16338286) | Extend the previous quick start to categorize cars by body style using AI. | **Categorize AI** |
| [

[... summary truncated for context management ...]
