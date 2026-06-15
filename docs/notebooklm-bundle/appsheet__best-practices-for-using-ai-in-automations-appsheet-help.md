# Best practices for using AI in automations - AppSheet Help

**Product Area:** appsheet
**Source:** https://support.google.com/appsheet/answer/16052759?hl=en

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
