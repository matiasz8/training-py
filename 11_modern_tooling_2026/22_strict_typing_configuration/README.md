# Configuración de Tipado Estricto

⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

El modo estricto de los type checkers activa todas las verificaciones de tipo disponibles, incluyendo la obligatoriedad de anotar todos los parámetros y retornos de funciones, prohibir el uso implícito de `Any`, y verificar que no existen rutas de código sin tipo. Es la configuración recomendada para código de producción crítico.

### Características Principales

- `mypy --strict`: activa 20+ flags de verificación estricta simultáneamente
- `pyright --strict` / `"typeCheckingMode": "strict"`: verificación máxima de pyright
- Prohibición de `Any` implícito con `--disallow-any-generics` y similares
- Verificación de funciones sin anotar con `--disallow-untyped-defs`
- Configuración gradual: migrar a strict de forma incremental por módulo

## 2. Aplicación Práctica

### Casos de Uso

- Librerías públicas que deben ser completamente type-safe para sus usuarios
- Código de dominio crítico donde los bugs de tipo pueden causar problemas graves
- Equipos que quieren adoptar tipado estricto gradualmente en un proyecto existente

### Ejemplo de Código

```toml
[tool.mypy]
strict = true
python_version = "3.11"
ignore_missing_imports = false
warn_return_any = true
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = "legacy_module.*"
ignore_errors = true
```

```toml
[tool.pyright]
typeCheckingMode = "strict"
pythonVersion = "3.11"
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

El tipado parcial o laxo proporciona una falsa sensación de seguridad. Las funciones sin anotar o con `Any` implícito quedan fuera del análisis del type checker, creando puntos ciegos donde pueden ocurrir errores de tipo en producción.

### Solución y Beneficios

- Cobertura de tipo completa: ninguna función queda sin verificar
- Detección de bugs en tiempo de desarrollo, no en producción
- Código más mantenible y auto-documentado gracias a las anotaciones explícitas
- Mejor soporte de autocompletado e inteligencia en el editor

## 4. Referencias

- https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict
- https://microsoft.github.io/pyright/#/configuration
- https://typing.readthedocs.io/en/latest/guides/writing_stubs.html
- https://mypy.readthedocs.io/en/stable/existing_code.html
- https://realpython.com/python-type-checking/

## 5. Tarea Práctica

### Nivel Básico

Activa `mypy --strict` en un módulo pequeño tuyo. Añade todas las anotaciones necesarias para que pase sin errores. Observa cómo el proceso te obliga a pensar en los tipos de cada función.

### Nivel Intermedio

Configura `strict = true` en `pyproject.toml` para mypy y `typeCheckingMode = "strict"` para pyright. Usa `[[tool.mypy.overrides]]` para excluir temporalmente módulos legados y adopta strict gradualmente.

### Nivel Avanzado

Diseña un plan de migración a tipado estricto para un proyecto existente: prioriza módulos por criticidad, usa `type: ignore` con comentarios justificados para casos excepcionales, y establece un proceso de PR que requiera tipado estricto en código nuevo.

### Criterios de Éxito

- [ ] Al menos un módulo del proyecto pasa `mypy --strict` sin errores
- [ ] La configuración de strict está en `pyproject.toml`, no solo como flag CLI
- [ ] Los `type: ignore` añadidos tienen comentarios explicando por qué son necesarios
- [ ] El pipeline CI/CD verifica el tipado estricto en los módulos configurados

## 6. Resumen

El tipado estricto transforma las anotaciones de tipo de adorno documentacional a una garantía real de corrección. Aunque requiere más esfuerzo inicial, especialmente al migrar código existente, el retorno en términos de bugs detectados temprano y mantenibilidad es significativo.

## 7. Reflexión

¿Qué porcentaje de tu código actual pasaría mypy strict sin modificaciones? ¿Cómo planificarías la migración incremental para no bloquear el desarrollo del equipo?
