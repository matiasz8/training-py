# Reglas Estrictas de Ruff para Código de Producción

⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Ruff ofrece más de 800 reglas divididas en categorías como seguridad (S/bandit), complejidad (C), anti-patrones (B/bugbear), pyupgrade (UP), anotaciones de tipo (ANN) y más. Activar un conjunto estricto de estas reglas eleva significativamente la calidad del código de producción y detecta bugs en tiempo de análisis estático.

### Características Principales

- Más de 800 reglas de 40+ plugins unificados en una sola herramienta
- Categorías clave para producción: `S` (seguridad), `B` (bugbear), `C` (complejidad), `UP` (modernización)
- `ruff check --select ALL` activa todas las reglas disponibles
- Reglas `FURB` para código más idiomático y `RUF` para reglas específicas de ruff
- Posibilidad de activar `E`, `W`, `F`, `I`, `N`, `ANN`, `D` para cobertura máxima

## 2. Aplicación Práctica

### Casos de Uso

- Proyectos con requisitos estrictos de seguridad que necesitan análisis tipo bandit
- Equipos que quieren detectar code smells y anti-patrones automáticamente
- Bases de código legado que se modernizan gradualmente con `UP` (pyupgrade)

### Ejemplo de Código

```toml
[tool.ruff.lint]
select = [
    "E", "F",    # pycodestyle + pyflakes (base)
    "I",         # isort
    "N",         # pep8-naming
    "S",         # bandit (seguridad)
    "B",         # bugbear (anti-patrones)
    "UP",        # pyupgrade (modernización)
    "C90",       # McCabe complejidad ciclomática
    "ANN",       # anotaciones de tipo
]
ignore = ["ANN101", "ANN102", "S101"]
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin reglas estrictas, el código de producción puede acumular vulnerabilidades de seguridad silenciosas, anti-patrones que dificultan el mantenimiento y código no idiomático que no aprovecha las características modernas de Python.

### Solución y Beneficios

- Detección temprana de vulnerabilidades de seguridad (hardcoded passwords, SQL injection patterns)
- Código más idiomático y moderno con las reglas UP automáticas
- Reducción de code smells mediante reglas B (bugbear) antes de code review
- Un único análisis estático reemplaza bandit, pylint, flake8 y más

## 4. Referencias

- https://docs.astral.sh/ruff/rules/
- https://docs.astral.sh/ruff/linter/
- https://bandit.readthedocs.io/en/latest/
- https://github.com/PyCQA/flake8-bugbear
- https://docs.astral.sh/ruff/settings/#lint_select

## 5. Tarea Práctica

### Nivel Básico

Activa las reglas `S` (bandit) en tu proyecto. Ejecuta `ruff check --select S .` y analiza cada warning reportado. Determina cuáles son falsos positivos y cuáles son problemas reales.

### Nivel Intermedio

Configura un conjunto estricto de reglas (`E`, `F`, `I`, `N`, `S`, `B`, `UP`) en `pyproject.toml`. Corrige todos los issues encontrados o añade supresiones justificadas con `noqa: <código>`.

### Nivel Avanzado

Implementa un proceso gradual de activación de reglas estrictas en un proyecto existente: primero activa solo `F` y `E`, luego añade reglas cada semana documentando los issues encontrados y corregidos.

### Criterios de Éxito

- [ ] `ruff check --select S .` no reporta vulnerabilidades de seguridad reales
- [ ] Las reglas UP actualizan el código a sintaxis Python moderna automáticamente
- [ ] Los `noqa` añadidos están justificados con un comentario explicativo
- [ ] La complejidad ciclomática (C90) no supera el umbral definido en ninguna función

## 6. Resumen

Las reglas estrictas de ruff convierten el linter en una primera línea de defensa para la calidad y seguridad del código de producción. Activar progresivamente más reglas permite mejorar la base de código existente sin bloquear el desarrollo.

## 7. Reflexión

¿Qué nivel de estricteza es apropiado para tu proyecto actual? ¿Cómo balancearías productividad del equipo con rigor en la calidad del código?
