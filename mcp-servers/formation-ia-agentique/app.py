"""ASGI entrypoint, detected by Vercel (`app` variable in `app.py`).

Local run: `uv run uvicorn app:app --reload --port 8000` then connect to http://localhost:8000/mcp
"""

from server import mcp

# Stateless + JSON responses: each serverless invocation is independent, no session affinity needed.
app = mcp.http_app(path="/mcp", stateless_http=True, json_response=True)
