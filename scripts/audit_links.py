from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CONFERENCE_ROOT = ROOT / "radar" / "data" / "conferences"
OUTPUT_ROOT = ROOT / "radar" / "outputs" / "audits"
PAPER_FIELDS = ["paper_url", "pdf_url", "openreview_url"]
CODE_FIELDS = ["code_url", "github_url", "repo_url"]


@dataclass
class LinkResult:
    url: str
    ok: bool
    status: int
    final_url: str
    error: str = ""
    soft_blocked: bool = False


def iter_manifests() -> list[Path]:
    return sorted(CONFERENCE_ROOT.rglob("papers_manifest.json"))


def normalize_url(url: str) -> str:
    if url.startswith("10."):
        return f"https://doi.org/{url}"
    return url


def check_url(url: str, timeout: int = 20) -> LinkResult:
    url = normalize_url(url)
    request = Request(url, headers={"User-Agent": "Mozilla/5.0 (Codex link audit)"})
    try:
        with urlopen(request, timeout=timeout) as response:
            response.read(1024)
            return LinkResult(url=url, ok=True, status=response.status, final_url=response.geturl())
    except HTTPError as error:
        host = urlparse(url).netloc.lower()
        soft_blocked = error.code == 403 and host in {"doi.org", "openreview.net"}
        return LinkResult(
            url=url,
            ok=soft_blocked,
            status=error.code,
            final_url=getattr(error, "url", url),
            error=error.reason if isinstance(error.reason, str) else str(error.reason),
            soft_blocked=soft_blocked,
        )
    except URLError as error:
        return LinkResult(url=url, ok=False, status=0, final_url=url, error=str(error.reason))
    except Exception as error:  # pragma: no cover - network edge cases
        return LinkResult(url=url, ok=False, status=0, final_url=url, error=str(error))


def collect_jobs(manifests: list[Path]) -> tuple[dict[str, list[dict]], list[str]]:
    by_manifest: dict[str, list[dict]] = {}
    urls: list[str] = []

    for manifest in manifests:
        items = json.loads(manifest.read_text(encoding="utf-8"))
        rows = []
        for item in items:
            title = item.get("title", "Untitled")
            for field in PAPER_FIELDS + CODE_FIELDS:
                url = item.get(field)
                if not url:
                    continue
                rows.append({"title": title, "field": field, "url": url})
                urls.append(url)
        by_manifest[str(manifest.relative_to(ROOT))] = rows

    return by_manifest, sorted(set(urls))


def run_audit(max_workers: int = 16) -> dict[str, LinkResult]:
    manifests = iter_manifests()
    _, urls = collect_jobs(manifests)
    results: dict[str, LinkResult] = {}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {executor.submit(check_url, url): url for url in urls}
        for future in as_completed(future_map):
            result = future.result()
            results[result.url] = result

    return results


def render_markdown(by_manifest: dict[str, list[dict]], results: dict[str, LinkResult]) -> str:
    total = len(results)
    direct_ok_count = sum(1 for result in results.values() if result.ok and not result.soft_blocked)
    soft_blocked_count = sum(1 for result in results.values() if result.soft_blocked)
    failed = [result for result in results.values() if not result.ok]
    redirect_count = sum(
        1 for result in results.values() if result.ok and not result.soft_blocked and result.final_url != result.url
    )
    verified_count = direct_ok_count + soft_blocked_count

    lines = [
        f"# Link Audit Report ({date.today().isoformat()})",
        "",
        "## Summary",
        f"- Unique URLs checked: {total}",
        f"- Reachable or soft-blocked responses: {verified_count}",
        f"- HTTP 200-399 responses: {direct_ok_count}",
        f"- Soft-blocked responses: {soft_blocked_count}",
        f"- Redirected responses: {redirect_count}",
        f"- Failed responses: {len(failed)}",
        "",
    ]

    if failed:
        lines.extend(["## Failed URLs", ""])
        for result in sorted(failed, key=lambda item: item.url):
            lines.append(f"- `{result.status}` {result.url} ({result.error})")
        lines.append("")

    lines.extend(["## Manifest Breakdown", ""])

    for manifest, rows in by_manifest.items():
        if not rows:
            continue
        lines.extend([f"### {manifest}", "", "| Title | Field | Status | Final URL |", "|---|---|---|---|"])
        for row in rows:
            result = results[row["url"]]
            if result.soft_blocked:
                status = f"{result.status} soft-blocked"
            elif result.ok:
                status = f"{result.status} ok"
            else:
                status = f"{result.status or 'ERR'} failed"
            final_url = result.final_url.replace("|", "%7C")
            title = row["title"].replace("|", "\\|")
            lines.append(f"| {title} | {row['field']} | {status} | {final_url} |")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    parser.add_argument("--max-workers", type=int, default=16)
    args = parser.parse_args()

    manifests = iter_manifests()
    by_manifest, _ = collect_jobs(manifests)
    results = run_audit(max_workers=args.max_workers)

    output = Path(args.output) if args.output else OUTPUT_ROOT / f"{date.today().isoformat()}-link-audit.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_markdown(by_manifest, results) + "\n", encoding="utf-8")
    print(f"written: {output}")

    failures = sum(1 for result in results.values() if not result.ok)
    soft_blocked = sum(1 for result in results.values() if result.soft_blocked)
    print(f"checked {len(results)} unique urls; soft_blocked={soft_blocked}; failures={failures}")


if __name__ == "__main__":
    main()
