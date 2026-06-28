import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get('/actuator/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'UP'

def test_listar_pet():
    response = client.get('/api/pets/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_listar_dono():
    response = client.get('/api/donos/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
