# memray: Memory Profiling Moderno

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

memray es un profiler de memoria para Python desarrollado por Bloomberg. Rastrea todas las asignaciones de memoria durante la ejecución del programa, incluyendo extensiones C nativas, y genera visualizaciones ricas como flamegraphs de memoria, histogramas de asignaciones y reportes temporales que muestran el crecimiento de memoria en el tiempo.

### Características Principales

- Rastreo completo de asignaciones: Python heap + extensiones C nativas
- Múltiples modos de visualización: flamegraph, tree, stats, temporal
- Modo live para ver asignaciones en tiempo real durante la ejecución
- Decorador `@memray.profile` para perfilar funciones específicas
- Integración con pytest mediante `pytest-memray`

## 2. Aplicación Práctica

### Casos de Uso

- Diagnosticar memory leaks en servicios Python de larga duración
- Identificar qué operaciones de datos consumen más memoria en pipelines ETL
- Verificar que una optimización de memoria realmente reduce el consumo

### Ejemplo de Código

```bash
uv tool install memray

memray run -o output.bin mi_script.py           # perfilar script
memray flamegraph output.bin                    # genera flamegraph HTML
memray tree output.bin                          # vista de árbol de asignaciones
memray stats output.bin                         # estadísticas de asignaciones
memray run --live mi_script.py                  # monitor en tiempo real
```

```python
import memray

with memray.Tracker("output.bin"):
    procesar_datos_grandes()             # perfilar bloque específico
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Los memory leaks en Python son difíciles de detectar porque el garbage collector oculta muchos problemas. Los servicios que consumen cada vez más memoria hasta crashear o requerir reinicios periódicos son un problema frecuente que sin herramientas adecuadas tarda días en diagnosticarse.

### Solución y Beneficios

- Visibilidad completa de todas las asignaciones de memoria con trazas de stack
- Flamegraphs de memoria que identifican visualmente las fuentes principales de consumo
- Detección de memory leaks mediante análisis temporal del crecimiento de memoria
- Integración con pytest para establecer límites de memoria en tests

## 4. Referencias

- https://bloomberg.github.io/memray/
- https://github.com/bloomberg/memray
- https://bloomberg.github.io/memray/flamegraph.html
- https://bloomberg.github.io/memray/live.html
- https://pypi.org/project/pytest-memray/

## 5. Tarea Práctica

### Nivel Básico

Instala memray y perfiliza un script que procese un dataset grande (ej: leer y transformar un CSV de 100MB). Genera el flamegraph HTML y identifica la operación que consume más memoria.

### Nivel Intermedio

Usa `memray.Tracker` como context manager para aislar la sección de código con mayor consumo. Compara el uso de `list` vs generadores para el mismo procesamiento y documenta la diferencia en memoria.

### Nivel Avanzado

Configura `pytest-memray` para establecer límites de memoria en tests críticos usando `@pytest.mark.limit_memory("50 MB")`. Integra los checks en CI/CD para prevenir regresiones de memoria.

### Criterios de Éxito

- [ ] El flamegraph de memoria identifica correctamente la función con mayor asignación
- [ ] Una optimización de memoria (ej: usar generadores) se valida con memray antes y después
- [ ] `memray stats` muestra las estadísticas más relevantes del perfil de memoria
- [ ] Al menos un test con límite de memoria está configurado con pytest-memray

## 6. Resumen

memray ofrece visibilidad sin precedentes sobre el uso de memoria en Python, incluyendo extensiones C que los profilers Python tradicionales no pueden ver. Sus visualizaciones intuitivas aceleran dramáticamente el diagnóstico de problemas de memoria que de otro modo tomarían días de investigación.

## 7. Reflexión

¿Cuánta memoria consumen realmente los procesos Python de tu infraestructura? ¿Has tenido alguna vez un servicio que crecía en memoria indefinidamente? ¿Cómo habrías diagnosticado ese problema con memray?
