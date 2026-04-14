# Ruff: Introducción y Velocidad

## ¿Qué es Ruff?

**Ruff** es un linter y formatter de Python extremadamente rápido, escrito en Rust. Creado por Astral (la misma empresa detrás de uv), Ruff reemplaza múltiples herramientas (Black, isort, Flake8, pylint, pyupgrade, y más) en una sola aplicación que es 10-100x más rápida que sus predecesoras.

## La Revolución de la Velocidad

Ruff puede lintear proyectos Python completos en milisegundos donde herramientas tradicionales toman segundos o minutos. Esta velocidad permite:
- **Feedback instantáneo** en el editor
- **Integración sin fricciones** en pre-commit hooks
- **CI/CD más rápidos** con checks en segundos
- **Desarrollo más fluido** sin interrupciones

## Arquitectura

Ruff está construido en Rust desde cero, aprovechando:
- **Parser optimizado**: AST parsing paralelo
- **Análisis incremental**: Solo analiza archivos modificados
- **Concurrencia nativa**: Procesa múltiples archivos en paralelo
- **Zero-copy parsing**: Minimiza allocaciones de memoria

## Capacidades Todo-en-Uno

### 1. Linter (reemplaza: Flake8, pylint, pycodestyle, pyflakes)
- 800+ reglas de linting
- Compatible con plugins populares de Flake8
- Detección de bugs y code smells

### 2. Formatter (reemplaza: Black)
- Estilo compatible con Black
- Formateo ultra-rápido
- Opinionated pero configurable

### 3. Import Sorter (reemplaza: isort)
- Organización automática de imports
- Compatible con configuración de isort
- Detección de imports sin usar

### 4. Code Transformer (reemplaza: pyupgrade, autoflake)
- Modernización automática de código
- Remover código muerto
- Fix automático de issues

## Comparación de Velocidad

### Benchmark: Django Repository (~350k LOC)

| Herramienta | Tiempo | Factor |
|-------------|--------|--------|
| pylint | 47.3s | 1x |
| Flake8 | 23.1s | 2x |
| pyflakes | 12.8s | 3.7x |
| **Ruff** | **0.4s** | **118x** |

### Benchmark: Formatting (100k LOC)

| Herramienta | Tiempo | Factor |
|-------------|--------|--------|
| Black | 8.2s | 1x |
| yapf | 15.3s | 0.5x |
| autopep8 | 11.7s | 0.7x |
| **Ruff** | **0.3s** | **27x** |

## Instalación

```bash
# Con uv (recomendado)
uv tool install ruff

# Con pip
pip install ruff

# Como binario standalone
curl -LsSf https://astral.sh/ruff/install.sh | sh
```

## Uso Básico

```bash
# Linting
ruff check .

# Formateo
ruff format .

# Auto-fix
ruff check --fix .

# Check + format en un comando
ruff check --fix . && ruff format .
```

## Integración con Editores

Ruff tiene soporte nativo para:
- **VS Code**: Extension oficial
- **PyCharm**: Plugin disponible
- **Neovim**: Via LSP
- **Sublime Text**: Package disponible
- **Emacs**: Via lsp-mode

## Por Qué Ruff en 2026

En 2026, Ruff se ha convertido en el estándar de facto para:
- **Startups** que necesitan velocidad de desarrollo
- **Empresas grandes** con código bases enormes
- **CI/CD moderno** donde cada segundo cuenta
- **Developers individuales** que valoran la productividad

La comunidad Python ha adoptado Ruff masivamente por su:
1. **Velocidad incomparable**
2. **Consolidación de herramientas**
3. **Mantenimiento activo**
4. **Compatibilidad excelente**

## Ecosistema Ruff

- **ruff-lsp**: Language Server Protocol
- **ruff-pre-commit**: Hook para pre-commit
- **ruff-vscode**: Extensión oficial de VS Code
- **ruff-action**: GitHub Action oficial

## Limitaciones y Trade-offs

**Ventajas:**
- ✅ Velocidad extrema
- ✅ Todo en uno
- ✅ Activamente mantenido
- ✅ Excelente documentation

**Consideraciones:**
- ⚠️ Algunas reglas de pylint aún no implementadas
- ⚠️ Comportamiento ocasionalmente diferente a Black (mínimo)
- ⚠️ Requiere Rust para contribuir al core

## Referencias

- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Ruff GitHub](https://github.com/astral-sh/ruff)
- [Ruff vs Other Tools](https://docs.astral.sh/ruff/faq/)
- [Rules Reference](https://docs.astral.sh/ruff/rules/)
