from fastapi.testclient import TestClient
from api_test import app


client = TestClient(app)


def test_add():
    response = client.get("/add/1/2")
    assert response.status_code == 200
    assert int(response.text) == 3


def test_sub():
    response = client.get("/sub/1/2")
    assert response.status_code == 200
    assert int(response.text) == -1


def test_mul():
    response = client.get("/mul/2/3")
    assert response.status_code == 200
    assert int(response.text) == 6
