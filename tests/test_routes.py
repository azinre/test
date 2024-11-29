import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from flask.testing import FlaskClient
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_read_route(client: FlaskClient):
    response = client.get("/products/1")
    assert response.status_code == 200


def test_update_route(client: FlaskClient):
    data = {"name": "Updated Product"}
    response = client.put("/products/1", json=data)
    assert response.status_code == 200

def test_delete_route(client: FlaskClient):
    response = client.delete("/products/1")
    assert response.status_code == 200

def test_list_all_route(client: FlaskClient):
    response = client.get("/products")
    assert response.status_code == 200

def test_list_by_name(client: FlaskClient):
    response = client.get("/products?name=Product+1")
    assert response.status_code == 200

def test_list_by_category(client: FlaskClient):
    response = client.get("/products?category=Category+A")
    assert response.status_code == 200

def test_list_by_availability(client: FlaskClient):
    response = client.get("/products?available=true")
    assert response.status_code == 200
