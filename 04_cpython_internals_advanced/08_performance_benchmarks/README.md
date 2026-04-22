# Benchmarks de Rendimiento: Modo Libre vs GIL
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Los **benchmarks de rendimiento** para CPython comparan el comportamiento del intérprete en modo con GIL versus el modo libre de GIL (free-threading) introducido en Python 3.13. Miden el rendimiento en tareas CPU-bound, I/O-bound y mixtas bajo distintas cargas de trabajo paralelas.

### Características Principales

- **Modo GIL**: un solo hilo ejecuta bytecode Python a la vez; paralelismo real limitado a I/O.
- **Modo free-threading**: múltiples hilos ejecutan bytecode en paralelo en distintos núcleos.
- **Overhead de sincronización**: en modo libre, las operaciones atómicas pueden ser más costosas.
- **Escalabilidad**: el modo libre escala con el número de núcleos en cargas CPU-bound.

## 2. Aplicación Práctica

### Casos de Uso

1. **Validar ganancias en cargas CPU-bound**: cálculos numéricos, procesamiento de texto masivo.
2. **Detectar regresiones**: comparar versiones de CPython para detectar degradaciones.
3. **Dimensionamiento de infraestructura**: decidir cuántos núcleos asignar a un proceso Python.

### Ejemplo de Código

```python
import time
import threading
import sys

def tarea_cpu(n: int) -> int:
    """Suma acumulativa para simular carga CPU."""
    return sum(range(n))

def medir_paralelo(num_hilos: int, n: int) -> float:
    inicio = time.perf_counter()
    hilos = [threading.Thread(target=tarea_cpu, args=(n,)) for _ in range(num_hilos)]
    for h in hilos:
        h.start()
    for h in hilos:
        h.join()
    return time.perf_counter() - inicio

  # Comparar rendimiento con distintas cantidades de hilos
for num_hilos in [1, 2, 4, 8]:
    duracion = medir_paralelo(num_hilos, 10_000_000)
    print(f"Hilos: {num_hilos:2d} | Tiempo: {duracion:.3f}s")

print(f"\nVersión CPython: {sys.version}")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin benchmarks objetivos, es difícil justificar la migración al modo libre de GIL o identificar regresiones de rendimiento introducidas por cambios en el intérprete.

### Solución y Beneficios

- Toma de decisiones basada en datos para elegir el modo de ejecución adecuado.
- Identificación temprana de cuellos de botella en aplicaciones concurrentes.
- Comunicación clara del impacto de rendimiento a equipos de ingeniería.

## 4. Referencias

- https://docs.python.org/3/howto/free-threading-python.html
- https://peps.python.org/pep-0703/
- https://pyperformance.readthedocs.io/
- https://github.com/python/pyperformance
- https://docs.python.org/3/library/timeit.html

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Implementa un benchmark simple que mida el tiempo de una tarea CPU-bound con 1, 2 y 4 hilos.
- Compara los resultados e identifica si hay ganancia de paralelismo.

### Nivel Intermedio

- Usa `timeit` o `perf_counter` para medir con mayor precisión.
- Crea gráficas de rendimiento vs número de hilos para validar escalabilidad.

### Nivel Avanzado

- Instala `pyperformance` y ejecuta la suite completa en modo GIL y modo libre.
- Documenta los resultados y explica las diferencias observadas.

### Criterios de Éxito

- El benchmark mide correctamente el tiempo de ejecución con distintos números de hilos.
- Los resultados muestran la diferencia esperada entre modo GIL y modo libre.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El informe incluye al menos tres conclusiones respaldadas por datos.

## 6. Resumen

- Los benchmarks son herramientas esenciales para cuantificar el impacto del modo libre de GIL.
- Las cargas CPU-bound escalan con el número de núcleos en free-threading.
- Los resultados dependen del hardware, la carga de trabajo y la versión de CPython.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Qué tipo de carga de trabajo de tu proyecto se beneficiaría más del modo libre?
- ¿Cómo garantizarías que tus benchmarks son reproducibles y justos?
- ¿Qué métrica usarías para decidir si vale la pena migrar al modo free-threading?
