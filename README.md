# Google AI Workspace Documentation Archive

This repository is a machine-readable Markdown archive of public Google documentation for AI features available outside Google Cloud, focused on Google Workspace Business/Enterprise usage and adjacent end-user tools.

Excluded: Google Cloud, Vertex AI, Firebase, BigQuery, Ads, Analytics, and other developer/cloud products. Included: Gemini for Google Workspace, Gemini Apps for work/school accounts, Gmail, Docs, Sheets, Slides, Drive, Calendar, Meet, Chat, Google Vids, NotebookLM, Workspace Learning Center, Admin Console guidance, Workspace site pages, and selected Workspace developer pages when they describe Workspace integrations rather than Google Cloud.

## How to use

- Start with `sources/manifest.json` for a structured list of documents.
- Read product folders under `docs/`.
- Every Markdown file includes YAML front matter with `title`, `source_url`, `product_area`, and `retrieved_at`.
- Use this as a retrieval corpus for agents that need to help users solve business problems with Google AI and Workspace tools.

## Coverage summary

| Product area | Documents |
|---|---:|
| admin-console | 17 |
| appsheet | 9 |
| calendar | 5 |
| chat | 4 |
| docs-editors | 9 |
| drive | 5 |
| forms | 5 |
| gemini-apps | 5 |
| gmail | 9 |
| google-vids | 12 |
| keep | 3 |
| looker-studio | 5 |
| meet | 7 |
| notebooklm | 17 |
| sheets | 7 |
| slides | 6 |
| workspace-developers | 5 |
| workspace-learning-center | 4 |
| workspace-site | 147 |
| workspace-studio | 12 |
| workspace-studio-admin | 5 |


Total documents: 298

## Important notes

- This archive preserves source URLs for citation and freshness checks.
- Some Google Help pages were collected through a Markdown extraction service because direct support.google.com crawling rate-limited this environment; those files contain `extraction_method: web_extract`.
- Google frequently changes Workspace AI availability, admin controls, and feature names; agents should prefer the source URL when making high-stakes decisions.
- The crawl intentionally avoids Google Cloud documentation.

## Regeneration

The generation script used locally is `build_google_ai_workspace_docs.py` in the repository root.
