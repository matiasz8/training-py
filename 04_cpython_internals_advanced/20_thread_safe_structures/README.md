# Estructuras de Datos Seguras para Hilos
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Las **estructuras de datos seguras para hilos** (thread-safe) son aquellas que garantizan la corrección de sus operaciones cuando son accedidas concurrentemente por múltiples hilos. En Python, `queue.Queue` es la estructura más usada, pero existen otras opciones según el patrón de acceso requerido.

### Características Principales

- **`queue.Queue`**: cola FIFO thread-safe; la más recomendada para comunicación entre hilos.
- **`queue.LifoQueue`**: cola LIFO (pila) thread-safe.
- **`queue.PriorityQueue`**: cola de prioridad thread-safe.
- **`collections.deque`**: thread-safe para `append` y `popleft` en los extremos.
- **Diccionarios (`dict`)**: en CPython con GIL las operaciones individuales son atómicas; con free-threading requieren protección explícita.

## 2. Aplicación Práctica

### Casos de Uso

1. **Sistema de tareas en background**: una `Queue` distribuye trabajo entre workers.
2. **Buffer de mensajes**: acumular logs o eventos desde múltiples hilos para procesamiento posterior.
3. **Pipeline de procesamiento**: encadenar etapas usando colas como canales entre hilos.

### Ejemplo de Código

```python
import threading
import queue
import time
from typing import Optional

def worker(cola_entrada: queue.Queue, cola_salida: queue.Queue, id_worker: int) -> None:
    """Procesa tareas de la cola de entrada y pone resultados en la de salida."""
    while True:
        try:
            tarea: Optional[int] = cola_entrada.get(timeout=1.0)
        except queue.Empty:
            break
        resultado = tarea * tarea
        cola_salida.put((id_worker, tarea, resultado))
        cola_entrada.task_done()

# Crear colas
tareas: queue.Queue[int] = queue.Queue()
resultados: queue.Queue = queue.Queue()

# Poner 20 tareas en la cola
for i in range(20):
    tareas.put(i)

# Lanzar 4 workers
workers = [
    threading.Thread(target=worker, args=(tareas, resultados, i), daemon=True)
    for i in range(4)
]
for w in workers:
    w.start()

tareas.join()  # Esperar a que se procesen todas las tareas

# Recoger resultados
while not resultados.empty():
    wid, entrada, salida = resultados.get()
    print(f"Worker {wid}: {entrada}² = {salida}")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Implementar estructuras de datos thread-safe desde cero es complejo y propenso a errores sutiles. Las estructuras de la biblioteca estándar ofrecen garantías verificadas y comportamiento predecible, ahorrando tiempo y previniendo bugs difíciles de diagnosticar.

### Solución y Beneficios

- Corrección garantizada sin necesidad de implementar sincronización propia.
- API familiar que simplifica la arquitectura de sistemas concurrentes.
- Integración nativa con el modelo de hilos de Python.

## 4. Referencias

- https://docs.python.org/3/library/queue.html
- https://docs.python.org/3/library/collections.html#collections.deque
- https://docs.python.org/3/howto/free-threading-python.html
- https://peps.python.org/pep-0703/
- https://docs.python.org/3/library/threading.html

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Implementa un sistema de workers que lea tareas de una `queue.Queue` y procese cada una.
- Usa `task_done()` y `join()` para saber cuándo se completó todo el trabajo.

### Nivel Intermedio

- Implementa un pipeline de dos etapas usando dos colas: la primera transforma los datos y la segunda los agrega.
- Maneja correctamente la señal de terminación para los workers.

### Nivel Avanzado

- Implementa una `PriorityQueue` que procese tareas con diferentes prioridades.
- Mide el throughput del sistema bajo distintas cargas y números de workers.

### Criterios de Éxito

- Todos los items son procesados exactamente una vez, verificado con assertions.
- No se producen deadlocks ni workers que queden bloqueados indefinidamente.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El sistema se comporta correctamente tanto con 1 como con 8 workers.

## 6. Resumen

- Python ofrece estructuras de datos thread-safe nativas en `queue` y `collections`.
- `queue.Queue` es el componente central del patrón productor-consumidor en Python.
- Con free-threading, elegir las estructuras correctas es más crítico que en el modelo con GIL.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿En qué situaciones una `deque` es suficiente y cuándo necesitas una `Queue`?
- ¿Cómo diseñarías un sistema de workers tolerante a fallos con `Queue`?
- ¿Qué diferencias hay entre `queue.Queue` y `asyncio.Queue`?
