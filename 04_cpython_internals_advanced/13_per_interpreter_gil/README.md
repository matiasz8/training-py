# GIL por Intérprete (Per-Interpreter GIL)
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

El **GIL por intérprete** (per-interpreter GIL), introducido por PEP 684, permite que cada subintérprete tenga su propio Global Interpreter Lock independiente. Esto significa que dos subintérpretes en hilos distintos pueden ejecutar bytecode Python en paralelo, superando la limitación histórica del GIL global compartido.

### Características Principales

- **GIL independiente**: cada subintérprete gestiona su propio bloqueo sin interferir con los demás.
- **Paralelismo real en Python puro**: sin necesidad de extensiones C ni multiprocessing.
- **Estado aislado**: el GIL propio refuerza el aislamiento de estado entre subintérpretes.
- **Configuración explícita**: se activa al crear el subintérprete con `own_gil=True`.

## 2. Aplicación Práctica

### Casos de Uso

1. **Cálculos CPU-bound paralelos**: ejecutar algoritmos numéricos en subintérpretes con GIL propio.
2. **Servidores de aplicaciones**: atender múltiples peticiones en subintérpretes paralelos.
3. **Benchmarking de paralelismo**: medir ganancias reales frente al modelo de hilos tradicional.

### Ejemplo de Código

```python
import _interpreters
import threading
import time

def tarea_en_subinterpretador(interp_id: int, nombre: str) -> None:
    codigo = f"""
import time
inicio = time.perf_counter()
resultado = sum(i * i for i in range(500_000))
duracion = time.perf_counter() - inicio
print(f'{nombre}: resultado={resultado}, tiempo={duracion:.3f}s')
"""
    _interpreters.run_string(interp_id, codigo)

  # Crear dos subintérpretes con GIL propio (Python 3.12+)
interp1 = _interpreters.create()
interp2 = _interpreters.create()

inicio = time.perf_counter()
t1 = threading.Thread(target=tarea_en_subinterpretador, args=(interp1, "Interp-A"))
t2 = threading.Thread(target=tarea_en_subinterpretador, args=(interp2, "Interp-B"))
t1.start(); t2.start()
t1.join(); t2.join()

print(f"Tiempo total paralelo: {time.perf_counter() - inicio:.3f}s")
_interpreters.destroy(interp1)
_interpreters.destroy(interp2)
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

El GIL global impedía que hilos Python ejecutaran bytecode simultáneamente. El GIL por intérprete elimina este cuello de botella a nivel de subintérprete, habilitando verdadero paralelismo para código CPU-bound sin abandoner el modelo de memoria de CPython.

### Solución y Beneficios

- Escalabilidad en tareas CPU-bound sin migrar a multiprocessing.
- Mejor uso de sistemas multinúcleo con código Python puro.
- Compatibilidad gradual: los subintérpretes sin `own_gil` siguen funcionando como antes.

## 4. Referencias

- https://peps.python.org/pep-0684/
- https://docs.python.org/3/library/interpreters.html
- https://peps.python.org/pep-0703/
- https://docs.python.org/3/c-api/init.html#sub-interpreter-support
- https://docs.python.org/3/howto/free-threading-python.html

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Crea dos subintérpretes y ejecuta una tarea CPU-bound en cada uno secuencialmente.
- Mide el tiempo total de ejecución secuencial.

### Nivel Intermedio

- Ejecuta las mismas tareas en paralelo usando hilos y compara el tiempo con la ejecución secuencial.
- Verifica que el speedup es cercano a 2x en un sistema con al menos 2 núcleos.

### Nivel Avanzado

- Implementa un benchmark que compare el rendimiento con 1, 2, 4 y 8 subintérpretes paralelos.
- Documenta el speedup observado y las limitaciones encontradas.

### Criterios de Éxito

- La ejecución paralela es más rápida que la secuencial en tareas CPU-bound.
- El aislamiento del GIL se demuestra con métricas de tiempo.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El análisis de resultados incluye al menos dos conclusiones respaldadas por datos.

## 6. Resumen

- PEP 684 introduce el GIL por intérprete, habilitando paralelismo real en Python puro.
- Cada subintérprete gestiona su propio GIL de forma independiente.
- Es un paso fundamental hacia un CPython completamente libre de GIL global.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Qué escenarios de tu trabajo actual se beneficiarían del GIL por intérprete?
- ¿Cuáles son las diferencias prácticas entre per-interpreter GIL y free-threading (PEP 703)?
- ¿Cómo afecta el GIL por intérprete al diseño de la arquitectura de tu aplicación?
