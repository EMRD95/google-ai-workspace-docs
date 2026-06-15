#!/usr/bin/env python3
"""Build a machine-readable Markdown repository of non-Cloud Google AI/Workspace docs."""
import json, re, time, hashlib, pathlib, urllib.parse, sys
from collections import defaultdict, deque
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ROOT = pathlib.Path('/home/ubu/google-ai-workspace-docs')
SEED_FILE = pathlib.Path('/home/ubu/google_ai_doc_urls.json')
SESSION = requests.Session()
SESSION.headers.update({'User-Agent':'Mozilla/5.0 (compatible; docs-archiver/1.0; +https://github.com)'} )

AI_TERMS = re.compile(r'\b(Gemini|generative AI|artificial intelligence|AI|Duet AI|NotebookLM|Google Vids|Workspace Studio|Workspace Flows|Help me write|Help me visualize|Take notes for me|Ask Gemini|smart compose|smart reply|grammar|summary|summari[sz]e|translate for me|audio overview|image generation|created with AI|AI classification|automation)\b', re.I)
EXCLUDE = re.compile(r'(cloud\.google\.com|firebase|vertex-ai|bigquery|dialogflow|google-ads|admob|analytics|merchants|payments|youtube|play.google.com|mapsplatform|developers.google.com/(?!workspace))', re.I)
ALLOWED_HOSTS = {'support.google.com','workspace.google.com','developers.google.com'}
PRODUCT_BUCKETS = [
    ('admin', '/a/'),('workspace-learning','/a/users/'),('gmail','/mail/'),('calendar','/calendar/'),('docs-editors','/docs/'),('sheets','/docs/'),('slides','/docs/'),('drive','/drive/'),('meet','/meet/'),('chat','/chat/'),('gemini-apps','/gemini/'),('notebooklm','/notebooklm'),('vids','/vids'),('workspace-site','workspace.google.com'),('workspace-developers','developers.google.com/workspace'),
]

def norm_url(url):
    url = url.strip()
    if not url.startswith('http'): return None
    p = urllib.parse.urlsplit(url)
    if p.netloc not in ALLOWED_HOSTS: return None
    if EXCLUDE.search(url): return None
    q = urllib.parse.parse_qsl(p.query, keep_blank_values=False)
    keep=[]
    for k,v in q:
        if k in ('hl','co','ref_topic'):
            if k=='hl': v='en'
            keep.append((k,v))
    if not any(k=='hl' for k,_ in keep):
        keep.append(('hl','en'))
    query=urllib.parse.urlencode(keep)
    return urllib.parse.urlunsplit((p.scheme,p.netloc,p.path.rstrip('/'),query,''))

def slugify(s, maxlen=80):
    s=re.sub(r'[^A-Za-z0-9]+','-',s).strip('-').lower()
    return (s[:maxlen].strip('-') or 'untitled')

def bucket(url, title=''):
    u=url.lower(); t=title.lower()
    if 'notebooklm' in u: return 'notebooklm'
    if 'vids' in u or 'google vids' in t: return 'google-vids'
    if '/gemini/' in u: return 'gemini-apps'
    if '/mail/' in u or 'gmail' in t: return 'gmail'
    if '/calendar/' in u: return 'calendar'
    if '/meet/' in u: return 'meet'
    if '/chat/' in u: return 'chat'
    if '/drive/' in u: return 'drive'
    if '/docs/' in u:
        if 'spreadsheet' in t or 'sheets' in t: return 'sheets'
        if 'slides' in t or 'presentation' in t: return 'slides'
        if 'forms' in t: return 'forms'
        return 'docs-editors'
    if '/a/users/' in u: return 'workspace-learning-center'
    if '/a/' in u: return 'admin-console'
    if 'developers.google.com/workspace' in u: return 'workspace-developers'
    if 'workspace.google.com' in u: return 'workspace-site'
    return 'other-google-ai'

def fetch(url):
    try:
        r=SESSION.get(url, timeout=10)
        if r.status_code>=400:
            return None, f'HTTP {r.status_code}'
        if 'text/html' not in r.headers.get('content-type',''):
            return None, 'non-html'
        return r.text, None
    except Exception as e:
        return None, str(e)

def extract(url, html):
    soup=BeautifulSoup(html,'html.parser')
    for tag in soup(['script','style','noscript','svg','form','iframe']): tag.decompose()
    title=''
    if soup.find('h1'): title=soup.find('h1').get_text(' ',strip=True)
    if not title and soup.title: title=soup.title.get_text(' ',strip=True)
    selectors=['article','main','div[role="main"]','.article-container','.devsite-article-body','.hcfe-content','.user-feedback-hidden']
    main=None
    for sel in selectors:
        main=soup.select_one(sel)
        if main and len(main.get_text(' ',strip=True))>300: break
    if not main:
        candidates=soup.find_all(['article','main','section','div'])
        main=max(candidates, key=lambda x: len(x.get_text(' ',strip=True)), default=soup.body or soup)
    text=main.get_text('\n',strip=True)
    markdown=md(str(main), heading_style='ATX', bullets='-')
    markdown=re.sub(r'\n{3,}','\n\n',markdown).strip()
    links=[]
    for a in main.find_all('a', href=True):
        nu=norm_url(urllib.parse.urljoin(url,a['href']))
        if nu: links.append(nu)
    return {'title': title or url, 'text': text, 'markdown': markdown, 'links': sorted(set(links))}

