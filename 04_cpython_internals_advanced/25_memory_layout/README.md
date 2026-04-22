# Diseño de Memoria de Objetos Python
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

El **diseño de memoria** (memory layout) de los objetos Python describe cómo CPython organiza los campos de un objeto en la memoria: el encabezado `PyObject`, los datos propios del objeto y el alineado de campos. Comprender este diseño permite optimizar el uso de caché del procesador, reducir el footprint de memoria y escribir extensiones C eficientes.

### Características Principales

- **Encabezado fijo**: todos los objetos comienzan con `ob_refcnt` y `ob_type`.
- **Datos específicos del tipo**: los campos del objeto siguen inmediatamente al encabezado.
- **Alineación**: los campos se alinean a múltiplos de su tamaño natural para rendimiento.
- **`__slots__`**: elimina el `__dict__` de las instancias para reducir el footprint de memoria.

## 2. Aplicación Práctica

### Casos de Uso

1. **Optimización de memoria**: usar `__slots__` en clases con millones de instancias.
2. **Extensiones C eficientes**: diseñar structs C que minimicen el padding y desperricio.
3. **Análisis de footprint**: medir y reducir el uso de memoria de objetos en producción.

### Ejemplo de Código

```python
import sys

# Comparar footprint de clase con y sin __slots__
class PuntoConDict:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

class PuntoConSlots:
    __slots__ = ("x", "y", "z")

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

punto_dict = PuntoConDict(1.0, 2.0, 3.0)
punto_slots = PuntoConSlots(1.0, 2.0, 3.0)

print(f"Tamaño con __dict__:  {sys.getsizeof(punto_dict)} bytes")
print(f"Tamaño con __slots__: {sys.getsizeof(punto_slots)} bytes")
print(f"Ahorro por instancia: {sys.getsizeof(punto_dict) - sys.getsizeof(punto_slots)} bytes")

# Con 1M de instancias
N = 1_000_000
print(f"\nAhorro con {N:,} instancias: "
      f"{(sys.getsizeof(punto_dict) - sys.getsizeof(punto_slots)) * N / 1024 / 1024:.1f} MB")

# Inspeccionar el layout del dict de una instancia normal
print(f"\nAtributos de PuntoConDict: {punto_dict.__dict__}")
print(f"PuntoConSlots no tiene __dict__: {not hasattr(punto_slots, '__dict__')}")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin conocer el diseño de memoria, es fácil crear clases que usen el doble o el triple de memoria de lo necesario debido al `__dict__` implícito o al padding de campos. En sistemas con millones de objetos, esto puede agotar la RAM disponible.

### Solución y Beneficios

- Reducción significativa de memoria con `__slots__` en clases de dominio.
- Mejor rendimiento de caché del procesador al compactar los datos del objeto.
- Diagnóstico preciso del footprint de memoria de las estructuras de datos del sistema.

## 4. Referencias

- https://docs.python.org/3/reference/datamodel.html#slots
- https://docs.python.org/3/library/sys.html#sys.getsizeof
- https://docs.python.org/3/c-api/structures.html
- https://peps.python.org/pep-0703/
- https://devguide.python.org/internals/memory-management/

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Mide el tamaño de diferentes tipos de objetos con `sys.getsizeof()`.
- Compara el footprint de una clase con `__dict__` versus con `__slots__`.

### Nivel Intermedio

- Crea una clase de dominio con 5 atributos y optimízala con `__slots__`.
- Mide el ahorro de memoria con 1 millón de instancias usando `tracemalloc`.

### Nivel Avanzado

- Analiza el layout de memoria de un `PyObject` personalizado en C usando `ctypes.sizeof()`.
- Implementa una estructura de datos compacta usando `array.array` o `struct` para datos homogéneos.

### Criterios de Éxito

- El ahorro de memoria de `__slots__` se cuantifica con evidencia numérica.
- El comportamiento del `__dict__` versus `__slots__` se documenta con tests explícitos.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El análisis incluye las limitaciones de `__slots__` (herencia, mixins).

## 6. Resumen

- El diseño de memoria de objetos Python sigue la estructura `PyObject` más datos específicos del tipo.
- `__slots__` elimina el `__dict__` implícito, reduciendo drásticamente el footprint de memoria.
- Comprender el layout de memoria es esencial para optimizar aplicaciones con muchos objetos.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Qué clases de tu proyecto actual se beneficiarían de usar `__slots__`?
- ¿Cuándo es contraproducente usar `__slots__` (herencia múltiple, mixins dinámicos)?
- ¿Cómo cambiaría el diseño de tus estructuras de datos si el uso de memoria fuera una restricción crítica?
