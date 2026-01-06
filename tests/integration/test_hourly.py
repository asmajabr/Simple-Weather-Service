# tests/integration/test_hourly.py
from http import HTTPStatus
from fastapi.testclient import TestClient
import pytest
from src.app import app

client = TestClient(app)

def test_hourly_selected_vars():
    r = client.get("/weather/hourly?lat=51.5072&lon=-0.1276&vars=temperature_2m,windspeed_10m")
    assert r.status_code == HTTPStatus.OK
    body = r.json()
    assert set(body["selected"]) == {"temperature_2m", "windspeed_10m"}
    assert body["hourly"]["temperature_2m"][0] == pytest.approx(17.3)
