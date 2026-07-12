# Google AI Workspace Docs

A compact, flat documentation corpus for Google AI, Google Workspace, and official AI-related integrations.

This repository intentionally keeps the public structure minimal: no documentation tree, no JSON manifests, and no tracked Python scripts. The full source corpus is merged into a single LLM-ready text file.

## Files

- `llms.txt` — short index and corpus description.
- `llms-full.txt` — complete single-file corpus for LLM ingestion.

## Corpus contents

`llms-full.txt` contains:

- 473 official source documents
- 473 preserved source URLs
- original document titles
- product / coverage area metadata
- extracted source content only

No agent-written guides or synthetic workflow notes are included in the corpus.

## Source policy

Only official, traceable sources are included.

Official Google sources are the priority. Official non-Google sources are allowed when they document a relevant Google AI / Workspace integration or adjacent workflow, for example official draw.io documentation.

Excluded:

- community posts
- forum threads
- unofficial blog posts
- synthetic guides
- generated explanations not present in the original sources

## Source URL bases

The corpus currently includes pages from these source bases:

| Source base URL | Pages |
|---|--:|
| `https://workspace.google.com/blog` | 79 |
| `https://workspace.google.com/intl` | 48 |
| `https://developers.google.com/workspace` | 35 |
| `https://support.google.com/docs` | 31 |
| `https://support.google.com/a` | 26 |
| `https://support.google.com/workspace-studio` | 21 |
| `https://workspace.google.com/resources` | 20 |
| `https://workspace.google.com/learning` | 18 |
| `https://support.google.com/gemini` | 19 |
| `https://support.google.com/chat` | 17 |
| `https://support.google.com/chrome` | 15 |
| `https://support.google.com/notebooklm` | 13 |
| `https://developers.google.com/apps-script` | 11 |
| `https://knowledge.workspace.google.com/admin/generative-ai` | 10 |
| `https://support.google.com/youtube` | 10 |
| `https://support.google.com/appsheet` | 9 |
| `https://support.google.com/drive` | 8 |
| `https://support.google.com/websearch` | 8 |
| `https://support.google.com/mail` | 7 |
| `https://support.google.com/meet` | 7 |
| `https://workspace.google.com/solutions` | 7 |
| `https://knowledge.workspace.google.com/admin/studio` | 6 |
| `https://workspace.google.com/products` | 6 |
| `https://cloud.google.com` | 5 |
| `https://support.google.com/calendar` | 5 |
| `https://support.google.com/photos` | 5 |
| `https://blog.google` | 9 |
| `https://support.google.com/android` | 3 |
| `https://support.google.com/g` | 1 |
| `https://support.google.com/keep` | 3 |
| `https://support.google.com/maps` | 3 |
| `https://workspace.google.com/ai` | 2 |
| `https://www.drawio.com/docs` | 2 |
| `https://workspace.google.com/security` | 1 |
| `https://workspace.google.com/studio` | 1 |
| `https://www.drawio.com/doc` | 1 |

## Coverage by theme

| Theme | Pages |
|---|--:|
| `workspace-site` | 163 |
| `workspace-studio` | 29 |
| `chat-developers` | 26 |
| `chat` | 18 |
| `gemini-apps` | 21 |
| `google-vids` | 18 |
| `notebooklm` | 19 |
| `admin-console` | 17 |
| `workspace-learning-center` | 14 |
| `chrome-ai` | 13 |
| `apps-script-ai` | 11 |
| `gmail` | 10 |
| `youtube-ai` | 10 |
| `appsheet` | 9 |
| `sheets` | 9 |
| `drive` | 8 |
| `search-ai` | 8 |
| `docs-editors` | 7 |
| `meet` | 7 |
| `workspace-developers` | 7 |
| `slides` | 6 |
| `calendar` | 5 |
| `forms` | 5 |
| `looker-studio` | 5 |
| `photos-ai` | 5 |
| `workspace-studio-admin` | 5 |
| `android-ai` | 3 |
| `external_drawio` | 3 |
| `keep` | 3 |
| `maps-ai` | 3 |
| `chrome-enterprise-ai` | 2 |
| `ai-studio` | 1 |
| `gemini-enterprise` | 1 |
| `google-ai` | 1 |
| `workspace-meet` | 1 |

## Updates

The documents are intended to be refreshed regularly as Google AI / Workspace features and official help pages change.

Regular maintenance should:

- add newly published official pages
- remove dead or replaced pages
- keep only official, traceable sources
- preserve the flat repository layout
- update `llms-full.txt` and this README together

Last corpus update: 2026-07-09.
Last maintenance check: 2026-07-12.

## Usage

Use `llms-full.txt` when giving a model the complete corpus context.

Use `llms.txt` for a short overview of what the repository contains.
