# 🐍 Python Erudito 2026

> Sistema modular de aprendizaje avanzado de Python actualizado a las tecnologías más modernas de 2026

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

| Módulo | Completado | Total | Progreso | Porcentaje |
|--------|-----------|-------|----------|------------|
| Fundamentos Python | 0 | 12 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Python Intermedio | 0 | 15 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Poo Basica Intermedia | 0 | 12 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Cpython Internals Avanzado | 0 | 5 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Concurrencia Moderna | 0 | 25 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Tipado Metaprogramacion | 0 | 22 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Patrones Diseno | 0 | 88 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Arquitectura Aplicaciones | 0 | 18 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Testing Qa | 0 | 16 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Performance Optimizacion | 0 | 14 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Tooling Moderno 2026 | 0 | 9 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Fastapi Completo | 0 | 28 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Ecosistema Backend | 0 | 20 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Python Avanzado 2026 | 0 | 45 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Data Science Basico | 0 | 10 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
| Security Moderna | 0 | 40 | ░░░░░░░░░░░░░░░░░░░░ | 0.0% |
|--------|-----------|-------|----------|------------|
| **TOTAL** | **0** | **379** | ░░░░░░░░░░░░░░░░░░░░ | **0.0%** |

*Última actualización: py-erudito*


## 🗂️ Estructura de Módulos

### 🟢 Nivel Básico (Opcional para quienes ya conocen Python)

#### [01 - Fundamentos de Python](01_fundamentos_python/)
Variables, tipos de datos, estructuras de control, estructuras de datos built-in, funciones básicas, comprehensions. Temas marcados como `(optional)` para programadores experimentados.

**Temas**: 12 | **Tiempo estimado**: 15-20 horas

#### [02 - Python Intermedio](02_python_intermedio/)
Decoradores básicos, manejo de archivos, excepciones, iteradores, generadores, módulos estándar importantes.

**Temas**: 15 | **Tiempo estimado**: 20-25 horas

#### [03 - POO Básica e Intermedia](03_poo_basica_intermedia/)
Clases, herencia, polimorfismo, métodos especiales, properties, descriptores, composición vs herencia.

**Temas**: 12 | **Tiempo estimado**: 18-22 horas

---

### 🔵 Nivel Intermedio-Avanzado

#### [04 - CPython Internals Avanzado](04_cpython_internals_avanzado/)
Historia del GIL, **PEP 703 free-threading**, **PEP 684 subinterpreters**, thread-safety sin GIL, object model, reference counting, estrategias de migración.

**Temas**: 27 | **Tiempo estimado**: 40-50 horas

**Temas destacados**:
- Free-threading Python 3.13+ (modo `--disable-gil`)
- Subinterpreters con per-interpreter GIL
- Thread-safety en código Python moderno
- Biased reference counting
- Immortal objects (PEP 683)

#### [05 - Concurrencia y Paralelismo Moderno](05_concurrencia_moderna/)
Threading con/sin GIL, subinterpreters para aislamiento, multiprocessing con shared memory, asyncio avanzado, patrones de concurrencia, testing concurrent.

**Temas**: 25 | **Tiempo estimado**: 35-45 horas

**Temas destacados**:
- Threading escalable sin GIL
- Subinterpreters para sandboxing y plugins
- TaskGroups y structured concurrency
- Race condition detection

#### [06 - Tipado Estático y Metaprogramación](06_tipado_metaprogramacion/)
Type hints avanzados, Generics, Protocol, TypeGuard, metaclases, descriptores, AST manipulation, introspección.

**Temas**: 22 | **Tiempo estimado**: 30-40 horas

---

### 🟣 Nivel Avanzado - Patrones y Arquitectura

#### [07 - Patrones de Diseño Completos](07_patrones_diseno/)
88 patrones organizados en 8 subcategorías: GoF básicos/avanzados, pythónicos, arquitectónicos, sistemas distribuidos, concurrencia, mensajería, gestión de objetos.

**Temas**: 88 patrones | **Tiempo estimado**: 100-120 horas

**Subcategorías**:
- [01 - Patrones GoF Básicos](07_patrones_diseno/01_gof_basicos/) (11 patrones)
- [02 - Patrones Pythónicos](07_patrones_diseno/02_pythonicos/) (14 patrones)
- [03 - Patrones GoF Avanzados](07_patrones_diseno/03_gof_avanzados/) (12 patrones)
- [04 - Patrones Arquitectónicos](07_patrones_diseno/04_arquitectonicos/) (13 patrones)
- [05 - Patrones de Sistemas Distribuidos](07_patrones_diseno/05_sistemas_distribuidos/) (12 patrones)
- [06 - Patrones de Concurrencia](07_patrones_diseno/06_concurrencia/) (14 patrones)
- [07 - Patrones de Mensajería](07_patrones_diseno/07_mensajeria/) (4 patrones)
- [08 - Patrones de Gestión de Objetos](07_patrones_diseno/08_gestion_objetos/) (8 patrones)

#### [08 - Arquitectura de Aplicaciones](08_arquitectura_aplicaciones/)
SOLID, Dependency Injection, DDD, Hexagonal Architecture, CQRS, Event Sourcing, logging estructurado, observabilidad.

**Temas**: 18 | **Tiempo estimado**: 25-35 horas

#### [09 - Testing y Quality Assurance](09_testing_qa/)
pytest avanzado, fixtures, mocking, coverage, property-based testing (hypothesis), mutation testing, pytest-asyncio.

