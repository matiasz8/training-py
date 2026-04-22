# Canales de Comunicación entre Subintérpretes
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Los **canales de comunicación** son el mecanismo oficial para intercambiar datos entre subintérpretes en CPython. Dado que los subintérpretes tienen memoria aislada, los datos deben transferirse a través de canales que serialicen o compartan objetos de forma segura. El módulo `_interpqueues` y la API de canales del módulo `interpreters` implementan esta funcionalidad.

### Características Principales

- **Colas por intérprete**: estructuras de datos que permiten el paso de mensajes entre subintérpretes.
- **Tipos soportados**: se transfieren tipos inmutables básicos (int, str, bytes, None) sin copia costosa.
- **Sincronización implícita**: las operaciones de envío y recepción son thread-safe.
- **Sin referencias directas**: se prohíbe pasar objetos mutables complejos sin serialización.

## 2. Aplicación Práctica

### Casos de Uso

1. **Pipeline de procesamiento**: un subintérprete produce datos y otro los consume a través de una cola.
2. **Resultados de cálculos**: recoger el resultado de tareas ejecutadas en subintérpretes aislados.
3. **Coordinación de estado**: comunicar eventos o señales entre subintérpretes sin compartir memoria.

### Ejemplo de Código

```python
import _interpreters
import _interpqueues as queues

  # Crear una cola compartida entre intérpretes
cola_id = queues.create()

  # Subintérprete productor
interp_productor = _interpreters.create()
codigo_productor = f"""
import _interpqueues as q
cola = {cola_id}
for i in range(5):
    q.put(cola, i * i)
print("Productor: 5 cuadrados enviados.")
"""

  # Ejecutar productor
_interpreters.run_string(interp_productor, codigo_productor)

  # Consumir resultados desde el intérprete principal
resultados = []
for _ in range(5):
    valor, _ = queues.get(cola_id)
    resultados.append(valor)

print(f"Resultados recibidos: {resultados}")

_interpreters.destroy(interp_productor)
queues.destroy(cola_id)
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin canales de comunicación, los subintérpretes serían compartimentos estancos inútiles para la computación distribuida dentro del proceso. Los canales permiten coordinar trabajo y recoger resultados de forma segura.

### Solución y Beneficios

- Comunicación segura entre intérpretes sin romper el aislamiento de memoria.
- Paso de datos sin serialización costosa para tipos básicos.
- Base para implementar patrones productor-consumidor y pipelines intra-proceso.

## 4. Referencias

- https://peps.python.org/pep-0734/
- https://docs.python.org/3/library/interpreters.html
- https://peps.python.org/pep-0554/
- https://docs.python.org/3/c-api/init.html
- https://github.com/python/cpython/blob/main/Modules/_interpreters_common.h

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Crea una cola y envía 5 enteros desde un subintérprete al intérprete principal.
- Verifica que los valores recibidos coinciden con los enviados.

### Nivel Intermedio

- Implementa un patrón productor-consumidor con dos subintérpretes y una cola compartida.
- Maneja el caso en que la cola está vacía al intentar leer.

### Nivel Avanzado

- Implementa un pipeline de tres etapas: ingesta → transformación → salida, cada una en su subintérprete.
- Mide el throughput del pipeline y compáralo con la versión de un solo intérprete.

### Criterios de Éxito

- Los datos se transfieren correctamente entre subintérpretes a través de la cola.
- No se producen condiciones de carrera ni bloqueos (deadlocks).
- Los tests en `tests/test_basic.py` pasan correctamente.
- Los recursos (colas e intérpretes) se liberan correctamente al finalizar.

## 6. Resumen

- Los canales de comunicación permiten el paso de mensajes entre subintérpretes aislados.
- Solo se soportan tipos básicos inmutables para garantizar la seguridad del aislamiento.
- Son la base para patrones de concurrencia intra-proceso como pipelines y productor-consumidor.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Qué patrones de comunicación serían más útiles en tu aplicación actual?
- ¿Cómo manejarías la comunicación de objetos complejos (por ejemplo, DataFrames) entre subintérpretes?
- ¿En qué difiere este modelo del paso de mensajes en sistemas distribuidos?
