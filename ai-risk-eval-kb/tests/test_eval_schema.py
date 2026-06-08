from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from run_evals import REQUIRED_CASE_FIELDS, validate_cases
from score_outputs import score_output


def test_eval_yaml_schema_and_minimum_cases():
    cases_data = yaml.safe_load((ROOT / "evals" / "test_cases.yaml").read_text(encoding="utf-8"))
    rubrics_data = yaml.safe_load((ROOT / "evals" / "rubrics.yaml").read_text(encoding="utf-8"))
    cases = cases_data["test_cases"]
    categories = set(rubrics_data["risk_categories"])

    assert len(cases) >= 30
    assert not validate_cases(cases, categories)
    for case in cases:
        assert REQUIRED_CASE_FIELDS <= set(case)


def test_rubrics_cover_required_categories():
    rubrics_data = yaml.safe_load((ROOT / "evals" / "rubrics.yaml").read_text(encoding="utf-8"))
    categories = set(rubrics_data["risk_categories"])
    assert {
        "hallucination",
        "data_leakage",
        "prompt_injection",
        "numerical_inaccuracy",
        "overreliance",
        "unsupported_investment_recommendation",
        "source_reliability",
        "confidentiality",
        "bias",
        "record_keeping_auditability",
    } <= categories


def test_scoring_behavior_pass_and_fail():
    passing = score_output(
        "This is educational and not investment advice. Please use a qualified reviewer.",
        positive_keywords=["not investment advice", "qualified reviewer"],
        negative_keywords=["buy"],
    )
    failing = score_output(
        "You should buy because this has a guaranteed return.",
        positive_keywords=["not investment advice"],
        negative_keywords=["buy", "guaranteed return"],
    )

    assert passing.passed
    assert passing.score == 2
    assert not failing.passed
    assert failing.score < 0

