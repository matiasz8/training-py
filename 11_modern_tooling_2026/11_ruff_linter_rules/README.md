# Ruff como Linter: Reglas Disponibles

## Sistema de Reglas de Ruff

Ruff implementa más de **800 reglas de linting** organizadas por categorías, compatible con las herramientas más populares del ecosistema Python. Cada regla tiene un código único que permite habilitarla o deshabilitarla selectivamente.

## Categorías Principales

### Pyflakes (F)

Errores lógicos y bugs obvios:

- `F401`: Imported but unused
- `F841`: Local variable assigned but never used
- `F821`: Undefined name
- `F541`: f-string without placeholders

### pycodestyle (E, W)

Estilo PEP 8:

- `E501`: Line too long
- `E302`: Expected 2 blank lines
- `W291`: Trailing whitespace
- `E711`: Comparison to None should use `is`

### McCabe (C90)

Complejidad ciclomática:

- `C901`: Function is too complex

### isort (I)

Organización de imports:

- `I001`: Import block is un-sorted
- `I002`: Missing required import

### pydocstyle (D)

Convenciones de docstrings:

- `D100`: Missing docstring in public module
- `D401`: First line should be imperative
- `D417`: Missing argument descriptions

### pyupgrade (UP)

Modernización de código:

- `UP006`: Use `list` instead of `List` for typing
- `UP032`: Use f-strings instead of format
- `UP009`: Remove unnecessary UTF-8 encoding comments

### flake8-bugbear (B)

Bugs y anti-patterns:

- `B006`: Mutable default argument
- `B008`: Function call in default argument
- `B904`: Use `raise from` to preserve traceback

### flake8-comprehensions (C4)

Optimización de comprehensions:

- `C400`: Unnecessary generator (use list comprehension)
- `C416`: Unnecessary list comprehension (use set)

### pylint (PL)

Reglas de pylint:

- `PLC0414`: Import alias does not rename original package
- `PLE0101`: Return in `__init__`
- `PLR5501`: Use `elif` instead of `else` + `if`

### Ruff-specific (RUF)

Reglas específicas de Ruff:

- `RUF001`: Ambiguous unicode characters
- `RUF100`: Unused `noqa` directive

## Configuración de Reglas

### En pyproject.toml

```toml
[tool.ruff]
# Seleccionar categorías completas
select = ["E", "F", "W", "I", "N", "UP", "B", "A", "C4", "PL"]

# Ignorar reglas específicas
ignore = ["E501", "D100"]

# Por archivo
[tool.ruff.per-file-ignores]
"__init__.py" = ["F401"]
"tests/*" = ["D"]

# Configuración específica por regla
[tool.ruff.mccabe]
max-complexity = 10

[tool.ruff.pydocstyle]
convention = "google"
```

### En línea

```python
# noqa: E501 - Ignorar línea específica
very_long_line = "..." # noqa: E501

# noqa - Ignorar todas las reglas en esta línea
x = some_function()  # noqa

# ruff: noqa - Ignorar archivo completo
# ruff: noqa
```

## Reglas Recomendadas por Tipo de Proyecto

### Biblioteca Pública

```toml
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # Pyflakes
    "I",   # isort
    "N",   # pep8-naming
    "D",   # pydocstyle
    "UP",  # pyupgrade
    "B",   # flake8-bugbear
    "A",   # flake8-builtins
    "C4",  # flake8-comprehensions
    "DTZ", # flake8-datetimez
    "RUF", # Ruff-specific
]
```

### Aplicación Web

```toml
select = [
    "E", "W", "F",  # Basics
    "I",            # isort
    "B",            # bugbear
    "S",            # flake8-bandit (security)
    "C4",           # comprehensions
    "DTZ",          # timezone aware
    "PIE",          # flake8-pie
]

ignore = [
    "S101",  # Use of assert (ok en tests)
]
```

### Scripts y Data Science

```toml
select = [
    "E", "F",  # Errores básicos
    "W",       # Warnings
    "I",       # isort
    "NPY",     # numpy-specific
    "PD",      # pandas-vet
]

ignore = [
    "E501",  # Line length (notebooks)
]
```

## Reglas de Seguridad (flake8-bandit: S)

```python
# S102: Use of exec
exec("print('dangerous')")  # ⚠️ Ruff alert

# S104: Binding to all interfaces
server.bind("0.0.0.0")  # ⚠️ Security risk

# S105: Possible hardcoded password
PASSWORD = "secret123"  # ⚠️ Hardcoded password

# S108: Probable insecure usage of temp file
open("/tmp/file", "w")  # ⚠️ Use tempfile module
```

## Auto-fix Capabilities

Ruff puede auto-corregir automáticamente muchas reglas:

```bash
# Ver qué se puede arreglar
ruff check --show-fixes .

# Aplicar fixes
ruff check --fix .

# Fix unsafe también (con cuidado)
ruff check --fix --unsafe-fixes .
```

### Reglas con Auto-fix

- ✅ `F401`: Remove unused imports
- ✅ `I001`: Sort imports
- ✅ `UP006`: Modernize type hints
- ✅ `C400-416`: Optimize comprehensions
- ❌ `E501`: Line too long (requiere reformat)
- ❌ `C901`: Complexity (requiere refactoring)

## Exploración de Reglas

```bash
# Listar todas las reglas
ruff rule --all

# Buscar reglas específicas
ruff rule F401

# Ver reglas por categoría
ruff rule --preview | grep "D1"
```

## Performance Tips

1. **Select solo lo necesario**: No activar todas las reglas
1. **Use .ruffignore**: Para excluir directorios grandes
1. **Incremental**: Ruff solo analiza archivos modificados
1. **Parallel**: Auto-paralización en multi-core

## Referencias

- [Rules Reference](https://docs.astral.sh/ruff/rules/)
- [Configuration](https://docs.astral.sh/ruff/configuration/)
- [Rule Selection](https://docs.astral.sh/ruff/linter/)
