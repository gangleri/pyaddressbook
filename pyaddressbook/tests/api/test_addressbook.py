from unittest.mock import MagicMock
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture
from pyaddressbook.api.addressbook import get_routes


@fixture
def client():
    mock_repo = MagicMock()
    mock_repo.create_contact.return_value = {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "555-555-5555",
    }

    app = FastAPI()
    app.include_router(get_routes(mock_repo), prefix="/api")
    return TestClient(app)

def test_create_contact(client):
    contact_data = {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "555-555-5555",
    }
    response = client.post("/api/addressbook/v1/contacts", json=contact_data)

    # Assert the response status code is 201 (created)
    assert response.status_code == 201
    # Assert the response json contains the contact data
    assert response.json() == contact_data
