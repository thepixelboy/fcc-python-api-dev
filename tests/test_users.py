from app import schemas

from .database import client, session


def test_root(client, session):
    res = client.get("/")
    assert res.json().get("message") == "Welcome to my API"
    assert res.status_code == 200


def test_create_user(client, session):
    res = client.post(
        "/users/",
        json={"email": "test@example.com", "password": "password123"},
    )

    new_user = schemas.User(**res.json())
    assert new_user.email == "test@example.com"
    assert res.status_code == 201


def test_login_user(client, session):
    res = client.post(
        "/login/",
        data={"username": "test@example.com", "password": "password123"},
    )
    assert res.status_code == 200
