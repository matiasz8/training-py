"""Ejemplo funcional de importaciones desde la libreria estandar."""

from math import ceil
from pathlib import Path
from statistics import mean


def build_report_path(base_dir: str, module_name: str) -> Path:
    """Construye una ruta usando pathlib."""
    return Path(base_dir) / module_name / "report.txt"


def estimate_iterations(values: list[int], chunk_size: int) -> int:
    """Combina statistics y math para un calculo simple."""
    if chunk_size <= 0:
        raise ValueError("chunk_size debe ser mayor que 0")
    if not values:
        return 0
    return ceil(mean(values) / chunk_size)


def main() -> None:
    print(build_report_path("training-py", "01_python_fundamentals"))
    print(f"Iteraciones estimadas: {estimate_iterations([10, 14, 12], 4)}")


if __name__ == "__main__":
    main()
