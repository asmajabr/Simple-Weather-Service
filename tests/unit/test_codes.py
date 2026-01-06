
# tests/unit/test_codes.py
"""
Feature: Robust weather code mapping with a safe fallback for unknown values.

User Story:
  As a client of the Weather API,
  When the service encounters an unrecognized weather code,
  Then it should return "Unknown" instead of failing or returning incorrect text.

TDD flow:
  - Red: intentionally expect a wrong value to prove the test detects incorrect behavior.
  - Green: restore expected value to "Unknown".
  - Refactor: run Ruff and keep tests green (no behavior change).
"""

from src.helpers import code_to_text


def test_code_to_text_known_codes():
    """Known weather codes must map to expected human text (contract of the feature)."""
    assert code_to_text(0) == "Clear"
    assert code_to_text(1) == "Mainly clear"
    assert code_to_text(2) == "Partly cloudy"
    assert code_to_text(3) == "Overcast"


def test_code_to_text_unknown_code():
    """
    Unknown or out-of-range codes should return the safe default: "Unknown".
    Use this test for your video to demonstrate Red → Green:
      - Red (on purpose): temporarily change expected value to "Undefined".
      - Green: revert back to "Unknown".
    """
    assert code_to_text(999) == "Unknown"
