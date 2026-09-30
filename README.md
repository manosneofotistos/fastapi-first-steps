# First API

Practice API using Python 3.11, FastAPI, and Uvicorn.

## Setup on Windows PowerShell

Open the cloned repository folder, then run:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8766
```

Open http://127.0.0.1:8766/docs in the browser.
Stop the server with Ctrl+C in its terminal.

## Endpoints

- GET /hello: optional `name` query parameter, default `World`.
- POST /greet: JSON body containing a required string field `name`.

Both return a JSON greeting. No data is stored.