---
title: "Enable and use the Code Interpreter  |  Data Studio  |  Google Cloud Documentation"
source_url: "https://cloud.google.com/looker/docs/studio/conversational-analytics-code-interpreter?hl=en"
product_area: "looker-studio"
retrieved_at: "2026-06-15T09:34:34Z"
extraction_method: "web_extract"
---

# Enable and Use the Code Interpreter — Data Studio / Conversational Analytics

**Source:** Google Cloud Documentation  
**URL:** <https://cloud.google.com/looker/docs/studio/conversational-analytics-code-interpreter?hl=en>  
**Last updated:** 2026-06-11 UTC

---

## Overview

The **Code Interpreter** is a feature of **Conversational Analytics** in **Data Studio** that converts natural language questions into **Python code** to perform advanced analytics and generate visualizations.

It extends standard SQL-powered BI capabilities by supporting more flexible and advanced analysis, including:

- Basic computations
- Charting and visualizations
- Advanced analytics
- Time series forecasting
- Statistical or coding-based analysis that would otherwise require specialized expertise

> The Code Interpreter is available for Conversational Analytics as part of a **Data Studio Pro subscription**.

It uses **the engine that powers Gemini chat** to translate user questions into Python code and execute that code.

Google also provides information on data usage here:  
[How and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance)

---

## Prerequisites

To use the Code Interpreter, you must meet the requirements for Conversational Analytics in Data Studio:

- You must be a user under a **Data Studio Pro subscription**.
- **Gemini in Data Studio** and the **Code Interpreter** setting must be enabled for the Google Cloud project associated with your Data Studio Pro subscription.

Relevant setup documentation:

- [Conversational Analytics setup and requirements](https://docs.cloud.google.com/data-studio/conversational-analytics-setup#setup_and_requirements)
- [Enable and disable Gemini in Data Studio](https://docs.cloud.google.com/data-studio/enable-and-disable-gemini-in-data-studio)

---

## Enable the Code Interpreter for Agents

To enable the Code Interpreter for all conversations and data agents:

1. In the left navigation panel within **Conversational Analytics**, click the **Advanced analytics** toggle to enable the Code Interpreter.
2. After enabling it, use Conversational Analytics normally to start conversations and ask questions of your data.

Once enabled, the Code Interpreter translates natural language prompts into Python code and executes that code to provide answers, analysis, and visualizations.

---

## Known Limitations

The Code Interpreter has several important limitations:

- It uses **Python** to solve problems. Because Python is more flexible than structured query languages, results may show **more variability** than responses from the core Conversational Analytics experience.
- For **Looker data**, Conversational Analytics can return a maximum of **5,000 rows per query**.
- The Code Interpreter supports only a specific set of Python libraries.
- The following visualization chart type is **not supported** in Code Interpreter responses:
  - Maps

> This feature is in Pre-GA. For support with errors, unexpected results, feedback, or to request support for additional Python libraries, send an email to [conversational-analytics-feedback@google.com](mailto:conversational-analytics-feedback@google.com).

For broader limitations, see:  
[Known limitations in Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics-data#known-limitations)

---

## Supported Python Libraries

The Code Interpreter supports the following Python libraries:

```text
altair
attrs
chess
contourpy
cycler
entrypoints
fonttools
fpdf
geopandas
imageio
jinja2
joblib
jsonschema
jsonschema-specifications
kiwisolver
lxml
markupsafe
matplotlib
mpmath
numexpr
numpy
opencv-python
openpyxl
packaging
pandas
patsy
pdfminer-six
pillow
plotly
protobuf
pylatex
pyparsing
PyPDF2
python-dateutil
python-docx
python-pptx
pytz
referencing
reportlab
rpds-py
scikit-image
scikit-learn
scipy
seaborn
six
statsmodels
striprtf
sympy
tabulate
tensorflow
threadpoolctl
toolz
torch
tzdata
xlrd
```

---

## Suggested Questions and Use Cases

When enabled, the Code Interpreter expands the range of questions Conversational Analytics can answer beyond standard supported question types.

Example prompts include:

- Can you explain the key drivers for sales based on my data?
- What is the lifetime value for each of my customer segments, taking into account the average purchase frequency and the average order value?
- How do sales this year compare to sales last year?
- Identify outliers in my sales data to help identify products or regions that are performing particularly well or particularly poorly.
- Perform a cohort analysis to understand customer retention.
- Are my highest margin products also the most popular products? Use this answer to provide a suggestion on how to optimize my product mix.
- What is the compound annual growth rate, or CAGR, for sales by product category for the last 3 years?
- Show the CAGR as a bar chart with product category on the x-axis and CAGR o

[... summary truncated for context management ...]
