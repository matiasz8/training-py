"""
Protocoles y Structural Typing en Python.
PEP 544 - Interfaces implícitas sin herencia.
"""

from typing import Protocol, runtime_checkable


@runtime_checkable
class Drawable(Protocol):
    """Protocolo que define la interfaz para objetos dibujables."""
    
    def draw(self) -> str:
        """Método que debe implementar cualquier clase dibujable."""
        ...


class Circle:
    """Clase que implementa el protocolo sin herencia explícita."""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"Dibujando círculo de radio {self.radius}"


class Square:
    """Otra clase compatible con el protocolo."""
    
    def __init__(self, side: float):
        self.side = side
    
    def draw(self) -> str:
        return f"Dibujando cuadrado de lado {self.side}"


class NotDrawable:
    """Clase que NO implementa el protocolo."""
    pass


def render(shape: Drawable) -> None:
    """Función que acepta cualquier objeto que cumpla el protocolo."""
    print(shape.draw())


if __name__ == "__main__":
    # Ambos funcionan sin herencia explícita
    circle = Circle(5.0)
    square = Square(3.0)
    
    render(circle)
    render(square)
    
    # Verificación en runtime
    print(f"Circle es Drawable: {isinstance(circle, Drawable)}")
    
    not_drawable = NotDrawable()
    print(f"NotDrawable es Drawable: {isinstance(not_drawable, Drawable)}")
    
    # Type checker detectaría esto:
    # render(not_drawable)  # Error de tipo!
