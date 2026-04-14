# Protocol y Structural Typing

⏱️ **Tiempo estimado: 2-3 horas**

## 1. 📚 Definición

**Protocol** es un mecanismo de tipado estructural (structural typing) introducido en PEP 544 que permite definir interfaces implícitas basadas en la forma (estructura) de un objeto, no en su jerarquía de herencia. A diferencia del tipado nominal tradicional donde un objeto debe heredar explícitamente de una clase base, el structural typing verifica que un objeto "tenga la forma correcta" - es decir, que implemente los métodos y atributos necesarios.

En Python, esto formaliza el concepto de "duck typing": "si camina como pato y grazna como pato, entonces es un pato". Los Protocols permiten al type checker verificar duck typing estáticamente sin requerir herencia explícita. Defines un Protocol con los métodos que esperas, y cualquier clase que implemente esos métodos es automáticamente compatible, sin necesidad de heredar del Protocol.

La sintaxis básica usa `class MyProtocol(Protocol)` del módulo `typing`. Los métodos en un Protocol típicamente tienen cuerpos vacíos marcados con `...` (ellipsis). Por ejemplo:

```python
class Drawable(Protocol):
    def draw(self) -> str: ...
```

Cualquier clase con un método `draw()` que retorne `str` satisface este Protocol, sin importar su herencia. Esto contrasta con ABC (Abstract Base Classes) que requieren herencia explícita o registro manual mediante `register()`.

Los Protocols pueden tener métodos, propiedades, atributos de clase, y métodos especiales (`__len__`, `__getitem__`, etc). Python 3.8+ marcó los Protocols como estables. Python 3.12 mejoró el performance del runtime checking con `isinstance()` y `issubclass()` en Protocols.

Los Protocols son especialmente poderosos en Python porque permiten que código existente sin type hints sea compatible con nuevo código tipado, sin modificaciones. También son fundamentales para librerías que quieren ser flexibles con los tipos que aceptan, sin forzar herencia de clases específicas.

El módulo `typing` provee varios Protocols built-in como `SupportsInt`, `SupportsFloat`, `SupportsAbs`, `Sized`, `Iterable[T]`, `Iterator[T]`, etc., que representan interfaces comunes en Python. Los Protocols pueden ser genéricos usando TypeVar, permitiendo expresar relaciones de tipos complejas manteniendo flexibilidad.

## 2. 💡 Aplicación Práctica

### Casos de Uso

1. **APIs flexibles sin acoplamiento**: Una función `def save_data(storage: SupportsWrite)` acepta cualquier objeto con método `write()` - archivos, sockets, buffers, objetos custom - sin requerir herencia de una clase base específica. Esto hace las APIs más reutilizables y testables.

2. **Testing con mocks**: En tests, puedes crear objetos mock simples que implementan solo los métodos que el Protocol especifica, sin heredar de clases complejas. Esto simplifica enormemente la creación de test doubles y hace los tests más rápidos y mantenibles.

3. **Integración con librerías third-party**: Puedes definir un Protocol que describa la interfaz que necesitas, y cualquier clase de cualquier librería que tenga esa interfaz es automáticamente compatible, sin necesidad de wrappers o adapters. Esto es especialmente útil cuando trabajas con múltiples ORMs, loggers, o clientes HTTP que tienen APIs similares pero no comparten jerarquía.

### Código Ejemplo

