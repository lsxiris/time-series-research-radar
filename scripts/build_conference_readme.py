import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'radar' / 'data' / 'conferences' / 'ICLR' / '2026' / 'papers_manifest.json'
OUT = ROOT / 'radar' / 'data' / 'conferences' / 'ICLR' / '2026' / 'INDEX.md'


def main():
    items = json.loads(MANIFEST.read_text(encoding='utf-8'))
    lines = ['# ICLR 2026 时间序列论文索引', '']
    by_cat = {}
    for item in items:
        by_cat.setdefault(item['category'], []).append(item)
    for cat, papers in by_cat.items():
        lines.append(f'## {cat}')
        for p in papers:
            lines.append(f"- **{p['title']}**")
            lines.append(f"  - OpenReview: {p['openreview_url']}")
            lines.append(f"  - PDF: {p['pdf_url']}")
            lines.append(f"  - Forum ID: `{p['forum_id']}`")
        lines.append('')
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print(f'written: {OUT}')


if __name__ == '__main__':
    main()
