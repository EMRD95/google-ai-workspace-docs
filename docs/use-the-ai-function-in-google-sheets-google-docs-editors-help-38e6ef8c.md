---
title: "Use the AI function in Google Sheets - Google Docs Editors Help"
source_url: "https://support.google.com/docs/answer/15877199"
product_area: "sheets"
retrieved_at: "2026-06-15T17:21:05Z"
extraction_method: "web_extract"
---

# Use the AI Function in Google Sheets — Summary

**Source:** Google Docs Editors Help  
**URL:** https://support.google.com/docs/answer/15877199

---

## Overview

Google Sheets supports an AI function powered by **Google Workspace with Gemini**. It can be used directly in spreadsheet cells to generate or analyze text and retrieve current information.

> **Important:** This feature requires an eligible Google Workspace or Google AI plan.

The AI function can be invoked as either:

```excel
=AI()
```

or

```excel
=Gemini()
```

---

## What the AI Function Can Do

You can use the AI function in Google Sheets to:

- **Generate text**
- **Summarize information**
- **Categorize information**
- **Analyze sentiment**
- **Access real-time information from Google Search**

Google Workspace with Gemini uses relevant information from your sheet when generating or analyzing content.

---

## How to Use the AI Function in Sheets

1. Open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2. In a cell, enter an AI function using either `=AI()` or `=Gemini()`.

   Example:

   ```excel
   =AI(“Generate slogan for event in 10 words or less”, A2)
   ```

3. Alternatively, use the menu:

   **Insert → Function → AI**

4. Select the cell or cells containing an AI function.
5. Click **Generate and Insert**.
6. Optional: To regenerate output, click **Refresh and Insert**.

> **Tip:** When you click **“Generate and Insert”** or **“Refresh and Insert,”** generated content is inserted and the cell edit is attributed to you in version history.

---

## Add an AI Column to a Table

You can add an AI column directly to a table.

- When an AI column is added, the first non-header row automatically shows the AI function.
- After entering a specific function in that row, you can autofill the rest of the column with the same function and generate entries.

To add one:

- At the top right of the last column in the table, click **Insert AI column right**.

---

## Fill Columns with Gemini

> **Important:** This feature is currently only available in the US in English.

Gemini can help extend or complete spreadsheet columns to save time and reduce manual errors.

### Supported Fill Methods

- **Drag-and-drop**
  - If a column has at least one completed cell, you can use a drag entry point to fill the column based on table context.

- **Prompt-based filling**
  - For empty multi-cell selections, you can use a one-click **Fill** entry point.
  - Gemini can either:
    - Automatically fill cells when a column has at least one completed cell.
    - Use a custom prompt tailored to your needs.

---

## Syntax

```excel
AI(“prompt”,[optional range])
```

### Arguments

- **Prompt**
  - A specific instruction describing the desired action.
- **Range**
  - Optional.
  - The cell or range the prompt should use when generating data.

Using the optional range is highly recommended because the AI function does **not** have access to your entire spreadsheet or other Drive files.

---

## Example Prompts and Formulas

### Generate New Text

```excel
=AI(“Generate slogan for event in 10 words or less”, A2)
```

```excel
=AI("Create an email to the reviewer addressing specific items in their reviews.", A2:G2)
```

```excel
=AI("develop a list of keywords for the job title based on the summary of duties.", A2:C2)
```

---

### Summarize Input Cell or Range

```excel
=AI("For the customer, write a one sentence summary of their feedback.", A2:D2)
```

```excel
=AI("You are the owner of a pet sitting business. Write a 2 sentence summary for the customer about their pet’s last stay. Be a little funny.", F2)
```

```excel
=AI("List in bullet points the main themes of the book summary.", D2)
```

---

### Categorize Inputs

```excel
=AI("Classify the preview as either a spam email or not a spam email.", D2)
```

```excel
=AI("Categorize the customer inquiry as a compliment, exchange request, or return request.",C2)
```

```excel
=AI("Classify the restaurant by which New York City borough it belongs to. Use the neighborhood to help.", A2:C2)
```

---

### Analyze Sentiment

```excel
=AI("Classify the sentiment of the realtor analysis.”, D2)
```

```excel
=AI("Perform sentiment analysis on the emails sent by the customers to the barbershop.", C2)
```

```excel
=AI("Classify the body of the email, as either positive, negative, or neutral.", D2)
```

---

### Get Up-to-Date Information from the Web

```excel
=AI("What is the current capital of Kazakhstan?", A2)
```

```excel
=AI("What is the population of the list capital city?", A2:B2)
```

```excel
=AI("What is the birthday of the author who wrote the associated book. Only output the date", A2:B2")
```

---

## Using Non-Contiguous Ranges

If you want to refer to two ranges that are not next to each other, you can use concatenation inside the prompt.

Example:

```excel
=AI("Find the major themes in the customer feedback of "&B2&" using the comments: "&D2&"")
```

> **Tip:** If data in c

[... summary truncated for context management ...]
