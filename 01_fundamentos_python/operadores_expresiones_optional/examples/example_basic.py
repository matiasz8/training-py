"""Ejemplo funcional de operadores y expresiones."""


def calculate_total(subtotal: float, tax_rate: float, discount: float) -> float:
    """Aplica operadores aritmeticos para calcular un total final."""
    taxed = subtotal * (1 + tax_rate)
    return round(taxed - discount, 2)


def shipping_label(total: float, is_member: bool) -> str:
    """Usa expresiones booleanas y condicionales para decidir el envio."""
    free_shipping = total >= 50 or is_member
    return "envio gratis" if free_shipping else "envio estandar"


def main() -> None:
    total = calculate_total(48.0, 0.21, 5.0)
    print(f"Total final: {total}")
    print(f"Etiqueta: {shipping_label(total, is_member=False)}")
    print(f"7 in [3, 5, 7]: {7 in [3, 5, 7]}")
    print(f"2 ** 5 = {2 ** 5}")


if __name__ == "__main__":
    main()
