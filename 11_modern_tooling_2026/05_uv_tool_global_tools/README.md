# uv tool: Herramientas CLI Globales

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

`uv tool` instala herramientas CLI de Python (como `ruff`, `mypy`, `black`, `httpie`) en entornos aislados sin contaminar el Python global del sistema. Cada herramienta obtiene su propio entorno virtual gestionado automáticamente por uv.

### Características Principales

- Instalación de herramientas en entornos completamente aislados
- Acceso global al binario sin activar ningún entorno virtual
- `uv tool run` (alias: `uvx`) ejecuta herramientas sin instalarlas permanentemente
- Actualización sencilla con `uv tool upgrade`
- Lista de herramientas instaladas con `uv tool list`

## 2. Aplicación Práctica

### Casos de Uso

- Instalar `ruff`, `mypy`, `black` como herramientas de desarrollo globales
- Ejecutar herramientas de forma efímera con `uvx` en scripts CI/CD
- Reemplazar `pipx` con una alternativa más rápida y compatible

### Ejemplo de Código

```bash
uv tool install ruff           # instalar ruff globalmente
uv tool install mypy           # instalar mypy globalmente
uv tool list                   # ver herramientas instaladas

uvx ruff check .               # ejecutar ruff sin instalar
uvx black --check src/         # verificar formato sin instalar black

uv tool upgrade ruff           # actualizar a la última versión
uv tool uninstall black        # desinstalar una herramienta
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Instalar herramientas CLI con `pip install --user` o en el entorno global contamina Python del sistema y genera conflictos de dependencias cuando distintas herramientas requieren versiones incompatibles de los mismos paquetes.

### Solución y Beneficios

- Aislamiento completo: cada herramienta tiene sus propias dependencias
- Binarios disponibles globalmente sin necesidad de activar entornos
- `uvx` permite probar herramientas sin instalarlas permanentemente
- Más rápido que `pipx` gracias a la implementación en Rust

## 4. Referencias

- https://docs.astral.sh/uv/guides/tools/
- https://docs.astral.sh/uv/reference/cli/#uv-tool
- https://github.com/astral-sh/uv
- https://pypa.github.io/pipx/
- https://docs.astral.sh/uv/concepts/tools/

## 5. Tarea Práctica

### Nivel Básico

Instala `ruff` con `uv tool install ruff`. Verifica que `ruff --version` funciona desde cualquier directorio. Luego usa `uvx mypy --version` sin instalar mypy permanentemente.

### Nivel Intermedio

Crea un script bash que use `uvx` para ejecutar `ruff check` y `mypy` en un proyecto sin requerir instalación previa. Documenta los tiempos de ejecución comparados con la instalación tradicional.

### Nivel Avanzado

Configura un workflow de GitHub Actions que utilice `uvx` para ejecutar todas las herramientas de calidad de código (ruff, mypy, bandit) sin un paso de instalación de dependencias explícito.

### Criterios de Éxito

- [ ] `ruff --version` y `mypy --version` funcionan globalmente tras instalar con `uv tool`
- [ ] `uvx ruff check .` ejecuta correctamente sin instalación previa
- [ ] Las herramientas instaladas no aparecen en `pip list` del entorno global
- [ ] `uv tool list` muestra todas las herramientas instaladas con sus versiones

## 6. Resumen

`uv tool` resuelve el problema clásico de instalar herramientas CLI de Python sin contaminar el entorno global. Con `uvx`, es posible ejecutar cualquier herramienta de forma efímera, haciendo que los pipelines CI/CD sean más limpios y reproducibles.

## 7. Reflexión

¿Cómo cambiaría tu flujo de trabajo si toda instalación de herramientas en tu equipo fuera con `uv tool`? ¿Qué ventajas tendría para la incorporación de nuevos desarrolladores?
