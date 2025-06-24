import pytest
from fastapi.testclient import TestClient
from src.backend.main import app

def test_read_root():
    client = TestClient(app)
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"} 