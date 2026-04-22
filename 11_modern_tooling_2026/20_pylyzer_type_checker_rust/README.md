# Pylyzer: Type Checker Escrito en Rust

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

Pylyzer es un type checker y language server para Python implementado en Rust. Ofrece análisis de tipos extremadamente rápido con un enfoque en precisión y mensajes de error informativos. Es una alternativa moderna a mypy y pyright para proyectos que priorizan la velocidad de análisis.

### Características Principales

- Implementado completamente en Rust para máxima velocidad
- Language server (LSP) integrado para soporte en editores
- Mensajes de error descriptivos con sugerencias de corrección
- Análisis de código sin necesidad de ejecutar el intérprete Python
- Compatible con anotaciones de tipo estándar de Python (PEP 484, 526, 612)

## 2. Aplicación Práctica

### Casos de Uso

- Proyectos que requieren análisis de tipos ultrarrápido en CI/CD
- Equipos que buscan una alternativa a mypy con mejor rendimiento
- Exploración de herramientas de type checking de nueva generación escritas en Rust

### Ejemplo de Código

```bash
pip install pylyzer                  # o: uv tool install pylyzer
pylyzer src/                         # analiza el directorio src/
pylyzer --check-only main.py         # solo verificación sin server LSP

pylyzer --server                     # inicia como language server LSP
```

```python
def suma(a: int, b: int) -> int:
    return a + b

resultado: str = suma(1, 2)          # pylyzer detecta: int != str
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

mypy, aunque maduro y confiable, puede ser lento en proyectos grandes con muchas dependencias. Los tiempos de análisis de varios segundos o minutos en proyectos grandes dificultan su uso en flujos de trabajo iterativos y CI/CD rápido.

### Solución y Beneficios

- Análisis de tipos en milisegundos gracias a la implementación en Rust
- Language server responsivo para integración fluida en editores
- Sin dependencia del intérprete Python para ejecutar el análisis
- Ecosistema activo con actualizaciones frecuentes y mejoras continuas

## 4. Referencias

- https://github.com/mtshiba/pylyzer
- https://pypi.org/project/pylyzer/
- https://mtshiba.github.io/pylyzer/
- https://microsoft.github.io/language-server-protocol/
- https://docs.python.org/3/library/typing.html

## 5. Tarea Práctica

### Nivel Básico

Instala pylyzer con `uv tool install pylyzer`. Ejecútalo sobre un módulo Python con anotaciones de tipo y observa qué errores detecta. Compara la velocidad con `mypy` en el mismo archivo.

### Nivel Intermedio

Configura pylyzer como language server en tu editor (VS Code, Neovim). Escribe código con errores de tipo intencionales y verifica que pylyzer los detecta en tiempo real mientras escribes.

### Nivel Avanzado

Compara pylyzer con mypy y pyright en el mismo proyecto: número de errores detectados, velocidad, falsos positivos y calidad de los mensajes de error. Documenta cuál elegirías para producción y por qué.

### Criterios de Éxito

- [ ] `pylyzer src/` completa el análisis más rápido que `mypy src/` en el mismo proyecto
- [ ] Los errores de tipo detectados son válidos (no falsos positivos)
- [ ] El language server proporciona feedback en tiempo real en el editor
- [ ] Puedes configurar pylyzer en el pipeline de CI/CD

## 6. Resumen

Pylyzer representa la nueva generación de herramientas de análisis estático Python: implementadas en Rust, extremadamente rápidas y con excelentes mensajes de error. Aunque aún menos maduro que mypy o pyright, su velocidad lo hace especialmente valioso para proyectos grandes o workflows de CI/CD intensivos.

## 7. Reflexión

¿Vale la pena adoptar una herramienta más rápida pero menos madura como pylyzer, o prefieres la estabilidad de mypy/pyright? ¿Qué criterios usarías para tomar esta decisión?
