FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock README.md ./
COPY src ./src

RUN poetry install

COPY . .

RUN mkdir -p /app/data

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "health_app.api:app", "--host", "0.0.0.0", "--port", "8000"]