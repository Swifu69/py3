# Health App - Obligation 3

Author : Johan Sebastian Saire Borgersen

## Description

This project is a continuation of Oblig 2. The original health application has been extended with a FastAPI web API and Docker support.

The application can:

- create health records
- calculate BMI
- return BMI category
- calculate ideal weight
- save and load records from a JSON file
- run as a web API inside Docker

## Project Structure

```text
src/health_app/
    __init__.py
    health.py
    data.py
    main.py
    api.py

tests/
    test_health.py
    test_data.py

Dockerfile
docker-compose.yml
pyproject.toml
poetry.lock
README.md
```

## Installation

Install dependencies with Poetry:

```bash
poetry install
```

## Run tests

```bash
poetry run pytest tests/ -v
```

## Run the CLI application

```bash
poetry run python -m health_app.main
```

## Run the API locally

```bash
poetry run uvicorn health_app.api:app --reload
```

Open the interactive API documentation in the browser:

```text
http://localhost:8000/docs
```

## Run with Docker

Build and start the Docker container:

```bash
docker compose up --build
```

Stop the container:

```bash
docker compose down
```

The local `data/` folder is mounted into the container as `/app/data`, so the JSON file persists after the container stops.

## API Endpoints

### GET /

Health check endpoint.

Example:

```bash
curl http://localhost:8000/
```

Expected response:

```json
{
  "status": "ok",
  "app": "Health API"
}
```

### GET /records

Returns all stored health records.

Example:

```bash
curl http://localhost:8000/records
```

Expected response example:

```json
[
  {
    "name": "Alice",
    "weight_kg": 65.0,
    "height_m": 1.7,
    "bmi": 22.49,
    "category": "Normal",
    "ideal_weight": 63.6
  }
]
```

If no records exist, the endpoint returns:

```json
[]
```

### POST /records

Creates a new health record.

Example:

```bash
curl -X POST http://localhost:8000/records \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","weight_kg":65,"height_m":1.70}'
```

Expected response:

```json
{
  "name": "Alice",
  "weight_kg": 65.0,
  "height_m": 1.7,
  "bmi": 22.49,
  "category": "Normal",
  "ideal_weight": 63.6
}
```

## Notes

The core logic from Obligation 2 is reused. The FastAPI application imports and uses the existing `Health` class and the JSON persistence functions from `data.py`.

