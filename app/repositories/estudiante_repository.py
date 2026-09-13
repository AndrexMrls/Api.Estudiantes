from typing import List, Optional
from app.schemas.estudiante_schema import Estudiante

class EstudianteRepository:
    def __init__(self):
        self._db = {}

    def get_all(self) -> List[Estudiante]:
        return list(self._db.values())

    def get_by_id(self, id: int) -> Optional[Estudiante]:
        return self._db.get(id)

    def create(self, estudiante: Estudiante) -> Estudiante:
        self._db[estudiante.id] = estudiante
        return estudiante

    def update(self, id: int, estudiante: Estudiante) -> Optional[Estudiante]:
        if id in self._db:
            self._db[id] = estudiante
            return estudiante
        return None

    def delete(self, id: int) -> bool:
        if id in self._db:
            del self._db[id]
            return True
        return False