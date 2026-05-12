from datetime import UTC, datetime
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

ALLOWED_CATEGORIES = ["action", "børn", "comedy", "drama", "entertainment"]


def _generate_recommendation_ids(prefix: str | None = None) -> list[str]:
    if prefix is None:
        return [str(uuid4()) for _ in range(10)]

    values: list[str] = []
    for _ in range(10):
        _, second, third, fourth, fifth = str(uuid4()).split("-")
        values.append(f"{prefix}-{second}-{third}-{fourth}-{fifth}")
    return values


@app.get("/", response_class=HTMLResponse)
def root_help() -> str:
    return """
<html>
  <head>
    <title>API Help</title>
  </head>
  <body>
    <h1>API Help</h1>
    <p>This page lists currently implemented endpoints and how to use them.</p>

    <h2>GET endpoints</h2>
    <ul>
      <li><a href="/healthcheck">GET /healthcheck</a></li>
      <li><a href="/recommendations">GET /recommendations</a></li>
      <li><a href="/recommendations/action">GET /recommendations/{category}</a></li>
    </ul>

    <h3>GET /recommendations/{category}</h3>
    <p>Returns 10 fake recommendation IDs for an allowed category.</p>
    <p>Allowed categories: action, børn, comedy, drama, entertainment</p>

    <p>Good example:</p>
    <pre><code>curl http://localhost:8000/recommendations/drama
{
  "recommendations": ["drama000-1234-5678-9abc-def012345678"],
  "fallback": false,
  "category": "drama"
}</code></pre>

    <p>Bad example (invalid category):</p>
    <pre><code>curl http://localhost:8000/recommendations/sport
{
  "detail": {
    "error": "invalid category",
    "category": "sport",
    "allowed_categories": ["action", "børn", "comedy", "drama", "entertainment"]
  }
}</code></pre>

    <h2>POST endpoints</h2>
    <p>No POST endpoints are implemented yet.</p>
    <p>When available, use curl like:</p>
    <pre><code>curl -X POST http://localhost:8000/example -H "Content-Type: application/json" -d '{"key":"value"}'</code></pre>
  </body>
</html>
"""


@app.get("/healthcheck")
def healthcheck() -> dict[str, str]:
    now = datetime.now(tz=UTC).strftime("%H:%M:%S")
    return {"message": f"hello the time is {now}"}


@app.get("/recommendations")
def recommendations() -> dict[str, list[str] | bool]:
    return {"recommendations": _generate_recommendation_ids(), "fallback": False}


@app.get("/recommendations/{category}")
def recommendations_for_category(category: str) -> dict[str, list[str] | bool | str]:
    if category not in ALLOWED_CATEGORIES:
        raise HTTPException(
            status_code=422,
            detail={
                "error": "invalid category",
                "category": category,
                "allowed_categories": ALLOWED_CATEGORIES,
            },
        )

    prefix = category.ljust(8, "0")
    return {
        "recommendations": _generate_recommendation_ids(prefix=prefix),
        "fallback": False,
        "category": category,
    }
