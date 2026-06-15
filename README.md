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
| admin-console | 2 |
| appsheet | 5 |
| calendar | 2 |
| chat | 4 |
| docs-editors | 10 |
| gemini-apps | 1 |
| gmail | 7 |
| google-vids | 8 |
| meet | 4 |
| notebooklm | 5 |
| workspace-developers | 7 |
| workspace-learning-center | 4 |
| workspace-site | 151 |


Total documents: 210

## Important notes

- This archive preserves source URLs for citation and freshness checks.
- Some Google Help pages were collected through a Markdown extraction service because direct support.google.com crawling rate-limited this environment; those files contain `extraction_method: web_extract`.
- Google frequently changes Workspace AI availability, admin controls, and feature names; agents should prefer the source URL when making high-stakes decisions.
- The crawl intentionally avoids Google Cloud documentation.

## Regeneration

The generation script used locally is `build_google_ai_workspace_docs.py` in the repository root.
