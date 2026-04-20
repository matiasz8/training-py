# 🐍 Python Erudito 2026

> Sistema modular de aprendizaje avanzado de Python actualizado a las tecnologías más modernas de 2026

______________________________________________________________________

## 🎯 Guía de navegación rápida

Este README ahora cumple dos funciones:

1. **Hub de entrada** (para entender rápidamente cómo está armado el training), y
1. **Documento de detalle** (todo el contenido técnico original, más abajo).

Si es tu primera vez aquí, sigue este orden:

- 🗺️ Roadmap de Aprendizaje (Hub)
- 📚 Estructura del Programa (Hub)
- 🧩 Resumen de cada módulo (Hub)
- 🚀 Inicio Rápido (Hub)
- 📖 Documentación Completa (Hub)

______________________________________________________________________

## 🗺️ Roadmap de Aprendizaje (Hub)

```text
FASE 1: Base (4-6 semanas)
01_python_fundamentals → 02_intermediate_python → 03_basic_intermediate_oop

FASE 2: Núcleo técnico (6-8 semanas)
04_cpython_internals_advanced → 05_modern_concurrency → 06_typing_metaprogramming

FASE 3: Ingeniería de software (8-10 semanas)
07_design_patterns → 08_application_architecture → 09_testing_qa → 10_performance_optimization

FASE 4: Stack moderno 2026 (8-12 semanas)
11_modern_tooling_2026 → 12_fastapi_complete → 13_backend_ecosystem → 14_advanced_python_2026 → 15_basic_data_science → 16_modern_security
```

**Tiempo total estimado:** 7-10 meses, adaptable a tu ritmo.

______________________________________________________________________

## 📚 Estructura del Programa (Hub)

```text
training-python/
├── 01...16_*/         → módulos del plan de estudio
├── scripts/           → automatizaciones (incluye tracking de progreso)
├── GETTING_STARTED.md → setup paso a paso
├── STATUS.md          → estado global del programa
├── pyproject.toml     → tooling/dependencias
└── README.md          → mapa general + detalle completo
```

Flujo sugerido por tema:

```text
README del tema → examples → exercises → my_solution → tests → reflexión
```

______________________________________________________________________

## 🧩 Resumen de cada módulo (Hub)

| Módulo                                                          | Qué aprendes                                   |
| --------------------------------------------------------------- | ---------------------------------------------- |
| [01_python_fundamentals](01_python_fundamentals/)               | Base sólida del lenguaje                       |
| [02_intermediate_python](02_intermediate_python/)               | Flujo, archivos, excepciones, generators       |
| [03_basic_intermediate_oop](03_basic_intermediate_oop/)         | Diseño orientado a objetos aplicable           |
| [04_cpython_internals_advanced](04_cpython_internals_advanced/) | Internals, GIL/free-threading, subinterpreters |
| [05_modern_concurrency](05_modern_concurrency/)                 | Threading, multiprocessing, asyncio moderno    |
| [06_typing_metaprogramming](06_typing_metaprogramming/)         | Tipado avanzado y metaprogramación             |
| [07_design_patterns](07_design_patterns/)                       | Patrones para diseño robusto                   |
| [08_application_architecture](08_application_architecture/)     | Arquitectura modular y escalable               |
| [09_testing_qa](09_testing_qa/)                                 | Testing y calidad profesional                  |
| [10_performance_optimization](10_performance_optimization/)     | Profiling y optimización práctica              |
| [11_modern_tooling_2026](11_modern_tooling_2026/)               | uv, Ruff, type checking moderno                |
| [12_fastapi_complete](12_fastapi_complete/)                     | APIs modernas listas para producción           |
| [13_backend_ecosystem](13_backend_ecosystem/)                   | Integración backend e infraestructura          |
| [14_advanced_python_2026](14_advanced_python_2026/)             | PyO3 y desarrollo asistido por IA              |
| [15_basic_data_science](15_basic_data_science/)                 | Fundamentos de data science con Python         |
| [16_modern_security](16_modern_security/)                       | Seguridad moderna de software y supply chain   |

______________________________________________________________________

## 🚀 Inicio Rápido (Hub)

### 1) Documentación esencial

