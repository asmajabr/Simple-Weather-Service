# src/app.py - deterministic FastAPI app (no external calls)
from fastapi import FastAPI, Query
from .helpers import code_to_text

app = FastAPI(title="Simple Weather API (clean)", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/weather/current")
def current_weather(lat: float = Query(..., ge=-90, le=90), lon: float = Query(..., ge=-180, le=180)):
    """Return a deterministic sample "current" weather response for testing."""
    sample = {
        "source": "open-meteo",
        "current": {
            "temperature": 18.2,
            "weather_code": 1,
            "weather_text": code_to_text(1),
            "windspeed": 3.4,
        },
    }
    return sample

@app.get("/weather/forecast")
def forecast(lat: float = Query(..., ge=-90, le=90), lon: float = Query(..., ge=-180, le=180), days: int = Query(3, ge=1, le=7)):
    daily = {
        "time": ["2026-01-01", "2026-01-02", "2026-01-03"],
        "temperature_2m_max": [20.0, 21.0, 19.5],
        "temperature_2m_min": [10.0, 11.0, 9.2],
        "precipitation_sum": [0.0, 1.2, 0.0],
        "weathercode": [1, 2, 0],
    }
    return {"source": "open-meteo", "daily": daily}

@app.get("/weather/hourly")
def hourly(lat: float = Query(..., ge=-90, le=90), lon: float = Query(..., ge=-180, le=180), vars: str = Query("temperature_2m,windspeed_10m")):
    selected = [v.strip() for v in vars.split(",") if v.strip()]
    hourly = {
        "temperature_2m": [17.3, 17.0, 16.8],
        "windspeed_10m": [3.0, 2.8, 2.5],
    }
    filtered = {k: hourly.get(k, []) for k in selected}
    return {"source": "open-meteo", "selected": selected, "hourly": filtered}
