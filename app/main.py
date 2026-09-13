from fastapi import FastAPI, Depends
from typing import List
from app.schemas.estudiante_schema import Estudiante
from app.services.estudiante_service import EstudianteService
from app.dependencies.dependencies import get_estudiante_service

app = FastAPI(title="API Gestión de Estudiantes UNIREMINGTON")

@app.get("/estudiantes", response_model=List[Estudiante])
def obtener_estudiantes(service: EstudianteService = Depends(get_estudiante_service)):
    return service.obtener_todos()

@app.get("/estudiantes/{id}", response_model=Estudiante)
def obtener_estudiante(id: int, service: EstudianteService = Depends(get_estudiante_service)):
    return service.obtener_por_id(id)

@app.post("/estudiantes", response_model=Estudiante, status_code=201)
def registrar_estudiante(estudiante: Estudiante, service: EstudianteService = Depends(get_estudiante_service)):
    return service.registrar(estudiante)

@app.put("/estudiantes/{id}", response_model=Estudiante)
def actualizar_estudiante(id: int, estudiante: Estudiante, service: EstudianteService = Depends(get_estudiante_service)):
    return service.actualizar(id, estudiante)

@app.delete("/estudiantes/{id}")
def eliminar_estudiante(id: int, service: EstudianteService = Depends(get_estudiante_service)):
    return service.eliminar(id)