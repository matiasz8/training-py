# Testing de Thread Safety
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

El **testing de thread safety** es el conjunto de técnicas y herramientas para verificar que el código Python se comporta correctamente cuando múltiples hilos lo ejecutan simultáneamente. Incluye tests de stress, pruebas de invariantes bajo concurrencia, uso de herramientas de detección de data races y verificación de resultados deterministas.

### Características Principales

- **Tests de stress**: ejecutar operaciones concurrentes masivas y verificar invariantes.
- **Barrier synchronization**: usar `threading.Barrier` para sincronizar el inicio simultáneo de hilos.
- **Detección de data races**: herramientas como ThreadSanitizer o pruebas estadísticas.
- **Reproducibilidad**: aislar tests de concurrencia para hacerlos repetibles.

## 2. Aplicación Práctica

### Casos de Uso

1. **Validar estructuras de datos compartidas**: verificar que una caché thread-safe funciona bajo carga.
2. **Tests de regresión de concurrencia**: detectar condiciones de carrera introducidas por cambios.
3. **Benchmarking de corrección**: medir la tasa de éxito de operaciones concurrentes.

### Ejemplo de Código

```python
import threading
import unittest
from typing import Callable

class TestThreadSafety(unittest.TestCase):
    """Suite de tests para verificar thread safety."""

    def ejecutar_concurrentemente(
        self,
        funcion: Callable,
        num_hilos: int = 20,
        num_repeticiones: int = 100,
    ) -> list:
        """Ejecuta una función en múltiples hilos simultáneamente."""
        resultados = []
        errores = []
        barrera = threading.Barrier(num_hilos)
        lock = threading.Lock()

        def worker():
            barrera.wait()  # todos los hilos empiezan al mismo tiempo
            for _ in range(num_repeticiones):
                try:
                    resultado = funcion()
                    with lock:
                        resultados.append(resultado)
                except Exception as e:
                    with lock:
                        errores.append(e)

        hilos = [threading.Thread(target=worker) for _ in range(num_hilos)]
        for h in hilos:
            h.start()
        for h in hilos:
            h.join()

        self.assertEqual(errores, [], f"Errores concurrentes: {errores}")
        return resultados

    def test_contador_thread_safe(self):
        contador = 0
        lock = threading.Lock()

        def incrementar():
            nonlocal contador
            with lock:
                contador += 1
            return True

        self.ejecutar_concurrentemente(incrementar, num_hilos=10, num_repeticiones=100)
        self.assertEqual(contador, 1000)

if __name__ == "__main__":
    unittest.main(verbosity=2)
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Las condiciones de carrera son no deterministas y pueden no manifestarse en ejecuciones simples. Sin tests de concurrencia específicos, los bugs de thread safety solo se descubren en producción bajo alta carga, cuando el impacto es máximo.

### Solución y Beneficios

- Detección temprana de condiciones de carrera en el ciclo de desarrollo.
- Confianza demostrable en la corrección del código concurrente.
- Base reutilizable de utilidades de testing para todos los componentes del proyecto.

## 4. Referencias

- https://docs.python.org/3/library/threading.html#threading.Barrier
- https://docs.python.org/3/library/unittest.html
- https://docs.python.org/3/howto/free-threading-python.html
- https://github.com/google/sanitizers/wiki/ThreadSanitizerCppManual
- https://peps.python.org/pep-0703/

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Escribe un test que verifique un contador thread-safe con 10 hilos y 100 incrementos cada uno.
- Verifica que el resultado final es siempre `10 * 100 = 1000`.

### Nivel Intermedio

- Implementa la clase `ejecutar_concurrentemente` del ejemplo y úsala para testear la cola del ejercicio.
- Usa `threading.Barrier` para garantizar el inicio simultáneo de todos los hilos.

### Nivel Avanzado

- Diseña una suite de tests que cubra: invariantes de estado, ausencia de deadlocks y determinismo de resultados.
- Integra los tests con `pytest` y configura un umbral de confianza estadístico.

### Criterios de Éxito

- Los tests detectan correctamente la condición insegura (sin lock) y la condición segura (con lock).
- Los tests son repetibles y producen el mismo resultado en 100 ejecuciones consecutivas.
- Los tests en `tests/test_basic.py` pasan correctamente.
- La suite de tests incluye al menos tres invariantes verificables bajo concurrencia.

## 6. Resumen

- El testing de thread safety requiere técnicas específicas: barriers, stress tests y verificación de invariantes.
- Las condiciones de carrera son no deterministas; los tests deben ejecutarse muchas veces para tener confianza.
- Una buena suite de tests de concurrencia es tan valiosa como los tests unitarios estándar.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Qué componentes de tu proyecto actual carecen de tests de thread safety?
- ¿Cómo integrarías tests de concurrencia en tu pipeline de CI/CD?
- ¿Cuál es el número mínimo de repeticiones necesarias para tener confianza estadística en un test de concurrencia?
