# Conteo de Referencias Sesgado (Biased Reference Counting)
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

El **conteo de referencias sesgado** es una optimización del mecanismo de gestión de memoria de CPython diseñada para el modo sin GIL. Cada objeto tiene un contador de referencias "local" (propiedad del hilo que lo creó) y un contador "compartido" (para accesos de otros hilos). Esto reduce la sincronización necesaria cuando un objeto solo lo usa su hilo propietario.

### Características Principales

- **Propiedad por hilo**: el hilo creador actualiza su contador local sin necesidad de operaciones atómicas.
- **Contador compartido**: los demás hilos modifican un campo separado con operaciones atómicas.
- **Reducción de contención**: minimiza el tráfico de caché entre núcleos del procesador.
- **Compatibilidad**: funciona de forma transparente con el resto del runtime de CPython.

## 2. Aplicación Práctica

### Casos de Uso

1. **Objetos de larga vida en un solo hilo**: strings o tuplas creadas y consumidas por el mismo hilo se benefician directamente.
2. **Caches locales**: estructuras de datos que rara vez se comparten entre hilos.
3. **Benchmarks de rendimiento**: medición del impacto en aplicaciones CPU-bound sin GIL.

### Ejemplo de Código

```python
import sys
import threading

def inspect_refcount():
    # En CPython libre de GIL, el refcount observado puede diferir
    # según el hilo que realice la consulta
    obj = [1, 2, 3]
    print(f"Refcount en hilo creador: {sys.getrefcount(obj)}")

    def other_thread():
        # Al compartir el objeto, se incrementa el contador compartido
        ref = obj
        print(f"Refcount desde otro hilo: {sys.getrefcount(ref)}")

    t = threading.Thread(target=other_thread)
    t.start()
    t.join()

inspect_refcount()
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin el conteo sesgado, cada incremento o decremento del contador de referencias requeriría una operación atómica costosa visible para todos los núcleos. Esto provocaría una degradación masiva del rendimiento en aplicaciones con muchos hilos.

### Solución y Beneficios

- Operaciones locales sin coste de sincronización para el hilo propietario.
- Escalabilidad mejorada en sistemas multinúcleo.
- Base técnica para el modo libre de GIL introducido en Python 3.13.

## 4. Referencias

- https://docs.python.org/3/whatsnew/3.13.html
- https://peps.python.org/pep-0703/
- https://github.com/python/cpython/blob/main/InternalDocs/refcounting.md
- https://docs.python.org/3/howto/free-threading-python.html
- https://vstinner.github.io/python-free-threading.html

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Crea un objeto en un hilo y observa su `sys.getrefcount` desde el mismo hilo y desde otro hilo.
- Documenta las diferencias observadas.

### Nivel Intermedio

- Diseña un experimento para medir el coste de compartir un objeto entre N hilos.
- Compara el rendimiento entre objetos compartidos y objetos locales por hilo.

### Nivel Avanzado

- Investiga el código fuente de CPython (`Objects/object.c`) para ubicar la implementación del conteo sesgado.
- Escribe un test que verifique que el refcount global es la suma del local y el compartido.

### Criterios de Éxito

- El código ejecuta sin errores en Python 3.13+ con free-threading habilitado.
- Se observa y documenta la diferencia entre contadores local y compartido.
- Los tests en `tests/test_basic.py` pasan correctamente.
- La implementación incluye comentarios que explican cada paso.

## 6. Resumen

- El conteo de referencias sesgado separa los accesos locales de los compartidos para reducir sincronización.
- Es una pieza clave del modo libre de GIL en CPython 3.13+.
- Comprender este mecanismo ayuda a escribir código Python más eficiente en entornos multihilo.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Cómo cambia tu forma de pensar sobre la propiedad de objetos en Python multihilo?
- ¿En qué situaciones el conteo sesgado no ayuda (o puede perjudicar)?
- ¿Cómo aplicarías este conocimiento para optimizar una aplicación real?
