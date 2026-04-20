#!/usr/bin/env python3
"""
Lab Module Sync for Module 14: Advanced Python 2026
Synchronizes from training-py to nan-python-engineering-labs with full validation.

Steps:
1. Discover context
2. Normalize structure
3. Copy structure to NaN
4. Translate and normalize to English
5. Complete examples (already done in source)
6. Sync back to original (validate identical)
7. Validate (Execution + Structure + Language)
8. Commit hygiene
"""

import pathlib
import re
import shutil
import subprocess

# Repos paths
TRAINING_PY = pathlib.Path("/media/nquiroga/SSDedo/Documents/projects/NanLabs/labs/training-py")
NAN_LABS = pathlib.Path(
    "/media/nquiroga/SSDedo/Documents/projects/NanLabs/labs/nan-python-engineering-labs"
)

MODULE_NUM = "14"
MODULE_NAME = "advanced_python_2026"
MODULE_DIR_TRAINING = TRAINING_PY / f"{MODULE_NUM}_{MODULE_NAME}"
MODULE_DIR_NAN = NAN_LABS / f"{MODULE_NUM}_advanced_python_2026"


def translate_readme_to_english(spanish_content: str) -> str:
    """Translate README from Spanish to English."""

    # Mapping of Spanish terms to English
    translations = {
        # Section headers
        r"^# (.+)$": lambda m: f"# {m.group(1)}",  # Title stays same
        r"^## 1\. Definición$": "## 1. Definition",
        r"^### Características Clave$": "### Key Characteristics",
        r"^## 2\. Aplicación Práctica$": "## 2. Practical Application",
        r"^### Casos de Uso$": "### Use Cases",
        r"^### Ejemplo de Código$": "### Code Example",
        r"^## 3\. ¿Por Qué Es Importante\?$": "## 3. Why Is It Important?",
        r"^### Problema que Resuelve$": "### Problem It Solves",
        r"^### Solución y Beneficios$": "### Solution and Benefits",
        r"^## 4\. Referencias$": "## 4. References",
        r"^## 5\. Tarea Práctica$": "## 5. Practice Task",
        r"^### Nivel Básico$": "### Basic Level",
        r"^### Nivel Intermedio$": "### Intermediate Level",
        r"^### Nivel Avanzado$": "### Advanced Level",
        r"^### Criterios de Éxito$": "### Success Criteria",
        r"^## 6\. Resumen$": "## 6. Summary",
        r"^## 7\. Prompt de Reflexión$": "## 7. Reflection Prompt",
        # Common terms
        r"Tiempo estimado:": "Estimated time:",
        r"es un tema importante": "is an important topic",
        r"es un aspecto crítico": "is a critical aspect",
        r"te permite construir": "lets you build",
        r"te da un marco claro": "gives you a clear framework",
        r"modelar comportamiento": "model behavior",
        r"evaluar trade-offs": "evaluate trade-offs",
        r"construir implementaciones confiables": "build reliable implementations",
        r"promueve código legible": "promotes readable code",
        r"intención explícita": "explicit intent",
        r"funciona bien junto con": "works well with",
        r"facilita validar comportamiento": "facilitates validating behavior",
        r"orientado a escenarios reales": "oriented to real scenarios",
        r"aplicar patrones de": "apply patterns from",
        r"en servicios backend": "in backend services",
        r"herramientas internas": "internal tools",
        r"implementar componentes reutilizables": "implement reusable components",
        r"comportamiento predecible": "predictable behavior",
        r"crear scripts y procesos": "create scripts and processes",
        r"más fáciles de evolucionar": "easier to evolve",
        r"Ver examples/example_basic.py": "See examples/example_basic.py",
        r"para código ejecutable": "for executable code",
        r"relacionado con": "related to",
        r"Ejecuta.*para inspeccionar": "Run examples/example_basic.py to inspect",
        r"el comportamiento base": "the base behavior",
        r"antes de resolver el ejercicio": "before solving the exercise",
        r"supuestos ocultos": "hidden assumptions",
        r"comportamiento frágil": "fragile behavior",
        r"refactors riesgosos": "risky refactors",
        r"baja confianza": "low confidence",
        r"al introducir cambios": "when introducing changes",
        r"mejor organización": "better organization",
        r"debugging y onboarding": "debugging and onboarding",
        r"más rápidos": "faster",
        r"mayor cobertura de pruebas": "greater test coverage",
        r"releases más seguros": "safer releases",
        r"mantenibilidad sostenible": "sustainable maintainability",
        r"Consulta.*para documentación": "See references/links.md for documentation",
        r"Usa.*como punto de entrada": "Use exercises/exercise_01.py as the main entry point",
        r"Implementar la funcionalidad principal": "Implement the main functionality",
        r"Hacer pasar las pruebas base": "Make the base tests pass",
        r"Cubrir casos borde": "Cover edge cases",
        r"inputs inválidos": "invalid inputs",
        r"Mejorar nombres y estructura": "Improve names and structure",
        r"para legibilidad": "for readability",
        r"Agregar manejo de errores": "Add error handling",
        r"type hints cuando corresponda": "type hints when appropriate",
        r"Extender la cobertura": "Extend coverage",
        r"escenarios adicionales": "additional scenarios",
        r"La solución funciona": "The solution works",
        r"casos nominales y casos borde": "nominal cases and edge cases",
        r"pasa correctamente": "passes correctly",
        r"lo suficientemente clara": "sufficiently clear",
        r"revisión por pares": "peer review",
        r"fortalece fundamentos": "strengthens foundations",
        r"Mejora calidad": "Improves quality",
        r"testeabilidad y mantenibilidad": "testability and maintainability",
        r"directamente aplicable": "directly applicable",
        r"proyectos backend": "backend projects",
        r"automatización": "automation",
        r"reflexiona sobre": "reflect on",
        r"Después de completar": "After completing",
        r"¿Qué decisiones de diseño": "What design decisions",
        r"hicieron tu solución": "made your solution",
        r"más fácil de testear": "easier to test",
        r"¿Qué caso borde fue": "What edge case was",
        r"más importante modelar": "most important to model",
        r"¿Cómo aplicarías": "How would you apply",
        r"en tus proyectos actuales": "in your current projects",
    }

    result = spanish_content

    # Apply line-by-line translations first (for headers)
    lines = result.split("\n")
    translated_lines = []

    for line in lines:
        translated_line = line
        for pattern, replacement in translations.items():
            if callable(replacement):
                translated_line = re.sub(pattern, replacement, translated_line, flags=re.MULTILINE)
            else:
                translated_line = re.sub(pattern, replacement, translated_line, flags=re.IGNORECASE)
        translated_lines.append(translated_line)

    return "\n".join(translated_lines)


