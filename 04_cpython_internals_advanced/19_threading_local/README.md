# Threading Local
⏱️ **Tiempo estimado: 1 hora**

## 1. Definición

**`threading.local`** es una clase del módulo `threading` que permite crear variables con almacenamiento local por hilo. Cada hilo tiene su propia copia independiente de los atributos definidos en un objeto `threading.local`, por lo que no hay necesidad de sincronización para leer o escribir esos valores.

### Características Principales

- **Aislamiento automático**: cada hilo accede a su propia copia de la variable sin interferencias.
- **API simple**: se comporta como un objeto normal; los atributos se asignan directamente.
- **Inicialización perezosa**: los valores se crean la primera vez que cada hilo los asigna.
- **Sin sincronización**: al ser privados por hilo, no requieren locks ni operaciones atómicas.

## 2. Aplicación Práctica

### Casos de Uso

1. **Conexiones a base de datos**: cada hilo mantiene su propia conexión sin compartirla.
2. **Contexto de solicitud HTTP**: almacenar el usuario autenticado o el ID de petición por hilo.
3. **Buffers temporales**: acumuladores por hilo que se agregan al final sin sincronización.

### Ejemplo de Código

```python
import threading
import time

# Datos locales por hilo: cada hilo tiene su propio contexto
contexto = threading.local()

def procesar_solicitud(usuario: str, duracion: float) -> None:
    # Cada hilo inicializa su propio contexto
    contexto.usuario = usuario
    contexto.inicio = time.perf_counter()

    time.sleep(duracion)  # simular trabajo

    tiempo_total = time.perf_counter() - contexto.inicio
    print(f"Hilo {threading.current_thread().name}: "
          f"usuario={contexto.usuario}, tiempo={tiempo_total:.3f}s")

usuarios = [("alice", 0.1), ("bob", 0.05), ("carol", 0.15)]
hilos = [
    threading.Thread(
        target=procesar_solicitud,
        args=datos,
        name=f"Worker-{i}"
    )
    for i, datos in enumerate(usuarios)
]

for h in hilos:
    h.start()
for h in hilos:
    h.join()

# El hilo principal no tiene acceso a los datos de otros hilos
print(f"Hilo principal tiene contexto.usuario: {hasattr(contexto, 'usuario')}")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Pasar el contexto explícitamente a través de cada función en una cadena de llamadas es tedioso y propenso a errores. `threading.local` ofrece una forma elegante de mantener estado por hilo accesible desde cualquier punto de la pila de llamadas.

### Solución y Beneficios

- Eliminación de la necesidad de pasar parámetros de contexto a través de múltiples capas.
- Cero overhead de sincronización para datos que naturalmente pertenecen a un solo hilo.
- Patrón ampliamente usado en frameworks web como Flask, Django y SQLAlchemy.

## 4. Referencias

- https://docs.python.org/3/library/threading.html#thread-local-data
- https://docs.python.org/3/howto/free-threading-python.html
- https://peps.python.org/pep-0703/
- https://flask.palletsprojects.com/en/latest/reqcontext/
- https://docs.sqlalchemy.org/en/20/orm/session_basics.html

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Crea un objeto `threading.local` y asigna valores diferentes desde tres hilos.
- Verifica que cada hilo solo ve sus propios valores.

### Nivel Intermedio

- Implementa un "contexto de solicitud" con `threading.local` que almacene el ID de petición y el usuario.
- Simula un servidor que procesa 10 solicitudes concurrentes y registra el contexto de cada una.

### Nivel Avanzado

- Implementa una subclase de `threading.local` con valores por defecto y métodos de utilidad.
- Evalúa el impacto en memoria de mantener datos locales en un pool de 100 hilos.

### Criterios de Éxito

- Cada hilo accede exclusivamente a sus propios datos locales, verificado con assertions.
- No se usan locks para proteger los datos de `threading.local`.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El código incluye al menos un caso de uso realista de contexto de solicitud.

## 6. Resumen

- `threading.local` provee almacenamiento aislado por hilo sin necesidad de sincronización.
- Es el patrón estándar para datos de contexto en aplicaciones web y de servidor.
- Funciona igual en modo con GIL y en modo free-threading, haciendo el código portable.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Qué datos de tu aplicación actual serían buenos candidatos para `threading.local`?
- ¿Cuándo `threading.local` es una mejor opción que pasar el contexto como argumento?
- ¿Cómo interactúa `threading.local` con `contextvars.ContextVar` de Python 3.7+?
