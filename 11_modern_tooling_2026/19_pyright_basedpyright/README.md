# Pyright y BasedPyright

## Pyright: El Type Checker de Microsoft

**Pyright** es un type checker estático para Python desarrollado por Microsoft, escrito en TypeScript/Node.js. Es la base del soporte de Python en VS Code (Pylance) y se ha convertido en el type checker más rápido del ecosistema en 2026.

## BasedPyright: El Fork Comunitario

**BasedPyright** es un fork mantenido por la comunidad que surgió en 2024, ofreciendo features adicionales y configuraciones más flexibles que Pyright oficial. En 2026, ambas herramientas conviven: Pyright para estabilidad corporativa, BasedPyright para innovación comunitaria.

## Diferencias Principales

### Pyright (Oficial - Microsoft)

**Ventajas:**
- ✅ Mantenimiento oficial de Microsoft
- ✅ Integración perfecta con VS Code/Pylance
- ✅ Conservador y estable
- ✅ Documentación oficial excelente

**Filosofía:** Prioriza estabilidad y compatibilidad con VS Code

### BasedPyright (Fork Comunitario)

**Ventajas adicionales:**
- ✅ Features experimentales más rápido
- ✅ Configuración más flexible
- ✅ Respuesta rápida a issues de la comunidad
- ✅ Reglas opcionales más estrictas
- ✅ Mejor soporte para casos edge

**Filosofía:** Innovación y respuesta rápida a necesidades de la comunidad

## Instalación

### Pyright

```bash
# Con npm (recomendado)
npm install -g pyright

# Con uv
uv tool install pyright

# Con pip
pip install pyright
```

### BasedPyright

```bash
# Con npm
npm install -g basedpyright

# Con uv
uv tool install basedpyright

# Con pip
pip install basedpyright
```

## Performance: El Factor Clave

### Benchmark: Django Codebase (~350k LOC)

```bash
# mypy
$ time mypy .
... 42.3s

# Pyright
$ time pyright .
... 3.8s

# BasedPyright
$ time basedpyright .
... 3.9s
```

**Pyright/BasedPyright son ~11x más rápidos que mypy**

### Watch Mode

```bash
# Pyright watch - re-check automático en cambios
pyright --watch

# Instantáneo gracias a análisis incremental
```

## Configuración

### pyrightconfig.json (o pyproject.toml)

```json
{
  "include": ["src"],
  "exclude": ["**/node_modules", "**/__pycache__", "tests"],
  
  "typeCheckingMode": "strict",
  
  "reportMissingImports": true,
  "reportMissingTypeStubs": true,
  "reportUnusedImport": "warning",
  "reportUnusedVariable": "warning",
  "reportDuplicateImport": "error",
  
  "pythonVersion": "3.13",
  "pythonPlatform": "Linux",
  
  "executionEnvironments": [
    {
      "root": "src",
      "pythonVersion": "3.13",
      "extraPaths": ["lib"]
    }
  ]
}
```

### En pyproject.toml

```toml
[tool.pyright]
include = ["src"]
exclude = ["**/__pycache__"]
typeCheckingMode = "strict"
reportMissingImports = true
reportUnusedImport = "warning"
pythonVersion = "3.13"
```

### BasedPyright Specific Config

```json
{
  "typeCheckingMode": "strict",
  
  // Features exclusivas de BasedPyright
  "enableExperimentalFeatures": true,
  "reportImplicitStringConcatenation": "warning",
  "reportShadowedImports": "error",
  
  // Configuraciones más granulares
  "reportIncompatibleVariableOverride": "error",
  "reportIncompatibleMethodOverride": "error"
}
```

## Type Checking Modes

### Basic Mode
```python
# Permite mucha flexibilidad
def function(x):  # OK - sin tipos
    return x + 1
```

### Standard Mode (Default)
```python
# Balance entre strict y permisive
def function(x: int):  # Parámetros deben tener tipos
    return x + 1  # Return type inferido
```

### Strict Mode (Recomendado)
```python
# Máxima rigurosidad
def function(x: int) -> int:  # Todos los tipos explícitos
    return x + 1
```

## Features Avanzados

### Type Narrowing Superior

```python
from typing import Literal

def process(x: int | str | None) -> str:
    if x is None:
        return "none"
    elif isinstance(x, int):
        return str(x)
    else:
        return x.upper()  # Pyright sabe que x: str aquí

# Type narrowing con Literal
def handle_mode(mode: Literal["read", "write"]) -> None:
    if mode == "read":
        # Pyright sabe que mode es exactamente "read"
        ...
```

### Union Type Analysis

