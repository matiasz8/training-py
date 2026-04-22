# Aislamiento de Memoria entre Subintérpretes
⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

El **aislamiento de memoria** entre subintérpretes garantiza que el estado Python (objetos, módulos, variables globales) de un subintérprete no sea directamente accesible ni modificable por otro. Aunque comparten la memoria del proceso a nivel de sistema operativo, el runtime de CPython mantiene barreras lógicas entre intérpretes.

### Características Principales

- **`sys.modules` independiente**: cada subintérprete importa y gestiona sus propios módulos.
- **Sin referencias cruzadas directas**: los objetos Python no pueden pasar directamente entre intérpretes.
- **Datos inmutables compartibles**: ciertos objetos inmutables pueden compartirse bajo condiciones específicas.
- **Objetos inmortales**: strings internos y constantes pueden compartirse de forma segura entre intérpretes.

## 2. Aplicación Práctica

### Casos de Uso

1. **Ejecución de código de usuario**: aislar scripts de usuarios para que no afecten el estado del servidor.
2. **Tests reproducibles**: cada test corre en un subintérprete con estado limpio.
3. **Multi-tenant**: aislar la lógica de diferentes clientes en el mismo proceso.

### Ejemplo de Código

```python
import _interpreters

def demostrar_aislamiento():
    # Definir una variable en el intérprete principal
    variable_global = "soy del principal"

    # Crear subintérprete
    interp = _interpreters.create()

    # Intentar acceder a variable_global desde el subintérprete
    codigo = """
try:
    print(variable_global)
except NameError:
    print("Aislamiento correcto: variable_global no existe aquí.")

    # Estado independiente
datos_locales = {"clave": "valor_del_subinterpretador"}
print(f"Estado local: {datos_locales}")
"""
    _interpreters.run_string(interp, codigo)
    _interpreters.destroy(interp)

    # Verificar que datos_locales no "contamina" el intérprete principal
    try:
        print(datos_locales)
    except NameError:
        print("El intérprete principal no fue afectado.")

demostrar_aislamiento()
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin aislamiento de memoria, un subintérprete defectuoso podría corromper el estado global del proceso, afectando a todos los demás subintérpretes y al intérprete principal. Esto sería catastrófico en sistemas multi-tenant o de alta disponibilidad.

### Solución y Beneficios

- Fallos en un subintérprete no afectan a los demás.
- El estado global de módulos no se contamina entre contextos de ejecución.
- Facilita la construcción de sistemas más resilientes y seguros.

## 4. Referencias

- https://peps.python.org/pep-0684/
- https://docs.python.org/3/c-api/init.html#sub-interpreter-support
- https://peps.python.org/pep-0554/
- https://docs.python.org/3/library/interpreters.html
- https://peps.python.org/pep-0683/

## 5. Tarea Práctica

Usa `exercise/exercise_01.py` como punto de entrada principal.

### Nivel Básico

- Crea una variable en el intérprete principal y verifica que no es accesible en un subintérprete.
- Modifica el estado en el subintérprete y confirma que el principal no se ve afectado.

### Nivel Intermedio

- Diseña un test que simule una falla en un subintérprete (excepción no manejada) y verifique que el principal continúa operando.
- Mide el coste de crear y destruir un subintérprete con estado limpio.

### Nivel Avanzado

- Implementa un sistema de ejecución multi-tenant donde cada "inquilino" tiene su propio subintérprete.
- Agrega límites de tiempo de ejecución y mecanismos de terminación forzada.

### Criterios de Éxito

- El aislamiento de variables se demuestra con tests explícitos.
- Una falla en el subintérprete no interrumpe el proceso principal.
- Los tests en `tests/test_basic.py` pasan correctamente.
- El código gestiona correctamente el ciclo de vida de cada subintérprete.

## 6. Resumen

- El aislamiento de memoria entre subintérpretes es una garantía fundamental del runtime de CPython.
- Cada subintérprete tiene su propio `sys.modules`, variables globales y estado del intérprete.
- Este aislamiento es la base para sistemas Python multi-tenant y resilientes.

## 7. Reflexión

Después de completar este tema, reflexiona sobre:

- ¿Qué tipo de datos sería seguro compartir entre subintérpretes y por qué?
- ¿Cómo verificarías en producción que el aislamiento se mantiene bajo carga?
- ¿Qué diferencias hay entre el aislamiento de subintérpretes y el de procesos separados?
