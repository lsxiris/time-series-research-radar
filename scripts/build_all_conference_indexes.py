import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'radar' / 'data' / 'conferences'


def render_index(items, venue, year):
    lines = [f'# {venue} {year} 时间序列论文索引', '']
    if not items:
        lines.append('- 当前尚未录入论文')
        return '\n'.join(lines)
    by_cat = {}
    for item in items:
        by_cat.setdefault(item.get('category', 'uncategorized'), []).append(item)
    for cat, papers in by_cat.items():
        lines.append(f'## {cat}')
        for p in papers:
            lines.append(f"- **{p.get('title','Untitled')}**")
            if p.get('openreview_url'):
                lines.append(f"  - OpenReview: {p['openreview_url']}")
            if p.get('pdf_url'):
                lines.append(f"  - PDF: {p['pdf_url']}")
            if p.get('arxiv_url'):
                lines.append(f"  - arXiv: {p['arxiv_url']}")
            kws = p.get('keywords', [])
            if kws:
                lines.append(f"  - Keywords: {', '.join(kws)}")
        lines.append('')
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
