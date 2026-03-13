import argparse
import json
import os
from pathlib import Path
from urllib.request import urlopen, Request


def safe_name(text: str) -> str:
    bad = '<>:"/\\|?*'
    for ch in bad:
        text = text.replace(ch, '_')
    return text[:180]


def download(url: str, target: Path):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req, timeout=60) as resp:
        data = resp.read()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return len(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--outdir', required=True)
    parser.add_argument('--limit', type=int, default=0)
    parser.add_argument('--skip-existing', action='store_true')
    args = parser.parse_args()

    items = json.loads(Path(args.manifest).read_text(encoding='utf-8'))
    outdir = Path(args.outdir)

    count = 0
    for item in items:
        if args.limit and count >= args.limit:
            break
        pdf_url = item.get('pdf_url')
        title = item.get('title', 'untitled')
        if not pdf_url:
            continue
        filename = safe_name(title) + '.pdf'
        target = outdir / filename
        if args.skip_existing and target.exists():
            print(f'skip: {target}')
            count += 1
            continue
        try:
            size = download(pdf_url, target)
            print(f'downloaded: {target} ({size} bytes)')
            count += 1
        except Exception as e:
            print(f'failed: {title} -> {e}')


if __name__ == '__main__':
    main()
