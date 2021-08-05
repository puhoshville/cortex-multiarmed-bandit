FROM python:3.9-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Model A serving
FROM base AS model-a
COPY model_a.py .
CMD uvicorn --host 0.0.0.0 --port 8080 model_a:app


# Model B serving
FROM base AS model-b
COPY model_b.py .
CMD uvicorn --host 0.0.0.0 --port 8080 model_b:app
