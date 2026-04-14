"""Ejemplo funcional de funciones basicas."""


def greet(name: str, role: str = "Developer") -> str:
    """Devuelve un saludo usando parametros posicionales y opcionales."""
    return f"Hola, {name}. Tu rol actual es {role}."


def calculate_price(base: float, discount: float = 0.0, tax: float = 0.21) -> float:
    """Calcula un precio final reutilizando logica en una funcion."""
    return round(base * (1 - discount) * (1 + tax), 2)


def main() -> None:
    print(greet("Lin"))
    print(calculate_price(100.0, discount=0.1))


if __name__ == "__main__":
    main()