```python
from typing import Protocol, runtime_checkable, Iterator
from collections.abc import Sized


# ============================================================================
# PROTOCOL BÁSICO
# ============================================================================

class Drawable(Protocol):
    """
    Protocol para objetos dibujables.
    
    Cualquier clase que implemente draw() -> str satisface este protocol,
    sin necesidad de heredar explícitamente.
    """
    def draw(self) -> str: ...


# Clases que implementan el protocol implícitamente
class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"⭕ Circle(r={self.radius})"


class Square:
    def __init__(self, side: float):
        self.side = side
    
    def draw(self) -> str:
        return f"⬜ Square(s={self.side})"


class Triangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height
    
    def draw(self) -> str:
        return f"🔺 Triangle(b={self.base}, h={self.height})"


def render_shape(shape: Drawable) -> None:
    """
    Acepta cualquier objeto que implemente Drawable.
    
    No requiere herencia explícita - solo necesita tener draw().
    """
    print(shape.draw())


# Uso
circle = Circle(5.0)
square = Square(10.0)
triangle = Triangle(3.0, 4.0)

render_shape(circle)   # OK
render_shape(square)   # OK
render_shape(triangle)  # OK


# ============================================================================
# PROTOCOL CON PROPIEDADES Y ATRIBUTOS
# ============================================================================

class Identifiable(Protocol):
    """Protocol para objetos con ID."""
    
    @property
    def id(self) -> int: ...
    
    @property
    def name(self) -> str: ...


class User:
    def __init__(self, user_id: int, username: str):
        self._id = user_id
        self._name = username
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name


class Product:
    def __init__(self, product_id: int, title: str):
        self._id = product_id
        self._name = title
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name


def print_identifiable(item: Identifiable) -> None:
    """Imprime cualquier objeto identificable."""
    print(f"ID: {item.id}, Name: {item.name}")


user = User(1, "Alice")
product = Product(101, "Laptop")

print_identifiable(user)    # OK
print_identifiable(product)  # OK


# ============================================================================
# RUNTIME CHECKABLE PROTOCOLS
# ============================================================================

@runtime_checkable
class Closeable(Protocol):
    """
    Protocol que puede verificarse en runtime con isinstance().
    
    @runtime_checkable permite usar isinstance() y issubclass().
    """
    def close(self) -> None: ...


class FileHandler:
    def __init__(self, filename: str):
        self.filename = filename
    
    def close(self) -> None:
        print(f"Closing {self.filename}")


class DatabaseConnection:
    def __init__(self, host: str):
        self.host = host
    
    def close(self) -> None:
        print(f"Disconnecting from {host}")


# Runtime checking con isinstance()
file_handler = FileHandler("data.txt")
db_conn = DatabaseConnection("localhost")

print(isinstance(file_handler, Closeable))  # True
print(isinstance(db_conn, Closeable))       # True
print(isinstance("string", Closeable))      # False


# ============================================================================
# PROTOCOL GENÉRICO
# ============================================================================

from typing import TypeVar

T = TypeVar('T')


class Container(Protocol[T]):
    """Protocol genérico para contenedores."""
    
    def add(self, item: T) -> None: ...
    
    def get(self, index: int) -> T: ...
    
    def size(self) -> int: ...


class IntList:
    """Implementación concreta para enteros."""
    def __init__(self):
        self._items: list[int] = []
    
    def add(self, item: int) -> None:
        self._items.append(item)
    
    def get(self, index: int) -> int:
        return self._items[index]
    
    def size(self) -> int:
        return len(self._items)


class StrStack:
    """Implementación concreta para strings."""
    def __init__(self):
        self._items: list[str] = []
    
    def add(self, item: str) -> None:
        self._items.append(item)
    
    def get(self, index: int) -> str:
        return self._items[index]
    
    def size(self) -> int:
        return len(self._items)


def process_container[T](container: Container[T], item: T) -> None:
    """Procesa cualquier contenedor genérico."""
    container.add(item)
    print(f"Container now has {container.size()} items")


int_list = IntList()
process_container(int_list, 42)

str_stack = StrStack()
process_container(str_stack, "hello")


# ============================================================================
# PROTOCOL PARA COMPARABLE
# ============================================================================

from typing import Self  # Python 3.11+


class Comparable(Protocol):
    """Protocol para objetos comparables."""
    
    def __lt__(self, other: Self) -> bool: ...
    
    def __le__(self, other: Self) -> bool: ...
    
    def __gt__(self, other: Self) -> bool: ...
    
    def __ge__(self, other: Self) -> bool: ...


def find_max[T: Comparable](items: list[T]) -> T:
    """Encuentra el máximo en una lista de comparables."""
    if not items:
        raise ValueError("Empty list")
    
    max_item = items[0]
    for item in items[1:]:
        if item > max_item:
            max_item = item
    return max_item


# Funciona con tipos built-in que son comparables
print(find_max([3, 1, 4, 1, 5]))  # 5
print(find_max(["z", "a", "m"]))  # "z"


# ============================================================================
# PROTOCOL PARA SERIALIZABLE
# ============================================================================

class Serializable(Protocol):
    """Protocol para objetos serializables a dict."""
    
    def to_dict(self) -> dict[str, any]: ...
    
    @classmethod
    def from_dict(cls, data: dict[str, any]) -> Self: ...


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def to_dict(self) -> dict[str, any]:
        return {"name": self.name, "age": self.age}
    
    @classmethod
    def from_dict(cls, data: dict[str, any]) -> "Person":
        return cls(data["name"], data["age"])


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    
    def to_dict(self) -> dict[str, any]:
        return {"title": self.title, "author": self.author}
    
    @classmethod
    def from_dict(cls, data: dict[str, any]) -> "Book":
        return cls(data["title"], data["author"])


def save_to_json[T: Serializable](obj: T) -> str:
    """Serializa cualquier objeto Serializable a JSON string."""
    import json
    return json.dumps(obj.to_dict())


person = Person("Alice", 30)
book = Book("1984", "Orwell")

print(save_to_json(person))
print(save_to_json(book))


# ============================================================================
# PROTOCOL VS ABC (COMPARACIÓN)
# ============================================================================

from abc import ABC, abstractmethod


# Enfoque ABC (nominal typing)
class AbstractShape(ABC):
    """Requiere herencia explícita."""
    
    @abstractmethod
    def area(self) -> float:
        pass


class RectangleABC(AbstractShape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height


# Enfoque Protocol (structural typing)
class HasArea(Protocol):
    """No requiere herencia - solo implementar area()."""
    def area(self) -> float: ...


class CircleProtocol:
    """No hereda de HasArea pero es compatible."""
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14159 * self.radius ** 2


def total_area(shapes: list[HasArea]) -> float:
    """Calcula área total de cualquier objeto con area()."""
    return sum(shape.area() for shape in shapes)


# Protocol es más flexible - acepta cualquier clase con area()
shapes: list[HasArea] = [
    RectangleABC(5, 3),  # OK - hereda de AbstractShape
    CircleProtocol(2),   # OK - tiene area() sin heredar
]

print(f"Total area: {total_area(shapes)}")


# ============================================================================
# PROTOCOLS BUILT-IN ÚTILES
# ============================================================================

from typing import SupportsInt, SupportsFloat, SupportsAbs


def double_numeric(value: SupportsFloat) -> float:
    """Acepta cualquier objeto convertible a float."""
    return float(value) * 2


print(double_numeric(42))      # int -> OK
print(double_numeric(3.14))    # float -> OK
print(double_numeric("2.5"))   # str con __float__ -> OK (si lo tuviera)


if __name__ == "__main__":
    print("=== Protocol Demo Completado ===")
```

