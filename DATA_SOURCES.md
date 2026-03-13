# DATA SOURCES

## Current source types
- OpenReview conference / forum pages
- PMLR proceedings pages
- conference websites
- DOI links
- public PDF links

## Current coverage
### ICLR 2026
- public source pack for 14 time-series related papers
- OpenReview thread files (raw / structured)

### ICML 2025
- time-series related papers filtered from **PMLR Volume 267**, which is the proceedings volume of ICML 2025
- titles, paper page links, PDF links, OpenReview links, abstracts, tags

### KDD 2025
- time-series related papers collected from KDD 2025 public paper lists
- research track, ADS track, and benchmark track
- titles, DOI links, track labels, tags

## Known limitations
- KDD 2025 abstract extraction is incomplete because ACM DL pages are protected by anti-bot checks
- NeurIPS 2025 has not yet been added because the standard proceedings entry point currently does not expose a 2025 volume in the checked source path
- local PDF downloads are intentionally excluded from git tracking (`local_papers/`)

## Policy
This repository stores links and structured public metadata. It does not include private annotations or private research notes.
