# tests/integration/test_forecast.py
from http import HTTPStatus
from fastapi.testclient import TestClient
import pytest
from src.app import app

client = TestClient(app)

def test_forecast_daily_values():
    r = client.get("/weather/forecast?lat=51.5072&lon=-0.1276&days=3")
    assert r.status_code == HTTPStatus.OK
    body = r.json()
    daily = body["daily"]
    assert daily["temperature_2m_max"][0] == pytest.approx(20.0)
    assert daily["precipitation_sum"][1] == pytest.approx(1.2)
