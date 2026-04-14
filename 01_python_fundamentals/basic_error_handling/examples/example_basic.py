"""Ejemplo funcional de manejo basico de errores."""


def safe_divide(dividend: float, divisor: float) -> float | None:
    """Devuelve el resultado o None si el divisor es invalido."""
    try:
        return dividend / divisor
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
        return None


def parse_port(raw_value: str) -> int:
    """Valida una configuracion numerica y propaga errores utiles."""
    port = int(raw_value)
    if not 1 <= port <= 65535:
        raise ValueError("El puerto debe estar entre 1 y 65535.")
    return port


def main() -> None:
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    try:
        print(parse_port("8080"))
        print(parse_port("70000"))
    except ValueError as error:
        print(f"Error controlado: {error}")


if __name__ == "__main__":
    main()
