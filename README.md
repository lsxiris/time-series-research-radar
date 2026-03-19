# Time-Series Research Radar

[![CI](https://github.com/lsxiris/time-series-research-radar/actions/workflows/ci.yml/badge.svg)](https://github.com/lsxiris/time-series-research-radar/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

Time-Series Research Radar is an open research-maintenance project for tracking time-series papers across major ML venues. It turns conference updates into structured manifests, generated paper indexes, and lightweight research digests so researchers do not have to rebuild the same paper lists by hand.

The repository is intentionally maintained as a public-source layer rather than a private note dump. Every tracked paper should stay traceable to its public source, and every generated page should be reproducible from versioned manifests and scripts.

## Why This Repository Exists

- Reduce repetitive paper collection and link-cleaning work for time-series researchers.
- Keep conference-year paper packs organized in a format that can be maintained over time.
- Provide reusable outputs such as paper tables, topic maps, and weekly digests instead of one-off bookmarks.
- Make maintenance legible through changelog updates, reproducible scripts, and a clear contribution path.

## What You Can Use Today

- Curated paper manifests for ICLR, ICML, NeurIPS, and KDD under [`radar/data/conferences/`](./radar/data/conferences/)
- Generated conference pages such as [ICLR 2026](./radar/data/conferences/ICLR/2026/INDEX.md) and [ICML 2025](./radar/data/conferences/ICML/2025/INDEX.md)
- Public OpenReview thread summaries for selected ICLR 2026 papers
- Sample outputs:
  - [Sample weekly digest](./radar/outputs/digests/2026-W11.md)
  - [Sample topic map](./radar/outputs/maps/iclr-2026-topic-map.md)
  - [Sample paper index](./radar/outputs/paper_index.md)
  - [Latest link audit](./radar/outputs/audits/2026-03-18-link-audit.md)

## Quick Start

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/build_all_conference_indexes.py
python scripts/build_topic_map.py --manifest radar/data/conferences/ICLR/2026/papers_manifest.json --output radar/outputs/maps/iclr-2026-topic-map.md --title "ICLR 2026 Topic Map"
python scripts/generate_digest.py --week 2026-W11 --manifest radar/data/conferences/ICLR/2026/papers_manifest.json --output radar/outputs/digests/2026-W11.md --title "ICLR 2026 Early Signals"
python scripts/normalize_openreview_structured_summaries.py
python scripts/audit_links.py --output radar/outputs/audits/2026-03-18-link-audit.md
python scripts/validate_repository.py
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Repository Layout

```text
.
|-- radar/
|   |-- data/
|   |   |-- conferences/    # versioned conference manifests and generated indexes
|   |   `-- curated/        # curated cross-venue paper subsets
|   |-- docs/               # workflow, policy, and maintenance notes
|   `-- outputs/            # sample digests, maps, and generated artifacts
|-- scripts/                # repository automation and generation scripts
|-- tests/                  # smoke tests for repository contracts
`-- .github/                # CI and community health files
```

## Coverage Snapshot

- ICLR 2026 public-source pack with manifest and selected OpenReview thread summaries
- ICML 2025 manifest with 201 time-series related papers and metadata
- KDD 2025 manifest with 95 time-series related papers across multiple tracks
- Scaffolding for NeurIPS 2025, NeurIPS 2026, ICML 2026, and KDD 2026

## Data Quality Snapshot

- Latest link audit: 733 unique URLs checked, with 0 hard failures in the current manifests
- Soft-blocked URLs in the audit are currently concentrated on OpenReview forum pages and DOI endpoints, which often return anti-bot `403` responses to scripted checks
- Verified public code repositories are currently linked for 7 papers in the ICLR 2026 source pack

## Maintenance Workflow

1. Monitor public conference sources.
2. Add or correct structured manifests.
3. Regenerate conference indexes and sample outputs.
4. Validate repository integrity.
5. Audit public links and code repositories.
6. Update the changelog and maintenance notes.

Conference manifests, generated pages, and audit artifacts are updated incrementally as public sources evolve.

## Project Docs

- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [ROADMAP.md](./ROADMAP.md)
- [CHANGELOG.md](./CHANGELOG.md)
- [DATA_SOURCES.md](./DATA_SOURCES.md)
- [REPO_STATUS.md](./REPO_STATUS.md)
- [radar/docs/WORKFLOW.md](./radar/docs/WORKFLOW.md)
- [radar/docs/PROJECT_POSITIONING.md](./radar/docs/PROJECT_POSITIONING.md)
- [radar/docs/SOURCE_POLICY.md](./radar/docs/SOURCE_POLICY.md)

## Contributing

Issues and pull requests are welcome for missing papers, broken links, metadata corrections, code links, and workflow improvements. Contributions should keep sources traceable and should not introduce private notes or fabricated metadata.

## License

This repository is released under the [MIT License](./LICENSE).
