from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class RepositoryContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.index_module = load_module("build_all_conference_indexes", "scripts/build_all_conference_indexes.py")
        cls.digest_module = load_module("generate_digest", "scripts/generate_digest.py")
        cls.map_module = load_module("build_topic_map", "scripts/build_topic_map.py")
        cls.audit_module = load_module("audit_links", "scripts/audit_links.py")
        cls.normalize_module = load_module(
            "normalize_openreview_structured_summaries",
            "scripts/normalize_openreview_structured_summaries.py",
        )

    def test_top_level_docs_exist(self) -> None:
        for relative_path in [
            "README.md",
            "CONTRIBUTING.md",
            "ROADMAP.md",
            "CHANGELOG.md",
            "LICENSE",
            "SECURITY.md",
        ]:
            self.assertTrue((ROOT / relative_path).exists(), relative_path)

    def test_manifests_are_valid_lists(self) -> None:
        for manifest in ROOT.glob("radar/data/conferences/*/*/papers_manifest.json"):
            data = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertIsInstance(data, list, manifest.as_posix())
            for item in data:
                self.assertIn("title", item, manifest.as_posix())

    def test_index_renderer_emits_markdown_table(self) -> None:
        output = self.index_module.render_index(
            [
                {
                    "title": "Example Forecasting Paper",
                    "category": "forecasting",
                    "paper_url": "https://example.com/paper",
                    "keywords": ["forecasting"],
                }
            ],
            "DemoConf",
            "2026",
        )
        self.assertIn("| Title | Paper | Code | Topic |", output)
        self.assertIn("Example Forecasting Paper", output)

    def test_digest_renderer_uses_english_sections(self) -> None:
        output = self.digest_module.render_digest(
            [
                {
                    "title": "CoRA: Boosting Time Series Foundation Models",
                    "category": "forecasting",
                    "pdf_url": "https://example.com/paper",
                }
            ],
            "2026-W11",
            title="ICLR 2026",
        )
        self.assertIn("## Repository Activity", output)
        self.assertIn("## Watchlist Papers", output)

    def test_topic_map_renderer_emits_cluster_table(self) -> None:
        output = self.map_module.render_topic_map(
            [
                {
                    "title": "Aurora: Towards Universal Generative Multimodal Time Series Forecasting",
                    "category": "generation",
                    "keywords": ["multimodal", "forecasting"],
                }
            ],
            "ICLR 2026 Topic Map",
        )
        self.assertIn("| Cluster | Signal | Representative Papers |", output)
        self.assertIn("Aurora", output)

    def test_audit_normalizes_bare_doi_urls(self) -> None:
        self.assertEqual(
            self.audit_module.normalize_url("10.1145/3711896.3737442"),
            "https://doi.org/10.1145/3711896.3737442",
        )

    def test_structured_summary_normalization_rewrites_labels(self) -> None:
        sample = (
            "- 平均review分数（公开review）: 6.0\n"
            "- 分数范围: 4.0-8.0\n"
            "- 补实验/补指标: 1\n"
            "- 暂未自动抓到显式 score change 记录；当前保留公开评审分数区间 `4.0-8.0` 作为 rebuttal 前窗口。"
        )
        normalized = self.normalize_module.normalize_text(sample)
        self.assertIn("Average public review score", normalized)
        self.assertIn("Score range", normalized)
        self.assertIn("Add experiments or metrics", normalized)
        self.assertIn("No explicit score-change record was detected automatically", normalized)


if __name__ == "__main__":
    unittest.main()
