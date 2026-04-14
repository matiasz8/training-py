"""Ejemplo funcional de estructuras de control."""


def classify_temperature(value: int) -> str:
    """Clasifica una temperatura usando if/elif/else."""
    if value < 10:
        return "frio"
    if value < 24:
        return "templado"
    return "caluroso"


def average_valid_scores(scores: list[int | None]) -> float:
    """Usa un bucle con continue para ignorar valores vacios."""
    total = 0
    count = 0
    for score in scores:
        if score is None:
            continue
        total += score
        count += 1
    return total / count if count else 0.0


def main() -> None:
    print(f"18C -> {classify_temperature(18)}")
    print(f"Promedio valido: {average_valid_scores([10, None, 8, 9])}")


if __name__ == "__main__":
    main()