# Seeds
with open(SEED_FILE) as f: seeds=[norm_url(x['url']) for x in json.load(f)]
manual = [
 'https://support.google.com/a/users/answer/14506784?hl=en',
 'https://support.google.com/a/users/answer/14628736?hl=en',
 'https://support.google.com/a/users/answer/14143478?hl=en',
 'https://support.google.com/a/users/answer/15146419?hl=en',
 'https://support.google.com/mail/answer/13955415?hl=en',
 'https://support.google.com/mail/answer/14355636?hl=en',
 'https://support.google.com/docs/answer/13951448?hl=en',
 'https://support.google.com/docs/answer/14206696?hl=en',
 'https://support.google.com/docs/answer/15541387?hl=en',
 'https://support.google.com/docs/answer/13951445?hl=en',
 'https://support.google.com/docs/answer/15626206?hl=en',
 'https://support.google.com/meet/answer/16024610?hl=en',
 'https://support.google.com/meet/answer/14754931?hl=en',
 'https://support.google.com/meet/answer/13954947?hl=en',
 'https://support.google.com/meet/answer/14441737?hl=en',
 'https://support.google.com/chat/answer/15345722?hl=en',
 'https://support.google.com/chat/answer/17036303?hl=en',
 'https://support.google.com/calendar/answer/16690875?hl=en',
 'https://support.google.com/calendar/answer/16865189?hl=en',
 'https://support.google.com/gemini/answer/14620100?hl=en',
 'https://support.google.com/notebooklm/answer/16164461?hl=en',
 'https://support.google.com/notebooklm/answer/16269187?hl=en',
 'https://workspace.google.com/products/vids/',
 'https://workspace.google.com/solutions/ai/',
]
q=deque([u for u in seeds+[norm_url(x) for x in manual] if u])
seen=set(); docs=[]; errors=[]
MAX=180
while q and len(docs)<MAX:
    url=q.popleft()
    if not url or url in seen: continue
    seen.add(url)
    html,err=fetch(url)
    if err:
        errors.append({'url':url,'error':err}); continue
    item=extract(url,html)
    relevant=AI_TERMS.search(item['title']+'\n'+item['text']) or any(k in url.lower() for k in ['gemini','notebooklm','vids','ai'])
    if not relevant:
        continue
    item['url']=url
    item['bucket']=bucket(url,item['title'])
    docs.append(item)
    # Crawl one hop for AI-looking links and help topic neighbors.
    for link in item['links']:
        if link not in seen and (AI_TERMS.search(link) or any(x in link.lower() for x in ['gemini','notebooklm','vids','answer/139','answer/14','answer/15','answer/16','answer/17'])):
            q.append(link)
    if len(seen) % 25 == 0:
        print(f'progress seen={len(seen)} docs={len(docs)} queue={len(q)}', flush=True)
    time.sleep(0.03)

# Clean repo
ROOT.mkdir(parents=True, exist_ok=True)
for p in ROOT.glob('*'):
    if p.is_file(): p.unlink()
    elif p.is_dir():
        import shutil; shutil.rmtree(p)
(ROOT/'docs').mkdir()
(ROOT/'sources').mkdir()
by_bucket=defaultdict(list)
manifest=[]
for i,d in enumerate(docs,1):
    b=d['bucket']; by_bucket[b].append(d)
    outdir=ROOT/'docs'/b; outdir.mkdir(parents=True, exist_ok=True)
    slug=slugify(d['title'])
    fname=f'{slug}-{hashlib.sha1(d["url"].encode()).hexdigest()[:8]}.md'
    path=outdir/fname
    front={
        'title': d['title'].replace('"','\\"'),
        'source_url': d['url'],
        'product_area': b,
        'retrieved_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    }
    body='---\n'+'\n'.join(f'{k}: "{v}"' for k,v in front.items())+'\n---\n\n'
    body+=f'# {d["title"]}\n\nSource: {d["url"]}\n\n'
    body+=d['markdown']+'\n'
    path.write_text(body, encoding='utf-8')
    rel=str(path.relative_to(ROOT))
    manifest.append({'title':d['title'],'source_url':d['url'],'product_area':b,'path':rel})

(ROOT/'sources'/'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
(ROOT/'sources'/'errors.json').write_text(json.dumps(errors, indent=2, ensure_ascii=False), encoding='utf-8')

# Product indexes
for b,items in sorted(by_bucket.items()):
    lines=[f'# {b.replace("-"," ").title()}\n','Machine-readable archive of Google AI documentation for this product area.\n']
    for d in sorted(items, key=lambda x:x['title'].lower()):
        entry=next(m for m in manifest if m['source_url']==d['url'])
        lines.append(f'- [{d["title"]}](../{entry["path"]}) — [source]({d["url"]})')
    (ROOT/'docs'/b/'README.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')

coverage = sorted((b,len(v)) for b,v in by_bucket.items())
readme = f'''# Google AI Workspace Documentation Archive

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
for b,n in coverage:
    readme += f'| {b} | {n} |\n'
readme += f'''

Total documents: {len(docs)}

## Important notes

- This archive contains excerpts converted from public Google documentation pages, preserving source URLs for citation and freshness checks.
- Google frequently changes Workspace AI availability, admin controls, and feature names; agents should prefer the source URL when making high-stakes decisions.
- The crawl intentionally avoids Google Cloud documentation.

## Regeneration

The generation script used locally is `build_google_ai_workspace_docs.py` in the repository root.
'''
(ROOT/'README.md').write_text(readme, encoding='utf-8')
(pathlib.Path('/home/ubu/build_google_ai_workspace_docs.py')).replace(ROOT/'build_google_ai_workspace_docs.py')
print(json.dumps({'repo':str(ROOT),'docs':len(docs),'buckets':coverage,'errors':len(errors)}, indent=2))
