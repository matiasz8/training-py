# Introducción a los Subintérpretes
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Los **subintérpretes** son instancias independientes del intérprete de Python que coexisten dentro del mismo proceso. Cada subintérprete tiene su propio espacio de nombres global, módulos importados y estado del intérprete, pero comparten la memoria del proceso. Fueron estandarizados para uso general con PEP 554 y extendidos con PEP 734.

### Características Principales

- **Aislamiento de estado**: cada subintérprete tiene su propio `sys.modules`, `builtins` y variables globales.
- **Sin compartición implícita**: los objetos no se comparten automáticamente entre subintérpretes.
- **Paralelismo real**: con el GIL por intérprete (PEP 684), cada subintérprete puede ejecutar en paralelo.
- **Comunicación explícita**: los datos se intercambian a través de canales o colas dedicadas.

## 2. Aplicación Práctica

### Casos de Uso

1. **Aislamiento de plugins**: ejecutar código de terceros sin contaminar el estado global del proceso principal.
2. **Paralelismo sin hilos**: ejecutar tareas CPU-bound en subintérpretes separados.
3. **Sandboxing ligero**: restringir el acceso a módulos globales del proceso padre.

### Ejemplo de Código

```python
import _interpreters  # API experimental en Python 3.12+

def ejecutar_en_subinterpretador(codigo: str) -> None:
    """Ejecuta código en un subintérprete aislado."""
    interp_id = _interpreters.create()
    try:
        _interpreters.run_string(interp_id, codigo)
        print(f"Subintérprete {interp_id} ejecutó el código exitosamente.")
    finally:
        _interpreters.destroy(interp_id)

codigo = """
x = 42
print(f"Valor dentro del subintérprete: {x}")
"""
ejecutar_en_subinterpretador(codigo)

  # Verificar que 'x' no existe en el intérprete principal
try:
    print(x)
except NameError:
    print("'x' no existe en el intérprete principal: aislamiento correcto.")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Los hilos comparten todo el estado del intérprete, lo que dificulta el aislamiento de componentes. Los procesos separados consumen más memoria. Los subintérpretes ofrecen un punto intermedio: aislamiento dentro del mismo proceso.

### Solución y Beneficios

- Aislamiento más fuerte que los hilos sin el coste de memoria de los procesos.
- Base para el paralelismo real en CPython sin depender del multiprocessing.
- Arquitectura más segura para ejecutar código no confiable.

## 4. Referencias

- https://peps.python.org/pep-0554/
- https://peps.python.org/pep-0734/
- https://docs.python.org/3/library/interpreters.html
- https://docs.python.org/3/c-api/init.html#sub-interpreter-support
- https://docs.python.org/3/howto/free-threading-python.html

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Crea un subintérprete, ejecuta una operación simple y destruyelo correctamente.
- Verifica que las variables del subintérprete no son accesibles desde el intérprete principal.

### Nivel Intermedio

- Lanza dos subintérpretes en paralelo con `threading` y verifica el aislamiento entre ellos.
- Mide el tiempo de creación y destrucción de subintérpretes frente a procesos.

### Nivel Avanzado

- Implementa un sistema de plugins usando subintérpretes para aislar cada plugin.
- Gestiona errores en el subintérprete sin que afecten al proceso principal.

### Criterios de Éxito

- El subintérprete se crea, ejecuta código y se destruye sin errores.
- El aislamiento de estado entre intérpretes se demuestra con un test explícito.
- Los tests en `tests/test_basic.py` pasan correctamente.
- Los recursos del subintérprete se liberan siempre, incluso ante excepciones.

## 6. Resumen

- Los subintérpretes permiten aislamiento de estado dentro del mismo proceso Python.
- Son la base técnica para el paralelismo real sin dependencia del multiprocessing.
- PEP 554 y PEP 734 estandarizan su API para uso en código Python de alto nivel.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿En qué escenarios preferirías subintérpretes sobre hilos o procesos?
- ¿Cuáles son las limitaciones actuales del aislamiento entre subintérpretes?
- ¿Cómo usarías subintérpretes para mejorar la arquitectura de tu aplicación actual?
