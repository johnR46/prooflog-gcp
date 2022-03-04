from fastapi.testclient import TestClient

from app.handlers import app

client = TestClient(app)


def test_get_proof_logger():
    response = client.get("/user/proof")
    assert response.status_code == 200
    assert response.json()['message'] == 'Hello World'
