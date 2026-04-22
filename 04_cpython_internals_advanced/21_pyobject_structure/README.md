# Estructura PyObject en C
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

**`PyObject`** es la estructura C base de todos los objetos Python. Todo objeto en CPython —enteros, listas, funciones, clases— comienza con un encabezado `PyObject` que contiene el contador de referencias (`ob_refcnt`) y un puntero al tipo del objeto (`ob_type`). Comprender esta estructura es fundamental para entender cómo CPython gestiona la memoria.

### Características Principales

- **`ob_refcnt`**: contador de referencias; cuando llega a cero el objeto es liberado.
- **`ob_type`**: puntero a `PyTypeObject`, que define el comportamiento del objeto.
- **`PyVarObject`**: extensión de `PyObject` para objetos de tamaño variable (listas, strings, etc.) con campo `ob_size`.
- **Alineación de memoria**: el encabezado está alineado para optimizar el acceso a la caché.

## 2. Aplicación Práctica

### Casos de Uso

1. **Desarrollo de extensiones C**: todo objeto creado en una extensión comienza con `PyObject_HEAD`.
2. **Análisis de memoria**: inspeccionar el refcount de objetos desde Python o C para diagnosticar fugas.
3. **Implementación de tipos personalizados**: extender `PyObject` para crear tipos Python nativos en C.

### Ejemplo de Código

```python
import sys
import ctypes

def inspeccionar_pyobject(obj: object) -> None:
    """Inspecciona el encabezado PyObject de cualquier objeto Python."""
    direccion = id(obj)
    refcount = sys.getrefcount(obj)

    print(f"Objeto: {repr(obj)}")
    print(f"Tipo:   {type(obj).__name__}")
    print(f"ID (dirección de memoria): 0x{direccion:016x}")
    print(f"Refcount (incluye la llamada a getrefcount): {refcount}")
    print(f"Tamaño en memoria: {sys.getsizeof(obj)} bytes")
    print()

# Inspeccionar distintos tipos de objetos
for objeto in [42, "hola", [1, 2, 3], {"a": 1}, None]:
    inspeccionar_pyobject(objeto)

# Los enteros pequeños están internados (mismo objeto reutilizado)
a = 100
b = 100
print(f"a is b (entero pequeño): {a is b} (mismo PyObject: id={id(a)})")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin comprender la estructura `PyObject`, es imposible escribir extensiones C correctas, diagnosticar fugas de memoria a nivel de objetos, o entender por qué ciertas optimizaciones de CPython (interning, caching) son seguras.

### Solución y Beneficios

- Base sólida para desarrollar extensiones C eficientes y correctas.
- Capacidad de diagnosticar fugas de referencias con `sys.getrefcount`.
- Comprensión profunda del modelo de objetos de Python para optimizaciones avanzadas.

## 4. Referencias

- https://docs.python.org/3/c-api/structures.html
- https://docs.python.org/3/c-api/refcounting.html
- https://docs.python.org/3/library/sys.html#sys.getrefcount
- https://github.com/python/cpython/blob/main/Include/object.h
- https://realpython.com/cpython-source-code-guide/

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Usa `sys.getrefcount()` y `sys.getsizeof()` para inspeccionar al menos 5 tipos de objetos diferentes.
- Documenta el overhead del encabezado `PyObject` para cada tipo.

### Nivel Intermedio

- Escribe código que demuestre cómo el refcount cambia al asignar, pasar a funciones y eliminar referencias.
- Usa `ctypes` para leer directamente el campo `ob_refcnt` desde la dirección de memoria del objeto.

### Nivel Avanzado

- Escribe una extensión C mínima que cree y devuelva un `PyObject` personalizado con un campo adicional.
- Verifica que el refcount se gestiona correctamente al retornar el objeto a Python.

### Criterios de Éxito

- Se inspeccionan correctamente los campos `ob_refcnt` y `ob_type` de diferentes objetos.
- El comportamiento del refcount ante asignaciones y eliminaciones se documenta con ejemplos.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El análisis incluye al menos un objeto de tamaño variable (`PyVarObject`).

## 6. Resumen

- `PyObject` es el bloque de construcción fundamental de todos los objetos Python en CPython.
- Sus campos `ob_refcnt` y `ob_type` son la base del sistema de gestión de memoria.
- Comprender esta estructura es indispensable para el desarrollo avanzado con CPython.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Por qué Python usa conteo de referencias como mecanismo principal de gestión de memoria?
- ¿Qué implicaciones tiene que todos los objetos compartan el mismo encabezado `PyObject`?
- ¿Cómo cambiaría el diseño de `PyObject` en un sistema sin GIL?
