from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_root_help_returns_200() -> None:
    response = client.get("/")
    assert response.status_code == 200


def test_root_help_returns_html_content_type() -> None:
    response = client.get("/")
    assert response.headers["content-type"].startswith("text/html")


def test_root_help_contains_healthcheck_link() -> None:
    response = client.get("/")
    body = response.text
    assert 'href="/healthcheck"' in body
    assert "GET /healthcheck" in body


def test_root_help_contains_post_curl_guidance() -> None:
    response = client.get("/")
    body = response.text
    assert "POST endpoints" in body
    assert "curl -X POST" in body