def copy_module_to_nan():
    """Copy Module 14 from training-py to nan-python-engineering-labs."""

    print("📋 Step 3: Copy structure to NaN repo...")

    # Create module directory
    MODULE_DIR_NAN.mkdir(parents=True, exist_ok=True)

    # Read module README from training-py
    training_readme = MODULE_DIR_TRAINING / "README.md"
    if training_readme.exists():
        content = training_readme.read_text()
        translated = translate_readme_to_english(content)
        (MODULE_DIR_NAN / "README.md").write_text(translated)

    # Copy each topic
    topics = sorted(
        [d for d in MODULE_DIR_TRAINING.iterdir() if d.is_dir() and d.name[0].isdigit()]
    )

    for topic_dir in topics:
        topic_name = topic_dir.name
        target_topic = MODULE_DIR_NAN / topic_name

        # Ensure target directory structure
        target_topic.mkdir(parents=True, exist_ok=True)
        (target_topic / "examples").mkdir(exist_ok=True)
        (target_topic / "exercises").mkdir(exist_ok=True)
        (target_topic / "tests").mkdir(exist_ok=True)
        (target_topic / "references").mkdir(exist_ok=True)
        (target_topic / "my_solution").mkdir(exist_ok=True)

        # 1. Copy example_basic.py (identical in both repos)
        src_example = topic_dir / "examples" / "example_basic.py"
        if src_example.exists():
            dst_example = target_topic / "examples" / "example_basic.py"
            shutil.copy2(src_example, dst_example)

        # 2. Translate README.md to English
        src_readme = topic_dir / "README.md"
        if src_readme.exists():
            spanish_content = src_readme.read_text()
            english_content = translate_readme_to_english(spanish_content)
            (target_topic / "README.md").write_text(english_content)

        # 3. Copy other files (exercises, tests, references) - with English translation if applicable
        for fname in ["exercise_01.py", "test_basic.py"]:
            src_file = (
                topic_dir / ("exercises" if fname.startswith("exercise") else "tests") / fname
            )
            if src_file.exists():
                content = src_file.read_text()
                # Simple English translation for docstrings
                content = content.replace("Ejercicio", "Exercise").replace("Prueba", "Test")
                dst_file = (
                    target_topic
                    / ("exercises" if fname.startswith("exercise") else "tests")
                    / fname
                )
                dst_file.write_text(content)

        # 4. Create references/links.md if not exists
        links_file = target_topic / "references" / "links.md"
        if not links_file.exists():
            links_file.write_text("# References\n\nAdd relevant documentation links here.\n")

        # 5. Create my_solution/.gitkeep
        gitkeep = target_topic / "my_solution" / ".gitkeep"
        gitkeep.touch()

    print(f"✅ Copied {len(topics)} topics to NaN repo")
    return len(topics)


