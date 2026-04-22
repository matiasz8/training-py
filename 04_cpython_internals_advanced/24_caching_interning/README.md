# Caché e Interning de Objetos
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

El **caché e interning de objetos** son técnicas de optimización de CPython que reutilizan objetos existentes en lugar de crear nuevos, reduciendo el uso de memoria y el tiempo de asignación. El interning garantiza que múltiples referencias al mismo valor apunten al mismo objeto en memoria. El caché almacena objetos frecuentemente usados para evitar su creación repetida.

### Características Principales

- **Interning de strings**: `sys.intern()` fuerza el reuso del mismo objeto string para valores iguales.
- **Caché de enteros**: enteros entre -5 y 256 son pre-asignados y reutilizados.
- **Caché de bytecodes**: las constantes de funciones se cachean en el objeto código.
- **Identidad vs igualdad**: objetos internados pueden compararse con `is` en lugar de `==`.

## 2. Aplicación Práctica

### Casos de Uso

1. **Procesamiento masivo de strings**: internar claves de diccionarios o etiquetas repetitivas ahorra memoria.
2. **Lookup tables**: usar strings internados acelera comparaciones en parsers y compiladores.
3. **Análisis de patrones de uso**: identificar cuándo el interning automático vs manual es más conveniente.

### Ejemplo de Código

```python
import sys

# Demostrar interning automático de strings literales
s1 = "hola_mundo"
s2 = "hola_mundo"
print(f"Interning automático (literal): s1 is s2 = {s1 is s2}")

# Interning manual de strings dinámicos
s3 = "hola" + "_mundo"  # string dinámico, puede no estar internado
s4 = sys.intern(s3)
s5 = sys.intern("hola_mundo")
print(f"Interning manual: s4 is s5 = {s4 is s5}")

# Demostrar caché de enteros pequeños
a = 256
b = 256
print(f"Entero 256 cacheado: a is b = {a is b}")

c = 257
d = 257
print(f"Entero 257 NO cacheado: c is d = {c is d}")

# Medir impacto de interning en memoria
import tracemalloc
tracemalloc.start()

# Sin interning: muchos strings duplicados
sin_intern = ["clave_repetida"] * 10_000
snapshot1 = tracemalloc.take_snapshot()

# Con interning: un solo string compartido
clave = sys.intern("clave_repetida")
con_intern = [clave] * 10_000
snapshot2 = tracemalloc.take_snapshot()

print(f"\nMemoria sin interning: {sum(s.size for s in snapshot1.statistics('lineno')[:3])} bytes aprox")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

En aplicaciones que procesan millones de strings o valores repetitivos, la creación de objetos duplicados desperdicia memoria y tiempo de GC. El interning y el caché reducen drásticamente este overhead.

### Solución y Beneficios

- Reducción significativa del uso de memoria para datos con alta repetición.
- Comparaciones de identidad (`is`) más rápidas que comparaciones de valor (`==`).
- Menor presión sobre el GC al reducir el número total de objetos en memoria.

## 4. Referencias

- https://docs.python.org/3/library/sys.html#sys.intern
- https://docs.python.org/3/reference/expressions.html#atom-literals
- https://peps.python.org/pep-0683/
- https://docs.python.org/3/c-api/unicode.html
- https://realpython.com/python-string-interning/

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Demuestra el interning automático de strings literales y el caché de enteros pequeños.
- Verifica los límites del caché de enteros (de -5 a 256).

### Nivel Intermedio

- Mide el uso de memoria de una lista con 100,000 strings repetidos con y sin `sys.intern()`.
- Compara el tiempo de comparación con `==` versus `is` para strings internados.

### Nivel Avanzado

- Implementa un caché de objetos personalizado usando `weakref.WeakValueDictionary`.
- Evalúa cuándo el interning manual es beneficioso y cuándo puede ser contraproducente.

### Criterios de Éxito

- El comportamiento del interning automático y manual se demuestra con ejemplos claros.
- El ahorro de memoria del interning se cuantifica con `tracemalloc`.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El análisis incluye limitaciones y casos donde el interning no aplica.

## 6. Resumen

- El interning y el caché de objetos reducen la creación de objetos duplicados en CPython.
- Los enteros entre -5 y 256 y ciertos strings se cachean automáticamente.
- `sys.intern()` permite forzar el interning de strings en tiempo de ejecución.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿En qué parte de tu código actual podrías beneficiarte del interning de strings?
- ¿Qué riesgos hay al depender de `is` para comparar strings en lugar de `==`?
- ¿Cómo cambia el comportamiento del caché de objetos en el modo free-threading?
