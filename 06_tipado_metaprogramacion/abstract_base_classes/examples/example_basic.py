"""
Ejemplo básico: Abstract Base Classes (ABC) en Python
======================================================

Este ejemplo demuestra cómo usar ABC para:
1. Definir interfaces y clases abstractas
2. Forzar implementación de métodos en subclases
3. Implementar polimorfismo type-safe
4. Usar métodos abstractos y concretos
"""

from abc import ABC, abstractmethod
from typing import List, Protocol


# =============================================================================
# EJEMPLO 1: ABC Básica - Jerarquía de Animales
# =============================================================================

class Animal(ABC):
    """
    Clase abstracta que define la interfaz de un animal.
    
    No se puede instanciar directamente. Las subclases DEBEN
    implementar todos los métodos abstractos.
    """
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    @abstractmethod
    def make_sound(self) -> str:
        """Cada animal debe implementar su propio sonido."""
        pass
    
    @abstractmethod
    def move(self) -> str:
        """Cada animal se mueve de forma diferente."""
        pass
    
    def introduce(self) -> str:
        """Método concreto compartido por todos."""
        return f"Soy {self.name}, tengo {self.age} años"
    
    def describe(self) -> str:
        """Método concreto que usa métodos abstractos."""
        return (
            f"{self.introduce()}\n"
            f"  Sonido: {self.make_sound()}\n"
            f"  Movimiento: {self.move()}"
        )


class Dog(Animal):
    """Implementación concreta de Animal."""
    
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed
    
    def make_sound(self) -> str:
        return "Woof! Woof!"
    
    def move(self) -> str:
        return "Corriendo en cuatro patas"
    
    def fetch(self) -> str:
        """Método específico de Dog."""
        return f"{self.name} trae la pelota!"


class Bird(Animal):
    """Otra implementación concreta."""
    
    def __init__(self, name: str, age: int, can_fly: bool = True):
        super().__init__(name, age)
        self.can_fly = can_fly
    
    def make_sound(self) -> str:
        return "Tweet! Tweet!"
    
    def move(self) -> str:
        if self.can_fly:
            return "Volando con alas"
        return "Saltando en el suelo"


class Fish(Animal):
    """Pez que vive en agua."""
    
    def __init__(self, name: str, age: int, water_type: str):
        super().__init__(name, age)
        self.water_type = water_type
    
    def make_sound(self) -> str:
        return "Glub glub"
    
    def move(self) -> str:
        return f"Nadando en agua {self.water_type}"


# =============================================================================
# EJEMPLO 2: ABC con Propiedades Abstractas
# =============================================================================

class Shape(ABC):
    """Clase abstracta para formas geométricas."""
    
    @property
    @abstractmethod
    def area(self) -> float:
        """Las subclases deben calcular su área."""
        pass
    
    @property
    @abstractmethod
    def perimeter(self) -> float:
        """Las subclases deben calcular su perímetro."""
        pass
    
    def describe(self) -> str:
        """Método concreto que usa propiedades abstractas."""
        return (
            f"{self.__class__.__name__}:\n"
            f"  Área: {self.area:.2f}\n"
            f"  Perímetro: {self.perimeter:.2f}"
        )


class Rectangle(Shape):
    """Rectángulo con ancho y alto."""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    @property
    def area(self) -> float:
        return self.width * self.height
    
    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Círculo con radio."""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    @property
    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2
    
    @property
    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius


# =============================================================================
# EJEMPLO 3: ABC vs Protocol (comparación)
# =============================================================================

# ABC - verificación en tiempo de instanciación
class PaymentProcessor(ABC):
    """Procesador de pagos abstracto."""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Procesar pago."""
        pass
    
    @abstractmethod
    def refund(self, transaction_id: str) -> bool:
        """Reembolsar pago."""
        pass


class CreditCardProcessor(PaymentProcessor):
    """Procesador de tarjetas de crédito."""
    
    def process_payment(self, amount: float) -> bool:
        print(f"💳 Procesando ${amount:.2f} con tarjeta de crédito")
        return True
    
    def refund(self, transaction_id: str) -> bool:
        print(f"↩️  Reembolsando transacción {transaction_id}")
        return True


class PayPalProcessor(PaymentProcessor):
    """Procesador de PayPal."""
    
    def process_payment(self, amount: float) -> bool:
        print(f"🅿️  Procesando ${amount:.2f} con PayPal")
        return True
    
    def refund(self, transaction_id: str) -> bool:
        print(f"↩️  Reembolsando transacción {transaction_id} via PayPal")
        return True


# =============================================================================
# FUNCIONES DE DEMOSTRACIÓN
# =============================================================================

def demonstrate_polymorphism(animals: List[Animal]) -> None:
    """Demuestra polimorfismo con ABC."""
    print("\n🐾 POLIMORFISMO CON ABC")
    print("=" * 60)
    
    for animal in animals:
        print(animal.describe())
        print()


def calculate_total_area(shapes: List[Shape]) -> float:
    """Calcula área total de múltiples formas."""
    total = sum(shape.area for shape in shapes)
    print("\n📐 CÁLCULO DE ÁREAS")
    print("=" * 60)
    for shape in shapes:
        print(shape.describe())
        print()
    print(f"Área total: {total:.2f}")
    return total


def process_payments(processors: List[PaymentProcessor]) -> None:
    """Procesa pagos con diferentes procesadores."""
    print("\n💰 PROCESAMIENTO DE PAGOS")
    print("=" * 60)
    
    for i, processor in enumerate(processors, 1):
        print(f"\nPago #{i}:")
        processor.process_payment(100.00 * i)


def main():
    """Función principal de demostración."""
    print("=" * 60)
    print("ABSTRACT BASE CLASSES (ABC) - EJEMPLOS")
    print("=" * 60)
    
    # Ejemplo 1: Animales
    animals = [
        Dog("Rex", 5, "Golden Retriever"),
        Bird("Tweety", 2, can_fly=True),
        Fish("Nemo", 1, "salada")
    ]
    demonstrate_polymorphism(animals)
    
    # Ejemplo 2: Formas geométricas
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Rectangle(10, 2)
    ]
    calculate_total_area(shapes)
    
    # Ejemplo 3: Procesadores de pago
    processors = [
        CreditCardProcessor(),
        PayPalProcessor()
    ]
    process_payments(processors)
    
    # Demostrar que no se puede instanciar ABC
    print("\n" + "=" * 60)
    print("🚫 INTENTANDO INSTANCIAR ABC DIRECTAMENTE")
    print("=" * 60)
    try:
        animal = Animal("Generic", 0)
    except TypeError as e:
        print(f"❌ Error (esperado): {e}")
    
    print("\n" + "=" * 60)
    print("🎓 CONCEPTOS CLAVE:")
    print("=" * 60)
    print("1. ABC define contratos que las subclases deben cumplir")
    print("2. @abstractmethod fuerza implementación en subclases")
    print("3. No se pueden instanciar clases abstractas directamente")
    print("4. Permite polimorfismo type-safe")
    print("5. Útil para diseño de frameworks y APIs")
    print("=" * 60)


if __name__ == "__main__":
    main()
