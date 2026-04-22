# API Python para Subintérpretes
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

La **API Python para subintérpretes** es la interfaz de alto nivel que expone el módulo `interpreters` (y previamente `_interpreters`) para crear y gestionar subintérpretes directamente desde código Python. Estandarizada por PEP 734, ofrece una forma ergonómica de aprovechar el aislamiento de subintérpretes sin necesidad de escribir extensiones en C.

### Características Principales

- **`interpreters.create()`**: crea un nuevo subintérprete y devuelve un objeto `Interpreter`.
- **`interp.run()`**: ejecuta una función o cadena de código en el subintérprete.
- **`interp.close()`**: destruye el subintérprete y libera sus recursos.
- **Canales de comunicación**: integración con `interpreters.channel_create()` para pasar datos.

## 2. Aplicación Práctica

### Casos de Uso

1. **Paralelismo basado en subintérpretes**: ejecutar funciones Python en paralelo sin compartir estado.
2. **Entornos de evaluación seguros**: ejecutar scripts de usuario en un contexto aislado.
3. **Testing de módulos**: importar un módulo en un subintérprete limpio para pruebas reproducibles.

### Ejemplo de Código

```python
import _interpreters
import threading

def ejecutar_tarea(interp_id: int, codigo: str) -> None:
    """Ejecuta código en el subintérprete dado desde un hilo separado."""
    _interpreters.run_string(interp_id, codigo)

  # Crear dos subintérpretes aislados
interp1 = _interpreters.create()
interp2 = _interpreters.create()

codigo1 = "resultado = sum(range(1_000_000)); print(f'Interp1: {resultado}')"
codigo2 = "resultado = sum(range(2_000_000)); print(f'Interp2: {resultado}')"

  # Ejecutar en paralelo usando hilos
t1 = threading.Thread(target=ejecutar_tarea, args=(interp1, codigo1))
t2 = threading.Thread(target=ejecutar_tarea, args=(interp2, codigo2))

t1.start(); t2.start()
t1.join(); t2.join()

_interpreters.destroy(interp1)
_interpreters.destroy(interp2)
print("Ambos subintérpretes completaron su trabajo y fueron destruidos.")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Antes de la API Python para subintérpretes, el aislamiento dentro del proceso solo era alcanzable escribiendo código C o usando `multiprocessing` con el coste adicional de serialización. Esta API cierra la brecha.

### Solución y Beneficios

- Código Python puro para gestionar subintérpretes, sin extensiones C.
- Aislamiento de estado sin la sobrecarga de memoria de los procesos separados.
- Paralelismo real disponible a través de la API de alto nivel de Python 3.13+.

## 4. Referencias

- https://peps.python.org/pep-0734/
- https://docs.python.org/3/library/interpreters.html
- https://peps.python.org/pep-0554/
- https://docs.python.org/3/howto/free-threading-python.html
- https://github.com/python/cpython/blob/main/Lib/interpreters/__init__.py

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Crea dos subintérpretes y ejecuta código diferente en cada uno.
- Verifica que las variables definidas en uno no son accesibles desde el otro.

### Nivel Intermedio

- Ejecuta los dos subintérpretes en hilos paralelos y mide el tiempo total vs ejecución secuencial.
- Implementa manejo de errores que capture excepciones del subintérprete correctamente.

### Nivel Avanzado

- Usa canales de comunicación para pasar resultados entre subintérpretes.
- Implementa un pool reutilizable de subintérpretes para ejecutar tareas.

### Criterios de Éxito

- Los subintérpretes se crean, ejecutan y destruyen correctamente.
- El aislamiento entre subintérpretes se verifica con un test explícito.
- Los tests en `tests/test_basic.py` pasan correctamente.
- Los recursos se liberan siempre mediante gestión de contexto o `try/finally`.

## 6. Resumen

- La API Python de subintérpretes (PEP 734) hace accesible el aislamiento de estado desde Python puro.
- Permite paralelismo real sin `multiprocessing` ni código C.
- Es una de las características más importantes de CPython para aplicaciones concurrentes modernas.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿En qué situaciones la API Python es suficiente versus necesitar la API C?
- ¿Qué patrones de diseño facilitan el trabajo con subintérpretes?
- ¿Cómo impacta el uso de subintérpretes en la depuración y el perfilado?