**Temas**: 16 | **Tiempo estimado**: 22-28 horas

#### [10 - Performance y Optimización](10_performance_optimizacion/)
Profiling (cProfile, py-spy), benchmarking, Cython, NumPy vectorización, Numba, PyPy, caching, lazy evaluation.

**Temas**: 14 | **Tiempo estimado**: 20-26 horas

---

### 🔴 Nivel Experto - Tecnologías 2026

#### [11 - Tooling Moderno 2026](11_tooling_moderno_2026/)
**uv** (package manager en Rust), **Ruff** (linter/formatter all-in-one), **BasedPyright/Pylyzer** (type checkers modernos), pre-commit hooks, pytest avanzado, py-spy, memray.

**Temas**: 35 | **Tiempo estimado**: 45-55 horas

**Herramientas destacadas**:
- uv: resolución ultrarrápida de dependencias
- Ruff: reemplaza Black, isort, pylint con 100x velocidad
- BasedPyright: type checking estricto mejorado
- memray: memory profiling de nueva generación

#### [12 - FastAPI Completo](12_fastapi_completo/)
Todos los aspectos de FastAPI: routing, dependency injection, Pydantic V2, WebSockets, authentication (JWT, OAuth2), testing, SQLAlchemy 2.0, async databases, deployment, monitoring.

**Temas**: 28 | **Tiempo estimado**: 40-50 horas

#### [13 - Ecosistema Backend Moderno](13_ecosistema_backend/)
SQLAlchemy 2.0, PostgreSQL avanzado, Redis patterns, message queues (RabbitMQ, Kafka), Celery/ARQ, gRPC, observabilidad (OpenTelemetry), Prometheus.

**Temas**: 20 | **Tiempo estimado**: 28-36 horas

#### [14 - Python Avanzado 2026](14_python_avanzado_2026/)
**PyO3** (extensiones Rust), **AI-Assisted Development** (LangChain, LangGraph, agentes autónomos), **DevContainers**, pattern matching, dataclass improvements, free-threaded Python patterns.

**Temas**: 45 | **Tiempo estimado**: 60-75 horas

**Temas destacados**:
- PyO3 básico → intermedio → avanzado → casos reales
- LangChain y RAG patterns
- LangGraph para workflows complejos
- Agentes autónomos con ReAct
- DevContainers para desarrollo aislado

#### [15 - Data Science Básico](15_data_science_basico/)
NumPy, Pandas fundamentals, Matplotlib/Seaborn, data cleaning patterns, Jupyter notebooks.

**Temas**: 10 | **Tiempo estimado**: 15-20 horas

#### [16 - Seguridad Moderna](16_security_moderna/)
Supply chain security, **SBOM** (Software Bill of Materials), **Sigstore** (keyless signing), vulnerability scanning, **SOPS** (secrets encryption), **HashiCorp Vault**, secrets en Kubernetes, container security, secure coding.

**Temas**: 40 | **Tiempo estimado**: 50-60 horas

**Temas destacados**:
- Generación y análisis de SBOMs
- Firma de artefactos sin claves persistentes
- SOPS con age/KMS
- Vault para secrets dinámicos
- Security en CI/CD moderno

---

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
2. **💡 Aplicación Práctica**: Casos de uso reales con ejemplos
3. **🤔 ¿Por Qué Es Importante?**: Motivación, problema que resuelve, historia
4. **🔗 Referencias**: Documentación oficial + artículos técnicos + videos + repos GitHub
5. **✏️ Tarea de Práctica**: 3 ejercicios progresivos (básico → intermedio → avanzado)
6. **📝 Summary**: 3-5 puntos clave técnicos
7. **⏱️ Tiempo Estimado**: Duración aproximada del tema
8. **🧠 Mi Análisis Personal**: Sección vacía para tu reflexión

### Workflow Recomendado

1. **Leer README.md** del tema: entender definición, motivación, referencias
2. **Estudiar examples/**: ejecutar y experimentar con código de demostración
3. **Intentar exercises/**: empezar con básico, progresar a intermedio y avanzado
4. **Escribir en my_solution/**: implementar tu propia versión
5. **Validar con tests**: ejecutar `pytest tests/` para verificar corrección
6. **Escribir análisis personal**: reflexionar en sección "Mi Análisis Personal"
7. **Commit**: al hacer commit, pre-commit hook actualiza progreso automáticamente

## 🚀 Comenzar

### Opción 1: Con DevContainer (Recomendado)

1. Abre el proyecto en VS Code
2. Instala la extensión "Dev Containers"
3. `Cmd/Ctrl + Shift + P` → "Dev Containers: Reopen in Container"
4. Espera a que se configure el ambiente (automático)
5. ¡Listo! Todo instalado y configurado

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
uv pip install -e ".[dev,profiling,ai,pyo3,security]"

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
2. Crea una rama con tu mejora
3. Envía un Pull Request

## 📄 Licencia

Este proyecto es de uso educativo personal. El contenido está curado de fuentes públicas y documentación oficial.

## 🙏 Agradecimientos

- Documentación oficial de Python
- Real Python
- Martin Fowler (Patterns)
- Astral (uv, Ruff)
- PyO3 Team
- Comunidad Python

---

**¡Comienza tu viaje hacia la maestría en Python! 🚀**

*Última actualización: Enero 2026*
