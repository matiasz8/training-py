# Compatibilidad de Extensiones C con Free-Threading
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

La **compatibilidad de extensiones C** con el modo libre de GIL describe los requisitos y cambios necesarios para que módulos de extensión escritos en C (como NumPy, Cython o módulos propios) funcionen correctamente cuando CPython ejecuta sin el GIL. Una extensión incompatible puede provocar condiciones de carrera o fallos al cargar.

### Características Principales

- **Marca de compatibilidad**: las extensiones deben declarar `Py_mod_gil = Py_MOD_GIL_NOT_USED` para indicar que son seguras sin GIL.
- **Revisión de estado global**: cualquier variable global mutable en C debe protegerse con mutexes.
- **API estable**: el uso de `Py_LIMITED_API` reduce la superficie de cambios necesarios.
- **Modo degradado**: CPython puede re-habilitar el GIL si se carga una extensión incompatible.

## 2. Aplicación Práctica

### Casos de Uso

1. **Portabilidad de módulos propios**: adaptar extensiones C internas para free-threading.
2. **Auditoría de dependencias**: verificar qué paquetes de terceros son compatibles.
3. **Integración continua**: ejecutar tests en modo libre para detectar regresiones tempranas.

### Ejemplo de Código

```python
import sys
import sysconfig

  # Verificar si CPython fue compilado con soporte free-threading
def es_free_threading() -> bool:
    return bool(sysconfig.get_config_var("Py_GIL_DISABLED"))

  # Listar extensiones cargadas y verificar compatibilidad
def auditar_extensiones():
    for nombre, modulo in sys.modules.items():
        archivo = getattr(modulo, "__file__", "")
        if archivo and archivo.endswith((".so", ".pyd")):
            gil_requerido = not getattr(modulo, "__free_threaded__", False)
            estado = "INCOMPATIBLE" if gil_requerido else "compatible"
            print(f"{nombre:30s} -> {estado}")

if es_free_threading():
    print("Modo free-threading activo")
    auditar_extensiones()
else:
    print("Modo GIL activo")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Una sola extensión C incompatible puede forzar a CPython a re-habilitar el GIL silenciosamente, anulando todos los beneficios del modo libre sin advertencia explícita al desarrollador.

### Solución y Beneficios

- Proceso claro de auditoría y migración para extensiones existentes.
- Herramientas para detectar incompatibilidades antes de llegar a producción.
- Ecosistema más robusto a medida que los paquetes populares adoptan la marca de compatibilidad.

## 4. Referencias

- https://docs.python.org/3/howto/free-threading-extensions.html
- https://peps.python.org/pep-0703/
- https://docs.python.org/3/c-api/module.html
- https://docs.python.org/3/howto/free-threading-python.html
- https://cython.readthedocs.io/en/latest/src/userguide/nogil.html

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Verifica si tu instalación de CPython soporta free-threading con `sysconfig`.
- Lista las extensiones cargadas en un entorno virtual e identifica las potencialmente incompatibles.

### Nivel Intermedio

- Compila una extensión C mínima con la marca `Py_MOD_GIL_NOT_USED` y verifica que carga sin re-habilitar el GIL.
- Diseña un test que falle si el GIL se reactiva inesperadamente.

### Nivel Avanzado

- Toma una extensión C existente con estado global mutable y refactorízala para ser segura sin GIL.
- Documenta cada cambio realizado y su justificación.

### Criterios de Éxito

- Se identifica correctamente si la extensión es compatible con free-threading.
- La extensión compilada no reactiva el GIL al cargarse.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El código incluye manejo de errores para fallas de compilación o importación.

## 6. Resumen

- Las extensiones C deben declarar compatibilidad explícita para funcionar en modo libre de GIL.
- Una extensión incompatible degrada silenciosamente el rendimiento al re-habilitar el GIL.
- Auditar las dependencias es un paso crítico antes de migrar al modo free-threading.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Cuáles de tus dependencias actuales serían el mayor obstáculo para migrar a free-threading?
- ¿Qué estrategia usarías para migrar gradualmente un proyecto grande?
- ¿Cómo comunicarías a tu equipo la necesidad de auditar extensiones C?
