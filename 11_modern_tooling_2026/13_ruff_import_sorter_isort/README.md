# Ruff como Import Sorter: Reemplazo de isort

⏱️ **Tiempo estimado: 1 hora**

## 1. Definición

Ruff incluye un organizador de imports completo que reemplaza a isort con compatibilidad total. Organiza los imports en grupos (stdlib, terceros, locales), los ordena alfabéticamente dentro de cada grupo y soporta todas las configuraciones de isort a través de `[tool.ruff.lint.isort]` en `pyproject.toml`.

### Características Principales

- Organización de imports en secciones: stdlib → terceros → locales
- Compatible con la configuración existente de isort
- 10-100x más rápido que isort en proyectos grandes
- Corrige automáticamente el orden con `ruff check --fix`
- Integrado con el formateador de ruff para coherencia total

## 2. Aplicación Práctica

### Casos de Uso

- Estandarizar el orden de imports en toda la base de código con un solo comando
- Reemplazar isort en pre-commit hooks sin cambiar el comportamiento
- Mantener imports ordenados automáticamente en CI/CD

### Ejemplo de Código

```toml
[tool.ruff.lint]
select = ["I"]         # activa solo reglas de isort

[tool.ruff.lint.isort]
known-first-party = ["mi_paquete"]
force-single-line = false
combine-as-imports = true
```

```bash
ruff check --select I .         # verificar orden de imports
ruff check --select I --fix .   # corregir automáticamente
ruff check --diff .             # ver cambios sin aplicar
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Los imports desordenados dificultan la lectura del código y generan conflictos de merge innecesarios. isort resuelve esto pero es lento en proyectos grandes y requiere configuración separada del linter principal.

### Solución y Beneficios

- Una sola herramienta (ruff) para linting y organización de imports
- Velocidad extrema: analiza miles de archivos en segundos
- Configuración unificada en `pyproject.toml` junto al resto del proyecto
- Sin conflictos entre isort y el formateador: ruff los coordina internamente

## 4. Referencias

- https://docs.astral.sh/ruff/rules/#isort-i
- https://docs.astral.sh/ruff/settings/#lintisort
- https://pycqa.github.io/isort/
- https://docs.astral.sh/ruff/faq/#how-does-ruff-compare-to-isort
- https://github.com/astral-sh/ruff

## 5. Tarea Práctica

### Nivel Básico

Ejecuta `ruff check --select I --fix .` en un proyecto con imports desordenados. Observa los cambios realizados y verifica que el código sigue funcionando.

### Nivel Intermedio

Configura `[tool.ruff.lint.isort]` en `pyproject.toml` con `known-first-party` apuntando a tu paquete. Verifica que los imports locales se agrupan correctamente y añade ruff al pre-commit hook.

### Nivel Avanzado

Migra un proyecto existente con isort configurado a ruff. Compara la configuración de `.isort.cfg` con `[tool.ruff.lint.isort]` en `pyproject.toml`. Mide el tiempo de ejecución antes y después.

### Criterios de Éxito

- [ ] `ruff check --select I .` no reporta errores tras aplicar correcciones
- [ ] Los imports están organizados en secciones stdlib / terceros / locales
- [ ] La configuración isort está en `pyproject.toml` sin archivo `.isort.cfg` separado
- [ ] El pre-commit hook con ruff ordena imports automáticamente en cada commit

## 6. Resumen

Ruff reemplaza isort con total compatibilidad y una velocidad muy superior. Al integrar la organización de imports en la misma herramienta que el linting y formato, se simplifica la configuración del proyecto y se elimina la necesidad de coordinar múltiples herramientas.

## 7. Reflexión

¿Qué tan importante es para tu equipo mantener un orden consistente de imports? ¿Cómo afectaría eliminar isort del toolchain y reemplazarlo con ruff?
