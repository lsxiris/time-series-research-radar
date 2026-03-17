from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERIC_TOPICS = {"time-series", "other-time-series", "uncategorized"}


def text_blob(item: dict) -> str:
    values = [item.get("title", ""), item.get("category", "")]
    values.extend(item.get("keywords") or [])
    return " ".join(value for value in values if value).lower()


def link_for(item: dict) -> str:
    return item.get("paper_url") or item.get("pdf_url") or item.get("openreview_url") or ""


def infer_source_label(items: list[dict], manifest_path: Path | None) -> str:
    if items:
        venue = items[0].get("venue")
        year = items[0].get("year")
        if venue and year:
            return f"{venue} {year}"
    if manifest_path is not None:
        parts = manifest_path.parts
        if len(parts) >= 3:
            return f"{parts[-3]} {parts[-2]}"
    return "Current Batch"


def summarize_topics(items: list[dict]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for item in items:
        category = item.get("category")
        if category:
            counter[category] += 1
        for keyword in item.get("keywords") or []:
            if keyword not in GENERIC_TOPICS:
                counter[keyword] += 1
    return counter


def pick_highlights(items: list[dict], top_n: int) -> list[dict]:
    def score(item: dict) -> tuple[int, str]:
        blob = text_blob(item)
        title = (item.get("title") or "").lower()
        value = 0
        for token, weight in [
            ("foundation", 5),
            ("adapter", 4),
            ("multimodal", 4),
            ("diffusion", 4),
            ("generation", 3),
            ("benchmark", 3),
            ("causal", 3),
            ("adapt", 3),
            ("drift", 2),
            ("forecast", 2),
        ]:
            if token in blob or token in title:
                value += weight
        return value, title

    ranked = sorted(items, key=score, reverse=True)
    return ranked[:top_n]


def highlight_note(item: dict) -> str:
    blob = text_blob(item)
    if "foundation" in blob and "adapt" in blob:
        return "foundation-model adaptation for forecasting"
    if "multimodal" in blob:
        return "multimodal forecasting and cross-modal signal fusion"
    if "diffusion" in blob or item.get("category") == "generation":
        return "generative modeling and diffusion-style time-series synthesis"
    if "causal" in blob:
        return "causal structure or causal generation for temporal data"
    if "benchmark" in blob:
        return "benchmarking and evaluation infrastructure"
    if "adapt" in blob or "drift" in blob:
        return "adaptation and robustness under distribution shift"
    if "forecast" in blob:
        return "forecasting-focused modeling improvements"
    return "a useful time-series direction worth monitoring"


def build_repository_activity(items: list[dict], source_label: str) -> list[str]:
    if not items:
        return ["- No manifest was supplied, so this file is currently a digest template."]

    category_counter = Counter(item.get("category") or "uncategorized" for item in items)
    lines = [f"- Curated {len(items)} tracked papers for {source_label}."]

    top_categories = ", ".join(
        f"{label} ({count})" for label, count in category_counter.most_common(3)
    )
    lines.append(f"- Current distribution by category: {top_categories}.")
    return lines


def build_research_signals(items: list[dict]) -> list[str]:
    if not items:
        return ["- Add a manifest to generate automatic research signals."]

    lines: list[str] = []
    title_blob = " ".join(item.get("title", "") for item in items).lower()
    category_counter = Counter(item.get("category") or "uncategorized" for item in items)
    topic_counter = summarize_topics(items)

    if category_counter.get("forecasting", 0) >= max(3, len(items) // 3):
        lines.append("- Forecasting remains the center of gravity in this batch, so the repository is already useful for trend tracking in predictive modeling.")
    if category_counter.get("generation", 0) >= 2 or "diffusion" in title_blob:
        lines.append("- Generative and diffusion-style time-series work is visible enough to justify a dedicated watchlist.")
    if "foundation" in title_blob:
        lines.append("- Foundation-model adaptation is no longer a one-off theme and should be monitored as a recurring direction.")
    if "multimodal" in title_blob:
        lines.append("- Multimodal formulations are appearing in time-series forecasting instead of purely single-series approaches.")

    top_topics = [label for label, _ in topic_counter.most_common() if label not in GENERIC_TOPICS]
    if not lines and top_topics:
        lines.append(f"- The clearest research signals in the current batch are: {', '.join(top_topics[:3])}.")
    if not lines:
        lines.append("- The current batch is small, so the main value is fast paper navigation rather than a stable trend conclusion.")
    return lines


def build_next_steps(items: list[dict]) -> list[str]:
    if not items:
        return [
            "- Add the first conference manifest.",
            "- Regenerate indexes and a sample topic map.",
            "- Update the changelog with the first public data pack.",
        ]

    missing_code = sum(
        1
        for item in items
        if not (item.get("code_url") or item.get("github_url") or item.get("repo_url"))
    )
    missing_pdf = sum(1 for item in items if not item.get("pdf_url"))
    lines = []

    if missing_code:
        lines.append(f"- Backfill code links for {missing_code} tracked papers where repositories become public.")
    if missing_pdf:
        lines.append(f"- Backfill public PDF links for {missing_pdf} papers when source pages expose them.")
    lines.append("- Extend the digest with cross-venue comparison once another batch is refreshed.")
    return lines[:3]


def render_template(week: str) -> str:
    return "\n".join(
        [
            f"# Weekly Digest: {week}",
            "",
            "## Repository Activity",
            "- Add the latest conference or source-pack update.",
            "",
            "## Research Signals",
            "- Summarize the main themes that emerged in this batch.",
            "",
            "## Watchlist Papers",
            "- Add a short list of notable papers and why they matter.",
            "",
            "## Next Maintenance Steps",
            "- List the next visible repository updates.",
        ]
    )


def render_digest(
    items: list[dict],
    week: str,
    title: str | None = None,
    top_n: int = 4,
    source_label: str | None = None,
) -> str:
    if not items:
        return render_template(week)

    source_label = source_label or infer_source_label(items, None)
    display_title = title or source_label
    lines = [f"# Weekly Digest: {week}", "", f"Focus: {display_title}", ""]

    lines.extend(["## Repository Activity", *build_repository_activity(items, source_label), ""])
    lines.extend(["## Research Signals", *build_research_signals(items), ""])
    lines.extend(["## Watchlist Papers"])

    for item in pick_highlights(items, top_n):
        url = link_for(item)
        title_text = item.get("title", "Untitled")
        linked = f"[{title_text}]({url})" if url else title_text
        lines.append(f"- {linked}: {highlight_note(item)}.")

    lines.extend(["", "## Next Maintenance Steps", *build_next_steps(items)])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", required=True)
    parser.add_argument("--manifest")
    parser.add_argument("--output")
    parser.add_argument("--title")
    parser.add_argument("--top-n", type=int, default=4)
    args = parser.parse_args()

    manifest_path = Path(args.manifest) if args.manifest else None
    items = []
    source_label = None
    if manifest_path is not None:
        items = json.loads(manifest_path.read_text(encoding="utf-8"))
        source_label = infer_source_label(items, manifest_path)
        if args.title is None:
            args.title = source_label

    output = Path(args.output) if args.output else ROOT / "radar" / "outputs" / "digests" / f"{args.week}.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        render_digest(items, args.week, title=args.title, top_n=args.top_n, source_label=source_label) + "\n",
        encoding="utf-8",
    )
    print(f"written: {output}")


if __name__ == "__main__":
    main()