## 3. 🤔 ¿Por Qué Es Importante?

**Problema que resuelve**: Python siempre ha usado duck typing dinámicamente, pero los type checkers tradicionales requieren herencia explícita (nominal typing). Esto crea fricción: o fuerzas a usuarios de tu API a heredar de tus clases base (rígido), o pierdes type safety usando `Any` (inseguro). Los Protocols resuelven esta tensión permitiendo type checking estructural.

**Historia**: Los Protocols fueron propuestos en PEP 544 (2017) por Ivan Levkivskyi y otros contribuyentes de mypy, inspirándose en TypeScript interfaces, Go interfaces, y sistemas de tipos estructurales de lenguajes como OCaml. El objetivo era hacer que el sistema de tipos de Python respete su filosofía duck-typing mientras mantiene verificación estática. Se volvieron estables en Python 3.8.

**Solución**: Los Protocols permiten escribir código flexible que acepta "cualquier cosa que funcione" mientras el type checker verifica estáticamente que los objetos pasados realmente tengan los métodos necesarios. Esto combina lo mejor de ambos mundos: la flexibilidad de duck typing con la seguridad de static typing.

**Adopción real**: Frameworks modernos usan Protocols extensivamente. La stdlib de Python usa Protocols internamente (collections.abc). Librerías como structlog, loguru, y httpx usan Protocols para aceptar múltiples implementaciones sin acoplamiento. Los Protocols son ahora la forma idiomática de definir interfaces en Python type-safe.

## 4. 🔗 Referencias

- [PEP 544 - Protocols: Structural subtyping](https://peps.python.org/pep-0544/)
- [typing - Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)
- [mypy - Protocols and structural subtyping](https://mypy.readthedocs.io/en/stable/protocols.html)
- Ver: `references/links.md` para más recursos

## 5. ✏️ Tarea de Práctica

### Nivel Básico
Define un Protocol `Loggable` con un método `log(message: str) -> None`. Crea dos clases diferentes (`ConsoleLogger` y `FileLogger`) que implementen este protocol sin heredar de una clase común. Escribe una función `log_event(logger: Loggable, event: str)` que funcione con ambos loggers.

### Nivel Intermedio
Implementa un Protocol genérico `Repository[T]` con métodos:
- `get(id: int) -> T | None`
- `add(item: T) -> None`
- `update(id: int, item: T) -> bool`
- `delete(id: int) -> bool`
- `list_all() -> list[T]`

Crea dos implementaciones concretas: `InMemoryRepository[T]` y `CachedRepository[T]`. Escribe una función `count_items[T](repo: Repository[T]) -> int` que funcione con cualquier repositorio.

### Nivel Avanzado
Crea un sistema de plugins usando Protocols:
1. Define `Plugin(Protocol)` con métodos `name() -> str`, `version() -> str`, `execute(data: dict) -> dict`
2. Define `PluginLoader(Protocol)` con `load_plugins(directory: str) -> list[Plugin]` y `get_plugin(name: str) -> Plugin | None`
3. Implementa un `PluginRegistry` que descubra y ejecute plugins dinámicamente
4. Haz el sistema `@runtime_checkable` para validar plugins en tiempo de carga
5. Añade manejo de errores si un plugin no cumple el Protocol

## 6. 📝 Summary

- **Protocol** permite definir interfaces basadas en estructura, no en herencia (structural typing)
- Cualquier clase que implemente los métodos de un Protocol es automáticamente compatible
- `@runtime_checkable` permite usar `isinstance()` con Protocols para verificación en runtime
- Los Protocols son genéricos y pueden usar TypeVar para expresar relaciones de tipos complejas
- Son la forma idiomática de definir interfaces flexibles en Python moderno, respetando duck typing

## 7. 🧠 Mi Análisis Personal

> ✍️ **Espacio para tu reflexión**
>
> Escribe aquí tus observaciones, dudas y conclusiones después de completar este tema...
