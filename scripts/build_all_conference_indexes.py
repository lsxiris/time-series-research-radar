from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "radar" / "data" / "conferences"
GENERIC_TOPICS = {"time-series", "other-time-series", "uncategorized"}


def text_blob(item: dict) -> str:
    values = [item.get("title", ""), item.get("category", "")]
    values.extend(item.get("keywords") or [])
    return " ".join(value for value in values if value).lower()


def topic_text(item: dict) -> str:
    keywords = item.get("keywords") or []
    if keywords:
        return ", ".join(keywords)
    category = item.get("category")
    return category or "uncategorized"


def paper_link(item: dict) -> str:
    url = item.get("paper_url") or item.get("pdf_url") or item.get("openreview_url")
    return f"[Paper]({url})" if url else "N/A"


def code_link(item: dict) -> str:
    url = item.get("code_url") or item.get("github_url") or item.get("repo_url")
    return f"[Code]({url})" if url else "N/A"


def collect_stats(items: list[dict]) -> dict:
    keyword_counter: Counter[str] = Counter()
    code_count = 0
    forecasting_count = 0
    foundation_count = 0
    diffusion_count = 0
    multimodal_count = 0

    for item in items:
        keywords = item.get("keywords") or []
        keyword_counter.update(keywords)
        category = item.get("category")
        if category:
            keyword_counter[category] += 1

        blob = text_blob(item)
        if "forecast" in blob:
            forecasting_count += 1
        if "foundation" in blob:
            foundation_count += 1
        if "diffusion" in blob or "generative" in blob or category == "generation":
            diffusion_count += 1
        if "multimodal" in blob or "multi-modal" in blob:
            multimodal_count += 1
        if item.get("code_url") or item.get("github_url") or item.get("repo_url"):
            code_count += 1

    return {
        "total": len(items),
        "code": code_count,
        "forecasting": forecasting_count,
        "foundation": foundation_count,
        "diffusion": diffusion_count,
        "multimodal": multimodal_count,
        "keyword_counter": keyword_counter,
    }


def build_observations(stats: dict) -> list[str]:
    total = stats["total"]
    if total == 0:
        return ["- This page is waiting for the first curated batch."]

    observations: list[str] = []

    if stats["forecasting"] >= max(3, total // 3):
        observations.append(
            "- Forecasting is the dominant theme in this batch, making this page useful for trend tracking in predictive modeling."
        )
    if stats["foundation"] >= 2:
        observations.append("- Foundation-model and adaptation-style papers are visible enough to monitor as a recurring direction.")
    if stats["diffusion"] >= 2:
        observations.append("- Generative and diffusion-style methods appear repeatedly, suggesting stronger overlap with modern generative modeling.")
    if stats["multimodal"] >= 1:
        observations.append("- Multimodal time-series work is present in the current batch instead of pure single-series modeling only.")

    top_keywords = [
        keyword for keyword, _ in stats["keyword_counter"].most_common() if keyword not in GENERIC_TOPICS
    ]
    if not observations and top_keywords:
        observations.append(f"- The clearest cluster in the current batch is around: {', '.join(top_keywords[:3])}.")
    if not observations:
        observations.append("- This batch is still small, so the main value right now is fast navigation rather than interpretation.")
    return observations


def render_index(items: list[dict], venue: str, year: str) -> str:
    stats = collect_stats(items)
    lines = [
        f"# {venue} {year} Time-Series Papers",
        "",
        "A curated page for directly browsing paper links, code availability, and coarse topic tags.",
        "",
        "## Snapshot",
        f"- Total papers: {stats['total']}",
        f"- With code links: {stats['code']}",
        f"- Forecasting-related: {stats['forecasting']}",
        f"- Foundation-model-related: {stats['foundation']}",
        "",
        "## Maintainer Notes",
        *build_observations(stats),
        "",
    ]

    if not items:
        lines.extend(
            [
                "## Paper List",
                "",
                "| Title | Paper | Code | Topic |",
                "|---|---|---|---|",
                "| _TBD_ | N/A | N/A | waiting for the first curated batch |",
            ]
        )
        return "\n".join(lines)

    lines.extend(
        [
            "## Paper List",
            "",
            "| Title | Paper | Code | Topic |",
            "|---|---|---|---|",
        ]
    )

    def sort_key(item: dict) -> tuple[str, str]:
        return ((item.get("category") or "zzz").lower(), (item.get("title") or "").lower())

    for item in sorted(items, key=sort_key):
        title = (item.get("title") or "Untitled").replace("|", "\\|")
        topic = topic_text(item).replace("|", "\\|")
        lines.append(f"| {title} | {paper_link(item)} | {code_link(item)} | {topic} |")

    return "\n".join(lines)


def main() -> None:
    for venue_dir in sorted(BASE.iterdir()):
        if not venue_dir.is_dir():
            continue
        for year_dir in sorted(venue_dir.iterdir()):
            manifest = year_dir / "papers_manifest.json"
            if not manifest.exists():
                continue
            items = json.loads(manifest.read_text(encoding="utf-8"))
            output = year_dir / "INDEX.md"
            output.write_text(render_index(items, venue_dir.name, year_dir.name) + "\n", encoding="utf-8")
            print(f"written: {output}")


if __name__ == "__main__":
    main()
