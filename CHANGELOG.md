# Changelog

All notable changes to this repository are recorded here.

## 0.5.1 - 2026-03-18

### Added

- Link-audit script and generated audit report for tracked paper and code URLs
- Verified code links for the current ICLR 2026 public-source pack where public repositories were available

### Changed

- Normalized ICLR 2026 structured OpenReview summaries into English
- Refreshed conference indexes after code-link enrichment

## 0.5.0 - 2026-03-17

### Added

- English-first project documentation and clearer community-facing repository positioning
- GitHub community files: issue templates, pull request template, `CODEOWNERS`, code of conduct, and security policy
- Repository validation script and automated CI workflow
- Sample topic-map output for ICLR 2026
- `pyproject.toml`, `.editorconfig`, and repository smoke tests

### Changed

- Rewrote public-facing docs to remove mixed-language entry points and clarify maintainer workflow
- Upgraded digest generation to support structured English sample outputs from manifests
- Standardized conference index generation language and repository status pages

## 0.4.0 - 2026-03-13

### Added

- ICML 2025: 201 time-series related papers with title, PDF link, OpenReview link, abstract, and keywords
- KDD 2025: 95 time-series related papers across research, ADS, and benchmark tracks
- NeurIPS 2025 directory scaffolding pending public proceedings availability
- Collection scripts: `collect_icml2025_pmlr.py`, `collect_kdd2025_titles.py`
- Regenerated conference `INDEX.md` pages
- Local PDF batch download support for ICML 2025

### Notes

- ICML 2025 abstracts were auto-extracted from PMLR paper pages
- KDD 2025 abstracts remain incomplete because ACM DL pages are protected by anti-bot checks
- NeurIPS 2025 proceedings were not publicly available in the checked source path at the time of collection

## 0.3.0 - 2026-03-13

### Added

- NeurIPS 2026, ICML 2026, and KDD 2026 directory scaffolding
- Paper download script `download_papers.py`
- Conference manifest template `conference_template.json`
- Multi-conference index generator `build_all_conference_indexes.py`
- Download policy documentation

## 0.2.0 - 2026-03-13

### Added

- ICLR 2026 public-source pack with 14 papers and OpenReview thread files
- Conference index generation and source policy notes

## 0.1.0 - 2026-03-13

### Added

- Initial repository structure
- README, roadmap, changelog, and base scripts
