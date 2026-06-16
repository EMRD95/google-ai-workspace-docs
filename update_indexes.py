#!/usr/bin/env python3
import pathlib, re, json, shutil
from collections import defaultdict
from datetime import datetime, timezone

ROOT = pathlib.Path('/home/ubu/google-ai-workspace-docs')
DOCS = ROOT / 'docs'
NOTEBOOKLM = ROOT / 'notebooklm'
SOURCES = ROOT / 'sources'
DOCS.mkdir(parents=True, exist_ok=True)
SOURCES.mkdir(exist_ok=True)

front_re = re.compile(r'^---\n(.*?)\n---\n', re.S)

def parse_meta(txt):
    m = front_re.match(txt)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip().strip('"')
    return meta

def strip_frontmatter(txt):
    return front_re.sub('', txt, count=1).strip()

manifest = []
for p in sorted(DOCS.glob('*.md')):
    if p.name == 'README.md':
        continue
    txt = p.read_text(encoding='utf-8', errors='ignore')
    meta = parse_meta(txt)
    title_match = re.search(r'^#\s+(.+)$', txt, re.M)
    title = meta.get('title') or (title_match.group(1) if title_match else p.stem)
    url = meta.get('source_url', '')
    area = meta.get('product_area', 'unknown')
    manifest.append({
        'title': title,
        'source_url': url,
        'product_area': area,
        'path': str(p.relative_to(ROOT)),
    })

# Dedupe by source_url
uniq = []
seen = set()
for item in manifest:
    key = item['source_url'] or item['path']
    if key in seen:
        continue
    seen.add(key)
    uniq.append(item)
manifest = uniq

# Write raw manifest
(SOURCES / 'manifest.json').write_text(
    json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8'
)

# Coverage
by_area = defaultdict(list)
for m in manifest:
    by_area[m['product_area']].append(m)

coverage = sorted((b, len(v)) for b, v in by_area.items())

# Generate NotebookLM merged sources: one source per coverage area.
# These are aggregations of official extracted pages only; no synthetic documentation.
if NOTEBOOKLM.exists():
    shutil.rmtree(NOTEBOOKLM)
NOTEBOOKLM.mkdir(parents=True, exist_ok=True)

combined_manifest = []
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
for area, items in sorted(by_area.items()):
    out_path = NOTEBOOKLM / f'{area}__combined.md'
    lines = [
        '---',
        f'title: "Combined source: {area}"',
        f'product_area: "{area}"',
        f'source_count: {len(items)}',
        f'generated_at: "{now}"',
        'source_type: "coverage_merged_official_extracts"',
        '---',
        '',
        f'# Combined source: {area}',
        '',
        f'This file merges {len(items)} official extracted source document(s) from coverage area `{area}` for NotebookLM import limits.',
        'No synthetic documentation is added; each section preserves the source URL and extracted Markdown body.',
        '',
        '## Source index',
        '',
    ]
    for i, item in enumerate(items, 1):
        lines.append(f'{i}. {item["title"]} — {item["source_url"]}')
    lines.extend(['', '---', ''])

    for i, item in enumerate(items, 1):
        src_path = ROOT / item['path']
        txt = src_path.read_text(encoding='utf-8', errors='ignore')
        body = strip_frontmatter(txt)
        lines.extend([
            f'## Source {i}: {item["title"]}',
            '',
            f'- Source URL: {item["source_url"]}',
            f'- Original file: `{item["path"]}`',
            f'- Product area: `{area}`',
            '',
            body,
            '',
            '---',
            '',
        ])
    out_path.write_text('\n'.join(lines), encoding='utf-8')
    combined_manifest.append({
        'title': f'Combined source: {area}',
        'product_area': area,
        'source_count': len(items),
        'path': str(out_path.relative_to(ROOT)),
        'source_urls': [item['source_url'] for item in items],
    })

(SOURCES / 'manifest_notebooklm_combined.json').write_text(
    json.dumps(combined_manifest, indent=2, ensure_ascii=False), encoding='utf-8'
)

# Generate llms-full.txt: one single-file corpus for LLM ingestion.
# This concatenates the raw official extracts, preserving title/source/area metadata.
llms_lines = [
    '# Google AI Workspace Documentation Archive — llms-full.txt',
    '',
    f'Generated at: {now}',
    f'Total raw official source documents: {len(manifest)}',
    f'Total coverage areas: {len(by_area)}',
    '',
    'This file concatenates all raw official extracted documents from `docs/*.md` into one LLM-ingestion file.',
    'No synthetic documentation is added. Each section preserves source URL, product area, and original file path.',
    '',
    '## Coverage index',
    '',
]
for area, count in coverage:
    llms_lines.append(f'- {area}: {count} document(s)')
llms_lines.extend(['', '## Source index', ''])
for i, item in enumerate(manifest, 1):
    llms_lines.append(f'{i}. [{item["product_area"]}] {item["title"]} — {item["source_url"]}')
llms_lines.extend(['', '---', ''])

for i, item in enumerate(manifest, 1):
    src_path = ROOT / item['path']
    txt = src_path.read_text(encoding='utf-8', errors='ignore')
    body = strip_frontmatter(txt)
    llms_lines.extend([
        f'# Document {i}: {item["title"]}',
        '',
        f'Source URL: {item["source_url"]}',
        f'Product area: {item["product_area"]}',
        f'Original file: {item["path"]}',
        '',
        body,
        '',
        '---',
        '',
    ])
