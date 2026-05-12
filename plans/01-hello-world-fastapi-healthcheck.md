# Stage 01 - Hello World FastAPI Healthcheck

## Goal

Implement the stage-01 solution by introducing a FastAPI app under `src/`, exposing a reloadable local server workflow, and adding tests for a `/healthcheck` endpoint that returns the current time in the response message.

## Context

- Related files: `pyproject.toml`, `bin/`, `main.py` (to remove), `src/app.py` (new), `tests/test_healthcheck.py` (new)
- Related issues or links: Stage brief in `STAGE.md` on `stage-01`
- Constraints:
  - Keep source layout flat inside `src/`
  - Delete `main.py`
  - `bin/serve` must add `src` to `PYTHONPATH`
  - Use `uv` for dependency and command execution

## Approach

Move application code to `src/app.py`, run the server through a small executable script in `bin/` that sets `PYTHONPATH` for direct `app:app` imports, and add focused pytest coverage for the `/healthcheck` endpoint. Keep the implementation minimal and aligned with stage scope.

## Steps

- [ ] Add runtime dependencies: `fastapi`, `uvicorn`.
- [ ] Add dev dependency for tests: `httpx`.
- [ ] Create `src/app.py` with FastAPI app and `GET /healthcheck` route returning `{"message": "hello the time is {HH:MM:SS}"}`.
- [ ] Create executable `bin/serve` script that runs `uv run uvicorn app:app --reload` with `src` added to `PYTHONPATH`.
- [ ] Add `tests/test_healthcheck.py` covering HTTP 200 and message prefix.
- [ ] Configure pytest import path in `pyproject.toml` so tests can import `app` from `src`.
- [ ] Delete `main.py`.
- [ ] Run verification: `uv run pytest` and smoke-check `./bin/serve` + `GET /healthcheck`.

## Out of Scope

- Additional endpoints beyond `/healthcheck`
- Request/response models and validation work
- Persistence/database integration
- Authentication or authorization
- Packaging or deployment setup

## Open Questions

- Keep time formatting as 24-hour `HH:MM:SS` (current assumption), or use a locale-specific format?
