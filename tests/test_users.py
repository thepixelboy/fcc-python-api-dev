from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    res = client.get("/")
    assert res.json().get("message") == "Welcome to my API"
    assert res.status_code == 200
