# uv venv: Gestión de Entornos Virtuales

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

`uv venv` crea entornos virtuales de Python de forma ultrarrápida, en milisegundos. Implementado en Rust, no requiere `virtualenv` ni el módulo stdlib `venv`. Integra nativamente con `uv pip`, `uv sync` y `uv run`.

### Características Principales

- Creación de entornos en < 100ms (10-100x más rápido que virtualenv)
- Compatible con el estándar PEP 405 y herramientas existentes
- Permite especificar la versión Python con `--python 3.12`
- Integración con `uv run` para ejecutar scripts sin activación manual
- Manejo automático de `.python-version`

## 2. Aplicación Práctica

### Casos de Uso

- Aislar dependencias de proyectos para evitar conflictos entre versiones
- Crear entornos efímeros para pruebas rápidas en CI/CD
- Gestionar múltiples versiones de Python en el mismo equipo

### Ejemplo de Código

```bash
uv venv                          # entorno con Python por defecto
uv venv --python 3.12            # entorno con Python 3.12
source .venv/bin/activate        # activar en Unix/macOS
uv pip install requests fastapi  # instalar dependencias
uv run python script.py          # ejecutar sin activar el entorno
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Los entornos virtuales tradicionales con `venv` o `virtualenv` tardan 2-5 segundos en crearse y requieren activación manual. En pipelines de CI/CD con múltiples jobs, este tiempo se acumula significativamente.

### Solución y Beneficios

- Reducción drástica del tiempo de setup en pipelines CI/CD
- `uv run` elimina la necesidad de activación manual del entorno
- Consistencia entre entornos de desarrollo y producción
- Sin dependencias externas: uv es autocontenido

## 4. Referencias

- https://docs.astral.sh/uv/concepts/environments/
- https://docs.astral.sh/uv/reference/cli/#uv-venv
- https://peps.python.org/pep-0405/
- https://github.com/astral-sh/uv
- https://docs.astral.sh/uv/guides/projects/

## 5. Tarea Práctica

### Nivel Básico

Crea un entorno virtual con `uv venv`, actívalo e instala `requests`. Verifica con `python -c "import requests; print(requests.__version__)"`.

### Nivel Intermedio

Crea entornos con Python 3.11 y 3.12. Instala `numpy` en ambos. Compara los tiempos con `time uv venv` versus `time python -m venv`.

### Nivel Avanzado

Configura un pipeline de GitHub Actions que use `uv run` para ejecutar tests sin activación explícita del entorno. Mide el tiempo total de CI antes y después de migrar desde `venv`.

### Criterios de Éxito

- [ ] El entorno se crea en menos de 1 segundo medible con `time`
- [ ] `uv run python -c "import sys; print(sys.prefix)"` muestra el entorno correcto
- [ ] Las dependencias instaladas no afectan al Python global del sistema
- [ ] La versión de Python coincide con la especificada en `--python`

## 6. Resumen

`uv venv` moderniza la gestión de entornos virtuales en Python con velocidad extrema e integración fluida con el ecosistema uv. Reemplaza `virtualenv` y `venv` con una herramienta más rápida y ergonómica, siendo el punto de partida recomendado para proyectos Python en 2026.

## 7. Reflexión

¿Qué impacto tendría migrar todos tus proyectos actuales de `venv` a `uv venv`? ¿Qué consideraciones de compatibilidad tendrías en cuenta para un equipo con distintos sistemas operativos?
