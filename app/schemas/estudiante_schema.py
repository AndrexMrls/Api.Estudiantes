from pydantic import BaseModel

class Estudiante(BaseModel):
    id: int
    nombre: str
    programa: str
    semestre: int
    promedio: float