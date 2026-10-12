from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_default_page_has_10_users():
    r = client.get("/users")
    assert r.status_code == 200
    assert len(r.json()) == 10

def test_page_and_limit():
    r = client.get("/users?page=2&limit=5")
    assert [u["id"] for u in r.json()] == [6, 7, 8, 9, 10]

def test_last_page_is_partial():
    r = client.get("/users?page=3&limit=10")
    assert len(r.json()) == 5