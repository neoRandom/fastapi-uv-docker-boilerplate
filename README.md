# FastAPI with uv and Docker Boilerplate

Project with a simple Python (uv) + FastAPI + Redis + Postgres with Docker and Docker Compose.

Boilerplate to use in future projects.

Contains a Python 3.12.11 configuration with a main FastAPI entry, Pydantic Settings configuration, Postgres and Redis connection with SQLAlchemy, definition of models (with SQLAlchemy) and schemas (with pydantic) and an example of unit tests using pytest with pytest-asyncio.

## Requirements

Softwares installed:
- Docker 24.0+
- Docker Compose v2 or v3

Certify yourself that the Docker daemon is running in the background before running (`./cmd.core.sh` or `docker compose up -d`).

## Tools

- python 3.12.11 (slim)
- uv 0.8.22
- postgres 18.1 (alpine)
- redis 7.2 (alpine)
- Docker
- Docker Compose

Additionally (`compose-tools.yaml`):
- pgadmin
- redis-insight

## Packages (uv)

- uvicorn[standard] 0.40.0
- fastapi 0.128.0
- psycopg[binary] 3.3.2
- redis 7.1.0
- sqlalchemy 2.0.45
- pydantic 2.12.5
- pydantic-settings 2.12.0
- pytest 9.0.2
- pytest-asyncio 1.3.0

Also consider installing:
- celery[redis]
- httpx
- alembic
- flower

## Setup

- Run `cmd.setup.sh`
- Define the `.env`
- Define the `database/password.txt`
- Verify the python packages (add, remove etc)
- Verify the `compose.yaml` and `compose-tools.yaml` (add, remove etc) and check the: `worker` service and `web` healthcheck
- Verify the `app/Dockerfile` (set the CMD, change things etc)

About the `worker` service, it connects with:
- `celery` python package
- `app/src/worker.py` file
- `worker` definition at `compose.yaml`
