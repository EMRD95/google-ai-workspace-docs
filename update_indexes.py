#!/usr/bin/env python3
import pathlib, re, json, os
from collections import defaultdict
ROOT=pathlib.Path('/home/ubu/google-ai-workspace-docs')
manifest=[]
front_re=re.compile(r'^---\n(.*?)\n---\n', re.S)
for p in sorted((ROOT/'docs').rglob('*.md')):
    if p.name=='README.md': continue
    if 'notebooklm-bundle' in str(p): continue
    if p.parent.name == 'combined': continue
    txt=p.read_text(encoding='utf-8', errors='ignore')
    m=front_re.match(txt)
    meta={}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k,v=line.split(':',1); meta[k.strip()]=v.strip().strip('"')
    title=meta.get('title') or re.search(r'^#\s+(.+)$', txt, re.M).group(1) if re.search(r'^#\s+(.+)$', txt, re.M) else p.stem
    url=meta.get('source_url','')
    area=meta.get('product_area') or p.parent.name
    manifest.append({'title':title,'source_url':url,'product_area':area,'path':str(p.relative_to(ROOT))})
# dedupe source_url + keep web_extract additions with different filenames if URL absent
uniq=[]; seen=set()
for item in manifest:
    key=item['source_url'] or item['path']
    if key in seen: continue
    seen.add(key); uniq.append(item)
manifest=uniq
(ROOT/'sources').mkdir(exist_ok=True)
(ROOT/'sources'/'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
by=defaultdict(list)
for m in manifest: by[m['product_area']].append(m)
for b,items in by.items():
    d=ROOT/'docs'/b; d.mkdir(parents=True, exist_ok=True)
    lines=[f'# {b.replace("-"," ").title()}\n','Machine-readable archive of Google AI documentation for this product area.\n']
    for m in sorted(items,key=lambda x:x['title'].lower()):
        rel=os.path.relpath(ROOT/m['path'], d)
        src=f' — [source]({m["source_url"]})' if m['source_url'] else ''
        lines.append(f'- [{m["title"]}]({rel}){src}')
    (d/'README.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
coverage=sorted((b,len(v)) for b,v in by.items())
readme='''# Google AI Workspace Documentation Archive

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
'''
for b,n in coverage: readme += f'| {b} | {n} |\n'
readme += f'''

Total documents: {len(manifest)}

## Important notes

- This archive preserves source URLs for citation and freshness checks.
- Some Google Help pages were collected through a Markdown extraction service because direct support.google.com crawling rate-limited this environment; those files contain `extraction_method: web_extract`.
- Google frequently changes Workspace AI availability, admin controls, and feature names; agents should prefer the source URL when making high-stakes decisions.
- The crawl intentionally avoids Google Cloud documentation.

## Regeneration

The generation script used locally is `build_google_ai_workspace_docs.py` in the repository root.
'''
(ROOT/'README.md').write_text(readme, encoding='utf-8')
print(json.dumps({'total':len(manifest),'coverage':coverage},indent=2))
