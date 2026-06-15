# Google AI Workspace Documentation Archive

Flat Markdown archive of 437 Google AI/Workspace help articles. Ready for NotebookLM import.

## Quick start

- **NotebookLM:** Drag any `docs/*.md` file directly into NotebookLM
- **Agent/RAG:** Use `sources/manifest.json` as your index
- **Browse:** Open `docs/README.md` for a coverage table

## What's included

Gemini for Google Workspace across Gmail, Docs, Sheets, Slides, Drive, Calendar, Meet, Chat, Forms, Keep, Google Vids, NotebookLM, Gemini Apps, AppSheet, Looker Studio, Workspace Studio, plus Admin Console, Workspace Developers, and Workspace site pages.

## What's excluded

- Google Cloud (Vertex AI, BigQuery, Firebase…)
- Ads, Analytics, YouTube, Maps
- Community threads, defunct Labs/Experiments pages

## Coverage

| Area | Docs |
|------|------|
| admin-console | 17 |
| android-ai | 3 |
| apps-script-ai | 11 |
| appsheet | 9 |
| calendar | 5 |
| chat | 18 |
| chat-developers | 26 |
| chrome-ai | 13 |
| chrome-enterprise-ai | 2 |
| docs-editors | 7 |
| drive | 8 |
| forms | 5 |
| gemini-apps | 12 |
| gmail | 10 |
| google-vids | 17 |
| keep | 3 |
| looker-studio | 5 |
| maps-ai | 3 |
| meet | 7 |
| notebooklm | 16 |
| photos-ai | 5 |
| search-ai | 8 |
| sheets | 9 |
| slides | 6 |
| workspace-developers | 5 |
| workspace-learning-center | 14 |
| workspace-site | 149 |
| workspace-studio | 29 |
| workspace-studio-admin | 5 |
| youtube-ai | 10 |

**Total: 437 documents**

## File conventions

- Every `.md` has YAML frontmatter: `title`, `source_url`, `product_area`, `retrieved_at`
- `source_url` preserved for citation and freshness checks
- Prefer the source URL for high-stakes decisions

## Regeneration

```bash
python3 update_indexes.py
```
