from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFERENCE_ROOT = ROOT / "radar" / "data" / "conferences"
REQUIRED_DOCS = [
    ROOT / "README.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "ROADMAP.md",
    ROOT / "CHANGELOG.md",
    ROOT / "LICENSE",
    ROOT / "SECURITY.md",
]
REQUIRED_OUTPUTS = [
    ROOT / "radar" / "outputs" / "digests" / "2026-W11.md",
    ROOT / "radar" / "outputs" / "maps" / "iclr-2026-topic-map.md",
]
LINK_FIELDS = ["paper_url", "pdf_url", "openreview_url"]


def iter_manifests() -> list[Path]:
    return sorted(CONFERENCE_ROOT.rglob("papers_manifest.json"))


def validate_manifest(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        return [f"{path}: manifest must contain a JSON list"]

    for index, item in enumerate(data):
        if not isinstance(item, dict):
            errors.append(f"{path}: item {index} must be an object")
            continue
        if not item.get("title"):
            errors.append(f"{path}: item {index} is missing 'title'")
        if data and not any(item.get(field) for field in LINK_FIELDS):
            errors.append(f"{path}: item {index} must include at least one public link")
    return errors


def validate_indexes() -> list[str]:
    errors: list[str] = []
    for manifest in iter_manifests():
        index_file = manifest.parent / "INDEX.md"
        if not index_file.exists():
            errors.append(f"{index_file}: missing generated index")
    return errors


def validate_required_files() -> list[str]:
    errors: list[str] = []
    for path in REQUIRED_DOCS + REQUIRED_OUTPUTS:
        if not path.exists():
            errors.append(f"{path}: missing required repository file")
    return errors


def main() -> None:
    errors: list[str] = []
    for manifest in iter_manifests():
        errors.extend(validate_manifest(manifest))
    errors.extend(validate_indexes())
    errors.extend(validate_required_files())

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)

    print(f"validated {len(iter_manifests())} manifests and required repository files")


if __name__ == "__main__":
    main()
