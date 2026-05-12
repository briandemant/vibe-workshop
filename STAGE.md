# Stage 01: Hello FastAPI

In this stage, you will create your first API endpoint using FastAPI.

## Goal

Build and run a minimal FastAPI app that exposes a `GET /hello` endpoint returning a simple hello-world style JSON response.

## What you will do

- Add FastAPI app setup in the project entrypoint.
- Implement a `GET /hello` route.
- Return JSON from the route, for example:

```json
{"message": "Hello, world!"}
```

- Run the app locally and verify the endpoint in a browser or with curl.

## Success criteria

You are done when all of the following are true:

- The project starts successfully with `uv run`.
- Requesting `GET /hello` returns HTTP 200.
- The response is valid JSON containing a hello message.

## Helpful hints

- If FastAPI is missing, add it with `uv add fastapi`.
- You may also need an ASGI server such as Uvicorn (`uv add uvicorn`).
- Start by getting a single endpoint working before adding anything else.

## Out of scope for this stage

- Multiple endpoints
- Request body validation
- Database integration
- Authentication
