#!/usr/bin/env python3
import pathlib, re, json
from collections import defaultdict

ROOT = pathlib.Path('/home/ubu/google-ai-workspace-docs')
DOCS = ROOT / 'docs'
DOCS.mkdir(parents=True, exist_ok=True)

manifest = []
front_re = re.compile(r'^---\n(.*?)\n---\n', re.S)

for p in sorted(DOCS.glob('*.md')):
    if p.name == 'README.md':
        continue
    txt = p.read_text(encoding='utf-8', errors='ignore')
    m = front_re.match(txt)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip().strip('"')
    title = meta.get('title') or (re.search(r'^#\s+(.+)$', txt, re.M).group(1) if re.search(r'^#\s+(.+)$', txt, re.M) else p.stem)
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

# Write manifest
(ROOT / 'sources').mkdir(exist_ok=True)
(ROOT / 'sources' / 'manifest.json').write_text(
    json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8'
)

# Coverage
by_area = defaultdict(list)
for m in manifest:
    by_area[m['product_area']].append(m)

# Generate docs/README.md index
lines = [
    "# Google AI Workspace Documentation Archive",
    "",
    "Flat Markdown archive of Google AI/Workspace docs. **296 files, one folder.**",
    "",
    "## NotebookLM import",
    "",
    "Drag any `.md` file from this folder directly into NotebookLM. Each file is a standalone help article.",
    "",
    "## Coverage",
    "",
    "| Area | Docs |",
    "|------|------|",
]
for b, items in sorted(by_area.items()):
    lines.append(f"| {b} | {len(items)} |")
lines.append("")
lines.append(f"**Total: {len(manifest)} documents**")
lines.append("")
lines.append("## How to browse")
lines.append("")
lines.append("- All files are in this folder: `docs/*.md`")
lines.append("- `sources/manifest.json` — machine-readable index with `title`, `source_url`, `product_area`, `path`")
(DOCS / 'README.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

# Root README
root_lines = [
    "# Google AI Workspace Documentation Archive",
    "",
    f"Flat Markdown archive of {len(manifest)} Google AI/Workspace help articles. Ready for NotebookLM import.",
    "",
    "## Quick start",
    "",
    "- **NotebookLM:** Drag any `docs/*.md` file directly into NotebookLM",
    "- **Agent/RAG:** Use `sources/manifest.json` as your index",
    "- **Browse:** Open `docs/README.md` for a coverage table",
    "",
    "## What's included",
    "",
    "Gemini for Google Workspace across Gmail, Docs, Sheets, Slides, Drive, Calendar, Meet, Chat, Forms, Keep, Google Vids, NotebookLM, Gemini Apps, AppSheet, Looker Studio, Workspace Studio, plus Admin Console, Workspace Developers, and Workspace site pages.",
    "",
    "## What's excluded",
    "",
    "- Google Cloud (Vertex AI, BigQuery, Firebase…)",
    "- Ads, Analytics, YouTube, Maps",
    "- Community threads, defunct Labs/Experiments pages",
    "",
    "## Coverage",
    "",
    "| Area | Docs |",
    "|------|------|",
]
coverage = sorted((b, len(v)) for b, v in by_area.items())
for b, n in coverage:
    root_lines.append(f"| {b} | {n} |")
root_lines.append("")
root_lines.append(f"**Total: {len(manifest)} documents**")
root_lines.append("")
root_lines.append("## File conventions")
root_lines.append("")
root_lines.append("- Every `.md` has YAML frontmatter: `title`, `source_url`, `product_area`, `retrieved_at`")
root_lines.append("- `source_url` preserved for citation and freshness checks")
root_lines.append("- Prefer the source URL for high-stakes decisions")
root_lines.append("")
root_lines.append("## Regeneration")
root_lines.append("")
root_lines.append("```bash")
root_lines.append("python3 update_indexes.py")
root_lines.append("```")
(ROOT / 'README.md').write_text('\n'.join(root_lines) + '\n', encoding='utf-8')

coverage_data = sorted((b, len(v)) for b, v in by_area.items())
print(json.dumps({'total': len(manifest), 'coverage': coverage_data}, indent=2))
