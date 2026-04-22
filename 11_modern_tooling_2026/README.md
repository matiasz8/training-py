# Módulo 11: Tooling Moderno 2026

Este módulo cubre el ecosistema de herramientas modernas de Python en 2026, centrado en las herramientas más rápidas y eficientes escritas en Rust y las mejores prácticas actuales.

## 🎯 Objetivos del Módulo

- Dominar **uv** como gestor de paquetes y entornos ultrarrápido
- Utilizar **Ruff** como linter, formatter y import sorter todo-en-uno
- Implementar type checking moderno con **mypy, Pyright y pylyzer**
- Configurar workflows de calidad con **pre-commit**
- Aplicar testing avanzado con **pytest, hypothesis y mutmut**
- Usar herramientas modernas de profiling: **py-spy, memray, viztracer**

## 📚 Estructura del Módulo

### Grupo 1: uv - Gestor de Paquetes Ultrarrápido (9 temas)

1. [uv: Introducción y arquitectura](01_uv_introduction_architecture/)
1. [uv: Instalación y configuración inicial](02_uv_installation_configuration/)
1. [uv pip: Instalación de paquetes ultrarrápida](03_uv_pip_package_installation/)
1. [uv venv: Gestión de entornos virtuales](04_uv_venv_virtual_environments/)
1. [uv tool: Herramientas globales](05_uv_tool_global_tools/)
1. [uv en pyproject.toml](06_uv_pyproject_toml/)
1. [Lock files con uv (uv.lock)](07_uv_lock_files/)
1. [Workspaces y monorepos con uv](08_uv_workspaces_monorepos/)
1. [Scripts y entry points](09_uv_scripts_entry_points/)

### Grupo 2: Ruff - Linter y Formatter Ultrarrápido (8 temas)

10. [Ruff: Introducción y velocidad](10_ruff_introduction_speed/)
01. [Ruff como linter: reglas disponibles](11_ruff_linter_rules/)
01. [Ruff como formatter (Black replacement)](12_ruff_formatter_black/)
01. [Ruff como import sorter (isort replacement)](13_ruff_import_sorter_isort/)
01. [Configuración en pyproject.toml](14_ruff_pyproject_configuration/)
01. [Reglas estrictas para código de producción](15_ruff_strict_rules/)
01. [Performance benchmarks](16_ruff_performance_benchmarks/)
01. [Integración en workflow (pre-commit, CI/CD)](17_ruff_workflow_integration/)

### Grupo 3: Type Checkers Modernos (6 temas)

18. [mypy: Estado actual en 2026](18_mypy_current_state_2026/)
01. [Pyright y BasedPyright](19_pyright_basedpyright/)
01. [Pylyzer: Type checker en Rust](20_pylyzer_type_checker_rust/)
01. [Comparación: mypy vs pyright vs pylyzer](21_type_checkers_comparison/)
01. [Configuración de tipado estricto](22_strict_typing_configuration/)
01. [Type narrowing y type guards avanzados](23_type_narrowing_advanced_guards/)

### Grupo 4: Pre-commit y Hooks (3 temas)

24. [Pre-commit: Configuración y hooks esenciales](24_precommit_configuration_hooks/)
01. [Hooks de seguridad (detect-secrets, bandit)](25_precommit_security_hooks/)
01. [Performance y caching de hooks](26_precommit_performance_caching/)

### Grupo 5: Testing Moderno (5 temas)

27. [pytest avanzado: fixtures y parametrize](27_pytest_advanced_fixtures/)
01. [pytest-cov y análisis de coverage](28_pytest_cov_coverage/)
01. [pytest-xdist: paralelización de tests](29_pytest_xdist_parallelization/)
01. [Hypothesis: property-based testing](30_hypothesis_property_testing/)
01. [Mutation testing con mutmut](31_mutation_testing_mutmut/)

### Grupo 6: Debugging y Profiling Modernos (4 temas)

32. [py-spy: profiling sin overhead](32_pyspy_profiling_without_overhead/)
01. [memray: memory profiling moderno](33_memray_memory_profiling/)
01. [viztracer: tracing visual](34_viztracer_tracing_visual/)
01. [debugpy y remote debugging](35_debugpy_remote_debugging/)

## 🚀 Herramientas Destacadas 2026

### uv - El Nuevo Estándar

- **10-100x más rápido** que pip y pip-tools
- Escrito en Rust por Astral (creadores de Ruff)
- Compatible con pip pero con arquitectura moderna
- Gestión unificada de paquetes, entornos y herramientas

### Ruff - El Linter Universal

- **10-100x más rápido** que pylint, flake8, black, isort
- Reemplaza múltiples herramientas en una
- 800+ reglas compatibles con flake8, pylint, pycodestyle
- Integración perfecta con editores y CI/CD

### Type Checkers de Nueva Generación

- **Pyright/BasedPyright**: Rápido, preciso, Microsoft/comunidad
- **pylyzer**: Type checker en Rust, extremadamente rápido
- **mypy**: Maduro y estable, pero más lento

### Profiling Sin Overhead

- **py-spy**: Sampling profiler sin modificar código
- **memray**: Memory profiler con visualizaciones ricas
- **viztracer**: Tracing con timeline visual interactivo

## 📖 Metodología de Aprendizaje

Cada tema incluye:

- **README.md**: Teoría y conceptos (200-300 palabras)
- **examples/**: Código funcional y casos de uso reales
- **exercises/**: Ejercicios progresivos con instrucciones claras
- **my_solution/**: Espacio para tus soluciones
- **tests/**: Tests automatizados con pytest
- **references/**: Enlaces a documentación oficial 2026

## 🔗 Referencias Principales

- [uv Documentation](https://docs.astral.sh/uv/) - Astral
- [Ruff Documentation](https://docs.astral.sh/ruff/) - Astral
- [Pyright Documentation](https://microsoft.github.io/pyright/)
- [BasedPyright](https://docs.basedpyright.com/)
- [py-spy](https://github.com/benfred/py-spy)
- [memray](https://bloomberg.github.io/memray/)

## 💡 Por Qué Estas Herramientas en 2026

El ecosistema Python ha experimentado una revolución con herramientas escritas en Rust que son **órdenes de magnitud más rápidas** que sus predecesoras en Python. Este módulo se centra en las herramientas que se han convertido en el estándar de facto en 2026:

- **uv** está reemplazando pip, pip-tools, poetry, virtualenv
- **Ruff** ha reemplazado black, isort, flake8, pylint para muchos equipos
- **Profilers modernos** permiten analizar producción sin impacto
- **Type checking** es ahora instantáneo incluso en proyectos grandes

______________________________________________________________________

**Módulo actualizado a Enero 2026** - Herramientas y prácticas del estado del arte actual.
