# viztracer: Tracing Visual de Ejecución

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

viztracer es una herramienta de tracing que registra la ejecución de un programa Python a nivel de función, generando una línea de tiempo visual interactiva. A diferencia de los profilers de muestreo, viztracer registra CADA llamada a función, permitiendo ver el flujo de ejecución exacto, los tiempos precisos y las relaciones de llamadas en detalle.

### Características Principales

- Timeline visual interactiva basada en Perfetto (Google Chrome Tracing)
- Registro de cada llamada a función con tiempo de inicio y duración exactos
- Soporte para threads, subprocesos y código async/await
- Logging personalizado: añadir eventos custom al timeline
- Filtros para reducir el overhead: registrar solo funciones específicas

## 2. Aplicación Práctica

### Casos de Uso

- Entender el flujo de ejecución de código complejo con muchas llamadas anidadas
- Comparar visualmente el comportamiento de dos implementaciones alternativas
- Identificar llamadas inesperadas o redundantes en código de alta performance

### Ejemplo de Código

```bash
uv tool install viztracer

viztracer mi_script.py                    # genera result.json
vizviewer result.json                     # abre el viewer en el navegador

viztracer --output_file trace.json mi_script.py
viztracer --ignore_c_function mi_script.py  # solo funciones Python
viztracer --max_stack_depth 10 mi_script.py # limitar profundidad de tracing
```

```python
from viztracer import VizTracer

with VizTracer(output_file="trace.json") as tracer:
    resultado = mi_funcion_compleja()
    tracer.add_instant("checkpoint", args={"valor": resultado})
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Los profilers de sampling muestran dónde se pasa el tiempo en promedio, pero no revelan el flujo de ejecución exacto ni las interacciones entre componentes. Cuando el problema no es lentitud sino comportamiento inesperado o llamadas redundantes, necesitas un tracer, no un profiler.

### Solución y Beneficios

- Visualización del flujo de ejecución completo, no solo promedios estadísticos
- Identificación de llamadas redundantes o inesperadas que el sampling no detectaría
- Timeline interactiva que facilita la comunicación del análisis al equipo
- Soporte nativo para async/await, threads y código multihilo

## 4. Referencias

- https://viztracer.readthedocs.io/en/latest/
- https://github.com/gaogaotiantian/viztracer
- https://ui.perfetto.dev/
- https://developer.chrome.com/docs/devtools/performance/
- https://pypi.org/project/viztracer/

## 5. Tarea Práctica

### Nivel Básico

Instala viztracer y ejecútalo sobre un script con al menos 3 niveles de llamadas a funciones. Abre el resultado en el viewer y navega por la timeline. Identifica la función más anidada.

### Nivel Intermedio

Usa `VizTracer` como context manager para trazar solo una sección crítica de tu código. Añade al menos 2 eventos custom con `add_instant` para marcar checkpoints importantes en el timeline.

### Nivel Avanzado

Compara los traces de dos implementaciones alternativas del mismo algoritmo. Usa la vista de flamegraph de Perfetto para comparar visualmente cuál tiene menos llamadas anidadas y mejor distribución del tiempo.

### Criterios de Éxito

- [ ] La timeline generada muestra claramente la jerarquía de llamadas a funciones
- [ ] Los eventos custom aparecen en el timeline en los momentos correctos
- [ ] Puedes identificar una llamada redundante o inesperada en el trace
- [ ] El overhead de viztracer es aceptable para el uso en desarrollo (no en producción)

## 6. Resumen

viztracer complementa a los profilers de sampling como py-spy con una vista detallada del flujo de ejecución. Su timeline interactiva hace que el análisis de rendimiento sea accesible y comunicable, transformando datos de profiling en una narrativa visual clara sobre cómo se comporta el programa.

## 7. Reflexión

¿Qué parte de tu código tiene un flujo de ejecución complejo y difícil de entender leyendo el código fuente? ¿Cómo te ayudaría viztracer a entenderlo mejor?
