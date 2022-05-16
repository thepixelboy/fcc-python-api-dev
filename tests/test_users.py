from app import schemas
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    res = client.get("/")
    assert res.json().get("message") == "Welcome to my API"
    assert res.status_code == 200


def test_create_user():
    res = client.post(
        "/users/",
        json={"email": "test@example.com", "password": "password123"},
    )

    new_user = schemas.User(**res.json())
    assert new_user.email == "test@example.com"
    assert res.status_code == 201
