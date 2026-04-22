# Operaciones Atómicas en Python
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Las **operaciones atómicas** son operaciones que se ejecutan como una unidad indivisible, sin posibilidad de interrupción por otros hilos en medio de su ejecución. En CPython con free-threading, muchas operaciones que antes eran implícitamente atómicas gracias al GIL ahora requieren garantías explícitas mediante instrucciones atómicas del procesador o primitivas del runtime.

### Características Principales

- **Indivisibilidad**: la operación se completa completamente o no comienza, sin estados intermedios visibles.
- **Visibilidad inmediata**: el resultado de una operación atómica es visible para todos los hilos al instante.
- **Sin locks**: las operaciones atómicas son más eficientes que los mutexes para operaciones simples.
- **Tipos atómicos en C**: CPython usa `_Py_atomic_int`, `_Py_atomic_ptr` internamente para contadores.

## 2. Aplicación Práctica

### Casos de Uso

1. **Contadores compartidos**: incrementar un contador de peticiones sin condiciones de carrera.
2. **Flags de estado**: señalizar la terminación de un hilo a otros sin mutexes.
3. **Caches con invalidación**: marcar entradas de caché como inválidas de forma segura.

### Ejemplo de Código

```python
import threading
from typing import Final

  # Simular un contador atómico usando threading.Lock para garantía en CPython
class ContadorAtomico:
    def __init__(self, valor_inicial: int = 0) -> None:
        self._valor = valor_inicial
        self._lock = threading.Lock()

    def incrementar(self) -> int:
        with self._lock:
            self._valor += 1
            return self._valor

    def leer(self) -> int:
        return self._valor  # lectura simple, segura si es int

contador = ContadorAtomico()
NUM_HILOS: Final = 100
NUM_INC: Final = 1000

hilos = [
    threading.Thread(target=lambda: [contador.incrementar() for _ in range(NUM_INC)])
    for _ in range(NUM_HILOS)
]
for h in hilos:
    h.start()
for h in hilos:
    h.join()

esperado = NUM_HILOS * NUM_INC
print(f"Esperado: {esperado}, Obtenido: {contador.leer()}")
assert contador.leer() == esperado, "¡Condición de carrera detectada!"
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin operaciones atómicas, las actualizaciones concurrentes de valores compartidos producen resultados incorrectos. Una operación como `x += 1` que parece simple es en realidad tres pasos (leer, sumar, escribir) que pueden intercalarse con otros hilos.

### Solución y Beneficios

- Corrección garantizada para operaciones simples en entornos multihilo.
- Mayor rendimiento que mutexes completos para operaciones de actualización puntual.
- Base para la construcción de estructuras de datos lock-free de alto rendimiento.

## 4. Referencias

- https://docs.python.org/3/library/threading.html
- https://peps.python.org/pep-0703/
- https://docs.python.org/3/howto/free-threading-python.html
- https://github.com/python/cpython/blob/main/Include/cpython/pyatomic.h
- https://en.wikipedia.org/wiki/Compare-and-swap

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Implementa un contador compartido y demuestra una condición de carrera sin protección.
- Corrige el contador usando un `threading.Lock` y verifica la corrección.

### Nivel Intermedio

- Compara el rendimiento de un contador con `Lock` frente a `threading.local` para contadores por hilo.
- Usa `timeit` para medir el overhead de la sincronización.

### Nivel Avanzado

- Investiga `ctypes.c_int` y operaciones CAS (Compare-And-Swap) para implementar un contador sin GIL.
- Evalúa cuándo vale la pena implementar operaciones atómicas a nivel de C.

### Criterios de Éxito

- El contador produce el resultado correcto con 100 hilos y 1000 incrementos cada uno.
- Se demuestra la condición de carrera sin protección y su corrección con Lock.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El análisis incluye una comparación de rendimiento entre las implementaciones.

## 6. Resumen

- Las operaciones atómicas son indivisibles y esenciales para la corrección en entornos multihilo.
- En CPython, el GIL hacía implícitas muchas garantías atómicas; free-threading las hace explícitas.
- Elegir entre operaciones atómicas y mutexes depende de la complejidad y el rendimiento requerido.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Qué operaciones en tu código actual podrían no ser atómicas en un entorno multihilo?
- ¿Cuándo usarías operaciones atómicas en lugar de un mutex completo?
- ¿Cómo cambiaría tu diseño si todas las operaciones sobre datos compartidos deban ser explícitamente atómicas?
