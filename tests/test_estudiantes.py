import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.dependencies.dependencies import get_repository
from app.schemas.estudiante_schema import Estudiante

# Repositorio falso para aislar las pruebas
class FakeEstudianteRepository:
    def __init__(self):
        self._db = {}

    def get_all(self):
        return list(self._db.values())

    def get_by_id(self, id: int):
        return self._db.get(id)

    def create(self, estudiante: Estudiante):
        self._db[estudiante.id] = estudiante
        return estudiante

    def update(self, id: int, estudiante: Estudiante):
        if id in self._db:
            self._db[id] = estudiante
            return estudiante
        return None

    def delete(self, id: int):
        if id in self._db:
            del self._db[id]
            return True
        return False

# 1. Crear una única instancia global del repositorio falso
fake_repo = FakeEstudianteRepository()

def override_get_repository():
    return fake_repo

app.dependency_overrides[get_repository] = override_get_repository

client = TestClient(app)

# 2. Limpiar la base de datos falsa antes de cada prueba
@pytest.fixture(autouse=True)
def run_before_tests():
    fake_repo._db.clear()

# Datos de prueba
estudiante_data = {
    "id": 1,
    "nombre": "Andrés Felipe Morales",
    "programa": "Ingeniería de Sistemas",
    "semestre": 5,
    "promedio": 4.5
}

def test_registrar_estudiante():
    response = client.post("/estudiantes", json=estudiante_data)
    assert response.status_code == 201
    assert response.json()["nombre"] == "Andrés Felipe Morales"

def test_buscar_estudiante_existente():
    client.post("/estudiantes", json=estudiante_data)
    response = client.get("/estudiantes/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_buscar_estudiante_no_existente():
    response = client.get("/estudiantes/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Estudiante no encontrado"

def test_actualizar_estudiante():
    client.post("/estudiantes", json=estudiante_data)
    estudiante_actualizado = estudiante_data.copy()
    estudiante_actualizado["promedio"] = 4.8
    response = client.put("/estudiantes/1", json=estudiante_actualizado)
    assert response.status_code == 200
    assert response.json()["promedio"] == 4.8

def test_eliminar_estudiante():
    client.post("/estudiantes", json=estudiante_data)
    response_del = client.delete("/estudiantes/1")
    assert response_del.status_code == 200
    response_get = client.get("/estudiantes/1")
    assert response_get.status_code == 404

def test_datos_invalidos():
    datos_malos = {"id": "uno", "nombre": "Error"} # ID no es entero
    response = client.post("/estudiantes", json=datos_malos)
    assert response.status_code == 422 # Error de validación