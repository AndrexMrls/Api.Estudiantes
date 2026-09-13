from fastapi import HTTPException
from typing import List
from app.repositories.estudiante_repository import EstudianteRepository
from app.schemas.estudiante_schema import Estudiante

class EstudianteService:
    def __init__(self, repository: EstudianteRepository):
        self.repository = repository

    def obtener_todos(self) -> List[Estudiante]:
        return self.repository.get_all()

    def obtener_por_id(self, id: int) -> Estudiante:
        estudiante = self.repository.get_by_id(id)
        if not estudiante:
            raise HTTPException(status_code=404, detail="Estudiante no encontrado")
        return estudiante

    def registrar(self, estudiante: Estudiante) -> Estudiante:
        if self.repository.get_by_id(estudiante.id):
            raise HTTPException(status_code=400, detail="El estudiante ya existe")
        return self.repository.create(estudiante)

    def actualizar(self, id: int, estudiante: Estudiante) -> Estudiante:
        actualizado = self.repository.update(id, estudiante)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Estudiante no encontrado")
        return actualizado

    def eliminar(self, id: int):
        if not self.repository.delete(id):
            raise HTTPException(status_code=404, detail="Estudiante no encontrado")
        return {"mensaje": "Estudiante eliminado exitosamente"}