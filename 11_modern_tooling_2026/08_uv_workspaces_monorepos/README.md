# Workspaces y Monorepos con uv

⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Los workspaces de uv permiten gestionar múltiples paquetes Python relacionados dentro de un mismo repositorio (monorepo). Un workspace define un paquete raíz y miembros que comparten un único `uv.lock`, garantizando consistencia de dependencias entre todos los paquetes del monorepo.

### Características Principales

- Un único `uv.lock` compartido para todos los miembros del workspace
- Los miembros pueden depender entre sí con resolución local automática
- Compatible con la especificación de workspaces de PEP y el ecosistema Cargo (Rust)
- Resolución de dependencias unificada evita conflictos entre paquetes
- Instalación selectiva por miembro con `--package`

## 2. Aplicación Práctica

### Casos de Uso

- Monorepos con múltiples microservicios Python que comparten código común
- Proyectos con librerías internas y aplicaciones que las consumen
- Equipos grandes que quieren un único repositorio con múltiples paquetes independientes

### Ejemplo de Código

```toml
[tool.uv.workspace]
members = ["packages/*", "apps/*"]
```

```bash
uv sync                              # instala todos los miembros
uv sync --package mi-libreria        # instala solo un paquete
uv run --package mi-api python main.py
uv add --package mi-api requests     # añade dep a un miembro específico
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

En un monorepo sin workspaces, cada paquete mantiene su propio entorno y lock file, causando versiones inconsistentes de dependencias compartidas, duplicación de configuración y dificultad para probar integraciones entre paquetes.

### Solución y Beneficios

- Dependencias compartidas resueltas de forma unificada en todo el monorepo
- Cambios en librerías internas inmediatamente visibles para sus consumidores
- Configuración centralizada reduce mantenimiento
- CI/CD simplificado con un único proceso de resolución

## 4. Referencias

- https://docs.astral.sh/uv/concepts/workspaces/
- https://docs.astral.sh/uv/guides/workspaces/
- https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
- https://monorepo.tools/
- https://github.com/astral-sh/uv/tree/main/scripts/workspaces

## 5. Tarea Práctica

### Nivel Básico

Crea un workspace con un paquete raíz y dos miembros (`packages/lib-core` y `packages/lib-utils`). Configura el `pyproject.toml` raíz con `[tool.uv.workspace]` y ejecuta `uv sync`.

### Nivel Intermedio

Haz que un miembro del workspace dependa de otro internamente. Añade un test de integración que importe de ambos paquetes y verifica que `uv run pytest` los encuentra correctamente.

### Nivel Avanzado

Migra un proyecto existente con múltiples repositorios separados a un workspace de uv. Configura CI/CD para ejecutar tests solo en los paquetes modificados usando detección de cambios por directorio.

### Criterios de Éxito

- [ ] `uv sync` instala todos los miembros del workspace correctamente
- [ ] Los paquetes miembro pueden importarse entre sí sin instalación adicional
- [ ] El `uv.lock` es compartido y único para todo el workspace
- [ ] `uv run --package <nombre>` ejecuta en el contexto correcto del paquete

## 6. Resumen

Los workspaces de uv llevan la gestión de monorepos Python al siguiente nivel, ofreciendo la misma experiencia que Cargo en Rust: un único lock file, resolución de dependencias unificada y gestión simplificada de múltiples paquetes relacionados.

## 7. Reflexión

¿Cuándo tiene sentido usar un monorepo en lugar de múltiples repositorios separados? ¿Qué desafíos anticipas al migrar un equipo existente a esta estructura?
