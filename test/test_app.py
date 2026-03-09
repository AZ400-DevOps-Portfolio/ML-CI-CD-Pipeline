# test_app.py
# Automated tests for the Iris Model API.
# These run automatically in the CI pipeline on every push to GitHub.
# A failed test blocks the deployment — this is the "CI" part of CI/CD.

from fastapi.testclient import TestClient
import sys
import os

# Make sure the app module is importable
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """API should return a welcome message at root."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Iris Model API is running"}


def test_health_endpoint():
    """Health check should return healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_predict_setosa():
    """Classic setosa measurements should predict setosa."""
    response = client.post("/predict", json={
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    })
    assert response.status_code == 200
    assert response.json()["species"] == "setosa"
    assert response.json()["confidence"] >= 0.8


def test_predict_virginica():
    """Classic virginica measurements should predict virginica."""
    response = client.post("/predict", json={
        "sepal_length": 6.7,
        "sepal_width": 3.3,
        "petal_length": 5.7,
        "petal_width": 2.1
    })
    assert response.status_code == 200
    assert response.json()["species"] == "virginica"


def test_predict_returns_confidence():
    """Prediction response should always include a confidence score."""
    response = client.post("/predict", json={
        "sepal_length": 5.9,
        "sepal_width": 3.0,
        "petal_length": 4.2,
        "petal_width": 1.5
    })
    assert response.status_code == 200
    assert "confidence" in response.json()
    assert 0.0 <= response.json()["confidence"] <= 1.0


def test_predict_invalid_input():
    """Missing fields should return a 422 validation error."""
    response = client.post("/predict", json={
        "sepal_length": 5.1
        # missing required fields
    })
    assert response.status_code == 422