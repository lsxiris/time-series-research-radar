import json
import re
import urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'radar' / 'data' / 'conferences' / 'ICML' / '2025' / 'papers_manifest.json'
SOURCE = 'https://proceedings.mlr.press/v267/'
KEYWORDS = ['time series', 'timeseries', 'forecast', 'forecasting', 'temporal',
            'spatio-temporal', 'spatiotemporal', 'trajectory', 'event',
            'sequential', 'causal']


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=120).read().decode('utf-8', 'ignore')


def classify(title):
    t = title.lower()
    tags = []
    if 'forecast' in t: tags.append('forecasting')
    if 'time series' in t or 'timeseries' in t: tags.append('time-series')
    if 'classification' in t: tags.append('classification')
    if 'imputation' in t: tags.append('imputation')
    if 'anomaly' in t: tags.append('anomaly-detection')
    if 'spatio' in t or 'weather' in t: tags.append('spatiotemporal')
    if 'foundation' in t or 'zero-shot' in t: tags.append('foundation-models')
    if 'causal' in t: tags.append('causal')
    if 'representation' in t or 'embedding' in t: tags.append('representation')
    if 'diffusion' in t: tags.append('diffusion')
    if 'conformal' in t or 'uncertain' in t: tags.append('uncertainty')
    if not tags: tags.append('other-time-series')
    return tags


def extract_abstract(page_html):
    m = re.search(r'<div id="abstract" class="abstract">\s*(.*?)\s*</div>', page_html, re.S)
    if not m:
        return ''
    abstract = re.sub(r'<[^>]+>', ' ', m.group(1))
    return unescape(re.sub(r'\s+', ' ', abstract)).strip()


def main():
    html = fetch(SOURCE)
    blocks = re.split(r'<div class="paper">', html)[1:]
    items = []
    for block in blocks:
        title_m = re.search(r'<p class="title">\s*(.*?)\s*</p>', block, re.S)
        if not title_m:
            continue
        title = unescape(re.sub(r'<[^>]+>', '', title_m.group(1)).strip())
        low = title.lower()
        if not any(k in low for k in KEYWORDS):
            continue

        abs_m = re.search(r'href="([^"]*\.html)"', block)
        pdf_m = re.search(r'href="([^"]*\.pdf)"', block)
        or_m = re.search(r'href="(https://openreview\.net/forum\?id=[^"]+)"', block)

        abs_url = abs_m.group(1) if abs_m else ''
        pdf_url = pdf_m.group(1) if pdf_m else ''
        or_url = or_m.group(1) if or_m else ''

        abstract = ''
        if abs_url:
            try:
                page = fetch(abs_url)
                abstract = extract_abstract(page)
            except Exception:
                abstract = ''

        items.append({
            'title': title,
            'venue': 'ICML',
            'year': 2025,
            'category': 'time-series',
            'keywords': classify(title),
            'source_type': 'pmlr',
            'paper_url': abs_url,
            'pdf_url': pdf_url,
            'openreview_url': or_url,
            'abstract': abstract,
            'notes': ''
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'written: {OUT} ({len(items)} items)')


if __name__ == '__main__':
    main()
