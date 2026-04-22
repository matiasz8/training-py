# Objetos Inmortales (PEP 683)
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Los **objetos inmortales** son objetos Python cuyo contador de referencias nunca llega a cero porque están marcados como permanentes en el runtime. Introducidos por PEP 683 en Python 3.12, permiten que objetos como `None`, `True`, `False`, enteros pequeños y strings internados existan durante toda la vida del proceso sin ser liberados ni requerir operaciones de refcount.

### Características Principales

- **`ob_refcnt` especial**: un valor centinela (`_Py_IMMORTAL_REFCNT`) indica inmortalidad.
- **Sin `Py_DECREF` efectivo**: decrementar el refcount de un objeto inmortal es un no-op.
- **Compartibles entre subintérpretes**: al no tener refcount dinámico, son seguros sin sincronización.
- **Objetos inmortales por defecto**: `None`, `True`, `False`, `Ellipsis`, enteros -5 a 256.

## 2. Aplicación Práctica

### Casos de Uso

1. **Constantes globales compartidas**: strings de configuración que no deben liberarse nunca.
2. **Objetos singleton**: garantizar que ciertos objetos existan durante todo el proceso.
3. **Free-threading**: compartir objetos entre subintérpretes sin sincronización de refcount.

### Ejemplo de Código

```python
import sys

def es_inmortal(obj: object) -> bool:
    """
    Detecta si un objeto es inmortal verificando su refcount.
    Los objetos inmortales tienen un refcount muy alto (centinela).
    """
    # En CPython 3.12+, los objetos inmortales tienen refcount >= 2^30
    UMBRAL_INMORTAL = 1 << 30
    refcount = sys.getrefcount(obj)
    return refcount >= UMBRAL_INMORTAL

# Verificar objetos inmortales conocidos
candidatos = [None, True, False, ..., 0, 1, 42, 256, 257, "hola"]
for obj in candidatos:
    inmortal = es_inmortal(obj)
    rc = sys.getrefcount(obj)
    print(f"{repr(obj):10s} -> refcount={rc:12d}, inmortal={inmortal}")

# Demostrar que None siempre es el mismo objeto
def funcion_que_retorna_none():
    pass

resultado = funcion_que_retorna_none()
print(f"\nNone is None: {resultado is None}")
print(f"id(None) siempre igual: {id(None) == id(None)}")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

En un CPython con múltiples hilos, actualizar el refcount de objetos muy compartidos (como `None`) generaría tráfico de caché masivo entre núcleos. Los objetos inmortales eliminan completamente este problema para los objetos más usados.

### Solución y Beneficios

- Eliminación del overhead de refcount en los objetos más comunes del runtime.
- Seguridad para compartir objetos entre subintérpretes sin sincronización.
- Mejora de rendimiento mensurable en aplicaciones que usan intensivamente `None`, `True`, `False`.

## 4. Referencias

- https://peps.python.org/pep-0683/
- https://docs.python.org/3/whatsnew/3.12.html
- https://docs.python.org/3/c-api/refcounting.html
- https://peps.python.org/pep-0703/
- https://github.com/python/cpython/blob/main/Include/object.h

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Identifica al menos 5 objetos inmortales en CPython usando `sys.getrefcount()`.
- Verifica que el refcount de `None` no cambia al crear o destruir referencias a él.

### Nivel Intermedio

- Mide el rendimiento de una función que usa `None` intensivamente versus una que usa un objeto mutable.
- Documenta la diferencia en términos de operaciones de refcount.

### Nivel Avanzado

- Usa `ctypes` para leer el campo `ob_refcnt` directamente y confirmar el valor centinela de inmortalidad.
- Investiga qué otros objetos se convierten en inmortales al hacer `sys.intern()`.

### Criterios de Éxito

- Se identifican correctamente los objetos inmortales del runtime de CPython.
- La diferencia entre objetos inmortales y objetos con refcount alto se explica con precisión.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El análisis incluye implicaciones para el rendimiento en entornos multihilo.

## 6. Resumen

- PEP 683 introduce objetos inmortales cuyo refcount nunca llega a cero.
- `None`, `True`, `False` y las constantes básicas son inmortales en Python 3.12+.
- La inmortalidad elimina operaciones de refcount innecesarias y hace seguros los objetos compartidos entre subintérpretes.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Qué objetos de tu aplicación podrían beneficiarse de ser inmortales?
- ¿Cómo impacta la inmortalidad de objetos en el perfil de memoria de un proceso Python?
- ¿Qué tradeoffs introduce la inmortalidad de objetos en el diseño del runtime?
