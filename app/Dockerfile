ARG PYTHON_VERSION=3.12.11

FROM python:${PYTHON_VERSION}-slim AS build

# Install uv (pinned for reproducibility)
COPY --from=ghcr.io/astral-sh/uv:0.8.22 /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy     \
    UV_PROJECT_ENVIRONMENT="/app/.venv"

# ENV UV_NO_DEV=1  # IMPORTANT: Enable in production to exclude development dependencies

WORKDIR /app

# Install dependencies first to leverage Docker layer caching
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project

# === Runtime Stage ===

FROM python:${PYTHON_VERSION}-slim AS runtime

WORKDIR /app

# Security: Create user without privileges 
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Copy the virtual env from the build stage
COPY --from=build --chown=appuser:appuser /app/.venv /app/.venv

# Copy the source code into the container.
COPY --chown=appuser:appuser ./src ./src

# Python Settings
ENV PATH="/app/.venv/bin:$PATH" \
    VIRTUAL_ENV="/app/.venv"    \
    PYTHONUNBUFFERED=1          \
    PYTHONDONTWRITEBYTECODE=1

# Switch to the non-privileged user to run the application.
USER appuser

# Documents the port that the application listens on.
EXPOSE 8000

# Run the application.

# Python version:
# CMD ["python", "-m", "src.main"]

# FastAPI Version:
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
