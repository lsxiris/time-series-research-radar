# Contributing

Time-Series Research Radar is maintained as a public, traceable research-maintenance repository. The goal is not to collect everything, but to maintain a reliable and reproducible public-source layer for time-series research tracking.

## Good First Contributions

- Fix broken paper links, OpenReview links, DOI links, or code links
- Correct venue, year, category, or keyword metadata in a manifest
- Add newly available public conference paper entries
- Improve generated outputs such as digests or topic maps
- Improve repository automation, validation, or documentation

## Before You Open a Pull Request

1. Read [`radar/docs/SOURCE_POLICY.md`](./radar/docs/SOURCE_POLICY.md).
2. Keep every added record traceable to a public source.
3. Avoid mixing personal research notes into repository data files.
4. Regenerate affected outputs when a manifest changes.
5. Run `python scripts/validate_repository.py`.

## Expected Workflow

1. Fork the repository and create a focused branch.
2. Update manifests or scripts in a small, reviewable change set.
3. Regenerate relevant indexes or sample outputs.
4. Add a changelog entry when the change is user-visible.
5. Open a pull request with source links and a short maintenance note.

## Pull Request Checklist

- The change is traceable to a public source.
- Generated outputs were updated if the underlying manifests changed.
- The repository still validates locally.
- The change does not add private notes, private review content, or fabricated metadata.

## What Will Usually Be Rejected

- Unsourced paper metadata or unsupported claims
- Fabricated review summaries or rebuttal content
- Large copied text blocks from copyrighted sources without clear justification
- Private annotations intended for unpublished research work

## Style Notes

- Use English for public-facing documentation and filenames.
- Prefer structured manifests and scripts over manual one-off edits.
- Keep commit messages descriptive and maintenance-oriented.
