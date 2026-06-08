"""Validate mock eval cases and optionally score sample outputs."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from score_outputs import score_output


REQUIRED_CASE_FIELDS = {
    "id",
    "risk_category",
    "use_case",
    "severity",
    "prompt",
    "expected_behavior",
    "positive_keywords",
    "negative_keywords",
}


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validate_cases(cases: list[dict], rubric_categories: set[str]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    for index, case in enumerate(cases, start=1):
        missing = REQUIRED_CASE_FIELDS - set(case)
        if missing:
            errors.append(f"Case #{index} missing fields: {sorted(missing)}")
        case_id = case.get("id")
        if case_id in seen_ids:
            errors.append(f"Duplicate case id: {case_id}")
        seen_ids.add(case_id)
        if case.get("risk_category") not in rubric_categories:
            errors.append(f"{case_id} has unknown risk category: {case.get('risk_category')}")
        if not isinstance(case.get("positive_keywords"), list):
            errors.append(f"{case_id} positive_keywords must be a list")
        if not isinstance(case.get("negative_keywords"), list):
            errors.append(f"{case_id} negative_keywords must be a list")
    return errors


def run(repo_root: Path) -> int:
    eval_dir = repo_root / "evals"
    cases_data = load_yaml(eval_dir / "test_cases.yaml")
    rubrics_data = load_yaml(eval_dir / "rubrics.yaml")
    cases = cases_data.get("test_cases", [])
    rubric_categories = set(rubrics_data.get("risk_categories", {}))

    errors = validate_cases(cases, rubric_categories)
    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(cases)} test cases across {len(rubric_categories)} risk categories.")

    sample_dir = eval_dir / "sample_outputs"
    scored = 0
    passed = 0
    for case in cases:
        output_path = sample_dir / f"{case['id']}.txt"
        if not output_path.exists():
            continue
        result = score_output(
            output_path.read_text(encoding="utf-8"),
            positive_keywords=case["positive_keywords"],
            negative_keywords=case["negative_keywords"],
        )
        scored += 1
        passed += int(result.passed)
        status = "PASS" if result.passed else "FAIL"
        print(f"{case['id']}: {status} score={result.score}")

    if scored:
        print(f"Scored {scored} sample outputs: {passed} passed, {scored - passed} failed.")
    else:
        print("No sample outputs found. Schema validation complete.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run lightweight AI risk eval validation.")
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    args = parser.parse_args()
    return run(Path(args.repo_root))


if __name__ == "__main__":
    raise SystemExit(main())

