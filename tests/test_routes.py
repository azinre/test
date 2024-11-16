import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_read_route(client):
    response = client.get("/products/1")
    assert response.status_code == 200


def test_update_route(client):
    data = {"name": "Updated Product"}
    response = client.put("/products/1", json=data)
    assert response.status_code == 200

def test_delete_route(client):
    response = client.delete("/products/1")
    assert response.status_code == 200

def test_list_all_route(client):
    response = client.get("/products")
    assert response.status_code == 200

def test_list_by_name(client):
    response = client.get("/products?name=Product+1")
    assert response.status_code == 200

def test_list_by_category(client):
    response = client.get("/products?category=Category+A")
    assert response.status_code == 200

def test_list_by_availability(client):
    response = client.get("/products?available=true")
    assert response.status_code == 200
