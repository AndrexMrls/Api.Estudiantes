from fastapi import Depends
from app.repositories.estudiante_repository import EstudianteRepository
from app.services.estudiante_service import EstudianteService

# Instancia global para simular la persistencia en memoria durante la ejecución
repo_instance = EstudianteRepository()

def get_repository() -> EstudianteRepository:
    return repo_instance

def get_estudiante_service(repository: EstudianteRepository = Depends(get_repository)) -> EstudianteService:
    return EstudianteService(repository)