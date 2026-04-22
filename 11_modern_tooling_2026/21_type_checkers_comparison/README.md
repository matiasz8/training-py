# Comparación de Type Checkers: mypy vs Pyright vs Pylyzer

⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

El ecosistema Python cuenta con tres type checkers maduros: mypy (el original, Python), Pyright/BasedPyright (Microsoft, TypeScript/Node) y pylyzer (nueva generación, Rust). Cada uno tiene fortalezas distintas en velocidad, precisión, integración con editores y compatibilidad con el ecosistema de tipos Python.

### Características Principales

- **mypy**: El más maduro, lento pero muy preciso; estándar de facto
- **Pyright**: Muy rápido, base de Pylance (VS Code); strictmode excelente
- **BasedPyright**: Fork community de pyright con mejoras adicionales
- **pylyzer**: Rust, ultrarrápido, menos maduro; ideal para proyectos simples
- Todas son compatibles con anotaciones PEP 484/526/612 estándar

## 2. Aplicación Práctica

### Casos de Uso

- Elegir el type checker adecuado según el tamaño y complejidad del proyecto
- Comparar resultados de múltiples checkers para maximizar cobertura de bugs
- Integrar el type checker óptimo en el flujo CI/CD del equipo

### Ejemplo de Código

```bash
mypy src/ --strict                   # mypy en modo estricto
pyright src/                         # pyright análisis completo
basedpyright src/ --outputjson       # basedpyright con salida JSON
pylyzer src/                         # pylyzer ultrarrápido

time mypy src/                       # medir tiempo mypy
time pyright src/                    # medir tiempo pyright
time pylyzer src/                    # medir tiempo pylyzer
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Elegir el type checker equivocado puede resultar en análisis lentos que bloquean el CI/CD, falsos positivos que frustran al equipo, o falsos negativos que dejan pasar bugs de tipo que serán difíciles de encontrar en producción.

### Solución y Beneficios

- Conocer las fortalezas de cada herramienta permite una elección informada
- Usar dos checkers en paralelo puede detectar más bugs que uno solo
- mypy para proyectos maduros, pyright para velocidad y DX en el editor
- La comparación directa revela qué herramienta detecta más problemas reales

## 4. Referencias

- https://mypy-lang.org/
- https://microsoft.github.io/pyright/
- https://docs.basedpyright.com/
- https://github.com/mtshiba/pylyzer
- https://typing.readthedocs.io/en/latest/

## 5. Tarea Práctica

### Nivel Básico

Instala mypy, pyright y pylyzer con `uv tool install`. Ejecuta los tres en el mismo módulo Python. Compara qué errores detecta cada uno y cuál es más rápido.

### Nivel Intermedio

Crea un archivo Python con 10 errores de tipo diferentes (tipos incompatibles, parámetros incorrectos, atributos inexistentes). Verifica cuántos detecta cada herramienta. Documenta las diferencias.

### Nivel Avanzado

Configura los tres type checkers en un pipeline CI/CD. Analiza los tiempos de ejecución, el número de falsos positivos/negativos de cada uno y elabora una recomendación justificada para tu equipo.

### Criterios de Éxito

- [ ] Los tres type checkers están instalados y configurados en el proyecto
- [ ] Documentas al menos 3 diferencias concretas en los errores que cada uno detecta
- [ ] La comparación de velocidad muestra el orden correcto: pylyzer > pyright > mypy
- [ ] Tienes una recomendación justificada sobre qué herramienta usar en cada contexto

## 6. Resumen

No existe un único type checker "mejor" para todos los casos. mypy es el más confiable para proyectos complejos; pyright/basedpyright ofrece excelente DX en editores y velocidad; pylyzer es ideal cuando la velocidad es la prioridad absoluta. La elección depende del contexto específico del proyecto.

## 7. Reflexión

¿Usarías múltiples type checkers en paralelo para maximizar la cobertura de bugs, o el overhead de configuración no justifica el beneficio? ¿Qué criterio priorizarías: velocidad, precisión o integración con el editor?
