#!/usr/bin/env python3
"""Validate the public paper-package contract for this repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


CORE_FILES = (
    "audit-report.json",
    "audit-report_en.json",
    "figure-analysis.md",
    "figure-analysis_en.md",
    "paper-card.md",
    "paper-card_en.md",
    "source_bundle.json",
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    required_root = (
        "README.md",
        "README_CN.md",
        "SOURCE_AND_USE_NOTICE.md",
        "SOURCE_AND_USE_NOTICE_CN.md",
    )
    for name in required_root:
        if not (root / name).is_file():
            fail(errors, f"missing root file: {name}")
    if (root / "README_EN.md").exists():
        fail(errors, "README_EN.md is forbidden; README.md is the English default")

    folders = sorted(
        path for path in root.iterdir() if path.is_dir() and re.match(r"^\d{2}_", path.name)
    )
    expected_ranks = [f"{index:02d}" for index in range(1, len(folders) + 1)]
    actual_ranks = [path.name[:2] for path in folders]
    if actual_ranks != expected_ranks:
        fail(errors, f"folder ranks are not continuous newest-first navigation ranks: {actual_ranks}")

    dates: list[str] = []
    for folder in folders:
        match = re.match(r"^\d{2}_(\d{4}-\d{2}-\d{2})_.+", folder.name)
        if not match:
            fail(errors, f"invalid folder name: {folder.name}")
            continue
        dates.append(match.group(1))

        figures = folder / "figures"
        if not figures.is_dir() or not any(path.is_file() for path in figures.iterdir()):
            fail(errors, f"{folder.name}: figures/ is missing or empty")
        for name in CORE_FILES:
            if not (folder / name).is_file():
                fail(errors, f"{folder.name}: missing {name}")

        pdf = folder / "source_article.pdf"
        access = folder / "source_article_access.md"
        if pdf.is_file() == access.is_file():
            fail(errors, f"{folder.name}: require exactly one of source_article.pdf or source_article_access.md")
        if pdf.is_file() and pdf.read_bytes()[:4] != b"%PDF":
            fail(errors, f"{folder.name}: source_article.pdf is not a valid PDF signature")
        if access.is_file():
            text = access.read_text(encoding="utf-8")
            if "doi.org/" not in text.lower() or "rights" not in text.lower():
                fail(errors, f"{folder.name}: source_article_access.md lacks DOI or rights boundary")

        for name in ("source_bundle.json", "audit-report.json", "audit-report_en.json"):
            path = folder / name
            if not path.is_file():
                continue
            try:
                data = json.loads(path.read_text(encoding="utf-8-sig"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                fail(errors, f"{folder.name}: invalid {name}: {exc}")
                continue
            if name.startswith("audit-report"):
                findings = data.get("findings", [])
                bad = [item for item in findings if item.get("level") in {"error", "warning"}]
                if bad:
                    fail(errors, f"{folder.name}: {name} contains {len(bad)} error/warning finding(s)")

        for name, language_link in (
            ("paper-card.md", "paper-card_en.md"),
            ("paper-card_en.md", "paper-card.md"),
            ("figure-analysis.md", "figure-analysis_en.md"),
            ("figure-analysis_en.md", "figure-analysis.md"),
        ):
            path = folder / name
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8-sig")
            if language_link not in text:
                fail(errors, f"{folder.name}: {name} lacks reciprocal language switch")
            if name.startswith("paper-card"):
                sections = re.findall(r"^##\s+(\d{2})\b", text, re.MULTILINE)
                if sections != [f"{index:02d}" for index in range(1, 17)]:
                    fail(errors, f"{folder.name}: {name} does not contain ordered Sections 01-16")
            for target in re.findall(r"!\[[^\]]*\]\((?:<([^>]+)>|([^\s\)]+))\)", text):
                value = target[0] or target[1]
                if re.match(r"^[a-z]+://", value, re.I):
                    continue
                if not (folder / value).is_file():
                    fail(errors, f"{folder.name}: broken image link in {name}: {value}")

    if dates != sorted(dates, reverse=True):
        fail(errors, f"formal publication dates are not newest first: {dates}")
    return errors


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print(f"FAIL: {len(errors)} repository-contract error(s)")
        for item in errors:
            print(f"- {item}")
        return 1
    folders = [path for path in root.iterdir() if path.is_dir() and re.match(r"^\d{2}_", path.name)]
    print(f"PASS: {len(folders)} paper folders satisfy the bilingual package and source-access contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
