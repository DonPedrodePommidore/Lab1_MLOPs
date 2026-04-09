from fastapi.testclient import TestClient
from app import app

client = TestClient(app)



def test_welcome_root():
    response = client.get("/")
    assert response.json() == {"message": "Welcome to the ML API"}

def test_health_check():
    response = client.get("/health")
    assert response.json() == {"status": "ok"}