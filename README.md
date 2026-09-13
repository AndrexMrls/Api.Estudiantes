# API Gestión de Estudiantes - UNIREMINGTON

Este proyecto es una API REST desarrollada con FastAPI para la gestión de estudiantes, aplicando una arquitectura organizada por responsabilidades, inyección de dependencias y pruebas unitarias.

## Tecnologías Utilizadas
* Python
* FastAPI
* Uvicorn
* Pytest
* Pydantic

## Arquitectura del Proyecto
El proyecto está estructurado separando las responsabilidades:
* **Models:** Define las entidades base del dominio.
* **Schemas:** Maneja la validación de datos de entrada y salida (Pydantic).
* **Repositories:** Gestiona el almacenamiento de datos (simulado en memoria).
* **Services:** Centraliza la lógica de negocio.
* **Dependencies:** Implementa la inyección de dependencias.
* **Main:** Configura la aplicación y expone los endpoints.
* **Tests:** Contiene las pruebas unitarias utilizando un repositorio falso.

## Instalación y Configuración

1. Crear el entorno virtual:
   ```bash
   python -m venv venv
   ```

2. Activar el entorno virtual (Windows):
   ```bash
   venv\Scripts\activate
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución de la API

Para iniciar el servidor local, ejecuta el siguiente comando:
```bash
uvicorn app.main:app --reload
```
La documentación interactiva (Swagger UI) estará disponible en: `http://127.0.0.1:8000/docs`

## Pruebas Unitarias

Para ejecutar las pruebas unitarias que validan la lógica de la aplicación y la inyección de dependencias, utiliza:
```bash
python -m pytest -v
```

---
**Autor:** Andrés Felipe Morales Pretel  
**Institución:** Corporación Universitaria Remington (UNIREMINGTON) 
