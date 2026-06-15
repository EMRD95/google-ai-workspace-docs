---
title: "Watch and manage sheets with flows - Workspace Studio Help"
source_url: "https://support.google.com/workspace-studio/answer/16655443"
product_area: "workspace-studio"
retrieved_at: "2026-06-15T17:48:10Z"
extraction_method: "web_extract"
---

# Watch and Manage Sheets with Flows — Google Workspace Studio

**Source:** Google Workspace Studio Help  
**Purpose:** Explains how Workspace Studio flows can start when a Google Sheet changes, retrieve sheet data, and automatically update or clear rows.

---

## Core Concept

With Google Workspace Studio, flows can:

- Start automatically when a spreadsheet changes.
- Read data from sheets.
- Update rows in sheets.
- Clear rows in sheets.
- Pass sheet-related data into later flow steps using variables.

---

## Sheet Setup Requirements

In Sheets-related steps, rows can be filtered by column values. Column names are taken from the **first row** of the sheet.

The first row must meet these requirements:

- Column names must start in **cell A1**.
- Each name must be in a single cell, not merged cells.
- Each column name must be:
  - Unique
  - Non-empty

---

# “When a Sheet Changes” Starter

## How It Works

The **When a sheet changes** starter watches for changes using **two sets of conditions**:

1. **Find rows to watch for changes**
   - The flow starts only for changes to rows matching the conditions.
   - Matching is based on the **latest value** in the column.

2. **Select columns to watch**
   - The flow starts only when a change happens in selected columns.
   - Changes in other columns do **not** start the flow, even if the row matches the first condition set.
   - Multiple columns can be watched.

### Multiple Conditions

You can add multiple column conditions using **Add column** and choose:

- **AND** — row must match all conditions.
- **OR** — row must match at least one condition.

> The flow starts only if the change matches both sets of conditions.

If multiple rows change at once, such as when values are pasted into several rows, those changes are grouped into **one flow run**.

---

## Example Project Tracker Sheet

| **Project name** | **Assignee** | **Priority** | **Status** |
| --- | --- | --- | --- |
| Project A | Kim | Low | In progress |
| Project B | Yuri | High | Done |
| Project C | Lee | Medium | In progress |
| Project D | Kim | Medium | Done |
| Project E | Lee | High | Not started |

---

## Setup Examples

### Start for Any Change to the Sheet

By default, the starter watches:

- All rows
- New values in any column

---

### Start When One of Your Projects Changes to “High” Priority

For a project tracker with columns like **Project name**, **Assignee**, **Priority**, and **Status**:

- For rows to watch:
  - Column: `Assignee`
  - Value: your name
- For new values to watch:
  - Column: `Priority`
  - Value: `High`
  - To run for any priority change, set value to `Any`

**Important note:**

> Because the starter is based on the latest values in the column, it won’t start if the assignee is changed to someone besides you at the same time as the priority changes.

---

### Start When You’re Assigned a Project

- For rows to watch:
  - Column: `Assignee`
  - Value: `Any` or your name
- For new values to watch:
  - Column: `Assignee`
  - Value: your name

Because matching uses the latest column value, the flow can start for a row that just changed to your name.

---

## Variables from “When a Sheet Changes”

Later steps can reference variables containing:

- Spreadsheet and sheet details
- Who made the change
- Number of rows that changed and matched the conditions
- Data from the changed rows that matched the conditions

Data is available by column.

Example variable:

> **Latest values “Project name”**

This returns the project name from the row that started the flow.

If a bulk change affects several rows, the variable returns a **list of values**, but only from rows matching the starter conditions.

---

## Example: Email Kim When Projects Become High Priority

Message template:

> “**[Latest values “Project name”]** is now a high priority!”

Using the example tracker:

- If **Project A** changes from `Low` to `High`, Kim receives:

> “Project A is now a high priority!”

- If **all projects** change to `High`, Kim receives:

> “Project A, Project D is now a high priority!”

Only **Project A** and **Project D** are listed because only those rows have `Kim` in the **Assignee** column.

---

# “Get Sheet Contents”

## Purpose

The **Get sheet contents** step retrieves data by column from one or more matching rows.

It is important to set accurate matching conditions so the flow retrieves only relevant rows.

---

## Variables from “Get Sheet Contents”

Later steps can use variables containing:

- Spreadsheet and sheet details
- Number of rows matching the conditions
- Data from matching rows

There is one variable per column:

> **Matching values “_column name_”**

This variable contains the latest values for that column **only from rows that matched the conditions**, not from all rows.

If multiple rows match, it returns a **list of values** from that column.

---

## Example Project Tracker Sheet

| **Project name** | **Assignee** | **Priority** | **Status** |
| --- | --- | -

[... summary truncated for context management ...]
