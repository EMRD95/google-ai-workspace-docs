# Google AI Workspace Documentation Archive

Archive of 440 official AI/Workspace-related docs, plus 31 merged NotebookLM sources by coverage area.

## Quick start

- **NotebookLM:** import `notebooklm/*.md` (**31 sources**, under the 300-source limit)
- **Single-file LLM ingestion:** use `llms-full.txt`
- **Traceability:** raw extracted pages are preserved in `docs/*.md`
- **Agent/RAG:** use `sources/manifest.json` for raw docs or `sources/manifest_notebooklm_combined.json` for merged sources
- **Browse:** open `docs/README.md` or `notebooklm/README.md` for coverage tables

## Source policy

Only official, traceable source pages are included. Non-Google official sources are allowed when relevant (for example draw.io AI docs), but synthetic agent-written documentation is not included.

## What's included

Gemini for Google Workspace across Gmail, Docs, Sheets, Slides, Drive, Calendar, Meet, Chat, Forms, Keep, Google Vids, NotebookLM, Gemini Apps, AppSheet, Looker Studio, Workspace Studio, plus Admin Console, Workspace Developers, adjacent Google AI product docs, and selected official third-party integration docs such as draw.io AI diagram generation.

## What's excluded

- Google Cloud as standalone product documentation (Vertex AI, BigQuery, Firebase…)
- Non-official/untraceable articles, community threads, and agent-authored workflow notes
- Community threads, defunct Labs/Experiments pages

## Coverage

| Area | Raw docs | NotebookLM source |
|------|----------|-------------------|
| admin-console | 17 | `notebooklm/admin-console__combined.md` |
| android-ai | 3 | `notebooklm/android-ai__combined.md` |
| apps-script-ai | 11 | `notebooklm/apps-script-ai__combined.md` |
| appsheet | 9 | `notebooklm/appsheet__combined.md` |
| calendar | 5 | `notebooklm/calendar__combined.md` |
| chat | 18 | `notebooklm/chat__combined.md` |
| chat-developers | 26 | `notebooklm/chat-developers__combined.md` |
| chrome-ai | 13 | `notebooklm/chrome-ai__combined.md` |
| chrome-enterprise-ai | 2 | `notebooklm/chrome-enterprise-ai__combined.md` |
| docs-editors | 7 | `notebooklm/docs-editors__combined.md` |
| drive | 8 | `notebooklm/drive__combined.md` |
| external_drawio | 3 | `notebooklm/external_drawio__combined.md` |
| forms | 5 | `notebooklm/forms__combined.md` |
| gemini-apps | 12 | `notebooklm/gemini-apps__combined.md` |
| gmail | 10 | `notebooklm/gmail__combined.md` |
| google-vids | 17 | `notebooklm/google-vids__combined.md` |
| keep | 3 | `notebooklm/keep__combined.md` |
| looker-studio | 5 | `notebooklm/looker-studio__combined.md` |
| maps-ai | 3 | `notebooklm/maps-ai__combined.md` |
| meet | 7 | `notebooklm/meet__combined.md` |
| notebooklm | 16 | `notebooklm/notebooklm__combined.md` |
| photos-ai | 5 | `notebooklm/photos-ai__combined.md` |
| search-ai | 8 | `notebooklm/search-ai__combined.md` |
| sheets | 9 | `notebooklm/sheets__combined.md` |
| slides | 6 | `notebooklm/slides__combined.md` |
| workspace-developers | 5 | `notebooklm/workspace-developers__combined.md` |
| workspace-learning-center | 14 | `notebooklm/workspace-learning-center__combined.md` |
| workspace-site | 149 | `notebooklm/workspace-site__combined.md` |
| workspace-studio | 29 | `notebooklm/workspace-studio__combined.md` |
| workspace-studio-admin | 5 | `notebooklm/workspace-studio-admin__combined.md` |
| youtube-ai | 10 | `notebooklm/youtube-ai__combined.md` |

**Total raw documents: 440**
**Total NotebookLM merged sources: 31**

## File conventions

- Raw docs: every `docs/*.md` has YAML frontmatter with `title`, `source_url`, `product_area`, `retrieved_at`
- Merged docs: every `notebooklm/*__combined.md` is one coverage-area source containing the original source URLs and extracted bodies
- Prefer the source URL for high-stakes decisions

## Regeneration

```bash
python3 update_indexes.py
```
