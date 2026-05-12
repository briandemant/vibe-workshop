from datetime import UTC, datetime
from uuid import uuid4

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


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
    </ul>

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
def recommendations() -> list[str]:
    return [str(uuid4()) for _ in range(10)]
