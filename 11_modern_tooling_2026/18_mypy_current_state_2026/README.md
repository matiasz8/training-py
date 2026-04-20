# mypy: Estado Actual en 2026

## mypy en 2026: Madurez y Estabilidad

**mypy** sigue siendo el type checker de referencia en Python en 2026, con más de 10 años de desarrollo y una adopción masiva en la industria. Aunque han surgido alternativas más rápidas como Pyright y pylyzer, mypy mantiene su posición por su madurez, documentación extensa y compatibilidad amplia.

## Evolución y Estado Actual

### Historia Reciente

- **2014**: Lanzamiento inicial por Jukka Lehtosalo
- **2017**: Adopción por Dropbox
- **2022**: Versión 1.0 estable
- **2024**: Performance improvements significativos
- **2026**: mypy 1.12+ con soporte completo para Python 3.13

### Performance en 2026

Aunque mypy es más lento que Pyright o pylyzer, ha mejorado significativamente:

- **Daemon mode (dmypy)**: Cache persistente entre runs
- **Incremental mode**: Solo re-chequea archivos modificados
- **Parallel mode**: Multi-procesamiento para proyectos grandes
- **Optimizaciones**: 2-3x más rápido vs 2022

## Características Principales

### Type Checking Completo

```python
from typing import List, Optional, Protocol

def process_items(items: List[str]) -> Optional[dict[str, int]]:
    """mypy valida tipos completamente."""
    result: dict[str, int] = {}
    for item in items:
        result[item] = len(item)
    return result if result else None

# mypy detecta errores
x: int = "hello"  # error: Incompatible types
```

### Structural Subtyping (Protocols)

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

def render(shape: Drawable) -> None:
    shape.draw()

# mypy acepta Circle aunque no herede de Drawable
render(Circle())  # ✓ OK
```

### Gradual Typing

```python
# Código sin tipos - mypy lo permite
def old_function(x):
    return x + 1

# Nuevo código con tipos
def new_function(x: int) -> int:
    return old_function(x)  # mypy verifica el uso
```

## Configuración Moderna

### pyproject.toml (2026)

```toml
[tool.mypy]
# Python version
python_version = "3.13"

# Strict mode (recomendado para proyectos nuevos)
strict = true

# O configurar manualmente
disallow_untyped_defs = true
disallow_any_generics = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_return_any = true
no_implicit_optional = true
strict_equality = true

# Performance
incremental = true
cache_dir = ".mypy_cache"

# Plugins
plugins = [
    "pydantic.mypy",
    "sqlalchemy.ext.mypy.plugin",
]

# Per-module configuration
[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false

[[tool.mypy.overrides]]
module = "third_party.*"
ignore_missing_imports = true
```

## Daemon Mode (dmypy)

El modo daemon mantiene mypy corriendo en background para checks ultrarrápidos:

```bash
# Iniciar daemon
dmypy start

# Run checks (muy rápido)
dmypy check .

# Re-check después de cambios
dmypy check .  # Solo chequea archivos modificados

# Ver status
dmypy status

# Detener daemon
dmypy stop
```

**Performance comparison:**

- `mypy .`: 15-30 segundos (cold)
- `dmypy check .`: 1-3 segundos (warm)
- `dmypy check .` (incremental): 0.1-0.5 segundos

## Plugins Ecosystem

### Pydantic Plugin

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Alice", age="30")  # mypy error con plugin
```

```toml
[tool.mypy]
plugins = ["pydantic.mypy"]
```

### SQLAlchemy Plugin

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

# mypy entiende Mapped[] con el plugin
user.id = "invalid"  # error: Incompatible types
```

### Django Plugin (django-stubs)

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)

# mypy conoce los tipos de Django
article = Article.objects.get(title="Test")
article.title = 123  # error: Incompatible types
```

## Estrategias de Adopción

### Adopción Gradual

```bash
# Paso 1: Solo errores obvios
mypy --follow-imports=silent .

# Paso 2: Más estricto gradualmente
mypy --strict --follow-imports=silent .

# Paso 3: Por módulo
mypy --strict src/core/ src/utils/
```

### Strict Mode Progresivo

```toml
# Empezar con módulos críticos en strict
[[tool.mypy.overrides]]
module = "src.core.*"
strict = true

[[tool.mypy.overrides]]
module = "src.utils.*"
strict = true

# Resto más permisivo
[[tool.mypy.overrides]]
module = "src.*"
disallow_untyped_defs = false
```

## Comparación con Alternativas (2026)

| Característica    | mypy         | Pyright      | pylyzer    |
| ----------------- | ------------ | ------------ | ---------- |
| **Velocidad**     | 3/5          | 5/5          | 5/5        |
| **Precisión**     | 5/5          | 5/5          | 4/5        |
| **Plugins**       | ✅ Muchos    | ❌ Limitados | ❌ Ninguno |
| **Comunidad**     | ⭐⭐⭐⭐⭐   | ⭐⭐⭐⭐     | ⭐⭐⭐     |
| **Documentación** | ⭐⭐⭐⭐⭐   | ⭐⭐⭐⭐     | ⭐⭐⭐     |
| **Strict Mode**   | ✅ Excelente | ✅ Excelente | ⚠️ Básico  |

## Casos de Uso Ideales para mypy

1. **Proyectos con Django/Flask**: Plugins maduros
1. **Codebases legacy**: Adopción gradual fácil
1. **Equipos grandes**: Documentación extensa
1. **Bibliotecas públicas**: Compatibilidad amplia
1. **CI/CD establecidos**: Integración probada

## Limitaciones y Desafíos

### Performance en Proyectos Grandes

```bash
# Proyecto de 100k LOC
mypy .  # 30-45 segundos (cold)
dmypy check .  # 2-5 segundos (warm)

# vs Pyright
pyright .  # 3-8 segundos (cold)
```

### Tipado de Decoradores

```python
from typing import Callable, TypeVar

F = TypeVar('F', bound=Callable)

def decorator(f: F) -> F:
    return f  # mypy a veces tiene problemas aquí
```

### Type Narrowing Limitado

```python
def process(x: int | str) -> None:
    if isinstance(x, int):
        print(x + 1)  # mypy OK
    else:
        print(x.upper())  # mypy OK

    # Pero casos complejos pueden confundir a mypy
```

## Best Practices 2026

1. **Use daemon mode** en desarrollo: `dmypy`
1. **Strict mode** para código nuevo
1. **Plugins** para frameworks populares
1. **Incremental** siempre habilitado
1. **CI/CD** con caching para velocidad

## Migración a Alternativas

### ¿Cuándo considerar Pyright?

- Necesitas máxima velocidad
- Trabajas en VS Code principalmente
- No usas plugins específicos de mypy
- Performance es crítica en CI/CD

### ¿Cuándo quedarse con mypy?

- Tienes plugins críticos (Django, Pydantic, SQLAlchemy)
- Codebase grande ya configurada con mypy
- Equipo familiarizado con mypy
- Documentación de mypy es valiosa

## Referencias

- [mypy Documentation](https://mypy.readthedocs.io/)
- [mypy GitHub](https://github.com/python/mypy)
- [Type System Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Common Issues](https://mypy.readthedocs.io/en/stable/common_issues.html)
- [Django Stubs](https://github.com/typeddjango/django-stubs)
- [Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/mypy/)
