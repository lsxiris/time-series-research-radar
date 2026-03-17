from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THREAD_ROOT = ROOT / "radar" / "data" / "conferences" / "ICLR" / "2026" / "openreview_threads"

PHRASE_REPLACEMENTS = {
    "平均review分数（公开review）": "Average public review score",
    "分数范围": "Score range",
    "补实验/补指标": "Add experiments or metrics",
    "补解释/补理论": "Add explanation or theory",
    "补相关工作": "Add related work",
    "收缩主张/承认局限": "Narrow claims or acknowledge limitations",
    "补效率报告": "Add efficiency report",
    "改表述/改图示": "Revise wording or figures",
}

SCORE_CHANGE_PATTERN = re.compile(
    r"- 暂未自动抓到显式 score change 记录；当前保留公开评审分数区间 `([^`]+)` 作为 rebuttal 前窗口。"
)


def normalize_text(text: str) -> str:
    updated = text
    updated = updated.replace(" — OpenReview Structured Summary", " - OpenReview Structured Summary")
    for source, target in PHRASE_REPLACEMENTS.items():
        updated = updated.replace(source, target)

    updated = SCORE_CHANGE_PATTERN.sub(
        r"- No explicit score-change record was detected automatically; the current public review score range `\1` is kept as the pre-rebuttal window.",
        updated,
    )
    return updated


def main() -> None:
    updated_count = 0
    for path in sorted(THREAD_ROOT.glob("*-structured.md")):
        original = path.read_text(encoding="utf-8")
        normalized = normalize_text(original)
        if normalized != original:
            path.write_text(normalized, encoding="utf-8")
            updated_count += 1
            print(f"normalized: {path}")
    print(f"updated {updated_count} structured summaries")


if __name__ == "__main__":
    main()
