"""Ejemplo funcional de entrada y salida sin depender de input real."""


def parse_csv_line(raw_line: str) -> tuple[str, int, str]:
    """Transforma una linea simple separada por comas en valores tipados."""
    name, age, city = [part.strip() for part in raw_line.split(",")]
    return name, int(age), city


def format_receipt(name: str, total: float) -> str:
    """Genera una salida multilinea lista para mostrar o guardar."""
    return f"Cliente: {name}\nTotal: ${total:.2f}\nEstado: confirmado"


def main() -> None:
    customer = parse_csv_line("Grace Hopper, 37, New York")
    print(customer)
    print(format_receipt(customer[0], 149.99))


if __name__ == "__main__":
    main()
