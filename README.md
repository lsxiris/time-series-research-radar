# Time Series Research Radar

Time Series Research Radar is an open-source research intelligence project for tracking time-series papers across major ML / data mining venues.

## What this project does
The repository is designed to support a repeatable workflow for:
- conference paper tracking
- public-source metadata curation
- topic clustering
- method map generation
- benchmark map generation
- reviewer / rebuttal pattern mining
- weekly digest generation

The current scope focuses on **ICLR, ICML, NeurIPS, and KDD**, with support for public sources such as OpenReview, PMLR, conference websites, and paper landing pages.

## Project boundary
This repository maintains a **public-source layer only**.

It includes:
- paper metadata
- conference / year organization
- public links (PDF / OpenReview / DOI / proceedings)
- structured review-thread files when publicly available
- derived indexes, tags, and maps built from public material

It does **not** include:
- private research notes
- unpublished experiments
- personal dissertation strategy notes
- non-public annotations

## Current status
This repository is currently in a release-ready MVP stage.

Implemented so far:
1. conference/year directory structure
2. public-source packs for ICLR 2026 time-series papers
3. ICML 2025 time-series related paper manifest with titles, links, abstracts, and tags
4. KDD 2025 time-series related paper manifest with titles, DOI links, track labels, and tags
5. multi-conference index generation
6. local PDF batch download script

## Repository structure
```text
radar/
  data/
    conferences/
      ICLR/
      ICML/
      NeurIPS/
      KDD/
    raw/
    curated/
  outputs/
    papers/
    digests/
    maps/
  docs/
  config/
scripts/
```

## Installation
```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
```

## Quick start
### 1. Initialize workspace folders
```bash
python scripts/init_workspace.py
```

### 2. Build all conference indexes
```bash
python scripts/build_all_conference_indexes.py
```

### 3. Download public PDFs locally
```bash
python scripts/download_papers.py --manifest radar/data/conferences/ICML/2025/papers_manifest.json --outdir local_papers/ICML/2025 --skip-existing
```

### 4. Generate a weekly digest skeleton
```bash
python scripts/generate_digest.py --week 2026-W11
```

## Current conference coverage
### Ready
- ICLR 2026 public source pack
- ICML 2025 time-series related paper manifest
- KDD 2025 time-series related paper manifest

### In progress / pending public availability
- NeurIPS 2025
- NeurIPS 2026
- ICML 2026
- KDD 2026

## Documentation
- `README.zh-CN.md` — Chinese overview
- `CHANGELOG.md` — change history
- `ROADMAP.md` — roadmap
- `DATA_SOURCES.md` — source coverage and limitations
- `REPO_STATUS.md` — current repository release status
- `radar/docs/MAINTENANCE_PLAN.md` — maintenance plan
- `radar/docs/OSS_APPLICATION_PREP.md` — OSS support application prep notes
- `radar/docs/SOURCE_POLICY.md` — boundary of public vs private material

## Why this repository exists
Time-series paper tracking is fragmented across OpenReview, proceedings sites, conference websites, social media, blogs, and code repositories. Researchers often spend too much time on repetitive collection and too little time on actual analysis.

This project aims to turn that repetitive work into a maintainable public workflow.

## Maintenance principles
- keep sources traceable
- prefer structured output over ad-hoc notes
- allow manual correction over blind full automation
- do not fabricate reviews, results, or citations
- do not mix private research notes into the public repository

## License
MIT
