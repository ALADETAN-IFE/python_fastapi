# FastAPI Quickstart

This is a minimal FastAPI application used for learning and experimentation.

## What you'll find here

- `main.py` — the FastAPI app. The project currently exposes a single root GET endpoint (`/`).

## Prerequisites

- Python 3.10+ (or any modern Python 3.x)
- A POSIX-like shell (your workspace uses `bash.exe`) — commands below assume `bash`.

## Install (recommended)

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

2. Install FastAPI and an ASGI server (uvicorn):

```bash
pip install --upgrade pip
pip install fastapi uvicorn[standard]
```

## Run the app (development)

Start the server with uvicorn (auto-reload enabled):

```bash
uvicorn main:app --reload 
```

Then open your browser at:

- Interactive docs (Swagger UI): http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

Based on the current `main.py`, the app exposes:

- GET `/` — root endpoint that returns a greeting.

Example using curl:

```bash
curl -s http://127.0.0.1:8000/ | jq
```

Note: `main.py` currently returns a Python set literal; web frameworks will serialize JSON-compatible types. Consider returning a JSON object (dict) such as `{"message": "Hello World"}` for more predictable JSON output.

## Development tips

- If you plan to add dependencies, create a `requirements.txt` or `pyproject.toml`.
- Add type hints and Pydantic models for request/response schemas as your API grows.
- Use `--reload` only for development; omit it in production.

## Next steps (suggested)

1. Add more endpoints and example request/response models.
2. Add a `requirements.txt`:

```bash
pip freeze > requirements.txt
```

3. Optionally fix the root response in `main.py` to return a JSON object.

---

If you'd like, I can also patch `main.py` to return a well-formed JSON object (very small change) and/or add a `requirements.txt` — tell me which and I'll make those edits and verify the app runs.