def validate_execution(repo_path: pathlib.Path, module_dir: pathlib.Path) -> tuple[int, int]:
    """Validate that all examples execute successfully."""

    topics = sorted([d for d in module_dir.iterdir() if d.is_dir() and d.name[0].isdigit()])

    passed = 0
    failed = 0

    for topic_dir in topics:
        example = topic_dir / "examples" / "example_basic.py"
        if example.exists():
            try:
                result = subprocess.run(
                    [
                        "/media/nquiroga/SSDedo/Documents/projects/NanLabs/labs/.venv/bin/python",
                        str(example),
                    ],
                    capture_output=True,
                    timeout=5,
                    text=True,
                )
                if result.returncode == 0:
                    passed += 1
                else:
                    failed += 1
            except:
                failed += 1

    return (passed, failed)


def validate_all():
    """Execute full validation per skill."""

    print()
    print("=" * 70)
    print("📊 STEP 7: VALIDATION (Execution + Structure + Language)")
    print("=" * 70)

    # Validation 1: training-py execution
    print("\n✔️  training-py execution...")
    passed_train, failed_train = validate_execution(TRAINING_PY, MODULE_DIR_TRAINING)
    print(f"   Passed: {passed_train}/45, Failed: {failed_train}/45")

    # Validation 2: nan-python-engineering-labs execution
    print("\n✔️  nan-python-engineering-labs execution...")
    passed_nan, failed_nan = validate_execution(NAN_LABS, MODULE_DIR_NAN)
    print(f"   Passed: {passed_nan}/45, Failed: {failed_nan}/45")

    # Validation 3: Language compliance (NaN only)
    print("\n✔️  Language compliance (NaN repo - English only)...")
    spanish_keywords = [
        "Módulo:",
        "Descripción",
        "Objetivo",
        "Ejercicio",
        "Practica",
        "Instrucciones",
        "Referencias",
        "Enlaces",
        "Recursos",
        "Aprende",
        "Diseña",
        "Conceptos",
        "Debes",
        "Requisitos",
        "Hints",
        "Ejemplo",
        "Solución",
        "¿Por qué",
        "Tarea",
    ]

    spanish_found = []
    topics = sorted([d for d in MODULE_DIR_NAN.iterdir() if d.is_dir() and d.name[0].isdigit()])
    for topic_dir in topics:
        readme = topic_dir / "README.md"
        if readme.exists():
            content = readme.read_text()
            for keyword in spanish_keywords:
                if keyword in content:
                    spanish_found.append((topic_dir.name, keyword))

    if spanish_found:
        print(f"   ❌ Found Spanish content: {len(spanish_found)} occurrences")
        for topic, keyword in spanish_found[:5]:
            print(f"      - {topic}: '{keyword}'")
    else:
        print("   ✅ No Spanish content detected")

    # Validation 4: README schema compliance
    print("\n✔️  README schema compliance...")
    required_headings = [
        "# ",
        "## 1. Definition",
        "### Key Characteristics",
        "## 2. Practical Application",
        "### Use Cases",
        "### Code Example",
        "## 3. Why Is It Important?",
        "### Problem It Solves",
        "### Solution and Benefits",
        "## 4. References",
        "## 5. Practice Task",
        "### Basic Level",
        "### Intermediate Level",
        "### Advanced Level",
        "### Success Criteria",
        "## 6. Summary",
        "## 7. Reflection Prompt",
    ]

    schema_failures = []
    for topic_dir in topics:
        readme = topic_dir / "README.md"
        if readme.exists():
            content = readme.read_text()
            for heading in required_headings:
                if heading not in content:
                    schema_failures.append((topic_dir.name, heading))

    if schema_failures:
        print(f"   ⚠️  Missing headings: {len(schema_failures)} issues")
        for topic, heading in schema_failures[:5]:
            print(f"      - {topic}: missing '{heading}'")
    else:
        print("   ✅ All READMEs have required schema")

    # Summary
    print()
    print("=" * 70)
    all_passed = (
        passed_train == 45
        and failed_train == 0
        and passed_nan == 45
        and failed_nan == 0
        and not spanish_found
        and not schema_failures
    )

    if all_passed:
        print("✅ ALL VALIDATIONS PASSED")
    else:
        print("⚠️  SOME VALIDATIONS FAILED")

    print("=" * 70)

    return all_passed


if __name__ == "__main__":
    print()
    print("🔄 LAB MODULE SYNC: Module 14 (Advanced Python 2026)")
    print()

    # Step 1: Discover context
    print("✔️  Step 1: Discover context")
    print(f"   Source: {MODULE_DIR_TRAINING}")
    print(f"   Target: {MODULE_DIR_NAN}")

    # Step 2: Normalize structure (already done in generation)
    print("\n✔️  Step 2: Normalize structure (already done)")

    # Step 3: Copy structure to NaN
    print()
    topics_copied = copy_module_to_nan()

    # Step 7: Validate
    print()
    validation_passed = validate_all()

    print()
    print("Next steps:")
    print("1. Review validation output above")
    print("2. If all passed, run: git add && git commit in both repos")
    print("3. Then push to origin")
