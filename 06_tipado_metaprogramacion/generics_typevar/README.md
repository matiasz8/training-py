# Generics y TypeVar

⏱️ **Tiempo estimado: 2-3 horas**

## 1. 📚 Definición

**Generics** y **TypeVar** son mecanismos en Python que permiten escribir código reutilizable y type-safe que funciona con múltiples tipos sin sacrificar la seguridad de tipos. Introducidos en PEP 484, estos conceptos están inspirados en sistemas de tipos parametrizados de lenguajes como Java, C#, TypeScript y Haskell.

**TypeVar** es una "variable de tipo" que actúa como placeholder para un tipo concreto que se determinará en tiempo de uso. Por ejemplo, `T = TypeVar('T')` declara una variable de tipo `T` que puede ser `int`, `str`, `User`, o cualquier otro tipo. Cuando defines una función `def first(items: list[T]) -> T`, estás diciendo "esta función acepta una lista de elementos de tipo T y retorna un elemento del mismo tipo T". Si llamas `first([1, 2, 3])`, T es `int`, si llamas `first(["a", "b"])`, T es `str`.

**Generic** es una clase base que permite crear clases y funciones genéricas parametrizadas por tipos. `class Stack(Generic[T])` crea una pila que puede contener elementos de cualquier tipo, pero todos del mismo tipo. `Stack[int]` es una pila de enteros, `Stack[str]` es una pila de strings. El type checker garantiza que no mezcles tipos: si creas `stack: Stack[int]`, no puedes hacer `push("texto")`.

Python 3.12+ introduce una sintaxis moderna con **PEP 695** que simplifica la declaración de genéricos usando corchetes en la definición: `def first[T](items: list[T]) -> T` y `class Stack[T]`. Esto elimina la necesidad de declarar `TypeVar` explícitamente en muchos casos, haciendo el código más limpio y cercano a otros lenguajes con generics nativos.

Los TypeVars pueden tener **restricciones (constraints)** que limitan los tipos permitidos: `T = TypeVar('T', int, float)` solo acepta int o float. También pueden tener **bounds** que requieren herencia: `T = TypeVar('T', bound=BaseClass)` acepta cualquier subclase de BaseClass. Esto es útil para garantizar que T tenga ciertos métodos o propiedades.

Los genéricos son fundamentales para estructuras de datos type-safe (listas, diccionarios, árboles), algoritmos polimórficos (ordenamiento, búsqueda), y frameworks que necesitan mantener relaciones de tipos complejas. El módulo `typing` de Python provee varios tipos genéricos built-in: `List[T]`, `Dict[K, V]`, `Optional[T]`, `Callable[[Args], Return]`, entre otros.

## 2. 💡 Aplicación Práctica

### Casos de Uso

1. **Estructuras de datos reutilizables**: Una clase `Cache[K, V]` puede almacenar cualquier par key-value manteniendo type safety. Si defines `user_cache: Cache[int, User]`, el type checker garantiza que solo guardes `int` como keys y `User` como values, previniendo bugs de tipos.

2. **Funciones de utilidad polimórficas**: Funciones como `def clamp[T: (int, float)](value: T, min_val: T, max_val: T) -> T` funcionan con int y float sin duplicar código, mientras el type checker garantiza que todos los argumentos sean del mismo tipo numérico.

3. **ORMs y query builders**: SQLAlchemy y SQLModel usan genéricos para garantizar que `session.query(User)` retorne `List[User]`, no `List[Any]`. Esto previene errores donde intentas acceder atributos que no existen en el modelo retornado.

### Código Ejemplo

