# Repository Guidelines

## Project Structure & Module Organization
Core pipeline code lives in `dagster/`:
- `ingestion.py`: Jira, Tempo, and Excel ingestion logic (dlt + MariaDB).
- `repository.py`: Dagster jobs/ops registration.
- `dagster.yaml`, `workspace.yaml`, `Dockerfile`: local orchestration/runtime config.

Data inputs and schema bootstrap:
- `input/config/`: Excel mapping YAMLs (via `REF_MAPPING_CONFIG`).
- `init/001_schema.sql`: initial database schema helper.

Operational and product documentation:
- `docs/`: architecture, specs, status, and legacy notes.
- `deploy/ecs/`: ECS deployment assets for Metabase and NocoDB.
- `scripts/publish_confluence.py`: Confluence publishing utility.

## Build, Test, and Development Commands
- `docker compose build dagster-webserver dagster-daemon`
  Builds local Dagster services.
- `docker compose up -d dagster-webserver dagster-daemon`
  Starts orchestration stack; Dagster UI at `http://localhost:3001`.
- `docker compose logs -f dagster-webserver`
  Tails webserver logs for run/debug feedback.
- `uv run --env-file .env python3 scripts/publish_confluence.py --dry-run`
  Validates Confluence publishing without writing changes.

## Coding Style & Naming Conventions
- Follow existing Python style in `dagster/*.py`: 4-space indentation, type hints where useful, small helper functions.
- Use `snake_case` for variables/functions, `UPPER_SNAKE_CASE` for constants/env defaults.
- Keep table naming conventions consistent in MariaDB: `raw_*`, `ref_*`, `stg_*`, `mart_*`.
- Prefer focused modules; place new ingestion behavior in `dagster/ingestion.py` unless it justifies extraction.

## Testing Guidelines
There is currently no dedicated automated test suite in this repository. For changes:
- Run services locally with Docker Compose.
- Execute the relevant Dagster job(s) from the UI and verify logs/output tables.
- For Excel mappings, validate both single-file and all-mappings jobs.

## Commit & Pull Request Guidelines
Git history follows a Conventional Commit-like pattern (examples: `chore(deploy): ...`, `chore(docs): ...`). Keep using:
- `<type>(<scope>): <short summary>`

PRs should include:
- clear functional summary and impacted jobs/tables,
- config/env changes (if any),
- verification evidence (Dagster run result, logs, or table checks),
- linked issue/task when available.

## Security & Configuration Tips
- Never commit real secrets; use `.env.example` as the baseline.
- Required env vars include MariaDB and API credentials (`JIRA_*`, `TEMPO_API_TOKEN`).
- Treat `ecs-secrets-policy.json` and ECS task definitions as production-sensitive artifacts.
