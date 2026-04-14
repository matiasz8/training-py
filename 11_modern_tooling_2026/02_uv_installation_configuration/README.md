# uv: Instalación y Configuración Inicial

## Instalación de uv

**uv** se distribuye como un binario único sin dependencias, lo que simplifica enormemente su instalación en comparación con herramientas Python tradicionales que requieren un intérprete Python preexistente.

## Métodos de Instalación

### Linux y macOS (Recomendado)

El método oficial utiliza el instalador de Astral:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Este script:
1. Detecta tu sistema operativo y arquitectura
2. Descarga el binario apropiado desde GitHub Releases
3. Lo instala en `~/.local/bin/` (o `~/.cargo/bin/` si usas Rust)
4. Actualiza tu PATH automáticamente

### Instalación Manual

Si prefieres controlar el proceso:

```bash
# Descargar binario
wget https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-unknown-linux-gnu.tar.gz

# Extraer e instalar
tar xzf uv-*.tar.gz
mv uv ~/.local/bin/
chmod +x ~/.local/bin/uv
```

### Windows

```powershell
# Con PowerShell
irm https://astral.sh/uv/install.ps1 | iex

# O con winget
winget install astral-sh.uv
```

### Con Cargo (Rust)

Si ya tienes Rust instalado:

```bash
cargo install uv
```

## Configuración Inicial

### Variables de Entorno

uv respeta varias variables de entorno para personalizar su comportamiento:

```bash
# Ubicación de la caché
export UV_CACHE_DIR=~/.cache/uv

# Nivel de verbosidad
export UV_VERBOSE=1

# Usar índice de paquetes personalizado
export UV_INDEX_URL=https://pypi.org/simple

# Caché HTTP para paquetes
export UV_HTTP_TIMEOUT=30

# Número de workers para descarga paralela
export UV_CONCURRENT_DOWNLOADS=8
```

### Archivo de Configuración

uv puede configurarse mediante `pyproject.toml` o archivos de configuración dedicados:

**`.uv/config.toml`** (local al proyecto):

```toml
[tool.uv]
index-url = "https://pypi.org/simple"
extra-index-url = ["https://private.pypi.org/simple"]

[tool.uv.pip]
no-binary = ["scipy"]  # Compilar desde source
only-binary = [":all:"]  # Solo usar wheels

[tool.uv.resolution]
prerelease = "disallow"
```

## Verificación de la Instalación

```bash
# Versión instalada
uv version

# Ubicación del binario
which uv

# Ayuda general
uv --help

# Comandos disponibles
uv --help | grep "Commands:"
```

## Comandos Principales

uv organiza su funcionalidad en subcomandos:

| Comando | Propósito |
|---------|-----------|
| `uv pip` | Gestión de paquetes (compatible con pip) |
| `uv venv` | Creación de entornos virtuales |
| `uv tool` | Instalación de herramientas globales |
| `uv cache` | Gestión de caché |
| `uv self` | Auto-actualización de uv |

## Actualización de uv

```bash
# Auto-actualización
uv self update

# Verificar nueva versión
uv self update --check
```

## Integración con el Sistema

### Shell Completion

```bash
# Bash
uv generate-shell-completion bash > ~/.local/share/bash-completion/completions/uv

# Zsh
uv generate-shell-completion zsh > ~/.zfunc/_uv

# Fish
uv generate-shell-completion fish > ~/.config/fish/completions/uv.fish
```

### Integración con Editores

uv funciona transparentemente con editores que usan entornos virtuales estándar. No requiere plugins especiales.

## Best Practices

1. **Caché Global**: Mantén la caché en una ubicación estable
2. **Variables de Entorno**: Configura en tu `~/.bashrc` o `~/.zshrc`
3. **Actualizaciones**: Mantén uv actualizado con `uv self update`
4. **Mirroring**: Configura mirrors si tu red lo requiere

## Troubleshooting

### Problemas Comunes

```bash
# Limpiar caché si hay problemas
uv cache clean

# Verbosidad máxima para debugging
uv -vv pip install <package>

# Ver qué está haciendo uv
UV_LOG=debug uv pip install <package>
```

## Referencias

- [Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)
- [Configuration Reference](https://docs.astral.sh/uv/configuration/)
- [Environment Variables](https://docs.astral.sh/uv/reference/environment/)