```python
from typing import TypeVar, Generic, Protocol, Sequence
from collections.abc import Callable

# ============================================================================
# TYPEVAR BÁSICO - Variable de tipo genérica
# ============================================================================

T = TypeVar('T')  # Puede ser cualquier tipo


def get_first[T](items: list[T]) -> T | None:
    """Retorna el primer elemento o None si está vacía."""
    return items[0] if items else None


# Type checker infiere el tipo:
first_num = get_first([1, 2, 3])  # first_num: int | None
first_str = get_first(["a", "b"])  # first_str: str | None


def swap[T](a: T, b: T) -> tuple[T, T]:
    """Intercambia dos valores del mismo tipo."""
    return b, a


# ============================================================================
# TYPEVAR CON RESTRICCIONES
# ============================================================================

# T solo puede ser int o float
Number = TypeVar('Number', int, float)


def average(values: list[Number]) -> float:
    """Calcula el promedio de números."""
    return sum(values) / len(values)


avg_ints = average([1, 2, 3])  # OK: int es permitido
avg_floats = average([1.5, 2.5])  # OK: float es permitido
# avg_strs = average(["1", "2"])  # ERROR: str no es int ni float


# ============================================================================
# TYPEVAR CON BOUND (LÍMITE)
# ============================================================================

class Comparable(Protocol):
    """Protocol para objetos comparables."""
    def __lt__(self, other: "Comparable") -> bool: ...


CT = TypeVar('CT', bound=Comparable)


def find_max[CT](items: Sequence[CT]) -> CT:
    """Encuentra el máximo elemento en una secuencia comparable."""
    if not items:
        raise ValueError("Empty sequence")
    max_item = items[0]
    for item in items[1:]:
        if item > max_item:  # type: ignore
            max_item = item
    return max_item


# Funciona con cualquier tipo comparable
print(find_max([1, 5, 3]))  # 5
print(find_max(["a", "z", "m"]))  # "z"


# ============================================================================
# CLASES GENÉRICAS
# ============================================================================

class Stack[T]:
    """Pila genérica type-safe."""
    
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        """Añade un elemento a la pila."""
        self._items.append(item)
    
    def pop(self) -> T | None:
        """Remueve y retorna el último elemento."""
        return self._items.pop() if self._items else None
    
    def peek(self) -> T | None:
        """Retorna el último elemento sin removerlo."""
        return self._items[-1] if self._items else None
    
    def is_empty(self) -> bool:
        """Verifica si la pila está vacía."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Retorna el número de elementos."""
        return len(self._items)


# Uso con type safety
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
# int_stack.push("error")  # ERROR: Expected int, got str

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")


# ============================================================================
# GENÉRICOS CON MÚLTIPLES PARÁMETROS DE TIPO
# ============================================================================

class Pair[K, V]:
    """Par genérico key-value."""
    
    def __init__(self, key: K, value: V) -> None:
        self.key = key
        self.value = value
    
    def get_key(self) -> K:
        return self.key
    
    def get_value(self) -> V:
        return self.value
    
    def __repr__(self) -> str:
        return f"Pair({self.key}, {self.value})"


# Diferentes combinaciones de tipos
pair1: Pair[int, str] = Pair(1, "one")
pair2: Pair[str, float] = Pair("pi", 3.14)
pair3: Pair[str, list[int]] = Pair("numbers", [1, 2, 3])


# ============================================================================
# FUNCIONES GENÉRICAS CON CALLABLES
# ============================================================================

def map_list[T, R](items: list[T], func: Callable[[T], R]) -> list[R]:
    """
    Mapea una función sobre cada elemento de la lista.
    
    T es el tipo de entrada, R es el tipo de salida.
    El type checker garantiza que func acepta T y retorna R.
    """
    return [func(item) for item in items]


# Type checker infiere los tipos automáticamente
numbers = [1, 2, 3, 4, 5]
strings = map_list(numbers, str)  # list[int] -> list[str]
doubled = map_list(numbers, lambda x: x * 2)  # list[int] -> list[int]


# ============================================================================
# CACHE GENÉRICO
# ============================================================================

class Cache[K, V]:
    """Cache genérico type-safe."""
    
    def __init__(self, max_size: int = 100) -> None:
        self._cache: dict[K, V] = {}
        self._max_size = max_size
    
    def get(self, key: K) -> V | None:
        """Obtiene un valor de la cache."""
        return self._cache.get(key)
    
    def set(self, key: K, value: V) -> None:
        """Guarda un valor en la cache."""
        if len(self._cache) >= self._max_size:
            # Eliminar el primer elemento (simplificado)
            first_key = next(iter(self._cache))
            del self._cache[first_key]
        self._cache[key] = value
    
    def contains(self, key: K) -> bool:
        """Verifica si existe una key."""
        return key in self._cache


# Uso con type safety
user_cache: Cache[int, dict[str, str]] = Cache()
user_cache.set(1, {"name": "Alice", "email": "alice@example.com"})
user = user_cache.get(1)  # user: dict[str, str] | None


# ============================================================================
# EJEMPLOS AVANZADOS
# ============================================================================

# TypeVar covariante (usado en retornos)
T_co = TypeVar('T_co', covariant=True)


class Container[T_co]:
    """Contenedor covariante - puede retornar subtipos."""
    def __init__(self, value: T_co) -> None:
        self._value = value
    
    def get(self) -> T_co:
        return self._value


# TypeVar contravariante (usado en parámetros)
T_contra = TypeVar('T_contra', contravariant=True)


class Validator[T_contra]:
    """Validador contravariante - puede aceptar supertipos."""
    def validate(self, value: T_contra) -> bool:
        return True


if __name__ == "__main__":
    # Demostraciones
    print("=== Stack Demo ===")
    stack: Stack[int] = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Peek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Size: {stack.size()}")
    
    print("\n=== Cache Demo ===")
    cache: Cache[str, int] = Cache(max_size=3)
    cache.set("a", 1)
    cache.set("b", 2)
    print(f"Get 'a': {cache.get('a')}")
    print(f"Contains 'c': {cache.contains('c')}")
```

