# Lock Files con uv (uv.lock)

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

`uv.lock` es el archivo de lock generado automáticamente por uv que congela las versiones exactas de todas las dependencias (directas y transitivas) del proyecto. Garantiza builds reproducibles en cualquier máquina o entorno.

### Características Principales

- Generado automáticamente con `uv lock` o `uv sync`
- Registra versiones exactas, hashes y metadatos de todos los paquetes
- Multiplataforma: incluye resolución para diferentes sistemas operativos
- Debe versionarse en el repositorio junto al código fuente
- Actualización selectiva con `uv lock --upgrade-package <nombre>`

## 2. Aplicación Práctica

### Casos de Uso

- Garantizar que todo el equipo usa exactamente las mismas versiones de dependencias
- Reproducir builds de producción de forma exacta en CI/CD
- Auditar cambios de dependencias en pull requests revisando el diff del lock file

### Ejemplo de Código

```bash
uv lock                              # genera o actualiza uv.lock
uv sync                              # instala desde uv.lock exactamente
uv sync --frozen                     # instala sin modificar uv.lock (ideal para CI)

uv lock --upgrade-package requests   # actualiza solo requests y sus deps
uv lock --upgrade                    # actualiza todas las dependencias

uv export --format requirements-txt  # exporta a requirements.txt si se necesita
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin un lock file, dos desarrolladores que ejecuten `pip install -r requirements.txt` pueden obtener versiones distintas de las dependencias transitivas, causando el clásico problema "funciona en mi máquina" y bugs difíciles de reproducir.

### Solución y Beneficios

- Reproducibilidad total del entorno en cualquier máquina o momento
- Diff legible en PRs para revisar qué dependencias cambiaron y por qué
- Builds de CI/CD determinísticos y más seguros
- Verificación de hashes para mayor seguridad en la cadena de suministro

## 4. Referencias

- https://docs.astral.sh/uv/concepts/resolution/
- https://docs.astral.sh/uv/reference/cli/#uv-lock
- https://docs.astral.sh/uv/guides/projects/#lockfile
- https://packaging.python.org/en/latest/discussions/lock-files-a-complicated-topic/
- https://github.com/astral-sh/uv

## 5. Tarea Práctica

### Nivel Básico

Crea un proyecto con `pyproject.toml`, ejecuta `uv lock` y examina el contenido de `uv.lock`. Identifica las dependencias directas y transitivas.

### Nivel Intermedio

Añade una dependencia al `pyproject.toml`, ejecuta `uv lock` y observa el diff de `uv.lock`. Luego actualiza una dependencia con `--upgrade-package` y analiza los cambios.

### Nivel Avanzado

Configura un pipeline CI/CD que use `uv sync --frozen` para instalar dependencias. Añade un job que falle si `uv.lock` no está sincronizado con `pyproject.toml` usando `uv lock --check`.

### Criterios de Éxito

- [ ] `uv.lock` está versionado en el repositorio y el equipo lo mantiene actualizado
- [ ] `uv sync --frozen` en CI/CD instala exactamente las mismas versiones que en desarrollo
- [ ] Los cambios de dependencias son visibles y revisables en diffs de pull requests
- [ ] `uv lock --check` pasa sin errores en el pipeline de CI

## 6. Resumen

`uv.lock` es la clave para builds reproducibles en Python moderno. Al versionar este archivo junto al código, el equipo garantiza que todos trabajen con las mismas dependencias y que los despliegues sean predecibles y seguros.

## 7. Reflexión

¿Cómo gestionas actualmente la reproducibilidad de dependencias en tus proyectos? ¿Qué problemas has tenido por no tener lock files estrictos?
