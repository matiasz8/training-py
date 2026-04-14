# Basic Type Hints

⏱️ **Tiempo estimado: 2-3 horas**

## 1. 📚 Definición

Los **type hints** (anotaciones de tipo) fueron introducidos en Python 3.5 mediante PEP 484, proporcionando una sintaxis estándar para anotar tipos esperados de variables, parámetros de funciones y valores de retorno. A diferencia de lenguajes estáticamente tipados, Python no aplica estas anotaciones en tiempo de ejecución (runtime) por defecto - funcionan principalmente como documentación ejecutable y permiten que herramientas externas como **mypy**, **pyright** o **basedpyright** realicen análisis estático de tipos.

La sintaxis básica utiliza el operador `:` para anotar variables y parámetros, y `->` para anotar el tipo de retorno de funciones. Python 3.9+ simplificó el sistema permitiendo usar tipos nativos como `list`, `dict`, `tuple` directamente (antes se requería importar desde `typing`). Python 3.10 introdujo el operador `|` para uniones de tipos, reemplazando `Union`. Python 3.11 mejoró el rendimiento del módulo `typing`, y Python 3.12 introdujo la sintaxis de parámetros de tipo genérico con corchetes angulares.

Los type hints no afectan la semántica del código Python - un programa con type hints incorrectos se ejecuta igual que uno sin ellos. Su valor radica en:
1. **Detección temprana de errores**: IDEs y type checkers detectan bugs antes de ejecutar
2. **Documentación viva**: Los tipos son más precisos que comentarios y se mantienen sincronizados con el código
3. **Mejor autocompletado**: Los editores ofrecen sugerencias más precisas
4. **Refactoring seguro**: Cambios de tipo se propagan automáticamente en el análisis estático

El módulo `typing` proporciona tipos especiales como `Optional`, `Union`, `List`, `Dict`, `Tuple`, `Callable`, `TypeVar`, `Generic`, `Protocol`, entre otros, que permiten expresar relaciones de tipos complejas que el sistema de tipos nativo de Python no puede representar directamente.

## 2. 💡 Aplicación Práctica

### Casos de Uso

1. **Desarrollo de APIs y librerías públicas**: Una librería como `requests` o `httpx` usa type hints para que los usuarios vean qué tipos acepta cada parámetro y qué retorna cada función, reduciendo errores de integración y mejorando la experiencia del desarrollador en IDEs modernos.

2. **Aplicaciones empresariales con múltiples desarrolladores**: En equipos grandes, los type hints previenen errores de comunicación sobre contratos de funciones. Si una función espera `List[User]` y otra pasa `List[str]`, el type checker lo detecta antes del code review.

3. **Data pipelines y procesamiento de datos**: Al procesar datos con pandas, numpy o polars, los type hints aseguran que las transformaciones reciban el tipo correcto de DataFrame o Series, evitando errores runtime difíciles de debuggear en pipelines complejos.

### Código Ejemplo

```python
from typing import Optional, List, Dict, Callable

# Tipos básicos
def greet(name: str, age: int) -> str:
    """Saluda a una persona con su nombre y edad."""
    return f"Hola {name}, tienes {age} años"

# Optional indica que puede ser None
def find_user(user_id: int) -> Optional[str]:
    """Busca un usuario por ID, retorna None si no existe."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

# Colecciones genéricas
def process_scores(scores: List[float]) -> Dict[str, float]:
    """Procesa una lista de puntajes y retorna estadísticas."""
    return {
        "mean": sum(scores) / len(scores),
        "max": max(scores),
        "min": min(scores)
    }

# Funciones como parámetros (callbacks)
def apply_operation(numbers: List[int], 
                   operation: Callable[[int], int]) -> List[int]:
    """Aplica una operación a cada número de la lista."""
    return [operation(n) for n in numbers]

# Ejemplo de uso
result = apply_operation([1, 2, 3], lambda x: x * 2)
print(result)  # [2, 4, 6]

# Python 3.10+ - Unión de tipos con |
def parse_id(value: int | str) -> int:
    """Convierte un ID a entero desde int o str."""
    if isinstance(value, str):
        return int(value)
    return value

# Python 3.9+ - tipos nativos sin typing
def merge_lists(list1: list[int], list2: list[int]) -> list[int]:
    """Fusiona dos listas de enteros."""
    return list1 + list2
```

