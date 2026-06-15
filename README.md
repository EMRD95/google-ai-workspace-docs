# Google AI Workspace Documentation Archive

Machine-readable Markdown archive of public Google documentation for AI features in Google Workspace and adjacent tools.

**296 documents · 21 product areas · [github.com/EMRD95/google-ai-workspace-docs](https://github.com/EMRD95/google-ai-workspace-docs)**

## Quick start

| Use case | Go to |
|----------|------|
| Import all docs from one product into NotebookLM | `docs/combined/{area}__combined.md` — drag & drop |
| Browse by product | `docs/{product}/README.md` |
| Machine/agent consumption | `sources/manifest.json` |

## What's included

Gemini for Google Workspace across all major apps: Gmail, Docs, Sheets, Slides, Drive, Calendar, Meet, Chat, Forms, Keep, Google Vids, NotebookLM, Gemini Apps, AppSheet, Looker Studio, Workspace Studio, plus Admin Console guidance, Workspace Developers, and Workspace site pages.

## What's excluded

- Google Cloud products (Vertex AI, BigQuery, Firebase, etc.)
- Ads, Analytics, YouTube, Payments, Maps Platform
- Community forums and threads
- Defunct Workspace Labs/Experiments pages (404)

## Coverage

| Area | Docs | Description |
|------|-----:|-------------|
| workspace-site | 147 | Workspace product/solution pages (AI landing, customer stories) |
| admin-console | 17 | Admin controls for Gemini, Workspace Studio, add-ons |
| notebooklm | 17 | NotebookLM help center (full coverage) |
| google-vids | 12 | AI video creation, voiceovers, Help me create |
| workspace-studio | 12 | Flows, steps, integrations, user guide |
| appsheet | 9 | AI tasks in automations (Categorize, Summarize, Extract) |
| gmail | 9 | Help me write, summaries, suggested replies, side panel |
| docs-editors | 7 | Gemini in Docs, prompts guide |
| sheets | 7 | AI function, Help me organize, Smart Fill, Gemini side panel |
| meet | 7 | Take notes for me, Ask Gemini, translated captions |
| slides | 6 | Gemini in Slides, image generation, presentation creation |
| drive | 5 | Ask Gemini, folder/file summaries |
| forms | 5 | Gemini in Forms, response summaries, quiz creation |
| gemini-apps | 5 | Deep Research, Gems, connected apps |
| looker-studio | 5 | Conversational Analytics, data agents, code interpreter |
| workspace-developers | 5 | Workspace API AI integrations |
| calendar | 5 | Help me schedule, find times to meet, Gemini in Calendar |
| workspace-studio-admin | 5 | Admin controls for Studio steps, AI steps, activity alerts |
| workspace-learning-center | 4 | End-user AI quickstart guides |
| chat | 4 | Summarize conversations, Ask Gemini, side panel |
| keep | 3 | AI lists, supported languages |

## Structure

```
docs/
├── combined/                     ← 21 files, un par produit, pour NotebookLM
│   ├── README.md
│   ├── gmail__combined.md
│   ├── meet__combined.md
│   └── ...
├── admin-console/                ← 21 dossiers produit, chacun avec ses .md
├── appsheet/
├── ...
└── workspace-studio/
```

## File conventions

- Every doc has YAML frontmatter: `title`, `source_url`, `product_area`, `retrieved_at`
- Product READMEs index all docs in their folder + link to the combined file
- Combined files at `docs/combined/{area}__combined.md`

## Regeneration

```bash
python3 update_indexes.py   # Refresh manifest + READMEs (skips combined/)
```