```python
from typing import TypeGuard

def is_string_list(val: list[str] | list[int]) -> TypeGuard[list[str]]:
    return isinstance(val[0], str) if val else False

def process(items: list[str] | list[int]) -> None:
    if is_string_list(items):
        # Pyright sabe que items: list[str] aquí
        print(items[0].upper())
```

### Generic Type Inference

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
    
    def get(self) -> T:
        return self.value

# Pyright infiere tipos automáticamente
container = Container(42)  # Container[int]
x: int = container.get()   # ✓ OK
y: str = container.get()   # ✗ Error
```

## Integración con Editores

### VS Code (Pylance)

Pylance usa Pyright internamente:

```json
// settings.json
{
  "python.analysis.typeCheckingMode": "strict",
  "python.analysis.diagnosticMode": "workspace",
  "python.analysis.autoImportCompletions": true,
  "python.analysis.inlayHints.functionReturnTypes": true
}
```

### Neovim (LSP)

```lua
-- Con nvim-lspconfig
require('lspconfig').pyright.setup{
  settings = {
    python = {
      analysis = {
        typeCheckingMode = "strict",
        autoSearchPaths = true,
        useLibraryCodeForTypes = true
      }
    }
  }
}

-- O con BasedPyright
require('lspconfig').basedpyright.setup{...}
```

### Other Editors

- **Sublime Text**: LSP-pyright package
- **Emacs**: lsp-mode con pyright
- **Vim**: coc-pyright o ALE

## CLI Usage

```bash
# Check entire project
pyright

# Check specific files
pyright src/main.py tests/test_main.py

# Watch mode
pyright --watch

# Output formato JSON
pyright --outputjson

# Ver tipos inferidos
pyright --verbose

# Ignorar cache
pyright --skipunannotated
```

## BasedPyright Unique Features

### Better Error Messages

BasedPyright mejora los mensajes de error:

```python
# Pyright
# error: Argument of type "int" cannot be assigned to parameter "x" of type "str"

# BasedPyright
# error: Argument 'x' of type "int" cannot be assigned to parameter of type "str"
#   Expected type: str
#   Received type: int
#   Consider using: str(x)
```

### Enhanced Type Narrowing

```python
# BasedPyright entiende más patterns
def check(x: int | str | list) -> None:
    match x:
        case int():
            x + 1  # BasedPyright: x is int
        case str():
            x.upper()  # BasedPyright: x is str
        case list():
            len(x)  # BasedPyright: x is list
```

## Comparación mypy vs Pyright/BasedPyright

### Cuando Usar Pyright/BasedPyright

✅ **Prioridad**: Velocidad  
✅ **Editor**: VS Code  
✅ **Proyecto**: Nuevo o mediano  
✅ **Type narrowing**: Casos complejos  
✅ **CI/CD**: Builds rápidos críticos  

### Cuando Usar mypy

✅ **Plugins**: Django, SQLAlchemy, Pydantic  
✅ **Legacy**: Codebase grande existente  
✅ **Ecosystem**: Herramientas dependiendo de mypy  
✅ **Gradual**: Adopción incremental  

## Migración de mypy a Pyright

### Paso 1: Instalar y Probar

```bash
# Instalar
npm install -g pyright

# Probar sin cambiar nada
pyright .

# Comparar con mypy
mypy . > mypy_errors.txt
pyright . > pyright_errors.txt
diff mypy_errors.txt pyright_errors.txt
```

### Paso 2: Configurar

```toml
# pyproject.toml
[tool.pyright]
typeCheckingMode = "basic"  # Empezar permisivo
pythonVersion = "3.13"
```

### Paso 3: Incrementar Strictness

```toml
[tool.pyright]
typeCheckingMode = "standard"  # Luego standard
# typeCheckingMode = "strict"  # Finalmente strict
```

### Paso 4: CI/CD

```yaml
# .github/workflows/type-check.yml
- name: Type Check
  run: |
    npm install -g pyright
    pyright
```

## Best Practices 2026

1. **Strict mode** desde el inicio en proyectos nuevos
2. **Watch mode** en desarrollo para feedback instantáneo
3. **BasedPyright** para proyectos comunitarios innovadores
4. **Pyright** para proyectos corporativos estables
5. **CI/CD caching** de node_modules para velocidad

## Referencias

- [Pyright Documentation](https://microsoft.github.io/pyright/)
- [Pyright GitHub](https://github.com/microsoft/pyright)
- [BasedPyright Documentation](https://docs.basedpyright.com/)
- [BasedPyright GitHub](https://github.com/DetachHead/basedpyright)
- [Pylance (VS Code)](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
