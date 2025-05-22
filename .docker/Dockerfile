FROM python:3.13-alpine AS python-base

# Python
ENV PYTHONUNBUFFERED=1 \
    # Dont create .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # Dont ask for interaction
    POETRY_NO_INTERACTION=1 \ 
    # Create virtualenvs in the project directory
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # Cache poetry packages
    POETRY_CACHE_DIR=/tmp/.cache/pypoetry \
    # Create virtualenvs
    POETRY_VIRTUALENVS_CREATE=true \
    # Set poetry home
    POETRY_HOME=/opt/poetry \
    # Set poetry version
    POETRY_VERSION=2.1.3 \
    # Venv path
    VENV_PATH=/app/.venv 

# Add poetry and venv to PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH" 

FROM python-base AS builder

RUN apk update && apk add --no-cache \
    curl && \
    # Install poetry
    curl -sSL https://install.python-poetry.org | python3 - --version "$POETRY_VERSION"

# Set the working directory
WORKDIR /app

# Copy the poetry files
COPY pyproject.toml poetry.lock ./

# Install the dependencies without the dev and lint dependencies
RUN poetry install --no-root --without lint && rm -rf "$POETRY_CACHE_DIR"

FROM python-base AS runtime

COPY --from=builder $VENV_PATH $VENV_PATH

WORKDIR /app

# Copy the application code
COPY nginx_fastapi nginx_fastapi

COPY main.py main.py

ENTRYPOINT [ "gunicorn",  "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "-w", "4", "main:app"]