## 3. 🤔 ¿Por Qué Es Importante?

**Problema que resuelve**: Python es dinámicamente tipado, lo que otorga flexibilidad pero introduce riesgos. Un bug común es pasar el tipo incorrecto a una función y solo descubrirlo en producción cuando falla con datos inesperados. Por ejemplo, pasar `"123"` a una función que espera `int` puede fallar silenciosamente si usa operaciones matemáticas.

**Historia**: Antes de Python 3.5, los tipos se documentaban en docstrings o comentarios, pero estos no eran verificables automáticamente y se desincronizaban fácilmente. Guido van Rossum, creador de Python, trabajó en Dropbox donde vio grandes codebases Python sufrir de bugs de tipos. Esto motivó PEP 484 (2014), inspirado en lenguajes gradualmente tipados como TypeScript y el type checker mypy de Jukka Lehtosalo.

**Solución**: Los type hints introducen "tipado gradual opcional" - puedes anotar progresivamente partes críticas del código sin reescribir todo. Los type checkers como mypy analizan estáticamente y reportan inconsistencias antes de la ejecución. IDEs como VS Code con Pylance usan estas anotaciones para ofrecer autocompletado inteligente, detección de errores en vivo y refactoring seguro.

**Adopción**: Proyectos grandes como FastAPI, Pydantic, SQLModel hacen uso extensivo de type hints, convirtiéndolos en ciudadanos de primera clase. FastAPI usa type hints para validación automática de requests, generación de documentación OpenAPI y serialización. Pydantic v2 genera validadores optimizados en Rust basándose en los type hints.

## 4. 🔗 Referencias

- [Documentación oficial de Python - typing](https://docs.python.org/3/library/typing.html)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
- [PEP 526 - Syntax for Variable Annotations](https://peps.python.org/pep-0526/)
- [mypy - Optional Static Typing](http://mypy-lang.org/)
- Ver: `references/links.md` para más recursos

## 5. ✏️ Tarea de Práctica

### Nivel Básico
Crea una función `calculate_discount(price: float, discount_percent: float) -> float` que calcule el precio final después de aplicar un descuento. Añade validación para que el descuento esté entre 0 y 100. Incluye type hints en todos los parámetros y el retorno.

### Nivel Intermedio
Implementa un sistema de gestión de biblioteca con las siguientes funciones:
- `add_book(title: str, author: str, year: int) -> Dict[str, str | int]`: Crea un diccionario con la información del libro
- `search_books(books: List[Dict[str, str | int]], keyword: str) -> List[Dict[str, str | int]]`: Busca libros por palabra clave en título o autor
- `get_books_by_year(books: List[Dict[str, str | int]], year: int) -> Optional[List[Dict[str, str | int]]]`: Retorna libros de un año específico, None si no hay ninguno

Todas las funciones deben tener type hints completos.

### Nivel Avanzado
Crea un decorador genérico `@validate_types` que en tiempo de ejecución verifique que los argumentos pasados a una función coincidan con sus type hints. Debe:
- Inspeccionar la signature de la función decorada
- Extraer los type hints de parámetros y retorno
- Validar tipos en cada llamada usando `isinstance`
- Lanzar `TypeError` con mensaje descriptivo si hay mismatch
- Manejar `Optional`, `Union`, y colecciones genéricas como `List[int]`
- Funcionar con funciones que retornan `None`

## 6. 📝 Summary

- Los **type hints** son anotaciones opcionales que documentan tipos esperados sin afectar la ejecución
- Introducidos en PEP 484 (Python 3.5), permiten **detección estática de errores** mediante herramientas como mypy
- Python 3.9+ simplificó la sintaxis permitiendo `list[int]` en lugar de `List[int]` de `typing`
- Python 3.10+ usa `|` para uniones: `int | str` en lugar de `Union[int, str]`
- Son fundamentales en frameworks modernos como **FastAPI** y **Pydantic** para validación y generación automática de código

## 7. 🧠 Mi Análisis Personal

> ✍️ **Espacio para tu reflexión**
>
> Escribe aquí tus observaciones, dudas y conclusiones después de completar este tema...
