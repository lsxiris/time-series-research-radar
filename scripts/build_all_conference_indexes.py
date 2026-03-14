import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'radar' / 'data' / 'conferences'


def topic_text(item):
    keywords = item.get('keywords') or []
    if keywords:
        return ', '.join(keywords)
    category = item.get('category')
    return category or 'uncategorized'


def paper_link(item):
    url = item.get('paper_url') or item.get('pdf_url') or item.get('openreview_url')
    return f'[Paper]({url})' if url else '—'


def code_link(item):
    url = item.get('code_url') or item.get('github_url') or item.get('repo_url')
    return f'[Code]({url})' if url else '—'


def collect_stats(items):
    keyword_counter = Counter()
    for item in items:
        keyword_counter.update(item.get('keywords') or [])
        category = item.get('category')
        if category:
            keyword_counter[category] += 1

    forecasting_count = sum(
        1
        for item in items
        if 'forecast' in (item.get('title') or '').lower()
        or 'forecasting' in ' '.join(item.get('keywords') or []).lower()
        or (item.get('category') or '').lower() == 'forecasting'
    )
    foundation_count = sum(
        1
        for item in items
        if 'foundation' in (item.get('title') or '').lower()
        or 'foundation-models' in (item.get('keywords') or [])
    )
    diffusion_count = sum(
        1 for item in items if 'diffusion' in ' '.join(item.get('keywords') or []).lower() or 'diffusion' in (item.get('title') or '').lower()
    )
    multimodal_count = sum(
        1 for item in items if 'multimodal' in (item.get('title') or '').lower() or 'multi-modal' in (item.get('title') or '').lower()
    )
    code_count = sum(1 for item in items if item.get('code_url') or item.get('github_url') or item.get('repo_url'))

    return {
        'total': len(items),
        'code': code_count,
        'forecasting': forecasting_count,
        'foundation': foundation_count,
        'diffusion': diffusion_count,
        'multimodal': multimodal_count,
        'keyword_counter': keyword_counter,
    }


def build_observations(stats):
    observations = []
    total = stats['total']
    if total == 0:
        return ['- This page is waiting for the first curated batch.']

    if stats['foundation'] >= 2:
        observations.append('- Foundation-model and transfer-style papers are already a visible thread in this batch.')
    if stats['forecasting'] >= max(3, total // 3):
        observations.append('- Forecasting remains the dominant task, so this page is especially useful for trend tracking in prediction methods.')
    if stats['diffusion'] >= 2:
        observations.append('- Diffusion-style modeling appears repeatedly, suggesting stronger overlap between generative modeling and time-series research.')
    if stats['multimodal'] >= 1:
        observations.append('- Multimodal or cross-modal formulations are starting to show up instead of pure single-series modeling.')

    top_keywords = [
        keyword for keyword, _ in stats['keyword_counter'].most_common()
        if keyword not in {'time-series', 'other-time-series', 'uncategorized'}
    ]
    if not observations and top_keywords:
        observations.append(f"- The current batch clusters most visibly around: {', '.join(top_keywords[:3])}.")
    if not observations:
        observations.append('- This batch is still small, so the main value right now is fast navigation rather than trend interpretation.')
    return observations


def render_index(items, venue, year):
    stats = collect_stats(items)
    lines = [
        f'# {venue} {year} Time-Series Papers',
        '',
        'A curated page for directly browsing paper links and code availability.',
        '',
        '## Snapshot',
        f"- Total papers: {stats['total']}",
        f"- With code links: {stats['code']}",
        f"- Forecasting-related: {stats['forecasting']}",
        f"- Foundation-model-related: {stats['foundation']}",
        '',
        '## Maintainer Notes',
        *build_observations(stats),
        '',
    ]

    if not items:
        lines.extend([
            '## Paper List',
            '',
            '| Title | Paper | Code | Topic |',
            '|---|---|---|---|',
            '| _TBD_ | — | — | waiting for first batch |',
        ])
        return '\n'.join(lines)

    lines.extend([
        '## Paper List',
        '',
        '| Title | Paper | Code | Topic |',
        '|---|---|---|---|',
    ])

    def sort_key(item):
        return ((item.get('category') or 'zzz').lower(), (item.get('title') or '').lower())

    for item in sorted(items, key=sort_key):
        title = (item.get('title') or 'Untitled').replace('|', '\\|')
        topic = topic_text(item).replace('|', '\\|')
        lines.append(f'| {title} | {paper_link(item)} | {code_link(item)} | {topic} |')

    return '\n'.join(lines)


def main():
    for venue_dir in BASE.iterdir():
        if not venue_dir.is_dir():
            continue
        for year_dir in venue_dir.iterdir():
            manifest = year_dir / 'papers_manifest.json'
            if not manifest.exists():
                continue
            items = json.loads(manifest.read_text(encoding='utf-8'))
            out = year_dir / 'INDEX.md'
            out.write_text(render_index(items, venue_dir.name, year_dir.name), encoding='utf-8')
            print(f'written: {out}')


if __name__ == '__main__':
    main()
