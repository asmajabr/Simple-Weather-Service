# Simple Weather (clean starter)

Minimal FastAPI app with tests and GitHub Actions CI configured.
This repo is purposely small and deterministic so CI stays green.

## What's included
- `src/app.py` — FastAPI application (deterministic sample responses)
- `src/helpers.py` — mapping of weather codes to text
- `src/server.py` — uvicorn entrypoint (env-configurable)
- `tests/unit/test_codes.py` — unit tests for helper mapping
- `tests/integration/test_current.py` — simple integration-style tests using TestClient
- `pyproject.toml` — declares dependencies and ruff config
- `pytest.ini` — pytest config
- `.github/workflows/ci.yml` — CI workflow (ruff + pytest + build)
- `Dockerfile` — minimal containerization
- `requirements.txt` — runtime deps

## How to use
1. Create a new GitHub repo.
2. Upload the contents of this archive (or `git init` locally and push).
3. Open a PR to `main` (workflow runs on push and PR).
4. CI will run ruff and pytest.

This intentionally avoids external HTTP calls so tests are deterministic.
