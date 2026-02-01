# Ruff como Formatter (Black Replacement)

## Ruff Format: El Sucesor de Black

**Ruff format** es un formateador de código Python que mantiene compatibilidad del 99.9% con Black, pero es **30-50x más rápido**. En 2026, muchos proyectos han migrado de Black a Ruff por su velocidad sin sacrificar calidad.

## Características Principales

### Compatibilidad con Black
- Estilo casi idéntico a Black
- La mayoría del código formateado por Black será idéntico con Ruff
- Pequeñas diferencias documentadas y configurables

### Velocidad Extrema
- Formatear 100k líneas en ~300ms vs ~8s de Black
- No bloquea el editor
- Perfecto para pre-commit hooks sin latencia

### Zero Configuration
- Funciona out-of-the-box sin configuración
- Opinionated pero con opciones razonables
- Configuración compatible con Black

## Uso Básico

```bash
# Formatear un archivo
ruff format file.py

# Formatear directorio completo
ruff format .

# Ver qué cambiaría (dry-run)
ruff format --check .

# Ver diff de cambios
ruff format --diff .
```

## Diferencias con Black

### Compatibilidad del 99.9%

La mayoría del código será idéntico. Las diferencias principales:

#### 1. Trailing Commas en Comprehensions

```python
# Black
result = [
    x
    for x in range(10)
    if x % 2 == 0
]  # Sin trailing comma

# Ruff
result = [
    x
    for x in range(10)
    if x % 2 == 0,  # Con trailing comma
]
```

#### 2. Formateo de Docstrings

```python
# Black y Ruff formatean docstrings de manera ligeramente diferente
# en casos edge cases específicos
```

#### 3. Magic Trailing Comma

Ambos respetan la "magic trailing comma" para mantener multi-línea:

```python
# Trailing comma preserva formato multi-línea
function_call(
    arg1,
    arg2,
    arg3,  # ← Esto indica "mantener multi-línea"
)
```

## Configuración

### En pyproject.toml

```toml
[tool.ruff.format]
# Longitud de línea (default: 88 como Black)
line-length = 88

# Usar single quotes (default: double quotes)
quote-style = "double"  # o "single"

# Indent con espacios
indent-style = "space"  # o "tab"

# Estilo de final de línea
line-ending = "auto"  # "auto", "lf", "cr-lf"

# Indentación dentro de docstrings
docstring-code-format = true

# Línea de docstrings
docstring-code-line-length = 88

# Skipping magic trailing comma
skip-magic-trailing-comma = false
```

### Configuración Compatible con Black

```toml
[tool.ruff]
line-length = 100  # Si usabas --line-length 100 en Black

[tool.ruff.format]
quote-style = "single"  # Si usabas --skip-string-normalization
```

## Integración con Workflow

### Pre-commit Hook

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.0
    hooks:
      # Linter
      - id: ruff
        args: [--fix]
      # Formatter
      - id: ruff-format
```

### GitHub Actions

```yaml
# .github/workflows/lint.yml
- name: Ruff Format Check
  run: |
    ruff format --check .
```

### Make Target

```makefile
.PHONY: format
format:
	ruff format .

.PHONY: format-check
format-check:
	ruff format --check .
```

## Migración desde Black

### Paso 1: Instalar Ruff

```bash
uv tool install ruff
# o: pip install ruff
```

### Paso 2: Reemplazar en CI/CD

```yaml
# Antes
- name: Black
  run: black --check .

# Después  
- name: Ruff Format
  run: ruff format --check .
```

### Paso 3: Actualizar Pre-commit

```yaml
# Antes
- repo: https://github.com/psf/black
  rev: 23.12.0
  hooks:
    - id: black

# Después
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.6.0
  hooks:
    - id: ruff-format
```

### Paso 4: Formatear Todo el Código

```bash
# Formatear el proyecto completo
ruff format .

# Verificar diferencias
git diff

# Commit
git add .
git commit -m "Migrate from Black to Ruff format"
```

## Comparación de Rendimiento

### Benchmark: CPython Repository (~400k LOC)

```bash
# Black
$ time black --check .
All done! ✨ 🍰 ✨
3842 files would be left unchanged.
black --check .  8.24s user 0.31s system 99% cpu 8.573 total

# Ruff
$ time ruff format --check .
3842 files already formatted
ruff format --check .  0.29s user 0.08s system 340% cpu 0.108 total
```

**Resultado: Ruff es ~79x más rápido**

### En Editors

- **Black**: Formateo visible (~200ms)
- **Ruff**: Formateo instantáneo (<10ms)

## Casos de Uso Específicos

### Formatear Solo Archivos Modificados

```bash
# Con git
git diff --name-only --diff-filter=AM | grep '\.py$' | xargs ruff format

# En pre-commit (automático)
ruff format
```

### Formatear con Line Length Personalizado

```bash
ruff format --line-length 100 .
```

### Excluir Archivos/Directorios

```toml
[tool.ruff]
extend-exclude = [
    "migrations",
    "snapshots",
    "vendor",
]
```

## FAQ

### ¿Es 100% compatible con Black?

**99.9% compatible**. La mayoría del código es idéntico. Las diferencias son edge cases documentados.

### ¿Puedo usar Ruff format y Black juntos?

**No es recomendado**. Podrían pelear entre sí. Elige uno.

### ¿Qué hacer si Ruff formatea diferente a Black?

1. Verifica que usas las mismas opciones de configuración
2. Si es un edge case aceptable, migra a Ruff
3. Si es crítico, reporta en GitHub Issues

### ¿Ruff format soporta Jupyter Notebooks?

**Sí**, desde la versión 0.1.0:

```bash
ruff format notebook.ipynb
```

## Best Practices

1. **Use en CI/CD**: `ruff format --check` falla si hay código sin formatear
2. **Integre en el editor**: Formateo automático al guardar
3. **Pre-commit hook**: Previene commits con código sin formatear
4. **Consistencia**: Todo el equipo debe usar Ruff o Black, no mezclar

## Referencias

- [Ruff Formatter Documentation](https://docs.astral.sh/ruff/formatter/)
- [Black Compatibility](https://docs.astral.sh/ruff/formatter/black/)
- [Configuration Options](https://docs.astral.sh/ruff/settings/#format)
- [Migration Guide](https://docs.astral.sh/ruff/formatter/#migrating-from-black)
