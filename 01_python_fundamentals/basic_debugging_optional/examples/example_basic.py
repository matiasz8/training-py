"""Ejemplo funcional de debugging basico."""


def average_positive(values: list[int]) -> float:
    """Muestra un flujo simple de debugging con impresiones y aserciones."""
    print(f"[debug] valores recibidos={values}")
    positives = [value for value in values if value >= 0]
    print(f"[debug] valores positivos={positives}")
    if not positives:
        raise ValueError("Se necesita al menos un valor positivo.")

    result = sum(positives) / len(positives)
    print(f"[debug] promedio calculado={result}")
    assert result >= 0
    return result


def main() -> None:
    print(average_positive([10, -5, 20, 15]))


if __name__ == "__main__":
    main()