(ROOT / 'llms-full.txt').write_text('\n'.join(llms_lines), encoding='utf-8')

# Generate notebooklm/README.md
nb_lines = [
    '# NotebookLM merged sources',
    '',
    f'This folder contains **{len(combined_manifest)} merged Markdown sources**, one per coverage area, for the 300-source NotebookLM limit.',
    '',
    'Import these files instead of the raw `docs/*.md` files.',
    '',
    '| File | Coverage area | Original docs |',
    '|------|---------------|---------------|',
]
for item in combined_manifest:
    file_name = pathlib.Path(item['path']).name
    nb_lines.append(f'| `{file_name}` | {item["product_area"]} | {item["source_count"]} |')
nb_lines.append('')
nb_lines.append(f'**Total NotebookLM sources: {len(combined_manifest)}**')
nb_lines.append(f'**Original extracted docs represented: {len(manifest)}**')
(NOTEBOOKLM / 'README.md').write_text('\n'.join(nb_lines) + '\n', encoding='utf-8')

# Generate docs/README.md index
lines = [
    '# Google AI Workspace Documentation Archive',
    '',
    f'Flat Markdown archive of Google AI/Workspace docs. **{len(manifest)} raw files.**',
    '',
    '## NotebookLM import',
    '',
    f'Use `notebooklm/*.md`: **{len(combined_manifest)} merged sources**, one per coverage area, under the 300-source limit.',
    '',
    'Raw one-page-per-source files remain in `docs/*.md` for traceability and RAG indexing.',
    '',
    'For single-file LLM ingestion, use root `llms-full.txt`.',
    '',
    '## Coverage',
    '',
    '| Area | Docs | NotebookLM source |',
    '|------|------|-------------------|',
]
for b, n in coverage:
    lines.append(f'| {b} | {n} | `notebooklm/{b}__combined.md` |')
lines.append('')
lines.append(f'**Total raw documents: {len(manifest)}**')
lines.append(f'**Total NotebookLM merged sources: {len(combined_manifest)}**')
lines.append('')
lines.append('## How to browse')
lines.append('')
lines.append('- Raw official extracts: `docs/*.md`')
lines.append('- NotebookLM merged imports: `notebooklm/*.md`')
lines.append('- Raw manifest: `sources/manifest.json`')
lines.append('- NotebookLM manifest: `sources/manifest_notebooklm_combined.json`')
(DOCS / 'README.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

# Root README
root_lines = [
    '# Google AI Workspace Documentation Archive',
    '',
    f'Archive of {len(manifest)} official AI/Workspace-related docs, plus {len(combined_manifest)} merged NotebookLM sources by coverage area.',
    '',
    '## Quick start',
    '',
    f'- **NotebookLM:** import `notebooklm/*.md` (**{len(combined_manifest)} sources**, under the 300-source limit)',
    '- **Single-file LLM ingestion:** use `llms-full.txt`',
    '- **Traceability:** raw extracted pages are preserved in `docs/*.md`',
    '- **Agent/RAG:** use `sources/manifest.json` for raw docs or `sources/manifest_notebooklm_combined.json` for merged sources',
    '- **Browse:** open `docs/README.md` or `notebooklm/README.md` for coverage tables',
    '',
    '## Source policy',
    '',
    'Only official, traceable source pages are included. Non-Google official sources are allowed when relevant (for example draw.io AI docs), but synthetic agent-written documentation is not included.',
    '',
    '## What\'s included',
    '',
    'Gemini for Google Workspace across Gmail, Docs, Sheets, Slides, Drive, Calendar, Meet, Chat, Forms, Keep, Google Vids, NotebookLM, Gemini Apps, AppSheet, Looker Studio, Workspace Studio, plus Admin Console, Workspace Developers, adjacent Google AI product docs, and selected official third-party integration docs such as draw.io AI diagram generation.',
    '',
    '## What\'s excluded',
    '',
    '- Google Cloud as standalone product documentation (Vertex AI, BigQuery, Firebase…)',
    '- Non-official/untraceable articles, community threads, and agent-authored workflow notes',
    '- Community threads, defunct Labs/Experiments pages',
    '',
    '## Coverage',
    '',
    '| Area | Raw docs | NotebookLM source |',
    '|------|----------|-------------------|',
]
for b, n in coverage:
    root_lines.append(f'| {b} | {n} | `notebooklm/{b}__combined.md` |')
root_lines.append('')
root_lines.append(f'**Total raw documents: {len(manifest)}**')
root_lines.append(f'**Total NotebookLM merged sources: {len(combined_manifest)}**')
root_lines.append('')
root_lines.append('## File conventions')
root_lines.append('')
root_lines.append('- Raw docs: every `docs/*.md` has YAML frontmatter with `title`, `source_url`, `product_area`, `retrieved_at`')
root_lines.append('- Merged docs: every `notebooklm/*__combined.md` is one coverage-area source containing the original source URLs and extracted bodies')
root_lines.append('- Prefer the source URL for high-stakes decisions')
root_lines.append('')
root_lines.append('## Regeneration')
root_lines.append('')
root_lines.append('```bash')
root_lines.append('python3 update_indexes.py')
root_lines.append('```')
(ROOT / 'README.md').write_text('\n'.join(root_lines) + '\n', encoding='utf-8')

print(json.dumps({
    'raw_total': len(manifest),
    'notebooklm_sources': len(combined_manifest),
    'coverage': coverage,
}, indent=2))
