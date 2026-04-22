# Recolección de Basura Segura para Hilos
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

El **recolector de basura seguro para hilos** (thread-safe GC) es la reimplementación del GC cíclico de CPython para funcionar correctamente sin el GIL. Detecta y libera ciclos de referencias entre objetos incluso cuando múltiples hilos crean y destruyen objetos simultáneamente.

### Características Principales

- **Detección de ciclos**: identifica grupos de objetos mutuamente referenciados que no son alcanzables.
- **Generaciones**: organiza objetos en generaciones 0, 1 y 2 según su antigüedad.
- **Seguridad bajo concurrencia**: usa marcas atómicas para gestionar el estado de los objetos durante la recolección.
- **Triggereable manualmente**: se puede invocar con `gc.collect()`.

## 2. Aplicación Práctica

### Casos de Uso

1. **Ciclos en estructuras de datos**: listas o diccionarios que se referencian mutuamente.
2. **Objetos con `__del__`**: instancias que requieren limpieza explícita al ser recolectadas.
3. **Perfilado de memoria**: uso de `gc.get_objects()` para auditar objetos vivos.

### Ejemplo de Código

```python
import gc
import threading

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def crear_ciclo():
    a = Nodo(1)
    b = Nodo(2)
    a.siguiente = b
    b.siguiente = a  # ciclo: a -> b -> a

threads = [threading.Thread(target=crear_ciclo) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

  # Forzar recolección de ciclos creados por múltiples hilos
recolectados = gc.collect()
print(f"Objetos recolectados: {recolectados}")
print(f"Estadísticas GC: {gc.get_stats()}")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin un GC seguro para hilos, los ciclos de referencias creados concurrentemente podrían no liberarse o provocar corrupción de memoria al recolectarse en condiciones de carrera.

### Solución y Beneficios

- Prevención de fugas de memoria en aplicaciones multihilo de larga duración.
- Correcta finalización de objetos con `__del__` bajo concurrencia.
- Estadísticas precisas de memoria independientes del hilo que las consulte.

## 4. Referencias

- https://docs.python.org/3/library/gc.html
- https://peps.python.org/pep-0703/
- https://github.com/python/cpython/blob/main/InternalDocs/garbage_collector.md
- https://docs.python.org/3/howto/free-threading-python.html
- https://devguide.python.org/internals/garbage-collector/

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Crea ciclos de referencias desde múltiples hilos y verifica que `gc.collect()` los libera.
- Imprime las estadísticas del GC antes y después de la recolección.

### Nivel Intermedio

- Implementa una clase con `__del__` y verifica que se llama correctamente incluso en ciclos multihilo.
- Mide el tiempo de recolección con distintas cantidades de hilos.

### Nivel Avanzado

- Estudia `Modules/gcmodule.c` para entender cómo el GC marca objetos durante la recolección concurrente.
- Escribe un test de estrés que cree y destruya ciclos desde 8 hilos simultáneos sin fugas detectables.

### Criterios de Éxito

- Los ciclos creados concurrentemente son liberados correctamente.
- No se producen errores de segmentación ni corrupción al ejecutar en modo free-threading.
- Los tests en `tests/test_basic.py` pasan correctamente.
- Se documenta el comportamiento observado en los comentarios del código.

## 6. Resumen

- El GC de CPython 3.13+ opera de forma segura bajo múltiples hilos simultáneos.
- La correcta gestión de ciclos evita fugas de memoria en aplicaciones de larga duración.
- Conocer el GC permite tomar decisiones informadas sobre el ciclo de vida de los objetos.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Cuándo conviene evitar ciclos de referencias en lugar de depender del GC?
- ¿Cómo impacta el GC en la latencia de una aplicación de tiempo real?
- ¿Qué estrategias usarías para minimizar la presión sobre el GC en producción?