## 3. 🤔 ¿Por Qué Es Importante?

**Problema que resuelve**: Sin genéricos, tienes dos opciones malas para código reutilizable: (1) Duplicar código para cada tipo (`IntStack`, `StrStack`, etc.), o (2) Usar `Any` y perder type safety. Ambas son problemáticas: la primera viola DRY y es difícil de mantener, la segunda introduce bugs porque el type checker no puede ayudarte.

**Historia**: Los genéricos fueron introducidos en PEP 484 (2014-2015) por Guido van Rossum y el equipo de mypy, inspirándose en TypeScript, Java Generics, y los sistemas de tipos de lenguajes funcionales como Haskell. El objetivo era traer type safety parametrizado a Python sin sacrificar su naturaleza dinámica. Python 3.12 mejoró la sintaxis con PEP 695 (2023), eliminando verbosidad y haciendo los genéricos más accesibles.

**Solución**: Los genéricos permiten escribir código que funciona con múltiples tipos manteniendo garantías de tipo estáticas. Una sola implementación de `Stack[T]` reemplaza infinitas variantes específicas. El type checker verifica que uses consistentemente los tipos: si creas `Stack[int]`, solo puedes hacer `push(int)`, nunca `push(str)`.

**Adopción real**: Frameworks modernos dependen fuertemente de genéricos. FastAPI usa `List[Item]` para validar listas de modelos Pydantic, SQLAlchemy 2.0 usa genéricos para type-safe queries (`select(User)`), y librerías de data science como Polars usan genéricos para garantizar tipos de columnas. Los genéricos son ahora fundamentales para escribir Python type-safe profesional.

## 4. 🔗 Referencias

- [Documentación oficial - Generics](https://docs.python.org/3/library/typing.html#generics)
- [PEP 484 - Type Hints (Generics)](https://peps.python.org/pep-0484/#generics)
- [PEP 695 - Type Parameter Syntax](https://peps.python.org/pep-0695/)
- [mypy - Generic types](https://mypy.readthedocs.io/en/stable/generics.html)
- Ver: `references/links.md` para más recursos

## 5. ✏️ Tarea de Práctica

### Nivel Básico
Crea una función genérica `def duplicate[T](value: T, times: int) -> list[T]` que retorne una lista con el valor duplicado N veces. Debe funcionar con cualquier tipo: números, strings, objetos. Escribe tests que demuestren que funciona con al menos 3 tipos diferentes.

### Nivel Intermedio
Implementa una clase genérica `Queue[T]` (cola FIFO) con los siguientes métodos:
- `enqueue(item: T) -> None`: Añade al final
- `dequeue() -> T | None`: Remueve del inicio, retorna None si vacía
- `peek() -> T | None`: Ve el primer elemento sin remover
- `is_empty() -> bool`: Verifica si está vacía
- `size() -> int`: Retorna número de elementos

La cola debe ser type-safe: si creas `Queue[int]`, solo acepta ints.

### Nivel Avanzado
Implementa una clase genérica `LRU_Cache[K, V]` (Least Recently Used Cache) con:
- `get(key: K) -> V | None`: Obtiene valor y marca como usado recientemente
- `put(key: K, value: V) -> None`: Guarda valor, evicta el menos usado si está llena
- `max_size: int`: Capacidad máxima configurada en `__init__`
- Debe trackear el orden de uso internamente

Bonus: Añade un TypeVar bound para que K sea Hashable usando Protocol.

## 6. 📝 Summary

- **TypeVar** define variables de tipo que actúan como placeholders para tipos concretos
- **Generic** permite crear clases y funciones parametrizadas por tipos manteniendo type safety
- Python 3.12+ usa sintaxis moderna: `def func[T](x: T) -> T` y `class Stack[T]`
- TypeVars pueden tener **constraints** (`int | float`) o **bounds** (subclases de una clase base)
- Los genéricos son esenciales para estructuras de datos reutilizables, algoritmos polimórficos y frameworks modernos

## 7. 🧠 Mi Análisis Personal

> ✍️ **Espacio para tu reflexión**
>
> Escribe aquí tus observaciones, dudas y conclusiones después de completar este tema...
