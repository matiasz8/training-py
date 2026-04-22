# API en C para Subintérpretes
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

La **API en C para subintérpretes** expone las funciones del runtime de CPython que permiten crear, gestionar y destruir subintérpretes desde código C o extensiones. Funciones como `Py_NewInterpreterFromConfig()` dan control granular sobre el estado de cada subintérprete, incluyendo si comparte o no el GIL.

### Características Principales

- **`Py_NewInterpreterFromConfig`**: crea un subintérprete con configuración personalizada (Python 3.12+).
- **`Py_EndInterpreter`**: destruye un subintérprete y libera sus recursos.
- **`PyThreadState`**: cada subintérprete tiene su propio estado de hilo activo.
- **`PyInterpreterState`**: estructura C que representa el estado global de un subintérprete.

## 2. Aplicación Práctica

### Casos de Uso

1. **Servidores de aplicaciones embebidos**: incrustar CPython en aplicaciones C con múltiples contextos aislados.
2. **Extensiones de alto rendimiento**: lanzar subintérpretes desde C para ejecutar Python en paralelo.
3. **Testing de aislamiento**: crear subintérpretes de prueba en suites de test para C extensions.

### Ejemplo de Código

```python
import ctypes
import sys

  # Verificar que el intérprete actual tiene un ID válido
def obtener_info_interprete():
    """Muestra información del intérprete actual usando la API de Python."""
    import _interpreters
    id_actual = _interpreters.get_current()
    todos = list(_interpreters.list_all())
    print(f"Intérprete actual: {id_actual}")
    print(f"Total de intérpretes activos: {len(todos)}")
    for interp_id in todos:
        print(f"  - ID: {interp_id}")

obtener_info_interprete()

  # Demostrar creación y destrucción desde Python (proxy de la API C)
import _interpreters
nuevo = _interpreters.create()
print(f"Nuevo subintérprete creado con ID: {nuevo}")
_interpreters.run_string(nuevo, "import sys; print(f'Versión: {sys.version[:6]}')")
_interpreters.destroy(nuevo)
print("Subintérprete destruido correctamente.")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin la API C para subintérpretes, sería imposible incrustar CPython en aplicaciones nativas con múltiples contextos de ejecución aislados. La API provee el control de ciclo de vida necesario para integraciones robustas.

### Solución y Beneficios

- Control total sobre la creación, configuración y destrucción de intérpretes.
- Posibilidad de elegir si cada subintérprete tiene su propio GIL.
- Base para implementar bindings de Python en motores de videojuegos, editores, etc.

## 4. Referencias

- https://docs.python.org/3/c-api/init.html#sub-interpreter-support
- https://peps.python.org/pep-0684/
- https://peps.python.org/pep-0734/
- https://docs.python.org/3/c-api/init_config.html
- https://github.com/python/cpython/blob/main/Python/pylifecycle.c

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Usa `_interpreters.create()` y `_interpreters.destroy()` para crear y destruir un subintérprete.
- Verifica que el subintérprete aparece en `_interpreters.list_all()` mientras está activo.

### Nivel Intermedio

- Ejecuta código en el subintérprete con `_interpreters.run_string()` y captura la salida.
- Maneja correctamente las excepciones lanzadas dentro del subintérprete.

### Nivel Avanzado

- Escribe una extensión C mínima que use `Py_NewInterpreterFromConfig` para crear un subintérprete con GIL propio.
- Demuestra que el subintérprete puede ejecutar código Python en un hilo separado sin bloquear el intérprete principal.

### Criterios de Éxito

- El subintérprete se crea y destruye sin errores ni fugas de memoria.
- Las excepciones en el subintérprete no afectan al intérprete principal.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El ciclo de vida del subintérprete está completamente controlado.

## 6. Resumen

- La API C para subintérpretes permite gestionar intérpretes Python desde código nativo.
- Cada subintérprete tiene su propio `PyInterpreterState` y `PyThreadState`.
- El control granular del ciclo de vida es esencial para aplicaciones embebidas robustas.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Qué diferencias hay entre gestionar subintérpretes desde C versus desde Python?
- ¿Cuándo usarías `Py_NewInterpreterFromConfig` en lugar de `multiprocessing`?
- ¿Qué recursos deben liberarse explícitamente al destruir un subintérprete?
