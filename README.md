# Google AI Workspace Documentation Archive

Flat Markdown archive of 296 Google AI/Workspace help articles. Ready for NotebookLM import.

## Quick start

- **NotebookLM:** Drag any `docs/*.md` file directly into NotebookLM — no Gemini required, works as regular sources in the free tier
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
| appsheet | 9 |
| calendar | 5 |
| chat | 4 |
| docs-editors | 7 |
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

**Total: 296 documents**

## File conventions

- Every `.md` has YAML frontmatter: `title`, `source_url`, `product_area`, `retrieved_at`
- `source_url` preserved for citation and freshness checks
- Prefer the source URL for high-stakes decisions

## Regeneration

```bash
python3 update_indexes.py
```
