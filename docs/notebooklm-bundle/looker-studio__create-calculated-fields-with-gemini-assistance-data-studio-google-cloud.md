# Create calculated fields with Gemini assistance  |  Data Studio  |  Google Cloud Documentation

**Product Area:** looker-studio
**Source:** https://cloud.google.com/looker/docs/studio/create-calculated-fields-gemini

# Create Calculated Fields with Gemini Assistance — Data Studio

**Source:** Google Cloud Documentation — Data Studio  
**Page:** “Create calculated fields with Gemini assistance”  
**Last updated:** 2026-06-11 UTC  
**Audience:** Report editors in Data Studio

> Looker Studio is now called **Data Studio**.

---

## Overview

This documentation explains how to use **Gemini in Data Studio** to help create **calculated fields** by describing the field you want in natural language.

Data Studio uses Gemini to suggest a formula for a calculated field based on:

- Your prompt or description
- Fields from your data source
- Data Studio functions and operators

Gemini in Data Studio is part of the **Gemini for Google Cloud** portfolio and provides generative AI-powered assistance to help users analyze data and gain insights.

Relevant resources mentioned:

- [Gemini in Data Studio](https://docs.cloud.google.com/data-studio/gemini-overview)
- [Calculated fields in Data Studio](https://docs.cloud.google.com/data-studio/about-calculated-fields)
- [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview)
- [How and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance)

---

## Requirements Before You Begin

To use Gemini assistance for calculated fields, all of the following must be true:

- You must be a user under a **Data Studio Pro subscription**.
  - Data Studio Pro licenses are available at no cost to Looker users.
- To create **chart-specific calculated fields**, you must be an **editor of the report**.
- **Field Editing in Reports** must be enabled in the data source.
- **Gemini in Data Studio** must be enabled for your **Data Studio Pro project**.

---

## How to Create a Calculated Field with Gemini Assistance

Follow these steps:

1. While writing a calculated field, click the **Help me write a calculated field** icon in the bottom-right corner of the field editor.

2. If you have **not** started writing a calculated field:
   - Data Studio prompts you to either:
     - Select a suggested prompt, or
     - Describe the kind of calculated field you want to create.
   - To use a suggested prompt, click it.
   - To write your own prompt, enter a description and click **Create**.

3. If you have **already started** writing a calculated field:
   - Data Studio uses your existing formula as context.
   - Describe how you want to change the calculated field.
   - Click **Create**.

   Additional options while refining:
   - To edit your original prompt:
     - Hover over the prompt.
     - Click the **Edit** icon.
     - Update the prompt.
     - Click **Update**.
   - To remove the previous formula from Data Studio’s context:
     - Hover over the formula.
     - Click the **Reset** icon.
   - To refine the formula:
     - Click **Refine**.
     - Provide more details, such as:
       - Adding or removing a bucket
       - Adding another field to a concatenation
     - Click **Create**.

4. To add the generated formula to the calculated field definition, click **Apply**.

5. To save the field definition, click **Save**.

### Exiting Without Saving

To exit the formula generation dialog without saving changes:

- Click the **X** in the top-right corner, or
- Click outside the dialog.

---

## Limitations

Gemini assistance for calculated fields has these limitations:

- Gemini can only help create calculated fields that meet Data Studio’s standard criteria for what calculated fields can do.
- Data Studio will **not** suggest:
  - Parameters
  - `NATIVE_DIMENSION`
- The **Looker connector** supports only some calculated-field functions.

---

## Information Used by Gemini in Data Studio

When generating formulas, Data Studio uses:

- The prompt you write to create or edit a field
- The formula definition for any field you change or refine
- The schema of the underlying data source

---

## Sample Prompts and Generated Formulas

### Example 1: Merge City and State

Prompt:

```text
Merge city and state like City, State
```

Data Studio may return:

```sql
CONCAT(Users City, ", ", Users State)
```

---

### Example 2: Bucket Sale Price in Groups of 20

Prompt:

```text
bucket sale price in groups of 20
```

Data Studio may return:

```sql
CASE
      WHEN Order Items Sale Price < 20 THEN "0-20"
      WHEN Order Items Sale Price < 40 THEN "20-40"
      WHEN Order Items Sale Price < 60 THEN "40-60"
      WHEN Order Items Sale Price < 80 THEN "60-80"
      WHEN Order Items Sale Price < 100 THEN "80-100"
      WHEN Order Items Sale Price < 120 THEN "100-120"
      WHEN Order Items Sale Price < 140 THEN "120-140"
      WHEN Order Items Sale Price < 160 THEN "140-160"
      WHEN Order Items Sale Price < 180 THEN "160-180"
      WHEN Order Items Sale Price < 200 THEN "180-200"
      ELSE "200+"
END
```

---

## Troubleshooting

If an error occurs while creating a calculated field, verify that your request is asking for something achievabl

[... summary truncated for context management ...]
