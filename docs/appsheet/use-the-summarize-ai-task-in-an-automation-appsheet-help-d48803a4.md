---
title: "Use the Summarize AI task in an automation - AppSheet Help"
source_url: "https://support.google.com/appsheet/answer/16468184?hl=en"
product_area: "appsheet"
retrieved_at: "2026-06-15T12:25:04Z"
extraction_method: "web_extract"
---

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
