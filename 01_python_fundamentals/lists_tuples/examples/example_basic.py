"""Ejemplo funcional de listas y tuplas."""


def rotate_tasks(tasks: list[str]) -> list[str]:
    """Mueve la primera tarea al final usando slicing."""
    return tasks[1:] + tasks[:1]


def format_point(point: tuple[int, int]) -> str:
    """Desempaqueta una tupla y la convierte en texto."""
    x, y = point
    return f"Punto(x={x}, y={y})"


def main() -> None:
    tasks = ["leer", "practicar", "repasar"]
    print(rotate_tasks(tasks))
    print(format_point((3, 7)))


if __name__ == "__main__":
    main()