- [GETTING_STARTED.md](GETTING_STARTED.md)
- [STATUS.md](STATUS.md)
- [README.md](README.md)

### 2) Setup rápido

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows
uv pip install -e ".[dev,profiling,ai,pyo3,security,data]"
pre-commit install
uv run scripts/progress.py
```

### 3) Primer módulo

```bash
cd 01_python_fundamentals
cat README.md
```

______________________________________________________________________

## 📖 Documentación Completa (Hub)

- [GETTING_STARTED.md](GETTING_STARTED.md): instalación y arranque
- [STATUS.md](STATUS.md): seguimiento de avance
- [scripts/progress.py](scripts/progress.py): reporte automático de progreso
- [pyproject.toml](pyproject.toml): configuración del entorno y herramientas

______________________________________________________________________

## 📘 Detalle completo del programa (contenido original)

## 📖 Descripción

**Python Erudito** es un proyecto de autoaprendizaje estructurado que cubre desde fundamentos hasta temas avanzados de Python, incluyendo las últimas innovaciones de 2026: free-threading sin GIL (PEP 703), tooling basado en Rust (uv, Ruff), extensiones con PyO3, desarrollo asistido por IA, y arquitectura de seguridad moderna.

### 🎯 Características

- **200+ temas organizados en 17 módulos** temáticos independientes
- **Sin calendario fijo**: aprende a tu propio ritmo
- **Plantillas pre-pobladas** con contenido curado
- **Ejercicios progresivos** (básico → intermedio → avanzado) con tests
- **88 patrones de diseño** completamente documentados
- **Infraestructura moderna**: DevContainers, pre-commit hooks, tracking automático
- **Ecosistema Rust**: uv, Ruff, PyO3
- **Python 3.13+**: free-threading, subinterpreters

## 📊 Mi Progreso de Aprendizaje

| Módulo                     | Completado  | Total   | Progreso             | Porcentaje   |
| -------------------------- | ----------- | ------- | -------------------- | ------------ |
| Fundamentos Python         | 0           | 12      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Python Intermedio          | 0           | 15      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Poo Basica Intermedia      | 0           | 12      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Cpython Internals Avanzado | 0           | 5       | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Concurrencia Moderna       | 0           | 25      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Tipado Metaprogramacion    | 0           | 22      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Patrones Diseno            | 0           | 88      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Arquitectura Aplicaciones  | 0           | 18      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Testing Qa                 | 0           | 16      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Performance Optimizacion   | 0           | 14      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Tooling Moderno 2026       | 0           | 9       | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Fastapi Completo           | 0           | 28      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Ecosistema Backend         | 0           | 20      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Python Avanzado 2026       | 0           | 45      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Data Science Basico        | 0           | 10      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| Security Moderna           | 0           | 40      | ░░░░░░░░░░░░░░░░░░░░ | 0.0%         |
| --------                   | ----------- | ------- | ----------           | ------------ |
| **TOTAL**                  | **0**       | **379** | ░░░░░░░░░░░░░░░░░░░░ | **0.0%**     |

*Última actualización: py-erudito*

## 🗂️ Estructura de Módulos

### 🟢 Nivel Básico (Opcional para quienes ya conocen Python)

#### [01 - Fundamentos de Python](01_python_fundamentals/)

Variables, tipos de datos, estructuras de control, estructuras de datos built-in, funciones básicas, comprehensions. Temas marcados como `(optional)` para programadores experimentados.

**Temas**: 12 | **Tiempo estimado**: 15-20 horas

#### [02 - Python Intermedio](02_intermediate_python/)

Decoradores básicos, manejo de archivos, excepciones, iteradores, generators, módulos estándar importantes.

**Temas**: 15 | **Tiempo estimado**: 20-25 horas

#### [03 - POO Básica e Intermedia](03_basic_intermediate_oop/)

Clases, herencia, polymorphism, métodos especiales, properties, descriptores, composición vs herencia.

**Temas**: 12 | **Tiempo estimado**: 18-22 horas

______________________________________________________________________

### 🔵 Nivel Intermedio-Avanzado

#### [04 - CPython Internals Avanzado](04_cpython_internals_advanced/)

Historia del GIL, **PEP 703 free-threading**, **PEP 684 subinterpreters**, thread-safety sin GIL, object model, reference counting, estrategias de migración.

**Temas**: 27 | **Tiempo estimado**: 40-50 horas

**Temas destacados**:

- Free-threading Python 3.13+ (modo `--disable-gil`)
- Subinterpreters con per-interpreter GIL
- Thread-safety en código Python moderno
- Biased reference counting
- Immortal objects (PEP 683)

#### [05 - Concurrencia y Paralelismo Moderno](05_modern_concurrency/)

Threading con/sin GIL, subinterpreters para aislamiento, multiprocessing con shared memory, asyncio avanzado, patrones de concurrencia, testing concurrent.

**Temas**: 25 | **Tiempo estimado**: 35-45 horas

**Temas destacados**:

- Threading escalable sin GIL
- Subinterpreters para sandboxing y plugins
- TaskGroups y structured concurrency
- Race condition detection

#### [06 - Tipado Estático y Metaprogramación](06_typing_metaprogramming/)

Type hints avanzados, Generics, Protocol, TypeGuard, metaclases, descriptores, AST manipulation, introspección.

**Temas**: 22 | **Tiempo estimado**: 30-40 horas

______________________________________________________________________

### 🟣 Nivel Avanzado - Patrones y Arquitectura

#### [07 - Patrones de Diseño Completos](07_design_patterns/)

88 patrones organizados en 8 subcategorías: GoF básicos/avanzados, pythónicos, arquitectónicos, sistemas distribuidos, concurrencia, mensajería, gestión de objetos.

**Temas**: 88 patrones | **Tiempo estimado**: 100-120 horas

**Subcategorías**:

- [01 - Patrones GoF Básicos](07_design_patterns/01_basic_gof/) (11 patrones)
- [02 - Patrones Pythónicos](07_design_patterns/02_pythonic_patterns/) (14 patrones)
- [03 - Patrones GoF Avanzados](07_design_patterns/03_advanced_gof/) (12 patrones)
- [04 - Patrones Arquitectónicos](07_design_patterns/04_architectural/) (13 patrones)
- [05 - Patrones de Sistemas Distribuidos](07_design_patterns/05_distributed_systems/) (12 patrones)
- [06 - Patrones de Concurrencia](07_design_patterns/06_concurrency/) (14 patrones)
- [07 - Patrones de Mensajería](07_design_patterns/07_messaging/) (4 patrones)
- [08 - Patrones de Gestión de Objetos](07_design_patterns/08_object_management/) (8 patrones)

#### [08 - Arquitectura de Aplicaciones](08_application_architecture/)

SOLID, Dependency Injection, DDD, Hexagonal Architecture, CQRS, Event Sourcing, logging estructurado, observability.

**Temas**: 18 | **Tiempo estimado**: 25-35 horas

#### [09 - Testing y Quality Assurance](09_testing_qa/)

pytest avanzado, fixtures, mocking, coverage, property-based testing (hypothesis), mutation testing, pytest-asyncio.

**Temas**: 16 | **Tiempo estimado**: 22-28 horas

#### [10 - Performance y Optimización](10_performance_optimization/)

Profiling (cProfile, py-spy), benchmarking, Cython, NumPy vectorización, Numba, PyPy, caching, lazy evaluation.

**Temas**: 14 | **Tiempo estimado**: 20-26 horas

______________________________________________________________________

### 🔴 Nivel Experto - Tecnologías 2026

#### [11 - Tooling Moderno 2026](11_modern_tooling_2026/)

**uv** (package manager en Rust), **Ruff** (linter/formatter all-in-one), **BasedPyright/Pylyzer** (type checkers modernos), pre-commit hooks, pytest avanzado, py-spy, memray.

**Temas**: 35 | **Tiempo estimado**: 45-55 horas

**Herramientas destacadas**:

- uv: resolución ultrarrápida de dependencias
- Ruff: reemplaza Black, isort, pylint con 100x velocidad
- BasedPyright: type checking estricto mejorado
- memray: memory profiling de nueva generación

#### [12 - FastAPI Completo](12_fastapi_complete/)

Todos los aspectos de FastAPI: routing, dependency injection, Pydantic V2, WebSockets, authentication (JWT, OAuth2), testing, SQLAlchemy 2.0, async databases, deployment, monitoring.

**Temas**: 28 | **Tiempo estimado**: 40-50 horas

#### [13 - Ecosistema Backend Moderno](13_backend_ecosystem/)

SQLAlchemy 2.0, PostgreSQL avanzado, Redis patterns, message queues (RabbitMQ, Kafka), Celery/ARQ, gRPC, observability (OpenTelemetry), Prometheus.

**Temas**: 20 | **Tiempo estimado**: 28-36 horas

#### [14 - Python Avanzado 2026](14_advanced_python_2026/)

**PyO3** (extensiones Rust), **AI-Assisted Development** (LangChain, LangGraph, agentes autónomos), **DevContainers**, pattern matching, dataclass improvements, free-threaded Python patterns.

**Temas**: 45 | **Tiempo estimado**: 60-75 horas

**Temas destacados**:

- PyO3 básico → intermedio → avanzado → casos reales
- LangChain y RAG patterns
- LangGraph para workflows complejos
- Agentes autónomos con ReAct
- DevContainers para desarrollo aislado

#### [15 - Data Science Básico](15_basic_data_science/)

NumPy, Pandas fundamentals, Matplotlib/Seaborn, data cleaning patterns, Jupyter notebooks.

**Temas**: 10 | **Tiempo estimado**: 15-20 horas

#### [16 - Seguridad Moderna](16_modern_security/)

Supply chain security, **SBOM** (Software Bill of Materials), **Sigstore** (keyless signing), vulnerability scanning, **SOPS** (secrets encryption), **HashiCorp Vault**, secrets en Kubernetes, container security, secure coding.

**Temas**: 40 | **Tiempo estimado**: 50-60 horas

**Temas destacados**:

- Generación y análisis de SBOMs
- Firma de artefactos sin claves persistentes
- SOPS con age/KMS
- Vault para secrets dinámicos
- Security en CI/CD moderno

______________________________________________________________________

## 🎓 Metodología de Estudio

### Estructura de cada Tema

Cada tema individual contiene:

```
tema_ejemplo/
├── README.md                 # Plantilla de aprendizaje completa
├── examples/                 # Código de demostración comentado
│   ├── basic_example.py
│   └── advanced_example.py
├── exercises/                # Ejercicios progresivos
│   ├── basic_exercise.py
│   ├── intermediate_exercise.py
│   └── advanced_exercise.py
├── tests/                    # Tests con pytest para validar
│   ├── test_basic.py
│   ├── test_intermediate.py
│   └── test_advanced.py
├── my_solution/              # TU CÓDIGO AQUÍ
│   └── (tus archivos .py)
└── references/               # Links a recursos externos
    └── links.md
