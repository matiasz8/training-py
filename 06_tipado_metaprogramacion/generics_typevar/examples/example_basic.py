"""
Genéricos y TypeVar en Python.
Permite crear código type-safe reutilizable.
"""

from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')


class Stack(Generic[T]):
    """Stack genérico type-safe."""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Añade un elemento al stack."""
        self._items.append(item)
    
    def pop(self) -> Optional[T]:
        """Extrae el último elemento."""
        return self._items.pop() if self._items else None
    
    def peek(self) -> Optional[T]:
        """Ve el último elemento sin extraerlo."""
        return self._items[-1] if self._items else None
    
    def is_empty(self) -> bool:
        """Verifica si el stack está vacío."""
        return len(self._items) == 0


class Pair(Generic[K, V]):
    """Par clave-valor genérico."""
    
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value
    
    def __repr__(self) -> str:
        return f"Pair({self.key!r}, {self.value!r})"


def get_first_element(items: List[T]) -> Optional[T]:
    """Función genérica que retorna el primer elemento."""
    return items[0] if items else None


if __name__ == "__main__":
    # Stack de enteros
    int_stack: Stack[int] = Stack()
    int_stack.push(1)
    int_stack.push(2)
    print(f"Pop: {int_stack.pop()}")  # 2
    
    # Stack de strings
    str_stack: Stack[str] = Stack()
    str_stack.push("hello")
    str_stack.push("world")
    print(f"Peek: {str_stack.peek()}")  # "world"
    
    # Pair con tipos diferentes
    pair = Pair[str, int]("edad", 30)
    print(pair)
    
    # Función genérica
    first_num = get_first_element([1, 2, 3])
    first_str = get_first_element(["a", "b", "c"])
    print(f"First number: {first_num}, First string: {first_str}")
