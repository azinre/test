import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_read_route(client):
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json["name"] == "Product 1"

def test_update_route(client):
    data = {"name": "Updated Product"}
    response = client.put("/products/1", json=data)
    assert response.status_code == 200
    assert response.json["name"] == "Updated Product"
