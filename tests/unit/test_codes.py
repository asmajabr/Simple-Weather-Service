
# tests/unit/test_codes.py
"""
Unit tests for src.helpers.code_to_text()

TDD flow:
- Start Red: intentionally expect a wrong value for an unknown code.
- Go Green: fix the expectation to "Unknown".
- Refactor (optional): tidy helper without changing behavior.
"""

# Local import
from src.helpers import code_to_text


def test_code_to_text_known_codes():
    """Known weather codes must map to expected human text."""
    assert code_to_text(0) == "Clear"
    assert code_to_text(1) == "Mainly clear"
    assert code_to_text(2) == "Partly cloudy"
    assert code_to_text(3) == "Overcast"


def test_code_to_text_unknown_code():
    """
    Unknown or out-of-range codes should return the safe default: "Unknown".
    Use this to demonstrate TDD (Red → Green) in your recording:
      - Red: temporarily change expected value to "Undefined".
      - Green: revert back to "Unknown".
    """
    assert code_to_text(999) == "Unknown"
