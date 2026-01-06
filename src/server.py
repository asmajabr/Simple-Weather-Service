# src/server.py - entrypoint for local running

# 1) Standard library
import os

# 2) Third-party
import uvicorn

# 3) Local
from src.app import app

if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run(app, host=host, port=port)
