# Stage 02: Create an HTML API Help Page at `/`

In this stage, you will make the root endpoint (`/`) return a useful HTML help page for your API.

The goal is to make it easy for someone opening the API in a browser to understand:

- what endpoints currently exist
- which HTTP method each endpoint uses
- how to call each endpoint

## Requirements

Implement a `GET /` endpoint that returns HTML (not JSON, not plain text).

Your page should include:

- A short heading/title for the API help page
- A section listing implemented endpoints
- For each `GET` endpoint:
  - show a plain clickable link (for example: `/healthcheck`)
- For each `POST` endpoint:
  - show a `curl` example command demonstrating how to call it

## Scope for this stage

Right now, your app currently includes:

- `GET /healthcheck`

Your help page must include that endpoint now, and should be written clearly so it can be expanded later as more endpoints are added.

## Notes

- Keep the page simple and readable.
- Focus on usefulness over styling.
- Do not remove or break existing endpoints while adding `/`.
