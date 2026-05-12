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


def test_root_help_contains_recommendations_link() -> None:
    response = client.get("/")
    body = response.text
    assert 'href="/recommendations"' in body
    assert "GET /recommendations" in body


def test_root_help_contains_category_recommendations_docs() -> None:
    response = client.get("/")
    body = response.text
    assert "GET /recommendations/{category}" in body
    assert "Allowed categories: action, børn, comedy, drama, entertainment" in body


def test_root_help_contains_good_and_bad_category_examples() -> None:
    response = client.get("/")
    body = response.text
    assert "curl http://localhost:8000/recommendations/drama" in body
    assert "drama000-1234-5678-9abc-def012345678" in body
    assert "curl http://localhost:8000/recommendations/sport" in body
    assert '"error": "invalid category"' in body


def test_root_help_contains_post_curl_guidance() -> None:
    response = client.get("/")
    body = response.text
    assert "POST endpoints" in body
    assert "curl -X POST" in body
