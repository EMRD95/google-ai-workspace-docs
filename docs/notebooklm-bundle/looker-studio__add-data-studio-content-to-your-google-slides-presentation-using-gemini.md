# Add Data Studio content to your Google Slides presentation using Gemini assistance  |  Google Cloud Documentation

**Product Area:** looker-studio
**Source:** https://cloud.google.com/looker/docs/studio/add-looker-studio-slides-gemini

# Add Data Studio Content to Google Slides Using Gemini Assistance — Summary

**Source:** Google Cloud Documentation  
**Product note:** *Looker Studio is now called Data Studio.*  
**Last updated:** 2026-06-11 UTC

## Overview

This page explains how to use **Gemini in Data Studio** to generate or enhance **Google Slides presentations** from **Data Studio reports**.

Gemini can:

- Insert Data Studio report charts into Google Slides **as images**
- Generate a **textual summary for each chart**
- Insert those summaries as **text elements**
- Create a full Google Slides deck from:
  - All report visualizations
  - Selected report visualizations
  - Data Studio content imported into an existing Slides presentation

> Gemini in Data Studio is part of the **Gemini for Google Cloud** portfolio and provides generative AI-powered assistance for analyzing and gaining insights from data.

Relevant data governance information:  
[How and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance)

---

## Key Requirements Before You Begin

To use this feature, all applicable requirements must be met:

- You must be under a **Data Studio Pro subscription**.
  - Data Studio Pro licenses are available at no cost to Looker users.
- **Gemini in Data Studio** must be enabled for your Data Studio project.
- The **Gemini for Google Cloud API** must be enabled in your Google Cloud project.
- You must be a **viewer or editor** of the Data Studio report.
- If you are only a viewer, the sharing option **Disable viewers from generating Google Slides with Gemini in Data Studio** must **not** be selected.
- You must be an **editor** of the Google Slides presentation you want to import content into.
- To add Data Studio content to an existing Google Slides presentation, you must install the **Data Studio add-on for Google Workspace**.

Important API:

```text
cloudaicompanion.googleapis.com
```

---

## Generate a Google Slides Presentation from All Visualizations

Use this option to create a deck containing every visualization in a Data Studio report.

### Steps

1. Open a Data Studio report in **view mode** or **edit mode**.
2. In the panel manager, select the **Gemini** panel.
3. Select **Generate Slides**.
4. Select **All visualizations**.
5. Data Studio generates a Google Slides presentation and saves it to your **Google Drive**.

### Generated Presentation Includes

- A **title slide** with:
  - Data Studio report title
  - Your name
  - Date generated
  - Link to the Data Studio report
- One slide for every chart, including:
  - Chart title, if available
  - Textual chart summary
- A **closing slide**

### Important Limitation

After generating the presentation this way, you **cannot edit it further in Data Studio**. To view or edit it, click the link in the **Gemini** panel.

---

## Generate a Presentation from Selected Visualizations

Use this option to choose specific report components for the generated Slides deck.

### Steps

1. Open a Data Studio report in **view mode** or **edit mode**.
2. In the panel manager, select the **Gemini** panel.
3. Select **Generate Slides**.
4. Select **Let me choose**.
5. Click the component or components to add.
   - To select multiple components:
     - **Shift-click** each component, or
     - Drag a selection area over the canvas.
   - Charts, titles, and filters are separate components.
   - Gemini only generates text summaries for **visualizations**.
6. Choose whether to add the selected components to:
   - A new slide, or
   - The current slide.
7. Click **Done** in the top banner.
8. Data Studio adds the selected components to the **Gemini** panel.
   - To disable a textual summary, click the **Summary on** icon.
   - To remove a visualization, click the **Delete** icon.
9. Repeat the selection process to add more components.
10. When finished, select **Generate Slides** in the **Gemini** panel.
11. Data Studio generates the presentation and saves it to your **Google Drive**.

### Generated Presentation Includes

- A title slide with:
  - Report title
  - Your name
  - Generation date
  - Link to the Data Studio report
- The slides you created from selected components
- A closing slide

### Important Limitation

After generation, the presentation **cannot be further edited in Data Studio**. Use the link in the **Gemini** panel to open it in Google Slides.

---

## Add Data Studio Content to an Existing Google Slides Presentation

This workflow uses the **Data Studio add-on for Google Workspace**.

### Requirement

Install the add-on:

- [Data Studio add-on for Google Workspace](https://workspace.google.com/marketplace/app/looker_studio/771955699012)

The add-on only works if:

- You are a **Data Studio Pro user**
- Gemini in Data Studio is enabled for your Data Studio project

### Steps

1. In Google Slides, click the **Data Studio** icon on the right-hand toolbar to open the **Data Studio** panel.
2. Click **Import**.
3. Data S

[... summary truncated for context management ...]
