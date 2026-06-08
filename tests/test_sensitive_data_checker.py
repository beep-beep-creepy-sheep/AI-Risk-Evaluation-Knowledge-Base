from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_sensitive_data import check_text


def test_sensitive_data_checker_flags_obvious_patterns():
    findings = check_text(
        "Please review client portfolio account 123456789 for Ms. Jane Smith at jane.smith@example.com."
    )
    finding_types = {finding["type"] for finding in findings}

    assert "client_portfolio_phrase" in finding_types
    assert "account_number" in finding_types
    assert "person_name" in finding_types
    assert "email" in finding_types


def test_sensitive_data_checker_allows_mock_professional_text():
    findings = check_text(
        "Use mock data to explain volatility. Include human review, source checking, and assumptions."
    )

    assert findings == []

