import argparse
import json
from pathlib import Path


def render_markdown(items):
    lines = ['# Paper Index', '']
    for index, item in enumerate(items):
        if index:
            lines.append('')
        lines.append(f"## {item.get('title', 'Untitled')}")
        lines.append(f"- venue: {item.get('venue', '')}")
        lines.append(f"- year: {item.get('year', '')}")
        lines.append(f"- topic: {', '.join(item.get('topics', []))}")
        lines.append(f"- support_level: {item.get('support_level', '')}")
        lines.append(f"- risk_level: {item.get('risk_level', '')}")
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    data = json.loads(Path(args.input).read_text(encoding='utf-8'))
    out = render_markdown(data)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(out.rstrip() + '\n', encoding='utf-8')
    print(f'written: {output_path}')


if __name__ == '__main__':
    main()
