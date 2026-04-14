"""Ejemplo funcional de strings avanzados."""


def build_slug(title: str) -> str:
    """Normaliza un titulo para usarlo como slug."""
    return "-".join(title.strip().lower().split())


def highlight_keyword(text: str, keyword: str) -> str:
    """Reemplaza una palabra clave usando metodos de string."""
    return text.replace(keyword, keyword.upper())


def format_progress(module: str, completed: int, total: int) -> str:
    """Usa f-strings para armar un reporte legible."""
    percentage = 0.0 if total == 0 else completed / total * 100
    return f"{module}: {completed}/{total} ({percentage:.1f}%)"


def main() -> None:
    print(build_slug("  Python Fundamentals Module  "))
    print(highlight_keyword("python makes automation fun", "automation"))
    print(format_progress("Module 01", 4, 12))


if __name__ == "__main__":
    main()
