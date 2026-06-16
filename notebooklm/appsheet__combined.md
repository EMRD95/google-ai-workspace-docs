---
title: "Combined source: appsheet"
product_area: "appsheet"
source_count: 9
generated_at: "2026-06-16T08:47:02Z"
source_type: "coverage_merged_official_extracts"
---

# Combined source: appsheet

This file merges 9 official extracted source document(s) from coverage area `appsheet` for NotebookLM import limits.
No synthetic documentation is added; each section preserves the source URL and extracted Markdown body.

## Source index

1. Best practices for using AI in automations - AppSheet Help — https://support.google.com/appsheet/answer/16052759?hl=en
2. Create apps using Gemini for App Creation - AppSheet Help — https://support.google.com/appsheet/answer/14699210?hl=en
3. Gemini for App Creation FAQ - AppSheet Help — https://support.google.com/appsheet/answer/14797537?hl=en
4. Overview of AI in automations - AppSheet Help — https://support.google.com/appsheet/answer/16045284?hl=en
5. Quick start: Extract information from an image using AI - AppSheet Help — https://support.google.com/appsheet/answer/15985259
6. Use Gemini in AppSheet - AppSheet Help — https://support.google.com/appsheet/answer/16106353?hl=en
7. Use the Categorize AI task in an automation - AppSheet Help — https://support.google.com/appsheet/answer/15983005?hl=en
8. Use the Extract AI task in an automation - AppSheet Help — https://support.google.com/appsheet/answer/15969430?hl=en
9. Use the Summarize AI task in an automation - AppSheet Help — https://support.google.com/appsheet/answer/16468184?hl=en

---

## Source 1: Best practices for using AI in automations - AppSheet Help

- Source URL: https://support.google.com/appsheet/answer/16052759?hl=en
- Original file: `docs/best-practices-for-using-ai-in-automations-appsheet-help-0022b1fa.md`
- Product area: `appsheet`

# Best Practices for Using AI in AppSheet Automations

