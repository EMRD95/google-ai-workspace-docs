---
title: "Use the AI function in Google Sheets (Workspace Experiments) - Google Docs Editors Help"
source_url: "https://support.google.com/docs/answer/15820999?hl=en"
product_area: "sheets"
retrieved_at: "2026-06-15T11:54:03Z"
extraction_method: "web_extract"
---

# Use the AI function in Google Sheets (Workspace Experiments)

**Important:** This feature is part of the **Google Workspace Experiments** trusted tester program. To check if you have access, open a spreadsheet on Google Sheets and look for the **“Summarize this table”** icon on the right.  
[Learn where you can use Workspace Experiments features](https://support.google.com/docs/answer/13607340).

## Capabilities

You can use the AI function to:

- **Generate text** – tailored to your data using Gemini.
- **Summarize information** – extract key takeaways from spreadsheet content.
- **Categorize information** – group data and detect patterns (includes sentiment analysis).
- **Analyze sentiment** – classify the emotional tone of text.
- **Access real-time information** – fetch up-to-date answers from Google Search.

## Basic Usage

1. Open a [Google Sheets](https://docs.google.com/spreadsheets/u/0/) spreadsheet.
2. In a cell, enter either **`=AI()`** or **`=Gemini()`**.  
   Example:  
   `=AI(“Generate slogan for event in 10 words or less”, A2)`  
   Or go to **Insert → Function → AI**.
3. Select the cell(s) containing the AI function.
4. Click **Generate and Insert**.
5. *Optional:* Click **Refresh and Insert** to regenerate.

> **Tip:** When you generate or refresh, the cell edit is attributed to you in version history.

## Adding an AI Column to a Table

- Click **Insert AI column right** at the top right of the table’s last column.
- The first non-header row displays the AI function automatically.  
- Enter a prompt in that row; then you can autofill the rest of the column.

## Fill Columns with Gemini

*Also available for Google AI Ultra and Google AI Pro accounts.*

- **Drag-and-drop fill:** If a column has at least one completed cell, a new drag entry point lets you fill the rest based on table context.
- **Prompt-based filling:** For an empty multi-cell selection, use the one-click “Fill” entry point. Choose automatic fill (if the column already has a completed cell) or enter a custom prompt.

## Syntax

```excel
AI(“prompt”,[optional range])
```

- **prompt:** A description of the action you want (in quotes).  
- **optional range:** The cells the prompt should reference when generating output. **Strongly recommended** to improve accuracy.

## Detailed Examples

### Generate New Text
```excel
=AI(“Generate slogan for event in 10 words or less”, A2)
=AI("Create an email to the reviewer addressing specific items in their reviews.", A2:G2)
=AI("develop a list of keywords for the job title based on the summary of duties.", A2:C2)
```

### Summarize Input
```excel
=AI("For the customer, write a one sentence summary of their feedback.", A2:D2)
=AI("You are the owner of a pet sitting business. Write a 2 sentence summary for the customer about their pet’s last stay. Be a little funny.", F2)
=AI("List in bullet points the main themes of the book summary.", D2)
```

### Categorize Inputs
```excel
=AI("Classify the preview as either a spam email or not a spam email.", D2)
=AI("Categorize the customer inquiry as a compliment, exchange request, or return request.",C2)
=AI("Classify the restaurant by which New York City borough it belongs to. Use the neighborhood to help.", A2:C2)
```

### Analyze Sentiment
```excel
=AI("Classify the sentiment of the realtor analysis.", D2)
=AI("Perform sentiment analysis on the emails sent by the customers to the barbershop.", C2)
=AI("Classify the body of the email, as either positive, negative, or neutral.", D2)
```

### Fetch Real-Time Information
```excel
=AI("What is the current capital of Kazakhstan?", A2)
=AI("What is the population of the list capital city?", A2:B2)
=AI("What is the birthday of the author who wrote the associated book. Only output the date", A2:B2")
```

## Handling Non‑contiguous Ranges

Use concatenation inside the prompt to reference multiple separate ranges, but be aware that changes to those ranges will **not** trigger a refresh automatically. You must regenerate manually.

Example:  
```excel
=AI("Find the major themes in the customer feedback of "&B2&" using the comments: "&D2&"")
```

## Giving Feedback

- Click **Good suggestion** 👍 or **Bad suggestion** 👎 at the bottom right of the generated output.
- In the pop-up, you can choose which data to include:
  - Prompts
  - Ranges (only the referenced cells, without their context)
  - Outputs
- For a bad suggestion: click **Next** to select the issue and add details.
- For a good suggestion: click **Submit**.
- For general feedback: **Help → Help Sheets improve**.
- For legal issues: [create a request](https://support.google.com/legal/answer/3110420).

> **Important:** Feedback may be human‑readable. Do not submit personal, confidential, or sensitive information.

## Limitations

- Responses are **text‑only**.
- The AI function **cannot access your entire spreadsheet or Drive files** unless you explicitly include data via the optional range.
- **Undo/Redo** is not supported. Use **Refresh and Insert

[... summary truncated for context management ...]
