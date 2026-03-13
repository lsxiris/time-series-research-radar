from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIRS = [
    ROOT / 'radar' / 'data' / 'raw',
    ROOT / 'radar' / 'data' / 'curated',
    ROOT / 'radar' / 'outputs' / 'papers',
    ROOT / 'radar' / 'outputs' / 'digests',
    ROOT / 'radar' / 'outputs' / 'maps',
    ROOT / 'radar' / 'config',
    ROOT / 'radar' / 'docs',
]

for d in DIRS:
    d.mkdir(parents=True, exist_ok=True)
    print(f'created: {d}')
