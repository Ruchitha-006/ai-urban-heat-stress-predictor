import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_predict():
    payload = {
        "city": "Delhi",
        "age": 30,
        "working_hours": 8,
        "hydration_level": 3
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200