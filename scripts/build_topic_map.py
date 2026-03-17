from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

GENERIC_TOPICS = {"time-series", "other-time-series", "uncategorized"}


def text_blob(item: dict) -> str:
    values = [item.get("title", ""), item.get("category", "")]
    values.extend(item.get("keywords") or [])
    return " ".join(value for value in values if value).lower()


def collect_labels(items: list[dict]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for item in items:
        category = item.get("category")
        if category:
            counter[category] += 1
        for keyword in item.get("keywords") or []:
            if keyword not in GENERIC_TOPICS:
                counter[keyword] += 1
    return counter


def representative_titles(items: list[dict], label: str, limit: int = 3) -> list[str]:
    matched = []
    for item in items:
        keywords = item.get("keywords") or []
        if item.get("category") == label or label in keywords or label.replace("-", " ") in text_blob(item):
            matched.append(item.get("title", "Untitled"))
        if len(matched) >= limit:
            break
    return matched


def build_cross_cutting_signals(items: list[dict]) -> list[str]:
    blob = " ".join(item.get("title", "") for item in items).lower()
    signals = []
    if "foundation" in blob:
        signals.append("- Foundation-model adaptation is a visible cross-cutting thread.")
    if "diffusion" in blob or any(item.get("category") == "generation" for item in items):
        signals.append("- Generative and diffusion-style modeling keeps overlapping with time-series research.")
    if "multimodal" in blob:
        signals.append("- Multimodal forecasting is present and worth separating into its own watchlist.")
    if "benchmark" in blob:
        signals.append("- Benchmark and evaluation artifacts are emerging alongside new modeling work.")
    if not signals:
        signals.append("- The current batch is still best read as a navigation aid rather than a stable thematic map.")
    return signals


def render_topic_map(items: list[dict], title: str) -> str:
    labels = collect_labels(items)
    top_labels = labels.most_common(6)
    lines = [f"# {title}", ""]

    if not items:
        lines.extend(
            [
                "No papers are available yet.",
                "",
                "## Next Step",
                "- Add the first manifest and regenerate this map.",
            ]
        )
        return "\n".join(lines)

    lines.extend(
        [
            "## Summary",
            f"- Total tracked papers: {len(items)}",
            f"- Dominant labels: {', '.join(f'{label} ({count})' for label, count in top_labels[:4])}",
            "",
            "## Cluster Overview",
            "",
            "| Cluster | Signal | Representative Papers |",
            "|---|---|---|",
        ]
    )

    for label, count in top_labels:
        titles = representative_titles(items, label)
        signal = f"{count} tracked papers"
        title_cell = "; ".join(titles) if titles else "No representative titles yet"
        lines.append(f"| {label} | {signal} | {title_cell} |")

    lines.extend(["", "## Cross-Cutting Signals", *build_cross_cutting_signals(items)])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()

    items = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_topic_map(items, args.title) + "\n", encoding="utf-8")
    print(f"written: {output}")


if __name__ == "__main__":
    main()