```

### Plantilla README.md

Cada tema incluye:

1. **📚 Definición**: Explicación técnica completa (200-300 palabras)
1. **💡 Aplicación Práctica**: Casos de uso reales con ejemplos
1. **🤔 ¿Por Qué Es Importante?**: Motivación, problema que resuelve, historia
1. **🔗 Referencias**: Documentación oficial + artículos técnicos + videos + repos GitHub
1. **✏️ Tarea de Práctica**: 3 ejercicios progresivos (básico → intermedio → avanzado)
1. **📝 Summary**: 3-5 puntos clave técnicos
1. **⏱️ Tiempo Estimado**: Duración aproximada del tema
1. **🧠 Mi Análisis Personal**: Sección vacía para tu reflexión

### Workflow Recomendado

1. **Leer README.md** del tema: entender definición, motivación, referencias
1. **Estudiar examples/**: ejecutar y experimentar con código de demostración
1. **Intentar exercises/**: empezar con básico, progresar a intermedio y avanzado
1. **Escribir en my_solution/**: implementar tu propia versión
1. **Validar con tests**: ejecutar `pytest tests/` para verificar corrección
1. **Escribir análisis personal**: reflexionar en sección "Mi Análisis Personal"
1. **Commit**: al hacer commit, pre-commit hook actualiza progreso automáticamente

## 🚀 Comenzar

### Opción 1: Con DevContainer (Recomendado)

1. Abre el proyecto en VS Code
1. Instala la extensión "Dev Containers"
1. `Cmd/Ctrl + Shift + P` → "Dev Containers: Reopen in Container"
1. Espera a que se configure el ambiente (automático)
1. ¡Listo! Todo instalado y configurado

### Opción 2: Instalación Local

```bash
# Instalar uv (ultra-fast package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Crear entorno virtual
uv venv

