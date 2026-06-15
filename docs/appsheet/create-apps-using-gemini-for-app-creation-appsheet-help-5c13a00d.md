---
title: "Create apps using Gemini for App Creation - AppSheet Help"
source_url: "https://support.google.com/appsheet/answer/14699210?hl=en"
product_area: "appsheet"
retrieved_at: "2026-06-15T09:15:22Z"
extraction_method: "web_extract"
---

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
