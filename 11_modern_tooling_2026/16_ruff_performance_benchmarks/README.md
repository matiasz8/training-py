# Benchmarks de Performance de Ruff

⏱️ **Tiempo estimado: 1 hora**

## 1. Definición

Ruff es entre 10 y 100 veces más rápido que las herramientas de linting y formato tradicionales de Python. Esta diferencia de rendimiento, posible gracias a su implementación en Rust, cambia fundamentalmente la experiencia de desarrollo: el análisis de código pasa de segundos a milisegundos, incluso en proyectos con decenas de miles de archivos.

### Características Principales

- Análisis de 1M+ líneas de código en menos de 1 segundo
- Paralelismo nativo: utiliza todos los núcleos disponibles del CPU
- Caching inteligente: solo re-analiza archivos modificados
- Sin overhead de startup del intérprete Python
- Resultados idénticos a las herramientas que reemplaza

## 2. Aplicación Práctica

### Casos de Uso

- Equipos con bases de código grandes donde flake8/pylint son demasiado lentos
- Pipelines CI/CD donde cada segundo de análisis importa
- Desarrollo local con análisis en tiempo real integrado en el editor

### Ejemplo de Código

```bash
time flake8 .             # referencia: puede tardar 30s+ en proyectos grandes
time ruff check .         # mismo análisis en < 1s

time black --check .      # formato check: puede tardar 10s+
time ruff format --check .# mismo check en < 100ms

hyperfine 'ruff check .' 'flake8 .'   # benchmark formal con hyperfine
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Las herramientas de linting Python tradicionales (flake8, pylint, black, isort) están implementadas en Python y sufren del overhead del intérprete. En proyectos grandes o con ejecución frecuente (pre-commit, watch mode), la lentitud crea fricción real en el flujo de trabajo.

### Solución y Beneficios

- Feedback instantáneo en el editor sin penalizar el rendimiento del equipo
- Pre-commit hooks que completan en < 1 segundo en lugar de 30+
- CI/CD más rápido y barato al reducir tiempo de análisis estático
- Posibilidad de activar más reglas sin impacto en velocidad

## 4. Referencias

- https://docs.astral.sh/ruff/
- https://github.com/astral-sh/ruff/blob/main/BENCHMARKS.md
- https://astral.sh/blog/ruff
- https://github.com/sharkdp/hyperfine
- https://docs.astral.sh/ruff/faq/#how-does-ruff-compare-to-flake8

## 5. Tarea Práctica

### Nivel Básico

Mide el tiempo de `ruff check .` vs `flake8 .` en tu proyecto con `time`. Documenta la diferencia de velocidad y el número de archivos analizados.

### Nivel Intermedio

Instala `hyperfine` con `uvx hyperfine` y ejecuta un benchmark formal comparando ruff, flake8 y pylint. Genera un reporte con estadísticas de tiempo min/max/media.

### Nivel Avanzado

Configura el modo watch de ruff en tu editor. Mide la diferencia en tiempo de respuesta al guardar un archivo comparado con una configuración basada en flake8. Documenta el impacto en productividad.

### Criterios de Éxito

- [ ] `ruff check .` completa en menos de 1 segundo en el proyecto actual
- [ ] El benchmark documenta al menos 10x de mejora sobre flake8
- [ ] El pre-commit hook con ruff completa en < 2 segundos incluyendo otros hooks
- [ ] El análisis en el editor responde en tiempo real sin retraso perceptible

## 6. Resumen

Los benchmarks de ruff demuestran que la elección de tecnología (Rust vs Python) tiene impacto directo y medible en la productividad del equipo. Velocidades 10-100x superiores transforman el análisis estático de una tarea pesada en un proceso instantáneo que no interrumpe el flujo de trabajo.

## 7. Reflexión

¿Cuánto tiempo pierde tu equipo cada día esperando que los linters terminen? ¿Cómo cambiaría vuestra cultura de calidad de código si el análisis fuera instantáneo?
