FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=2.1.2
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app/shared

COPY shared ./

WORKDIR /app/source

COPY recognition_model/pyproject.toml recognition_model/poetry.lock* ./

RUN poetry install --no-interaction --no-ansi

COPY recognition_model .

CMD ["python", "main.py"]
