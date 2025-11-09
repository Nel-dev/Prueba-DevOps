from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_startupz():
    r = client.get("/startupz")
    assert r.status_code == 200
    assert r.json()["status"] == "started"

def test_readyz():
    r = client.get("/readyz")
    assert r.status_code == 200
    assert "details" in r.json()
