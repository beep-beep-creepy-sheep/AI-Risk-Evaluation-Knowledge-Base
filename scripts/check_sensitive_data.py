"""Flag obvious sensitive-data patterns in repository text files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PATTERNS: dict[str, re.Pattern[str]] = {
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "phone": re.compile(r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}\b"),
    "account_number": re.compile(r"\b(?:account|acct)[\s:_-]*(?:number|no|id)?[\s:_-]*\d{6,}\b", re.IGNORECASE),
    "client_id": re.compile(r"\bclient[\s:_-]*id[\s:_-]*[A-Za-z0-9-]{4,}\b", re.IGNORECASE),
    "address": re.compile(r"\b\d{1,5}\s+[A-Z][A-Za-z0-9.\s]+(?:Street|St|Road|Rd|Avenue|Ave|Lane|Ln|Drive|Dr)\b"),
    "person_name": re.compile(r"\b(?:Mr|Ms|Mrs|Dr)\.?\s+[A-Z][a-z]+\s+[A-Z][a-z]+\b"),
    "client_portfolio_phrase": re.compile(r"\bclient portfolio\b", re.IGNORECASE),
    "internal_data_phrase": re.compile(r"\binternal (?:data|memo|meeting notes|risk notes)\b", re.IGNORECASE),
}

TEXT_EXTENSIONS = {".md", ".txt", ".yaml", ".yml", ".py", ".csv"}
IGNORED_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    "node_modules",
    "dist",
    "cache",
}
IGNORED_FILES = {
    Path("evals/test_cases.yaml"),
    Path("evals/rubrics.yaml"),
}
IGNORED_TOP_LEVEL_DIRS = {"tests"}


def check_text(text: str) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for label, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            findings.append({"type": label, "match": match.group(0)})
    return findings


def _is_ignored_file(child: Path, root: Path) -> bool:
    try:
        relative = child.relative_to(root)
    except ValueError:
        relative = child
    return relative in IGNORED_FILES or any(part in IGNORED_TOP_LEVEL_DIRS for part in relative.parts)


def iter_text_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path] if path.suffix in TEXT_EXTENSIONS else []

    root = path.resolve()
    files: list[Path] = []
    for child in path.rglob("*"):
        if any(part in IGNORED_DIRS for part in child.parts):
            continue
        if _is_ignored_file(child.resolve(), root):
            continue
        if child.is_file() and child.suffix in TEXT_EXTENSIONS:
            files.append(child)
    return files


def check_path(path: Path) -> dict[Path, list[dict[str, str]]]:
    results: dict[Path, list[dict[str, str]]] = {}
    for file_path in iter_text_files(path):
        text = file_path.read_text(encoding="utf-8")
        findings = check_text(text)
        if findings:
            results[file_path] = findings
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Flag sensitive-data-like patterns.")
    parser.add_argument("path", nargs="?", default=".", help="File or directory to scan.")
    args = parser.parse_args()

    results = check_path(Path(args.path))
    if not results:
        print("No sensitive-data-like patterns found.")
        return 0

    print("Sensitive-data-like patterns found:")
    for file_path, findings in results.items():
        print(f"- {file_path}")
        for finding in findings:
            print(f"  - {finding['type']}: {finding['match']}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
