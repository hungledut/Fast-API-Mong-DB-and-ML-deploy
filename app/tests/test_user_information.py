"""User Information Unit Test"""
import json
from typing import Any
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

with open("app/tests/example_data/user_information_request.json", 'r', encoding='UTF-8') as f:
    user_information_request: dict[str, Any] = json.load(f)


def test_get_all_user_information():
    """Test get all user information success."""
    response = client.get("/user/all")
    assert response.status_code == 403

def test_rest_api_user_information():
    """Test add and get user information success."""
    response = client.post("/user/create", json=user_information_request)
    assert response.status_code == 403

    user_id = response.json()["data"]["id"]

    response = client.put(f"/user/update/{user_id}", json=user_information_request)
    assert response.status_code == 403

    response = client.get(f"/user/{user_id}")
    assert response.status_code == 403

    response = client.delete(f"/user/delete/{user_id}")
    assert response.status_code == 403
