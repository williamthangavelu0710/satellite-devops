# Stage 1: Build Python dependencies
FROM python:3.14-slim AS builder

WORKDIR /build

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runtime
FROM python:3.14-slim

WORKDIR /app

COPY --from=builder /install /usr/local
COPY main.py .

# Run as a non-root user
RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
