from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def render_readme(items: list[dict], title: str) -> str:
    category_counter = Counter(item.get("category") or "uncategorized" for item in items)
    lines = [
        f"# {title}",
        "",
        "This directory stores a public-source conference pack for time-series related papers.",
        "",
        "## Snapshot",
        f"- Total papers: {len(items)}",
    ]

    if category_counter:
        top_categories = ", ".join(
            f"{label} ({count})" for label, count in category_counter.most_common(4)
        )
        lines.append(f"- Top categories: {top_categories}")

    lines.extend(
        [
            "",
            "## Included Files",
            "- `papers_manifest.json` for structured metadata",
            "- `INDEX.md` for a generated paper table",
            "- additional public-source artifacts when available",
            "",
            "## Maintenance Rules",
            "- keep every record traceable to a public source",
            "- keep public-facing text in English",
            "- regenerate derived outputs after manifest updates",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()

    items = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    output_path = Path(args.output)
    output_path.write_text(render_readme(items, args.title) + "\n", encoding="utf-8")
    print(f"written: {output_path}")


if __name__ == "__main__":
    main()
