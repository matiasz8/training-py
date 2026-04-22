# Configuración de Ruff en pyproject.toml

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

Ruff se configura íntegramente en `pyproject.toml` bajo la sección `[tool.ruff]`. Esta configuración centralizada permite definir reglas activas, exclusiones, longitud de línea, versión de Python objetivo y configuración específica por plugin (isort, pep8-naming, etc.) en un único archivo versionado junto al código.

### Características Principales

- Sección `[tool.ruff.lint]` para reglas y exclusiones de linting
- Sección `[tool.ruff.format]` para configuración del formateador
- Selección de reglas por prefijos (`E`, `F`, `I`, `N`, `S`, `B`, etc.)
- Exclusiones por archivo/directorio con `exclude` y `per-file-ignores`
- Hereda configuración desde directorios padre para proyectos monorepo

## 2. Aplicación Práctica

### Casos de Uso

- Definir el conjunto de reglas de linting para toda la base de código
- Configurar exclusiones para archivos generados o código legado
- Compartir configuración entre múltiples proyectos dentro de un monorepo

### Ejemplo de Código

```toml
[tool.ruff]
line-length = 88
target-version = "py311"
exclude = ["migrations/", "*.pyi"]

[tool.ruff.lint]
select = ["E", "F", "I", "N", "S", "B", "UP"]
ignore = ["E501", "S101"]
per-file-ignores = {"tests/**" = ["S101", "ARG"]}

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Los proyectos Python tradicionales requieren múltiples archivos de configuración: `.flake8`, `.pylintrc`, `pyproject.toml` para black, `.isort.cfg`. Esta fragmentación dificulta el mantenimiento y genera inconsistencias entre herramientas.

### Solución y Beneficios

- Un único archivo de configuración para linting, formato e imports
- Control granular sobre qué reglas aplican y en qué archivos
- Configuración explícita y revisable en PRs junto al código
- Fácil compartición de configuración base entre proyectos del equipo

## 4. Referencias

- https://docs.astral.sh/ruff/configuration/
- https://docs.astral.sh/ruff/settings/
- https://docs.astral.sh/ruff/rules/
- https://docs.astral.sh/ruff/faq/
- https://github.com/astral-sh/ruff

## 5. Tarea Práctica

### Nivel Básico

Crea una configuración mínima de ruff en `pyproject.toml` con `select = ["E", "F"]`, `line-length = 88` y `target-version = "py311"`. Ejecuta ruff en tu proyecto y analiza los resultados.

### Nivel Intermedio

Añade las reglas `I` (isort), `N` (pep8-naming) y `B` (bugbear) a la configuración. Configura `per-file-ignores` para los tests. Verifica que cada conjunto de reglas detecta problemas reales en el código.

### Nivel Avanzado

Crea una configuración ruff compartida para un monorepo con un `pyproject.toml` raíz y configuraciones específicas en cada paquete miembro. Documenta las decisiones de qué reglas se aplican globalmente vs localmente.

### Criterios de Éxito

- [ ] `ruff check .` ejecuta sin errores de configuración y reporta solo problemas reales
- [ ] Las exclusiones de `per-file-ignores` funcionan correctamente en los tests
- [ ] La configuración reemplaza completamente cualquier archivo de configuración separado
- [ ] El equipo puede entender y modificar las reglas activas desde `pyproject.toml`

## 6. Resumen

La configuración de ruff en `pyproject.toml` centraliza todas las decisiones de calidad de código del proyecto. Con una sintaxis TOML clara y una documentación de reglas excelente, el equipo puede mantener un estándar de código consistente sin dispersar configuración en múltiples archivos.

## 7. Reflexión

¿Cuántas reglas activas son suficientes para tu proyecto sin generar demasiado ruido? ¿Cómo decidirías qué reglas activar al inicio vs cuáles añadir gradualmente?
