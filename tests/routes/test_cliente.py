from starlette.testclient import TestClient
from main import app


def test_crear_cliente():
    client = TestClient(app)
    data_cliente = {"nombre": "Test"}

    response = client.post("/api/V1/cliente/crear/", json={"nombre": "Test"})

    data = response.json()

    assert response.status_code == 200
    assert data["nuevo_cliente"]["nombre"] == "Test"


def test_obtener_cliente():
    client = TestClient(app)
    id_cliente = 1

    response = client.get(f"/api/V1/cliente/{id_cliente}")

    assert response.status_code == 200
    assert response.json() == {"id": id_cliente, "nombre": "Pepe"}