# Activar entorno
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Instalar dependencias
uv pip install -e ".[dev,profiling,ai,pyo3,security,data]"

# Instalar pre-commit hooks
pre-commit install

# Verificar instalación
uv run scripts/progress.py
```

## 📈 Tracking de Progreso

El script `scripts/progress.py` escanea automáticamente todas las carpetas `my_solution/` y genera un reporte de progreso:

```bash
# Ver progreso actual
uv run scripts/progress.py

# El README.md se actualiza automáticamente al hacer commits
git add .
git commit -m "Completado tema: threading con free-threading"
# → Pre-commit hook ejecuta progress.py automáticamente
```

## 🛠️ Herramientas Incluidas

### Linting y Formatting

```bash
# Ruff todo-en-uno (linting + formatting + import sorting)
ruff check .           # Lint
ruff format .          # Format
ruff check --fix .     # Auto-fix
```

### Type Checking

```bash
basedpyright          # Type checking estricto
```

### Testing

```bash
pytest                          # Ejecutar todos los tests
pytest -v                       # Verbose
pytest --cov=my_solution        # Con coverage
pytest -k "test_specific"       # Test específico
```

### Profiling

```bash
py-spy top -- python script.py           # Live profiling
memray run script.py                     # Memory profiling
viztracer script.py                      # Visual tracing
```

## 📚 Rutas de Aprendizaje Sugeridas

### Ruta 1: Python Moderno Completo (Principiante → Experto)

```
01 → 02 → 03 → 06 → 09 → 04 → 05 → 11 → 10 → 07 → 08 → 12 → 13 → 14 → 16 → 15
```

### Ruta 2: Backend Engineer (Conoces Python Básico)

```
06 → 09 → 11 → 12 → 13 → 07 → 08 → 16 → 05 → 10 → 14
```

### Ruta 3: Systems Programmer (Enfoque en Performance)

```
04 → 05 → 10 → 14 (PyO3) → 11 → 06 → 07 → 16
```

### Ruta 4: AI/ML Engineer

```
02 → 06 → 09 → 11 → 15 → 14 (AI-Assisted Dev) → 12 → 13
```

### Ruta 5: Modernización (Ya eres Senior, quieres estar al día 2026)

```
11 → 04 (free-threading) → 14 (PyO3 + AI) → 16 (Security moderna) → 05 → 07
```

## 🎯 Temas Más Relevantes de 2026

Si tienes tiempo limitado, prioriza estos temas críticos:

### Must-Learn 2026

- 🔥 **04/PEP 703 Free-Threading**: Python sin GIL
- 🔥 **04/PEP 684 Subinterpreters**: Aislamiento per-interpreter
- 🔥 **11/uv**: Package manager ultra-rápido
- 🔥 **11/Ruff**: Linting/formatting moderno
- 🔥 **14/PyO3**: Extensiones Rust para Python
- 🔥 **14/AI-Assisted Dev**: LangChain, LangGraph, agentes
- 🔥 **16/SBOM**: Supply chain security
- 🔥 **16/Sigstore**: Firma keyless de artefactos

### Nice-to-Have 2026

- 11/BasedPyright: Type checking mejorado
- 14/DevContainers: Desarrollo aislado
- 16/SOPS + Vault: Gestión de secretos
- 05/Structured Concurrency: TaskGroups

## 🤝 Contribuir

Este es un proyecto de autoaprendizaje personal, pero si encuentras errores o mejoras:

1. Fork el repositorio
1. Crea una rama con tu mejora
1. Envía un Pull Request

## 📄 Licencia

Este proyecto es de uso educativo personal. El contenido está curado de fuentes públicas y documentación oficial.

## 🙏 Agradecimientos

- Documentación oficial de Python
- Real Python
- Martin Fowler (Patterns)
- Astral (uv, Ruff)
- PyO3 Team
- Comunidad Python

______________________________________________________________________

**¡Comienza tu viaje hacia la maestría en Python! 🚀**

*Última actualización: Enero 2026*
