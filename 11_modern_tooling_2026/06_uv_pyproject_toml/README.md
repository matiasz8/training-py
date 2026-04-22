# uv y pyproject.toml: Metadatos Declarativos de Proyecto

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

`pyproject.toml` es el archivo estándar moderno de Python (PEP 517/518/621) para declarar metadatos del proyecto, dependencias y configuración de herramientas. uv lo utiliza como fuente única de verdad para gestión de paquetes, builds y configuración de desarrollo.

### Características Principales

- Estándar PEP 621 para metadatos del proyecto (`[project]`)
- Sección `[tool.uv]` para configuración específica de uv
- Dependencias de desarrollo en `[tool.uv.dev-dependencies]`
- Compatible con `pip`, `build`, `hatch`, `flit` y otros backends
- Un solo archivo reemplaza `setup.py`, `setup.cfg`, `requirements.txt`

## 2. Aplicación Práctica

### Casos de Uso

- Definir metadatos del proyecto y dependencias en un único archivo
- Separar dependencias de producción de las de desarrollo
- Configurar todas las herramientas del proyecto (ruff, mypy, pytest) en el mismo archivo

### Ejemplo de Código

```toml
[project]
name = "mi-proyecto"
version = "1.0.0"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.110",
    "httpx>=0.27",
]

[tool.uv]
dev-dependencies = [
    "pytest>=8.0",
    "ruff>=0.4",
    "mypy>=1.9",
]

[tool.ruff]
line-length = 88
target-version = "py311"
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Los proyectos Python tradicionales dispersan la configuración en múltiples archivos: `setup.py`, `setup.cfg`, `requirements.txt`, `requirements-dev.txt`, `tox.ini`, `.flake8`. Esto dificulta el mantenimiento y crea inconsistencias.

### Solución y Beneficios

- Un único archivo para toda la configuración del proyecto
- Legibilidad mejorada con formato TOML frente a INI o Python
- Compatibilidad con el ecosistema PyPI y herramientas modernas
- Versionado junto al código fuente en el repositorio

## 4. Referencias

- https://docs.astral.sh/uv/concepts/projects/
- https://peps.python.org/pep-0621/
- https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
- https://docs.astral.sh/uv/reference/settings/
- https://toml.io/en/

## 5. Tarea Práctica

### Nivel Básico

Crea un `pyproject.toml` con metadatos básicos del proyecto, al menos 3 dependencias de producción y 2 de desarrollo. Ejecuta `uv sync` para instalar todo.

### Nivel Intermedio

Añade configuración de `ruff`, `mypy` y `pytest` en el mismo `pyproject.toml`. Verifica que cada herramienta lee su configuración correctamente desde el archivo.

### Nivel Avanzado

Convierte un proyecto existente con `setup.py` y múltiples archivos de requirements a un único `pyproject.toml`. Documenta el proceso y verifica que el comportamiento es idéntico.

### Criterios de Éxito

- [ ] `uv sync` instala correctamente todas las dependencias declaradas
- [ ] Las herramientas leen su configuración desde `pyproject.toml` sin archivos adicionales
- [ ] El proyecto puede instalarse con `pip install .` usando el `pyproject.toml`
- [ ] Las dependencias de desarrollo no se instalan en producción con `uv sync --no-dev`

## 6. Resumen

`pyproject.toml` es el estándar moderno para proyectos Python, y uv lo adopta como pieza central de su ecosistema. Centralizar toda la configuración en un único archivo reduce la complejidad del proyecto y mejora la experiencia del desarrollador.

## 7. Reflexión

¿Cuántos archivos de configuración tiene tu proyecto actual? ¿Qué beneficios concretos obtendrías al migrarlos todos a `pyproject.toml`?
