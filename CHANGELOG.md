# CHANGELOG

## 0.4.0 - 2026-03-13
### Added
- ICML 2025: 201 time-series related papers with title, PDF link, OpenReview link, abstract, keywords
- KDD 2025: 95 time-series related papers (research + ADS + benchmark tracks) with title, DOI, keywords
- NeurIPS 2025: directory created, pending proceedings availability
- Collection scripts: `collect_icml2025_pmlr.py`, `collect_kdd2025_titles.py`
- All conference INDEX.md regenerated
- PDF batch download running in background for ICML 2025

### Notes
- ICML 2025 abstracts auto-extracted from PMLR individual paper pages
- KDD 2025 abstracts not yet extracted (ACM DL protected by Cloudflare)
- NeurIPS 2025 proceedings not yet publicly available on papers.nips.cc

## 0.3.0 - 2026-03-13
### Added
- NeurIPS/2026, ICML/2026, KDD/2026 directory scaffolding
- Paper download script `download_papers.py`
- Conference manifest template `conference_template.json`
- Multi-conference index generator `build_all_conference_indexes.py`
- Download policy doc `DOWNLOAD_POLICY.md`

## 0.2.0 - 2026-03-13
### Added
- ICLR 2026 public source pack (14 papers + 14 OpenReview thread files)
- Conference index generator, source policy doc

## 0.1.0 - 2026-03-13
### Added
- Initial repository structure, README, ROADMAP, CHANGELOG
- Basic scripts: init, index, digest
