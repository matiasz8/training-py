#!/usr/bin/env python3
"""
Script para trackear el progreso de aprendizaje en Python Erudito.

Escanea todas las carpetas my_solution/ en busca de archivos Python
no vacíos y genera un reporte de progreso que actualiza el README.md principal.
"""

import re
from collections import defaultdict
from pathlib import Path


def count_non_empty_py_files(solution_dir: Path) -> bool:
    """Verifica si hay archivos Python no vacíos en el directorio de solución."""
    if not solution_dir.exists():
        return False

    for py_file in solution_dir.glob("*.py"):
        # Leer archivo y verificar que no esté vacío (ignorando comentarios y whitespace)
        content = py_file.read_text(encoding="utf-8")
        # Eliminar comentarios y whitespace
        code_lines = [
            line.strip()
            for line in content.splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]
        if code_lines:
            return True
    return False


def scan_modules(base_path: Path) -> dict[str, dict[str, int]]:
    """
    Escanea todos los módulos y cuenta temas completados.

    Returns:
        Dict con estructura: {
            "module_name": {
                "completed": int,
                "total": int
            }
        }
    """
    progress = defaultdict(lambda: {"completed": 0, "total": 0})

    # Buscar todos los directorios que sean módulos (empiezan con número)
    module_dirs = sorted([d for d in base_path.iterdir() if d.is_dir() and d.name[:2].isdigit()])

    for module_dir in module_dirs:
        module_name = module_dir.name

        # Buscar todos los subdirectorios que sean temas (tienen README.md)
        topics = []

        # Para módulo de patrones, buscar en subcategorías
        if "patrones_diseno" in module_name:
            for subcat_dir in module_dir.iterdir():
                if subcat_dir.is_dir():
                    topics.extend(
                        [
                            t
                            for t in subcat_dir.iterdir()
                            if t.is_dir() and (t / "README.md").exists()
                        ]
                    )
        else:
            topics = [t for t in module_dir.iterdir() if t.is_dir() and (t / "README.md").exists()]

        progress[module_name]["total"] = len(topics)

        # Verificar cuántos tienen soluciones
        for topic_dir in topics:
            solution_dir = topic_dir / "my_solution"
            if count_non_empty_py_files(solution_dir):
                progress[module_name]["completed"] += 1

    return dict(progress)


def generate_progress_table(progress: dict[str, dict[str, int]]) -> str:
    """Genera una tabla Markdown con el progreso."""
    lines = [
        "## 📊 Mi Progreso de Aprendizaje",
        "",
        "| Módulo | Completado | Total | Progreso | Porcentaje |",
        "|--------|-----------|-------|----------|------------|",
    ]

    total_completed = 0
    total_topics = 0

    for module_name, stats in progress.items():
        completed = stats["completed"]
        total = stats["total"]
        total_completed += completed
        total_topics += total

        percentage = (completed / total * 100) if total > 0 else 0
        bar_length = 20
        filled = int(bar_length * completed / total) if total > 0 else 0
        bar = "█" * filled + "░" * (bar_length - filled)

        # Formatear nombre del módulo (remover número y guiones bajos)
        display_name = re.sub(r"^\d+_", "", module_name).replace("_", " ").title()

        lines.append(
            f"| {display_name} | {completed} | {total} | {bar} | {percentage:.1f}% |"
        )

    # Agregar total
    total_percentage = (total_completed / total_topics * 100) if total_topics > 0 else 0
    total_filled = int(20 * total_completed / total_topics) if total_topics > 0 else 0
    total_bar = "█" * total_filled + "░" * (20 - total_filled)

    lines.extend(
        [
            "|--------|-----------|-------|----------|------------|",
            f"| **TOTAL** | **{total_completed}** | **{total_topics}** | {total_bar} | **{total_percentage:.1f}%** |",
        ]
    )

    lines.append("")
    lines.append(f"*Última actualización: {Path.cwd().name}*")
    lines.append("")

    return "\n".join(lines)


def update_readme(base_path: Path, progress_table: str) -> None:
    """Actualiza el README.md principal con la tabla de progreso."""
    readme_path = base_path / "README.md"

    if not readme_path.exists():
        print(f"⚠️  README.md no encontrado en {base_path}")
        return

    content = readme_path.read_text(encoding="utf-8")

    # Buscar la sección de progreso y reemplazarla
    progress_section_pattern = r"## 📊 Mi Progreso de Aprendizaje.*?(?=\n## |\Z)"

    if re.search(progress_section_pattern, content, re.DOTALL):
        # Reemplazar sección existente
        new_content = re.sub(
            progress_section_pattern, progress_table.rstrip() + "\n\n", content, flags=re.DOTALL
        )
    else:
        # Agregar al final
        new_content = content.rstrip() + "\n\n" + progress_table

    readme_path.write_text(new_content, encoding="utf-8")
    print(f"✅ README.md actualizado en {readme_path}")


def main() -> None:
    """Función principal."""
    base_path = Path(__file__).parent.parent

    print("🔍 Escaneando módulos y temas...")
    progress = scan_modules(base_path)

    print("📝 Generando tabla de progreso...")
    progress_table = generate_progress_table(progress)

    print("\n" + progress_table)

    print("\n💾 Actualizando README.md...")
    update_readme(base_path, progress_table)

    print("\n✨ ¡Progreso actualizado correctamente!")


if __name__ == "__main__":
    main()