*Source: [Google AppSheet Help](https://support.google.com/appsheet/answer/16052759?hl=en)*

---

## 1. General Best Practices When Leveraging AI

### Set Expectations and Measure Impact
- AI does not always produce correct results; you must evaluate overall benefit.
- **Key questions to answer:**
  - What are you trying to accomplish?
  - What are the expected outcomes?
  - How will you measure impact? (e.g., cost/time savings, productivity gains)
  - What is the impact when AI is right? When it is wrong?
  - How often does AI get it right/wrong?

### Should I Use AI in Automations?
- AI tasks rely on **Google’s Gemini models** – no training required, but **not tailored to your data**.
- **Test AI tasks on a few examples first**, then expand to more data.
- **General suitability guidelines:**
  - If the task does **not require obscure knowledge**, AI may help.
  - If the required knowledge is **difficult to find online** or highly industry-specific, results may be poor.

### Human Review and Handling Unexpected Behavior
- Set up a collaborative workflow where humans can quickly review AI outputs in your app.
- Add automation steps to handle unexpected AI results.
  - **Example:** Define an `Enum` value named “Other” for catch‑all, then trigger a notification when “Other” is set so the enum can be updated.

---

## 2. Best Practices When Building Apps Using AI

### Provide Additional Details in AI Tasks
Every AI task has an **Additional details** field. Use it to clarify requirements and expected results.

| AI Task | Recommended Additional Details | Example |
|---------|-------------------------------|---------|
| **Categorize** | - Describe requirements for each category value.<br>- Indicate fallback value (e.g., “Other”) if unsure.<br>- Ensure recommended values match column type/format.<br>**Note:** An undefined value in an `Enum` column may cause unexpected behavior unless you [allow other values](https://support.google.com/appsheet/answer/10106509#allow-other-values). | Inexpensive: Less than 10 dollars<br>Moderately expensive: Between 10 and 50 dollars<br>Expensive: Over 50 dollars<br>Other: Not sure of value |
| **Extract** | - Describe the information to extract in detail.<br>- Indicate what to set if information is unknown.<br>- Match values to column type/format. | If not sure of Make, Model, or year, make best guess<br>If not sure of Color, set to “Other” |
| **Extract rows** | - Describe the information to extract in detail.<br>- Indicate fallback values if unknown.<br>- Match values to column type/format. | From the PDF file extract the items in the receipt that are above fifty dollars |
| **Summarize** | - Describe what the summary should include. | Summarize the customer feedback, highlighting the main areas for improvement |

### Add Column Descriptions
- For columns that store AI output, add descriptions to guide Gemini’s data evaluation ([how to configure column properties](https://support.google.com/appsheet/answer/10106509)).
- **Do not use expressions in column descriptions** for AI tasks – they won’t be evaluated and may harm result quality.

---

## 3. Best Practices for Inputs to AI Tasks

Share these guidelines with app users.

### Use Quality Images
- **Higher resolution** improves results; avoid blurry images. Consider setting image upload size to **High** ([control image size](https://support.google.com/appsheet/answer/10106529)).
- If text is **small relative to the image**, quality may suffer.
- **Pre‑process images** when possible:
  - Rotate and crop to isolate relevant subject matter.
  - Mark up the image to highlight important areas.
- Industry‑specific image content may reduce quality.
- See also: [limitations and known issues with images](https://support.google.com/appsheet/answer/15999115#limitations-images).

### Optimize PDF Documents
- **Split long PDFs** into smaller files.
- Use PDFs with **text rendered as text**, not scanned images of text.
- Avoid low‑resolution or small images inside PDFs.
- See also: [limitations and known issues with PDF documents](https://support.google.com/appsheet/answer/15999115#limitations-pdf-documents).

---

**Key takeaway:** Combine AI automation with clear instructions, human oversight, and careful input preparation to get the most reliable results.

---

## Source 2: Create apps using Gemini for App Creation - AppSheet Help

- Source URL: https://support.google.com/appsheet/answer/14699210?hl=en
- Original file: `docs/create-apps-using-gemini-for-app-creation-appsheet-help-5c13a00d.md`
- Product area: `appsheet`

# Create Apps Using Gemini for App Creation — AppSheet Help Summary

**Source:** https://support.google.com/appsheet/answer/14699210?hl=en  
**Product:** Google AppSheet  
**Feature:** Gemini for App Creation

---

## Overview

**Gemini for App Creation** lets AppSheet users create apps by describing a business process or app idea in natural language. Gemini generates an initial app structure—including tables, columns, and relationships—that users can review, edit, and turn into an AppSheet app.

> Gemini for App Creation allows you to build apps by simply _describing_ a business process or idea in natural language.

---

## Availability

Gemini for App Creation is available to **all AppSheet paid accounts**, including:

- Google Workspace customers with:
  - **AppSheet Core**
  - **AppSheet Enterprise Plus**
- Individual accounts with:
  - **AppSheet Publisher Pro**
  - **AppSheet Starter**
  - **AppSheet Core**
  - **AppSheet Enterprise Plus**

---

## Admin Controls

Users with administrator privileges can disable AI-assisted app creation.

- The setting is managed through **Turn Gemini for App Creation on or off**
- The setting applies at the **team level**
- If an organization has multiple teams, Gemini must be disabled separately for each relevant team

---

## How to Access Gemini for App Creation

1. Go to **My Apps**:
   - Sign in to [AppSheet](https://appsheet.com/)
   - **My Apps** displays by default
   - Or click **My Apps** in the top navigation
   - Or select **My Apps** from the account profile drop-down

2. Click:

```text
+ Create > App > Start with Gemini
```

3. The Gemini-assisted chat interface opens.

---

## App Creation Workflow

Gemini for App Creation uses a **three-step process**:

1. **Describe your app idea or process**
2. **Review and edit the app structure**
3. **Create and customize your app**

---

# Step 1: Describe Your App Idea or Process

At the Gemini prompt, users can either:

- Enter a natural-language description of the desired app or process
- Click one of the provided sample prompts to auto-populate the prompt

The description is also called a **prompt**.

**Recommendation:** Provide as much detail as possible.

---

## Example Prompt

The article uses a facility inspection app as an example:

> **Manage inspections of my facility. Our inspectors conduct facility inspections, and every week we need to check that everything is operating correctly at each facility, pass or fail an inspection, and create and submit reports.**

Gemini responds by generating an app structure that summarizes the data the app will manage.

---

## Example Generated App Structure

For the facility inspection example, Gemini creates tables such as:

```text
Inspectors
Reports
Inspections
Facilities
```

### Example Table Columns

For the `Inspections` table, Gemini generates columns including:

```text
Id
Facility Id
Inspector Id
Date
Status
Report Id
```

---

## Tables, Columns, and Links

Gemini generates:

### Tables

Tables are used to track app data and are similar to tabs in a spreadsheet.

Example tables:

```text
Inspectors
Reports
Inspections
Facilities
```

### Columns

Columns define the attributes of each row in a table.

Example columns in the `Inspections` table:

```text
Id
Facility Id
Inspector Id
Date
Status
Report Id
```

### Links Between Tables

Gemini can create relationships between tables.

Example:

- In the `Inspections` table:
  - `Facility Id` links to the `Name` column in the `Facilities` table
  - `Inspector Id` links to the `Name` column in the `Inspectors` table

---

# Step 2: Review and Edit Your App Structure

After Gemini generates the app structure, users should review it and decide whether additional information needs to be tracked.

## If the Structure Is Satisfactory

Click:

```text
Create app
```

This proceeds to app creation and customization.

## If the Structure Is Not Satisfactory

Users can:

- Edit the app structure
- Click **Start over** to discard the current structure and begin again

---

## Editing the App Structure

Users can edit the generated app structure by:

- Adding a table
- Editing a table
- Adding, editing, or deleting columns
- Editing table names
- Deleting tables

---

## Add a Table

Click:

```text
+ Add table
```

A dialog opens where users can:

- Enter the table name
- Add columns

### Important Note About the `Id` Column

> The `Id` column is created automatically, providing a unique ID for the table that can't be edited or deleted.

---

## Edit a Table

Click a table in the app structure to open the **Edit table** dialog.

Within the dialog, users can:

- Edit the table name
- Add columns
- Edit column names
- Edit column types
- Edit single-select or multi-select option values
- Delete columns
- Delete the entire table

After making changes, click:

```text
Save
```

---

## Supported Column Editing Options

When adding or editing a column, users can:

- Enter a column name
- Select a column type from a drop-down
-

[... summary truncated for context management ...]

---

## Source 3: Gemini for App Creation FAQ - AppSheet Help

- Source URL: https://support.google.com/appsheet/answer/14797537?hl=en
- Original file: `docs/gemini-for-app-creation-faq-appsheet-help-28b51a5e.md`
- Product area: `appsheet`

# Gemini for App Creation FAQ — AppSheet Help

**Source:** <https://support.google.com/appsheet/answer/14797537?hl=en>

## Overview

**Gemini for App Creation** is an AI-assisted feature in AppSheet that helps app creators build apps by describing a business process or idea. It is available to **all AppSheet paid accounts**, including eligible Google Workspace customers and individual paid AppSheet plans.

## Key Excerpts

> Gemini for App Creation allows app creators to build an app by simply _describing_ a business process or idea.

> AppSheet will return a list of suggested tables and columns, and app creators can choose to have the app created with that data schema, along with some pre-built views and actions.

> Gemini for App Creation is included as part of your paid AppSheet license: AppSheet Publisher Pro, AppSheet Starter, AppSheet Core, or AppSheet Enterprise Plus.

> Turning Gemini for App Creation on or off only affects the use of Gemini for app creators. It will not affect any Gemini features in Workspace.

## Availability

Gemini for App Creation is available to users with paid AppSheet access, including:

- **AppSheet Publisher Pro**
- **AppSheet Starter**
- **AppSheet Core**
- **AppSheet Enterprise Plus**
- Google Workspace customers who have **AppSheet Core** included through their Workspace license

Related reference:

- [Google Workspace editions that include AppSheet Core](https://support.google.com/a/answer/10100275?sjid=14898439068259244864-NC#core-editions)

## What the Feature Does

App creators can use Gemini for App Creation to:

- Describe a business process or app idea in natural language
- Receive suggested:
  - Tables
  - Columns
  - Data schema
- Generate an app based on the suggested schema
- Start with some pre-built:
  - Views
  - Actions

This is designed to help accelerate app creation by using AI to draft the initial app structure.

## Admin Controls

Administrators can turn Gemini for App Creation **on or off**.

### How to Disable It

Users with administrator privileges can disable the AI-assisted app creation feature by following Google’s instructions:

- [Turn Gemini for App Creation on or off](https://support.google.com/appsheet/answer/11918568#gemini-in-appsheet)

### Scope of the Setting

The setting applies at the **team level**.

Important implication:

- If your organization has multiple AppSheet teams, you must disable the feature separately for each relevant team.

## Availability for Only Some Users

The same team-level setting is used if an admin wants Gemini for App Creation to be available only to certain users.

Because the control is applied at the **team level**, admins need to manage access by configuring the setting for the appropriate teams.

## Relationship to Gemini in Google Workspace

Turning Gemini for App Creation on or off affects only **Gemini for app creators in AppSheet**.

It does **not** affect Gemini features in Google Workspace.

## Gemini Enterprise or Gemini Workspace Requirement

You **do not** need Gemini Enterprise or Gemini Workspace to use Gemini for App Creation.

The feature is included with paid AppSheet licenses, including users who receive **AppSheet Core entitlements through Google Workspace licenses**.

## Key Takeaways

- Gemini for App Creation lets AppSheet users generate an app by describing an idea or business process.
- It suggests tables, columns, schema, views, and actions.
- It is included with paid AppSheet licenses and eligible Workspace-based AppSheet Core access.
- Admins can disable it, but controls are applied per team.
- Disabling Gemini for App Creation does not impact Gemini features in Workspace.
- No separate Gemini Enterprise or Gemini Workspace license is required.

---

## Source 4: Overview of AI in automations - AppSheet Help

- Source URL: https://support.google.com/appsheet/answer/16045284?hl=en
- Original file: `docs/overview-of-ai-in-automations-appsheet-help-b0df0b8f.md`
- Product area: `appsheet`

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

---

## Source 5: Quick start: Extract information from an image using AI - AppSheet Help

- Source URL: https://support.google.com/appsheet/answer/15985259
- Original file: `docs/quick-start-extract-information-from-an-image-using-ai-appsheet-help-7cd05d19.md`
- Product area: `appsheet`

# Quick Start: Extract Information from an Image Using AI – AppSheet Help

**Scenario**: A car dealership owner wants to automatically populate inventory fields (make, model, color, year, description) by uploading a photo. The built automation uses an AI task to extract data and save it to an AppSheet database.

> See also the [Car identification with Gemini sample app](https://www.appsheet.com//template/showdef?appId=CarIdentificationwithGemini-2078346&quickStart=False) for a more comprehensive scenario.

---

## High‑Level Process

1. Create an AppSheet database with the required columns.
2. Generate an app from that database.
3. Build a bot with an **Extract** AI task to pull info from the uploaded image.
4. Simplify the input form so users only see the photo upload field.
5. Test the automation by uploading a car photo in the app preview.

---

## Step‑by‑Step Details

### 1. Create an AppSheet Database

- **Database name**: `Car inventory`
- **Table name**: `Car inventory` (rename from `Table 1`)
- **Delete all dummy rows** before adding real data.

**Columns to edit/add**:

| Original/New Column | Final Name | Type / Config                                                                 |
|---------------------|------------|-------------------------------------------------------------------------------|
| `Title`             | `Make`    | Text (rename only)                                                           |
| `Assignee`          | `Model`   | Type **Name** (or Text)                                                      |
| `Status`            | `Color`   | Enum (dropdown) with options:<br>White, Green, Yellow, Orange, Red, Blue, Silver, Black, **Other** (catch‑all)<br>Assign a color swatch to each. |
| `Date`              | `Year`    | **Number** (no thousands separator)                                          |
| (new)               | `Description` | Text                                                                       |
| (new)               | `Car photo` | Attachments → Image                                                        |

*Careful database design is fundamental – the data structure determines the app’s behavior.*

### 2. Create an App From the Database

- In the database editor, click **Apps > New AppSheet app**.
- Rename the app to `Car inventory`.
- Open the **Data** pane: the table is linked to your AppSheet database.
- Edit the `Year` column: turn **off** “Show thousands separator” (year values don’t need formatting).

### 3. Build the Automation (Bot)

**Bot creation**:

- Go to **Automation** (left nav). Click `+` → Create a new bot.
- Rename the bot to `Update car inventory`.

**Event**:

- Click **Configure event**.
- *Event name*: `Update car inventory`
- **Condition** (to ensure an image is present):

  ```
  ISNOTBLANK([Car photo])
  ```

  *This expression prevents the bot from running unless a photo has been uploaded.*

**Step – AI extraction**:

- Click **+ Add a step** (in the bot flow).
- *Step name*: `Extract from photo`
- Configuration in the right pane:
  - **Task type**: AI task
  - **AI task**: `Extract` (extracts info from photo, PDF, or text)
  - **Input column**: `Car photo`
  - **Output**:
    - **Save to table** (enabled)
    - Map extracted data to columns: **Make**, **Model**, **Color**, **Year**, **Description** (add each in order).

**Additional instructions** (copy this text exactly):

> If not sure of Make, Model, or Year, make best guess  
> If not sure of Color, set to "Other"  
> For Description, add 2 to 3 sentences

- **Save** the app.

### 4. Customize the Input Form

- Go to **App > Views**.
- Select the system‑generated `Car inventory_Form` view.
- Set **Column order** to **Manual**.
- Remove all columns **except `Car photo`** from the column order list.
- The live preview shows a form with only the photo upload field.

### 5. Test the Automation in the App Preview

- In the app preview, click the `Car photo` field and upload a car image (from your device or internet).
- Click **Save** – AppSheet syncs and triggers the bot.
- After sync, navigate to **Car inventory** list, open the new item. The Make, Model, Color, Year, and Description fields are auto‑populated by the AI.

---

## Next Steps

- Extend the automation to **categorize the car by body style** → see [Quick start: Categorize information using AI](https://support.google.com/appsheet/answer/16338286).
- Explore more Gemini‑powered [quick starts](https://support.google.com/appsheet/answer/16045284#quick-start).
- Learn about other AppSheet features via [quick starts](https://support.google.com/appsheet/answer/13474783).

---

**Key phrases & code snippet preserved verbatim**:

- `ISNOTBLANK([Car photo])` – condition for bot event
- Additional instructions text:
  ```
  If not sure of Make, Model, or Year, make best guess
  If not sure of Color, set to "Other"
  For Description, add 2 to 3 sentences
  ```

---

## Source 6: Use Gemini in AppSheet - AppSheet Help

- Source URL: https://support.google.com/appsheet/answer/16106353?hl=en
- Original file: `docs/use-gemini-in-appsheet-appsheet-help-20c004c5.md`
- Product area: `appsheet`

# Use Gemini in AppSheet — Summary

**Source:** [AppSheet Help: Use Gemini in AppSheet](https://support.google.com/appsheet/answer/16106353?hl=en)

## Overview

Gemini in AppSheet brings Gemini-powered capabilities to AppSheet through two main feature areas:

- **Gemini for App Creation**
- **Gemini in AppSheet Solutions**

These features are governed by different terms depending on how AppSheet is purchased:

> For AppSheet users purchasing AppSheet as part of Google Workspace, Gemini in AppSheet is considered to be a "Workspace Generative AI Service," subject to the "Workspace Generative AI Services" section of the [Google Workspace Service Specific Terms](https://workspace.google.com/terms/service-terms/).

> For AppSheet users purchasing AppSheet as a standalone offering, Gemini in AppSheet is considered to be an "AppSheet Generative AI Service," subject to the "AppSheet Generative AI Services" section of the [AppSheet Terms of Service](https://www.appsheet.com/Home/Terms).

---

## Gemini for App Creation

### Availability & Licensing

Gemini for App Creation is included with paid AppSheet licenses:

- **AppSheet Publisher Pro**
- **AppSheet Starter**
- **AppSheet Core**
- **AppSheet Enterprise Plus**

You may also have access to **AppSheet Core** through certain Google Workspace licenses.

> You don't need Gemini Enterprise or Gemini Workspace to use this feature.

### What It Does

Gemini for App Creation lets app creators build apps by describing a business process or idea in natural language.

AppSheet can then generate:

- Suggested **tables**
- Suggested **columns**
- A data schema
- Some pre-built **views**
- Some pre-built **actions**

Creators can choose to create the app based on the suggested schema.

Related help article:

- [Create apps using Gemini for App Creation](https://support.google.com/appsheet/answer/14699210)

### Admin Controls

Admins can disable AI-assisted app creation.

Key details:

- The setting is applied at the **team level**
- If an organization has multiple teams, it must be disabled separately for each relevant team
- Turning it off affects only Gemini-powered **app creation**
- It does **not** affect:
  - AI in automations
  - Gemini features in Google Workspace

Related help article:

- [Turn Gemini for App Creation on or off](https://support.google.com/appsheet/answer/11918568#gemini-for-app-creation)

---

## Gemini in AppSheet Solutions

### Availability & Licensing

Gemini in AppSheet Solutions is included with:

- **AppSheet Enterprise Plus**

> You don't need Gemini Enterprise or Gemini Workspace to use this feature.

### What It Does

Gemini in AppSheet Solutions enables Gemini-powered AI tasks in AppSheet automations.

Current AI task capabilities include:

- Extract information from an **image**
- Extract information from a **PDF file**
- Extract information from **text**
- Categorize information

The article notes that more AI features are planned:

> Add Gemini-powered AI tasks in automations to extract information from an image, PDF file, or text; or categorize information--with more AI features to come.

Related help article:

- [Overview of AI in automations](https://support.google.com/appsheet/answer/16045284)

### Governance Controls

Organizations can define a governance policy to control who can use AI in automations.

Related help article:

- [Control which app creators can use AI in automations](https://support.google.com/appsheet/answer/16052764)

### Credit Usage

Using Gemini in AppSheet Solutions consumes **credits**.

Credits are based on:

- The number of AI tasks run
- The complexity of those AI tasks
- Usage by users of apps owned by creators in your organization

> When you use Gemini in AppSheet Solutions, you consume _credits_ based on the number and complexity of the AI tasks that are run by users of the apps owned by creators in your organization.

Related help article:

- [Manage credits for Gemini usage](https://support.google.com/appsheet/answer/16274771)

---

## Key Takeaways

- Gemini in AppSheet includes both **AI-assisted app creation** and **AI-powered automation tasks**.
- **Gemini for App Creation** is available with several paid AppSheet licenses, including AppSheet Core and above.
- **Gemini in AppSheet Solutions** requires **AppSheet Enterprise Plus**.
- Neither feature requires a separate **Gemini Enterprise** or **Gemini Workspace** license.
- Admins can disable Gemini for App Creation at the **team level**.
- AI in automations can be governed through policy controls.
- Gemini automation usage consumes **credits** based on task quantity and complexity.

---

## Source 7: Use the Categorize AI task in an automation - AppSheet Help

- Source URL: https://support.google.com/appsheet/answer/15983005?hl=en
- Original file: `docs/use-the-categorize-ai-task-in-an-automation-appsheet-help-15acc472.md`
- Product area: `appsheet`

# Use the Categorize AI Task in an Automation – Summary

**Availability:**  
*AppSheet **Enterprise Plus** accounts only.*  
See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

The **Categorize AI** task uses AI to classify information into a predefined set of categories as part of an automation.

---

## Examples of Use Cases

- Analyze employee expense descriptions and auto-categorize by type: *Travel, Meals, Software, Training*.
- Read facility maintenance requests and categorize by urgency (*High, Medium, Low*) or equipment type (*HVAC, Plumbing, Electrical*).
- Classify customer survey/feedback responses into categories: *Bug Report, Feature Request, Positive Feedback, Billing Inquiry*.

---

## Get Started

- [Step through the quick start](https://support.google.com/appsheet/answer/16045284#quick-start)
- [Explore an app template](https://support.google.com/appsheet/answer/16045284#app-template)

---

## How to Add & Configure the Task

1. **Add** the **Categorize AI** task to a bot (as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task)).
2. **Configure** the task using the settings below.
3. **Save** the app.

### Configuration Settings

| Setting | Description |
|---------|-------------|
| **Task type** | Select **AI task**. |
| **Table** | The table defined in the [event](https://support.google.com/appsheet/answer/11445188) used by the task. |
| **AI task** | Select **Categorize**. |
| **Input columns** | Add **one or more** columns (max **10**) as input. Click **Add** and choose from the drop-down. <br><br>**Supported:** Basic column data types, virtual columns. <br>**Not supported:** <br>• Content types (`Drawing`, `File`, `Image`, `Signature`, `Thumbnail`, `Video`)<br>• `Color`<br>• Show types<br>• Other types: `URL`, `App`<br>• `List` columns (not supported at this time) |
| **Output** | Choose one:<br>• **Save to table** – writes the category to your data source.<br>• **Return value** – uses the category in later bot steps without storing. Access as `[AI-step].[column]`.<br><br>Then, select the column that defines the allowed category values. **Must be an `Enum` or `Ref` column.** <br>**Note on `Ref` columns:** Works only with existing values; at least one row must exist. AppSheet will not create new entries in the referenced table. |
| **Additional instructions** | **Recommended.** Provide detailed requirements for each category value, indicate fallback values for unknown results, and ensure recommended values match the column’s type/format. <br>**Max length:** 1000 characters. <br><br>Example:<br>`Inexpensive: Less than 10 dollars`<br>`Moderately expensive: Between 10 and 50 dollars`<br>`Expensive: Over 50 dollars`<br>`Other: Not sure of value`<br><br>**Important:** Using a value not defined in the `Enum`/`Ref` column can cause unexpected behavior **unless** you enable [allow other values](https://support.google.com/appsheet/answer/10106509#allow-other-values) in the column’s properties. |

> **Note on Best Practices:** When saving to table, review [Manage updates to row data by multiple bots](https://support.google.com/appsheet/answer/16136023#update-row-data-multiple-bots) to avoid conflicts.

---

## Related Resources

- [Best practices for using AI in automations](https://support.google.com/appsheet/answer/16052759)
- [Limitations with AI in automations](https://support.google.com/appsheet/answer/15999115)

---

## Source 8: Use the Extract AI task in an automation - AppSheet Help

- Source URL: https://support.google.com/appsheet/answer/15969430?hl=en
- Original file: `docs/use-the-extract-ai-task-in-an-automation-appsheet-help-1724e080.md`
- Product area: `appsheet`

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

---

## Source 9: Use the Summarize AI task in an automation - AppSheet Help

- Source URL: https://support.google.com/appsheet/answer/16468184?hl=en
- Original file: `docs/use-the-summarize-ai-task-in-an-automation-appsheet-help-d48803a4.md`
- Product area: `appsheet`

# Use the Summarize AI task in an automation – AppSheet Help

**Source:** [AppSheet Help Center](https://support.google.com/appsheet/answer/16468184?hl=en)  
**Availability:** AppSheet Enterprise Plus accounts only.

---

## Feature Overview

The **Summarize** AI task lets you condense long text into a shorter summary using AI, directly within an automation bot. You can supply multiple text columns as input.

### Example Use Cases

- Summarize meeting notes to review main highlights.
- Summarize information for a specific customer, highlighting the main points of concern.

---

## How to Configure the Summarize AI Task

1. Add a **Summarize** AI task to a bot (see [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task)).
2. Configure the settings as described below.
3. Save the app.

### Configuration Settings

| Setting | Description |
|---------|-------------|
| **Task type** | Select **AI task**. |
| **Table** | The table defined in the bot’s event. Click the edit icon to view/modify structure. |
| **AI task** | Choose **Summarize** from the list of AI task types. |
| **Input columns** | Add one or more columns (max 10) as input. Supported data types: basic columns and virtual columns.<br><br>**Unsupported types:**<br>- Content types: `Drawing`, `File`, `Image`, `Signature`, `Thumbnail`, `Video`<br>- `Color`<br>- Show types<br>- Other types: `URL`, `App`<br><br>**Notes:**<br>- `Ref` columns: only the label is evaluated.<br>- `List` columns are not supported. |
| **Output** | Choose one of:<br><br>- **Save to table** – stores the summary in a column of your data source.<br>- **Return value** – returns the summary for use in later steps (referenced as `[AI-step].[column]`), without permanent storage.<br><br>Then select a target column of type `LongText` or `Text`. |
| **Additional instructions** | (Recommended) Describe what to include in the summary, up to 1000 characters. Example:<br><br>_Summarize the customer feedback, highlighting the main areas for improvement_ |

---

## Important Notes & References

- See also: [Best practices for using AI in automations](https://support.google.com/appsheet/answer/16052759)
- [Limitations with AI in automations](https://support.google.com/appsheet/answer/15999115)

---

---
