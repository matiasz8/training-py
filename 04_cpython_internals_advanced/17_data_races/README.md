# Condiciones de Carrera (Data Races)
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Una **condición de carrera** (data race) ocurre cuando dos o más hilos acceden concurrentemente a una misma variable o estructura de datos, al menos uno de ellos realiza una escritura, y no existe ningún mecanismo de sincronización que ordene los accesos. El resultado depende del orden de ejecución de los hilos, que es no determinista.

### Características Principales

- **No determinismo**: el mismo código puede producir resultados diferentes en distintas ejecuciones.
- **Difícil de reproducir**: las condiciones de carrera pueden no manifestarse en pruebas pero sí en producción.
- **Silenciosas**: a menudo no producen excepciones; simplemente generan datos incorrectos.
- **Más comunes en free-threading**: sin el GIL, más operaciones requieren sincronización explícita.

## 2. Aplicación Práctica

### Casos de Uso

1. **Contadores globales sin protección**: múltiples hilos incrementando el mismo entero.
2. **Operaciones check-then-act**: verificar una condición y actuar basándose en ella sin atomicidad.
3. **Caché compartida sin locks**: leer y escribir en un diccionario desde múltiples hilos.

### Ejemplo de Código

```python
import threading
import time

# DEMOSTRACIÓN DE CONDICIÓN DE CARRERA
contador_inseguro = 0

def incrementar_inseguro(n: int) -> None:
    global contador_inseguro
    for _ in range(n):
        # Estas tres operaciones NO son atómicas en free-threading
        temp = contador_inseguro
        time.sleep(0)  # forzar cambio de contexto
        contador_inseguro = temp + 1

NUM_HILOS = 10
NUM_INC = 1000
hilos = [threading.Thread(target=incrementar_inseguro, args=(NUM_INC,)) for _ in range(NUM_HILOS)]
for h in hilos:
    h.start()
for h in hilos:
    h.join()

esperado = NUM_HILOS * NUM_INC
print(f"Esperado: {esperado}")
print(f"Obtenido: {contador_inseguro}")
print(f"¿Correcto?: {contador_inseguro == esperado}")
print("(Probablemente incorrecto: esto es una condición de carrera)")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Las condiciones de carrera son uno de los bugs más peligrosos en software concurrente: pueden ser silenciosas, intermitentes y devastadoras en producción. Comprender su naturaleza es el primer paso para escribir código multihilo correcto.

### Solución y Beneficios

- Reconocimiento temprano de patrones propensos a condiciones de carrera.
- Aplicación sistemática de sincronización donde sea necesaria.
- Mayor confianza al revisar código concurrente escrito por otros.

## 4. Referencias

- https://docs.python.org/3/howto/free-threading-python.html
- https://peps.python.org/pep-0703/
- https://docs.python.org/3/library/threading.html
- https://github.com/google/sanitizers/wiki/ThreadSanitizerAlgorithm
- https://en.wikipedia.org/wiki/Race_condition

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Reproduce la condición de carrera del ejemplo con 10 hilos y verifica el resultado incorrecto.
- Corrige el código usando `threading.Lock` y verifica que ahora produce el resultado esperado.

### Nivel Intermedio

- Identifica un patrón "check-then-act" en el código de ejercicio y protégelo correctamente.
- Escribe un test que detecte la condición de carrera usando múltiples ejecuciones.

### Nivel Avanzado

- Investiga `ThreadSanitizer` (TSan) y configúralo para detectar data races en una extensión C.
- Documenta tres patrones comunes de condiciones de carrera y sus soluciones correspondientes.

### Criterios de Éxito

- La condición de carrera se reproduce y documenta con evidencia (valores incorrectos).
- La versión corregida produce siempre el resultado esperado en 100 ejecuciones.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El código incluye comentarios que explican por qué cada sección es o no es segura.

## 6. Resumen

- Las condiciones de carrera son accesos concurrentes no sincronizados a datos compartidos mutables.
- Son más frecuentes y graves en CPython con free-threading al eliminarse las garantías del GIL.
- Identificar y prevenir data races es una habilidad fundamental del desarrollo concurrente.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Cómo identificarías condiciones de carrera en código Python existente?
- ¿Qué herramientas o técnicas usarías para detectar data races en producción?
- ¿Cuál es el equilibrio correcto entre sincronización y rendimiento en tu proyecto?
