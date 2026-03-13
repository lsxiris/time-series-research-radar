import json
import re
import urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'radar' / 'data' / 'conferences' / 'KDD' / '2025' / 'papers_manifest.json'
SOURCES = {
    'research': 'https://kdd2025.kdd.org/research-track-papers-2/',
    'ads': 'https://kdd2025.kdd.org/applied-data-science-ads-track-papers-2/',
    'bench': 'https://kdd2025.kdd.org/datasets-and-benchmarks-track-papers-2/'
}
KEYWORDS = ['time series', 'timeseries', 'forecast', 'forecasting', 'temporal', 'spatio-temporal', 'spatiotemporal', 'trajectory', 'event']


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'ignore')


def classify(title: str):
    t = title.lower()
    tags = []
    if 'forecast' in t:
        tags.append('forecasting')
    if 'time series' in t or 'timeseries' in t:
        tags.append('time-series')
    if 'classification' in t:
        tags.append('classification')
    if 'imputation' in t:
        tags.append('imputation')
    if 'anomaly' in t:
        tags.append('anomaly-detection')
    if 'spatio' in t or 'traffic' in t or 'weather' in t:
        tags.append('spatiotemporal')
    if 'recommendation' in t or 'recommender' in t:
        tags.append('sequential-recommendation')
    if 'stock' in t or 'financial' in t or 'market' in t:
        tags.append('finance')
    if 'adaptation' in t or 'drift' in t:
        tags.append('adaptation')
    if 'benchmark' in t or 'bench' in t or 'corpus' in t:
        tags.append('benchmark')
    if not tags:
        tags.append('other-time-series')
    return tags


def parse_page(url: str, track: str):
    html = fetch(url)
    text = re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>', ' ', html, flags=re.I)
    text = re.sub(r'<[^>]+>', '\n', text)
    text = unescape(text)
    lines = [re.sub(r'\s+', ' ', x).strip() for x in text.splitlines()]
    lines = [x for x in lines if x]
    items = []
    seen = set()
    for i, line in enumerate(lines):
        low = line.lower()
        if any(k in low for k in KEYWORDS):
            doi = ''
            for j in range(i+1, min(i+4, len(lines))):
                if lines[j].startswith('DOI: '):
                    doi = lines[j][5:]
                    break
            key = (line, doi)
            if key in seen:
                continue
            seen.add(key)
            items.append({
                'title': line,
                'venue': 'KDD',
                'year': 2025,
                'track': track,
                'category': 'time-series',
                'keywords': classify(line),
                'source_type': 'conference-page',
                'paper_url': doi,
                'pdf_url': '',
                'abstract': '',
                'notes': 'Abstract not auto-extracted yet; ACM page is protected by anti-bot checks.'
            })
    return items


def main():
    all_items = []
    for track, url in SOURCES.items():
        all_items.extend(parse_page(url, track))
    OUT.write_text(json.dumps(all_items, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'written: {OUT} ({len(all_items)} items)')


if __name__ == '__main__':
    main()
