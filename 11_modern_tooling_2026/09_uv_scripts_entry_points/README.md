# Scripts y Entry Points con uv

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

uv soporta scripts Python autónomos con dependencias inline (PEP 723) y entry points que exponen funciones del paquete como comandos CLI. Con `uv run`, las dependencias del script se instalan automáticamente en un entorno temporal y aislado.

### Características Principales

- Scripts autónomos con metadatos de dependencias declaradas como comentarios especiales (PEP 723)
- `uv run script.py` instala dependencias automáticamente en un entorno temporal
- Entry points declarados en `[project.scripts]` dentro de `pyproject.toml`
- `uv run --with <paquete> script.py` añade dependencias adicionales en tiempo de ejecución
- Reproducibilidad: el script define exactamente qué necesita para ejecutarse

## 2. Aplicación Práctica

### Casos de Uso

- Scripts de utilidad que se comparten entre equipos sin instalación previa
- Herramientas CLI instalables que los usuarios invocan por nombre tras instalar el paquete
- Automatización de tareas con scripts que auto-gestionan sus dependencias

### Ejemplo de Código

```toml
[project.scripts]
mi-herramienta = "mi_paquete.cli:main"
mi-servidor    = "mi_paquete.server:run"

[tool.uv.scripts]
lint = "ruff check ."
test = "pytest tests/"
```

```bash
uv run script.py                     # ejecuta con deps inline (PEP 723)
uv run --with httpx fetch.py         # añade httpx en tiempo de ejecución
uv run --script task migrate         # ejecuta script definido en pyproject.toml
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Compartir scripts Python entre equipos requiere instalar dependencias manualmente, documentar prerrequisitos y frecuentemente falla porque alguien tiene versiones incompatibles. Los entry points clásicos requerían configurar `setup.py` de forma compleja.

### Solución y Beneficios

- Scripts autocontenidos con dependencias declaradas inline para máxima portabilidad
- Ejecución inmediata con `uv run` sin pasos de instalación previos
- Entry points simples y declarativos en `pyproject.toml`
- Reproducibilidad garantizada para scripts de automatización

## 4. Referencias

- https://docs.astral.sh/uv/guides/scripts/
- https://peps.python.org/pep-0723/
- https://packaging.python.org/en/latest/guides/entry-points/
- https://docs.astral.sh/uv/reference/cli/#uv-run
- https://docs.astral.sh/uv/concepts/projects/

## 5. Tarea Práctica

### Nivel Básico

Crea un script Python con metadatos PEP 723 (bloque `# /// script ... # ///` al inicio) que use `httpx` para hacer una petición HTTP. Ejecútalo con `uv run script.py` sin instalar nada previamente.

### Nivel Intermedio

Define dos entry points en `pyproject.toml` para un paquete. Instala el paquete con `uv tool install -e .` y verifica que ambos comandos CLI están disponibles y ejecutables globalmente.

### Nivel Avanzado

Crea una colección de scripts PEP 723 para automatización de tareas de equipo (deploy, migración de BD, generación de reportes). Documenta cómo compartirlos mediante URL y ejecutarlos con `uv run <url>`.

### Criterios de Éxito

- [ ] `uv run script.py` ejecuta el script sin instalación previa de dependencias
- [ ] Los entry points declarados en `pyproject.toml` se instalan como comandos CLI
- [ ] El script funciona igual en distintas máquinas sin configuración adicional
- [ ] Las dependencias del script se instalan en un entorno temporal y aislado

## 6. Resumen

Los scripts PEP 723 y los entry points de uv simplifican la distribución de herramientas Python. `uv run` convierte cualquier script en una herramienta portable que se auto-configura, mientras que `[project.scripts]` en `pyproject.toml` reemplaza la configuración compleja de `setup.py`.

## 7. Reflexión

¿Qué scripts de tu equipo se beneficiarían de tener dependencias declaradas inline? ¿Cómo mejoraría el onboarding de nuevos desarrolladores con scripts que se auto-instalan?
