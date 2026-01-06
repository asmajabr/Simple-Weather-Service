# tests/integration/test_hourly.py

# Standard library
from http import HTTPStatus

import pytest

# Third-party
from fastapi.testclient import TestClient

# Local
from src.app import app

client = TestClient(app)


def test_hourly_selected_vars():
    # Build the query separately so the test line stays short
    query = "/weather/hourly?lat=51.5072&lon=-0.1276&vars=temperature_2m,windspeed_10m"
    r = client.get(query)
    assert r.status_code == HTTPStatus.OK
    body = r.json()
    assert set(body["selected"]) == {"temperature_2m", "windspeed_10m"}
    assert body["hourly"]["temperature_2m"][0] == pytest.approx(17.3)
