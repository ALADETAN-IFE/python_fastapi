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
# FastAPI Quickstart

This is a small, learning FastAPI project. The app lives in `main.py` and exposes a tiny in-memory items API.

## What you'll find here

- `main.py` — the FastAPI app. Current endpoints are listed below.

## Prerequisites

- Python 3.10+ (or any modern Python 3.x)
- A POSIX-like shell (your workspace uses `bash.exe`) — commands below assume `bash`.

## Install

Create and activate a virtual environment, then install FastAPI and an ASGI server:

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install --upgrade pip
pip install fastapi uvicorn[standard]
```

## Run (development)

Start the app with uvicorn (auto-reload for development):

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open the interactive docs at:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Current endpoints (from `main.py`)

The project currently exposes these endpoints:

- GET `/` — root endpoint. Returns a JSON greeting, e.g.:

	```json
	{"welcome": "Hello World"}
	```

- POST `/items` — add an item (current function signature accepts a query parameter named `item`). Example using curl:

	```bash
	# POST with query parameter
	curl -X POST "http://127.0.0.1:8000/items?item=apple"
	# Response:
	# {"message":"apple was added successfull","data":["apple"]}
	```

	Note: Because `create_item(item: str)` does not declare a Pydantic model or Body parameter, FastAPI treats `item` as a query parameter. You can also send data as form data or JSON if you change the function signature to accept a request body.

- GET `/items` — returns the current in-memory list of items (a JSON array). Example:

	```bash
	curl -s http://127.0.0.1:8000/items | jq
	```

- GET `/items/{item_id}` — returns the item at the given list index (0-based). Example:

	```bash
	curl -s http://127.0.0.1:8000/items/0
	```

	Caution: The current implementation does not validate the requested index; an out-of-range index will raise a server error (IndexError). See improvements below.

## Notes, pitfalls and suggested improvements

- Thread-safety: The app uses a plain Python list (`items = []`) as an in-memory store. With uvicorn's default workers and async concurrency, this can lead to race conditions. For learning or single-process development this is OK, but for correctness consider:

	- Using a threading.Lock around mutations, or
	- Using an in-memory replacement like `collections.deque` with explicit synchronization, or
	- Moving to an external datastore (SQLite, Redis, etc.) for multi-worker production.

- Request validation: Use Pydantic models for request bodies and responses. For example, change `create_item` to accept a model:

	```python
	from pydantic import BaseModel

	class Item(BaseModel):
			name: str

	@app.post('/items')
	def create_item(item: Item):
			items.append(item.name)
			return {'message': f'{item.name} was added successfully', 'data': items}
	```

- Error handling: Return 404 for out-of-range indexes instead of letting an unhandled IndexError bubble up:

	```python
	from fastapi import HTTPException

	@app.get('/items/{item_id}')
	def read_item(item_id: int):
			try:
					return items[item_id]
			except IndexError:
					raise HTTPException(status_code=404, detail='Item not found')
	```

- Persistence: The in-memory list is ephemeral and resets each run. Add a persistent store if you need durability.

## Next steps I can take for you

- Patch `main.py` to use a thread-safe in-memory store (Lock) and Pydantic models, plus the 404 fix for `GET /items/{item_id}`. I can make the changes and run a small smoke test.
- Add a `requirements.txt` generated from the environment.

Tell me which of the above you'd like me to do next and I'll implement it and verify the app runs.
