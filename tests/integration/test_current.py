# tests/integration/test_current.py
from http import HTTPStatus
from fastapi.testclient import TestClient
import pytest
from src.app import app

client = TestClient(app)

def test_current_weather_returns_expected_values():
    r = client.get("/weather/current?lat=51.5072&lon=-0.1276")
    assert r.status_code == HTTPStatus.OK
    body = r.json()
    assert body["source"] == "open-meteo"
    assert body["current"]["temperature"] == pytest.approx(18.2)
    assert body["current"]["weather_text"] == "Mainly clear"
