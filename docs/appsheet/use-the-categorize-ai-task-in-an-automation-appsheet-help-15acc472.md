---
title: "Use the Categorize AI task in an automation - AppSheet Help"
source_url: "https://support.google.com/appsheet/answer/15983005?hl=en"
product_area: "appsheet"
retrieved_at: "2026-06-15T12:25:04Z"
extraction_method: "web_extract"
---

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
