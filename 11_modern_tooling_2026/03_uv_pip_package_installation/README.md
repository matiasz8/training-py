# uv pip: Instalación de Paquetes Ultrarrápida

## Introducción a uv pip

**uv pip** es el subcomando de uv que proporciona una interfaz compatible con pip tradicional, pero con velocidad de 10-100x superior. Es un drop-in replacement que puedes usar inmediatamente sin cambiar tus workflows existentes.

## Comandos Básicos

### Instalación de Paquetes

```bash
# Instalar un paquete
uv pip install requests

# Instalar versión específica
uv pip install requests==2.31.0

# Instalar desde requirements.txt
uv pip install -r requirements.txt

# Instalar múltiples paquetes
uv pip install requests flask pandas
```

### Instalación con Constraints

```bash
# Desde archivo de constraints
uv pip install -r requirements.txt -c constraints.txt

# Con rango de versiones
uv pip install "django>=4.0,<5.0"

# Con extras
uv pip install "fastapi[all]"
```

## Velocidad y Optimizaciones

### Descarga Paralela

uv descarga múltiples paquetes simultáneamente usando workers concurrentes en Rust. Esto es especialmente notable en proyectos con muchas dependencias.

### Caché Inteligente

La caché global de uv significa que:

- Primera instalación: Descarga desde PyPI
- Instalaciones subsecuentes: Instantáneas desde caché
- Compartida entre todos los proyectos

### Resolución Rápida

El algoritmo PubGrub detecta conflictos tempranamente, ahorrando tiempo en casos de dependencias incompatibles.

## Compatibilidad con pip

uv pip mantiene compatibilidad casi completa con pip:

```bash
# Estos comandos funcionan igual
uv pip list
uv pip show requests
uv pip freeze
uv pip uninstall requests
uv pip install --upgrade requests
```

## Características Avanzadas

### Compilación desde Source

```bash
# Forzar compilación
uv pip install --no-binary :all: numpy

# Evitar binarios específicos
uv pip install --no-binary scipy numpy
```

### Índices Personalizados

```bash
# Índice alternativo
uv pip install --index-url https://custom.pypi.org/simple requests

# Índices múltiples
uv pip install --extra-index-url https://private.org/simple requests
```

### Instalación Editable

```bash
# Para desarrollo
uv pip install -e .
uv pip install -e ".[dev,test]"
```

## Comandos de Gestión

### Listar y Buscar

```bash
# Listar paquetes instalados
uv pip list

# Ver dependencias de un paquete
uv pip show flask

# Generar requirements.txt
uv pip freeze > requirements.txt
```

### Actualización y Limpieza

```bash
# Actualizar un paquete
uv pip install --upgrade requests

# Actualizar todo
uv pip install --upgrade -r requirements.txt

# Desinstalar
uv pip uninstall requests

# Desinstalar todo de requirements
uv pip uninstall -r requirements.txt
```

## Compilación de Dependencias

uv pip compile genera archivos de lock con versiones resueltas:

```bash
# Compilar requirements.txt a versiones exactas
uv pip compile requirements.in -o requirements.txt

# Con múltiples archivos
uv pip compile requirements.in dev-requirements.in -o requirements.txt

# Con Python específico
uv pip compile --python-version 3.12 requirements.in
```

## Sincronización de Entornos

```bash
# Sincronizar entorno con requirements.txt exacto
uv pip sync requirements.txt

# Esto:
# 1. Instala paquetes que faltan
# 2. Desinstala paquetes extra
# 3. Actualiza versiones incorrectas
```

## Comparación de Rendimiento

| Operación                    | pip | uv pip | Mejora |
| ---------------------------- | --- | ------ | ------ |
| Install 50 packages (cold)   | 45s | 5s     | 9x     |
| Install 50 packages (cached) | 30s | 0.5s   | 60x    |
| Resolve complex dependencies | 20s | 2s     | 10x    |
| pip freeze                   | 1s  | 0.1s   | 10x    |

## Best Practices

1. **Use uv pip compile**: Para reproducibilidad
1. **Especifique versiones**: En producción use versiones exactas
1. **Aproveche la caché**: Reutilice la caché en CI/CD
1. **Separate concerns**: `requirements.in` para dependencias directas, `requirements.txt` para todas

## Troubleshooting

```bash
# Ver qué está haciendo uv
uv pip install -v requests

# Máxima verbosidad
uv pip install -vv requests

# Ignorar caché
uv pip install --refresh requests

# Ver packages resueltos sin instalar
uv pip compile --dry-run requirements.in
```

## Referencias

- [uv pip Documentation](https://docs.astral.sh/uv/pip/)
- [uv pip Compatibility](https://docs.astral.sh/uv/pip/compatibility/)
- [pip-tools Migration Guide](https://docs.astral.sh/uv/guides/pip-tools/)
