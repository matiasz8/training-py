# Estrategias de Migración a Free-Threading
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Las **estrategias de migración a free-threading** son el conjunto de pasos, herramientas y patrones recomendados para adaptar código Python existente —escrito asumiendo la presencia del GIL— al modo de ejecución libre de GIL introducido en Python 3.13. Implica identificar dependencias del GIL, agregar sincronización explícita y validar la corrección.

### Características Principales

- **Auditoría de dependencias**: identificar extensiones C y paquetes que requieran el GIL.
- **Análisis de estado compartido**: localizar variables globales y estructuras mutables accedidas por múltiples hilos.
- **Pruebas de stress**: ejecutar tests bajo alta concurrencia para detectar condiciones de carrera latentes.
- **Migración incremental**: habilitar free-threading por módulo o componente, no todo a la vez.

## 2. Aplicación Práctica

### Casos de Uso

1. **Aplicaciones web con workers**: migrar un servidor Flask/Django para aprovechar paralelismo real.
2. **Pipelines de procesamiento de datos**: adaptar código numpy/pandas a free-threading gradualmente.
3. **Bibliotecas de propósito general**: preparar una librería para ser compatible con free-threading.

### Ejemplo de Código

```python
import sys
import sysconfig
import threading
from typing import Any

# Paso 1: Verificar el entorno de ejecución
def verificar_entorno() -> dict[str, Any]:
    return {
        "version": sys.version,
        "free_threading": bool(sysconfig.get_config_var("Py_GIL_DISABLED")),
        "gil_activo": sys._is_gil_enabled() if hasattr(sys, "_is_gil_enabled") else "N/A",
    }

# Paso 2: Identificar estado global mutable (patrón peligroso)
_cache_global: dict = {}  # ← requiere sincronización en free-threading
_lock_cache = threading.Lock()

def obtener_de_cache(clave: str) -> Any:
    """Patrón seguro: proteger caché compartida con Lock."""
    with _lock_cache:
        return _cache_global.get(clave)

def guardar_en_cache(clave: str, valor: Any) -> None:
    with _lock_cache:
        _cache_global[clave] = valor

# Paso 3: Test de stress para detectar condiciones de carrera
def test_stress_cache(num_hilos: int = 20, num_ops: int = 1000) -> bool:
    errores = []
    def operaciones():
        for i in range(num_ops):
            guardar_en_cache(f"clave_{i % 10}", i)
            obtener_de_cache(f"clave_{i % 10}")

    hilos = [threading.Thread(target=operaciones) for _ in range(num_hilos)]
    for h in hilos:
        h.start()
    for h in hilos:
        h.join()
    return len(errores) == 0

info = verificar_entorno()
print(f"Entorno: {info}")
ok = test_stress_cache()
print(f"Test de stress: {'PASÓ' if ok else 'FALLÓ'}")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Migrar a free-threading sin una estrategia puede introducir bugs sutiles de concurrencia que no aparecen en tests estándar pero sí en producción bajo carga. Una migración ordenada minimiza estos riesgos.

### Solución y Beneficios

- Proceso estructurado que reduce el riesgo de introducir condiciones de carrera.
- Identificación temprana de incompatibilidades con extensiones C.
- Validación objetiva de corrección a través de tests de stress y herramientas de análisis.

## 4. Referencias

- https://docs.python.org/3/howto/free-threading-python.html
- https://peps.python.org/pep-0703/
- https://docs.python.org/3/howto/free-threading-extensions.html
- https://github.com/python/cpython/blob/main/Doc/howto/free-threading-python.rst
- https://pypi.org/project/nogil/

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Audita el código de ejercicio e identifica todos los accesos a estado compartido mutable.
- Clasifica cada acceso como seguro, potencialmente inseguro o definitivamente inseguro.

### Nivel Intermedio

- Agrega sincronización explícita a los accesos identificados como inseguros.
- Ejecuta el código con 10 hilos y verifica que el resultado es correcto en 100 ejecuciones.

### Nivel Avanzado

- Diseña un plan de migración para un módulo Python hipotético con 3 componentes interdependientes.
- Implementa tests de stress automatizados que detecten condiciones de carrera.

### Criterios de Éxito

- Todos los accesos a estado compartido están documentados como seguros o protegidos.
- El test de stress produce resultados correctos en 100 ejecuciones consecutivas.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El plan de migración incluye criterios de éxito medibles para cada fase.

## 6. Resumen

- La migración a free-threading requiere auditar el estado compartido y agregar sincronización explícita.
- Una estrategia incremental reduce el riesgo de introducir bugs de concurrencia.
- Los tests de stress son la herramienta más efectiva para validar la corrección de la migración.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Cuál sería el mayor desafío de migrar tu proyecto actual a free-threading?
- ¿Cómo priorizarías qué partes del código migrar primero?
- ¿Qué métricas usarías para considerar que la migración fue exitosa?
