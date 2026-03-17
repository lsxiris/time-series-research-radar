# Download Policy

## Current Strategy

- The Git repository stores metadata, links, generated indexes, and automation scripts.
- Bulk PDF downloads are kept local by default.
- Public PDFs can be downloaded locally from a manifest when needed.

## Why This Policy Exists

- Keep repository size manageable
- Avoid committing large binary files unnecessarily
- Preserve the public-source origin of each document
- Lower long-term maintenance cost

## Local Download Path

Downloaded files should stay under `local_papers/`, which is intentionally excluded from Git tracking.
