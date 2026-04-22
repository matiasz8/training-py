# Algoritmo de Conteo de Referencias
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

El **algoritmo de conteo de referencias** es el mecanismo principal de gestión de memoria de CPython. Cada objeto mantiene un contador (`ob_refcnt`) que se incrementa al crear una nueva referencia al objeto y se decrementa al eliminarla. Cuando el contador llega a cero, el objeto es liberado inmediatamente.

### Características Principales

- **Liberación determinista**: los objetos se liberan en el momento exacto en que ya no son referenciados.
- **`Py_INCREF` / `Py_DECREF`**: macros C que incrementan y decrementan el contador.
- **Ciclos**: el conteo de referencias no puede liberar ciclos; para eso existe el GC cíclico.
- **`sys.getrefcount()`**: permite observar el refcount de cualquier objeto desde Python.

## 2. Aplicación Práctica

### Casos de Uso

1. **Diagnóstico de fugas de memoria**: rastrear objetos con refcount inesperadamente alto.
2. **Desarrollo de extensiones C**: manejar correctamente `Py_INCREF`/`Py_DECREF` en código nativo.
3. **Optimización de código**: evitar referencias innecesarias que retrasen la liberación de objetos grandes.

### Ejemplo de Código

```python
import sys

def demostrar_refcount():
    # Crear objeto y observar su refcount inicial
    lista = [1, 2, 3, 4, 5]
    print(f"Refcount inicial: {sys.getrefcount(lista)}")  # +1 por el argumento de getrefcount

    # Crear una referencia adicional
    otra_ref = lista
    print(f"Refcount con otra_ref: {sys.getrefcount(lista)}")

    # Pasar a una función (referencia temporal)
    def contar_dentro(obj):
        print(f"Refcount dentro de función: {sys.getrefcount(obj)}")

    contar_dentro(lista)

    # Eliminar referencia
    del otra_ref
    print(f"Refcount después de del: {sys.getrefcount(lista)}")

    # Almacenar en una lista (nueva referencia)
    contenedor = [lista]
    print(f"Refcount en contenedor: {sys.getrefcount(lista)}")

demostrar_refcount()

# Demostrar que objetos con refcount 0 se destruyen inmediatamente
class ObjetoConDestructor:
    def __del__(self):
        print("Objeto destruido (refcount llegó a 0)")

obj = ObjetoConDestructor()
print("Antes de del")
del obj
print("Después de del (destrucción fue inmediata)")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

La gestión manual de memoria en C es propensa a fugas y uso después de liberación. El conteo de referencias automatiza este proceso de forma determinista, haciendo que la gestión de memoria en Python sea segura sin requerir un GC de detención del mundo (stop-the-world).

### Solución y Beneficios

- Liberación de memoria predecible y sin pausas de GC para la mayoría de objetos.
- Destrucción determinista de recursos (archivos, conexiones) al salir del scope.
- Base comprensible para entender y optimizar el uso de memoria en Python.

## 4. Referencias

- https://docs.python.org/3/c-api/refcounting.html
- https://docs.python.org/3/library/sys.html#sys.getrefcount
- https://docs.python.org/3/extending/extending.html
- https://devguide.python.org/internals/memory-management/
- https://github.com/python/cpython/blob/main/Include/object.h

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Observa cómo cambia el refcount de un objeto al crear referencias, pasarlo a funciones y borrarlo.
- Documenta cada paso con `sys.getrefcount()`.

### Nivel Intermedio

- Crea un ciclo de referencias y demuestra que el GC es necesario para liberarlo.
- Usa `gc.collect()` para forzar la recolección y verifica la liberación.

### Nivel Avanzado

- Escribe una extensión C mínima que use `Py_INCREF`/`Py_DECREF` correctamente.
- Introduce intencionalmente una fuga de referencias y detecta dónde ocurre.

### Criterios de Éxito

- El comportamiento del refcount se demuestra para al menos 4 operaciones diferentes.
- La diferencia entre referencias fuertes y débiles se explica con un ejemplo.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El análisis incluye un caso donde el GC es necesario (ciclo de referencias).

## 6. Resumen

- El conteo de referencias es el mecanismo principal de gestión de memoria en CPython.
- La liberación es determinista: ocurre exactamente cuando el refcount llega a cero.
- Los ciclos de referencias requieren el GC cíclico como mecanismo complementario.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Por qué CPython usa conteo de referencias en lugar de un GC de marcado-y-barrido puro?
- ¿Cómo afecta el conteo de referencias al rendimiento en aplicaciones con muchos objetos de corta vida?
- ¿Qué prácticas de código minimizarían la presión sobre el sistema de conteo de referencias?
