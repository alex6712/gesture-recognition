# Stage 1 (генерация gRPC и установка зависимостей)
FROM python:3.12-slim AS builder

WORKDIR /build

ENV POETRY_VERSION=2.1.2 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:$PATH"

RUN apt-get update \
    && apt-get install -y curl build-essential \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY backend/recognition_api/pyproject.toml backend/recognition_api/poetry.lock* ./

RUN poetry install --no-interaction --no-ansi --only main \
    && pip install grpcio-tools

COPY backend/recognition_api/app ./app/

COPY protos/ ./protos/

# Временно генерируется только hardcoded .proto-сервис.
# Необходимо реализовать автоматизированную генерацию
# связанных сервисов.
RUN mkdir -p ./app/interservice_grpc/generated \
    && touch ./app/interservice_grpc/generated/__init__.py \
    && poetry run python -m grpc_tools.protoc \
      -I app/interservice_grpc/generated=protos \
      --python_out=. \
      --grpc_python_out=. \
      protos/recognition_model.proto

# Stage 2 (копирование файлов и запуск сервиса)
FROM python:3.12-slim AS runtime

WORKDIR /app

COPY --from=builder /build/app ./
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

CMD ["fastapi", "run", "main.py"]
