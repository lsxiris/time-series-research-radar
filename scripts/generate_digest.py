import argparse
from pathlib import Path

TEMPLATE = '''# Weekly Digest: {week}

## 本周新增
- 待补充

## 本周重点论文
- 待补充

## 本周 reviewer / rebuttal 模式
- 待补充

## 下周维护计划
- 待补充
'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--week', required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    out = root / 'radar' / 'outputs' / 'digests' / f'{args.week}.md'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEMPLATE.format(week=args.week), encoding='utf-8')
    print(f'written: {out}')


if __name__ == '__main__':
    main()
