import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "Running"
    assert "project" in data


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "UP"
    assert "timestamp" in data


def test_version(client):
    response = client.get("/version")

    assert response.status_code == 200

    data = response.get_json()

    assert "version" in data
    assert "environment" in data


def test_info(client):
    response = client.get("/api/info")

    assert response.status_code == 200

    data = response.get_json()

    assert data["framework"] == "Flask"


def test_security(client):
    response = client.get("/api/security")

    assert response.status_code == 200

    data = response.get_json()

    assert "trivy" in data
    assert "owasp_zap" in data


def test_system(client):
    response = client.get("/api/system")

    assert response.status_code == 200

    data = response.get_json()

    assert data["docker"] is True