
# tests/unit/test_codes.py
"""
Feature: Translate provider weather_code to human-readable weather_text,
with a safe fallback "Unknown" for unrecognized codes.

TDD demo:
- Red: expect a wrong value to prove the test detects incorrect behavior.
- Green: restore the expected value to "Unknown".
- Refactor: run Ruff and keep tests green (no behavior change).
"""

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

    Use this test during your recording:
    - Red: temporarily change the expectation to "Undefined" to force a failure.
    - Green: revert to "Unknown" to pass.
    """
    assert code_to_text(999) == "Unknown"
