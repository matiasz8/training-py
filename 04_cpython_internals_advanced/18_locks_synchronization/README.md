# Locks y Sincronización
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Los **locks y primitivas de sincronización** son mecanismos que coordinan el acceso a recursos compartidos entre hilos. Python ofrece varias primitivas en el módulo `threading`: `Lock`, `RLock`, `Condition`, `Semaphore`, `Event` y `Barrier`, cada una diseñada para patrones específicos de sincronización.

### Características Principales

- **`Lock`**: exclusión mutua básica; solo un hilo puede adquirirlo a la vez.
- **`RLock`**: lock reentrante; el mismo hilo puede adquirirlo múltiples veces.
- **`Condition`**: combina un lock con notificaciones entre hilos.
- **`Semaphore`**: controla el acceso a un número limitado de recursos concurrentes.
- **`Event`**: permite que un hilo señalice a otros que ocurrió un evento.

## 2. Aplicación Práctica

### Casos de Uso

1. **Sección crítica**: proteger un bloque de código donde solo un hilo debe operar a la vez.
2. **Pool de conexiones**: limitar con un `Semaphore` cuántos hilos pueden acceder simultáneamente a una BD.
3. **Coordinación productor-consumidor**: usar `Condition` para notificar disponibilidad de datos.

### Ejemplo de Código

```python
import threading
from collections import deque
from typing import Optional

class ColaSegura:
    """Cola thread-safe usando Condition para coordinación productor-consumidor."""

    def __init__(self, maxsize: int = 10) -> None:
        self._cola: deque = deque()
        self._maxsize = maxsize
        self._condicion = threading.Condition()

    def poner(self, item: object) -> None:
        with self._condicion:
            while len(self._cola) >= self._maxsize:
                self._condicion.wait()
            self._cola.append(item)
            self._condicion.notify_all()

    def obtener(self) -> object:
        with self._condicion:
            while not self._cola:
                self._condicion.wait()
            item = self._cola.popleft()
            self._condicion.notify_all()
            return item

cola = ColaSegura(maxsize=5)
resultados = []

def productor():
    for i in range(10):
        cola.poner(i)

def consumidor():
    for _ in range(10):
        resultados.append(cola.obtener())

t1 = threading.Thread(target=productor)
t2 = threading.Thread(target=consumidor)
t1.start(); t2.start()
t1.join(); t2.join()
print(f"Procesados: {sorted(resultados)}")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin sincronización, los datos compartidos pueden corromperse y los hilos pueden bloquear el sistema (deadlock) o desperdiciar CPU en espera activa (busy-wait). Las primitivas de sincronización ofrecen soluciones correctas y eficientes para estos problemas.

### Solución y Beneficios

- Corrección garantizada en el acceso a recursos compartidos.
- Patrones bien conocidos (productor-consumidor, barrera, semáforo) aplicables directamente.
- Código más legible y mantenible que la sincronización manual con banderas.

## 4. Referencias

- https://docs.python.org/3/library/threading.html
- https://docs.python.org/3/library/queue.html
- https://docs.python.org/3/howto/free-threading-python.html
- https://peps.python.org/pep-0703/
- https://en.wikipedia.org/wiki/Monitor_(synchronization)

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Implementa una sección crítica con `Lock` que proteja un recurso compartido.
- Verifica que sin el lock el resultado es incorrecto y con él es correcto.

### Nivel Intermedio

- Implementa el patrón productor-consumidor usando `Condition` o `queue.Queue`.
- Asegúrate de que el consumidor termina correctamente cuando el productor finaliza.

### Nivel Avanzado

- Implementa un pool de workers con `Semaphore` que limite a 3 hilos accediendo a un recurso a la vez.
- Detecta y previene un posible deadlock en el diseño propuesto.

### Criterios de Éxito

- El `Lock` previene condiciones de carrera demostradas en el ejercicio.
- El patrón productor-consumidor funciona correctamente sin deadlocks.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El código usa gestores de contexto (`with`) para garantizar la liberación de locks.

## 6. Resumen

- Python ofrece un conjunto rico de primitivas de sincronización en el módulo `threading`.
- Elegir la primitiva correcta simplifica el código y previene errores difíciles de depurar.
- Con free-threading, la sincronización explícita es aún más importante que en el modelo con GIL.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Cuándo usarías `Condition` en lugar de `Event` o `queue.Queue`?
- ¿Cómo detectarías un deadlock en una aplicación Python en producción?
- ¿Qué primitiva de sincronización usarías para tu próximo proyecto multihilo?
