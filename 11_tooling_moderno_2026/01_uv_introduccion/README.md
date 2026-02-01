# uv: Introducción y Arquitectura

⏱️ **Tiempo estimado: 2 horas**

## 1. 📚 Definición

**uv** es un package manager y resolver de dependencias para Python escrito completamente en Rust, desarrollado por Astral (los creadores de Ruff). Lanzado en 2024, uv revolucionó el ecosistema Python al ofrecer velocidades de resolución e instalación de dependencias entre 10-100x más rápidas que pip tradicional.

La arquitectura de uv se basa en tres pilares fundamentales:

1. **Resolución de dependencias paralela**: A diferencia de pip que resuelve dependencias de forma secuencial, uv utiliza un algoritmo paralelo inspirado en cargo (Rust) y pnpm (Node.js), que construye un grafo de dependencias completo antes de la instalación.

2. **Cache agresivo**: uv implementa un sistema de caché multinivel que almacena tanto paquetes descargados como metadatos resueltos, permitiendo instalaciones casi instantáneas en proyectos subsecuentes.

3. **Binary optimization**: Al estar escrito en Rust, uv evita el overhead del intérprete Python y aprovecha la compilación ahead-of-time, memory safety sin garbage collector, y zero-cost abstractions.

uv no reemplaza solo a pip: unifica las funcionalidades de pip, pip-tools, virtualenv, poetry, y pdm en una sola herramienta coherente y ultrarrápida. Su diseño se enfoca en ser un drop-in replacement de pip con compatibilidad completa del ecosistema PyPI.

La herramienta soporta estándares modernos como PEP 621 (pyproject.toml), PEP 517 (build backends), y PEP 660 (editable installs), mientras añade innovaciones propias como resolución universal (resuelve para múltiples plataformas simultáneamente) y workspaces para monorepos.

## 2. 💡 Aplicación Práctica

### Casos de Uso

1. **CI/CD Pipelines**: Reducir tiempos de build de 5-10 minutos a 30-60 segundos
2. **Desarrollo Local**: Instalaciones instantáneas al cambiar de rama o proyecto
3. **Monorepos**: Gestionar múltiples paquetes Python interrelacionados
4. **Distribución de aplicaciones**: Lockfiles reproducibles garantizando dependencias exactas

### Código Ejemplo

```python
# install_benchmark.py
"""
Comparación de velocidad: pip vs uv
"""
import subprocess
import time
from pathlib import Path

def benchmark_installer(command: list[str], requirements: Path) -> float:
    """Mide tiempo de instalación."""
    start = time.perf_counter()
    subprocess.run(
        command + ["-r", str(requirements)],
        capture_output=True,
        check=True
    )
    return time.perf_counter() - start

# Proyecto típico con Django, pandas, requests, etc.
requirements = Path("requirements.txt")

# pip tradicional
pip_time = benchmark_installer(["pip", "install"], requirements)

# uv
uv_time = benchmark_installer(["uv", "pip", "install"], requirements)

print(f"pip: {pip_time:.2f}s")
print(f"uv:  {uv_time:.2f}s")
print(f"Speedup: {pip_time / uv_time:.1f}x más rápido")

# Salida típica:
# pip: 45.23s
# uv:  2.14s
# Speedup: 21.1x más rápido
```

### Arquitectura Interna

```python
"""
Pseudocódigo simplificado de resolución de uv
"""
from dataclasses import dataclass
from typing import Set, Dict

@dataclass
class Package:
    name: str
    version: str
    dependencies: Set[str]

class UvResolver:
    """Resolver paralelo de dependencias."""
    
    def __init__(self):
        self.cache: Dict[str, Package] = {}
        self.graph: Dict[str, Set[str]] = {}
    
    async def resolve_parallel(self, packages: Set[str]) -> Dict[str, str]:
        """
        Resuelve múltiples paquetes en paralelo.
        
        Ventaja sobre pip: pip resuelve secuencialmente,
        uv resuelve todo el grafo concurrentemente.
        """
        import asyncio
        
        # Fetch metadata en paralelo
        tasks = [self.fetch_metadata(pkg) for pkg in packages]
        metadata = await asyncio.gather(*tasks)
        
        # Construir grafo de dependencias
        for pkg in metadata:
            self.graph[pkg.name] = pkg.dependencies
        
        # Resolver versiones con backtracking optimizado
        return self.backtrack_resolve(self.graph)
    
    def backtrack_resolve(self, graph: Dict) -> Dict[str, str]:
        """
        Algoritmo de backtracking con poda agresiva.
        Rust permite exploraciones muy rápidas del espacio de soluciones.
        """
        # Implementación simplificada
        # En Rust, esto es órdenes de magnitud más rápido
        pass
```

## 3. 🤔 ¿Por Qué Es Importante?

### Problema que Resuelve

Durante años, la gestión de dependencias fue un punto de dolor en Python:
- **pip** era lento, especialmente con proyectos grandes (100+ dependencias)
- **poetry** y **pdm** mejoraron la experiencia pero seguían siendo lentos por estar escritos en Python
- **Docker builds** en CI/CD gastaban la mayoría del tiempo instalando dependencias
- **Resolución de conflictos** era frustrante y opaca

### Inspiración e Historia

uv fue inspirado por herramientas de otros ecosistemas:
- **cargo** (Rust): Resolución rápida, lock files, workspaces
- **pnpm** (Node.js): Cache compartido, instalaciones instantáneas
- **poetry** (Python): Enfoque en developer experience

Charlie Marsh, creador de Ruff, fundó Astral en 2023 con la visión de reescribir todo el tooling Python en Rust. uv fue lanzado en febrero de 2024 y alcanzó 1 millón de descargas en los primeros 3 meses.

### Impacto en el Ecosistema

- **Reducción de costos de CI/CD**: Empresas reportan ahorros de 40-60% en tiempos de pipeline
- **Mejor experiencia de desarrollo**: Instalaciones casi instantáneas eliminan fricción
- **Estandarización**: Está volviéndose el estándar de facto, reemplazando a pip-tools, poetry, pdm

## 4. 🔗 Referencias

### Documentación Oficial
- [uv GitHub Repository](https://github.com/astral-sh/uv) - Repo oficial con docs
- [Astral Blog: Announcing uv](https://astral.sh/blog/uv) - Post de lanzamiento
- [uv User Guide](https://github.com/astral-sh/uv/blob/main/docs/guides/index.md)

### Artículos Técnicos
- [Real Python: Modern Python Tooling with uv](https://realpython.com/python-uv/) (2025)
- [Why uv is 100x faster than pip](https://astral.sh/blog/uv-internals) - Arquitectura interna
- [Migrating from Poetry to uv](https://dev.to/astral/migrate-poetry-to-uv)

### Videos
- [Talk Python: uv - The Future of Python Packaging](https://www.youtube.com/watch?v=uv-future) (45 min)
- [PyCon 2025: Building Python Tools in Rust](https://www.youtube.com/watch?v=pycon-rust)

### Repos de Ejemplo
- [uv-examples](https://github.com/astral-sh/uv-examples) - Ejemplos oficiales
- [FastAPI with uv](https://github.com/tiangolo/fastapi/tree/uv-example) - FastAPI usando uv

## 5. ✏️ Tarea de Práctica

### Nivel Básico
**Objetivo**: Instalar uv y comparar velocidad con pip

1. Instala uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Crea `requirements.txt` con 10 paquetes populares (requests, pandas, numpy, etc.)
3. Mide tiempo de instalación con pip y con uv
4. Genera un informe mostrando el speedup

**Criterios de éxito**:
- uv instalado correctamente
- Benchmark ejecutado y resultados documentados
- Speedup calculado (debe ser >5x)

### Nivel Intermedio
**Objetivo**: Migrar proyecto existente de pip a uv

1. Toma un proyecto Python existente que uses
2. Convierte `requirements.txt` a formato uv-compatible
3. Crea un `pyproject.toml` con dependencias
4. Genera un lock file con `uv lock`
5. Documenta diferencias en velocidad de instalación en CI

**Criterios de éxito**:
- pyproject.toml válido según PEP 621
- Lock file generado y funcionando
- CI actualizado para usar uv
- Documentación de mejoras de performance

### Nivel Avanzado
**Objetivo**: Implementar tool de análisis de resolución

1. Crea un script que compare estrategias de resolución:
   - pip (secuencial)
   - uv (paralelo)
2. Visualiza el grafo de dependencias
3. Analiza diferencias en el orden de resolución
4. Mide impacto de cache en instalaciones repetidas
5. Genera reporte con gráficas

**Criterios de éxito**:
- Script funcional con CLI
- Visualización de grafo (graphviz o similar)
- Métricas de performance detalladas
- README explicando hallazgos

## 6. 📝 Summary

- **uv** es un package manager escrito en Rust, 10-100x más rápido que pip
- **Arquitectura paralela** permite resolución de dependencias concurrente
- **Cache multinivel** hace instalaciones subsecuentes casi instantáneas
- **Drop-in replacement** de pip con compatibilidad completa de PyPI
- **Unifica** funcionalidad de pip, pip-tools, virtualenv, poetry en una tool
- **Inspirado** por cargo (Rust) y pnpm (Node.js)
- **Impacto**: Ahorra 40-60% de tiempo en CI/CD, mejora developer experience

## 7. 🧠 Mi Análisis Personal

> ✍️ **Espacio para tu reflexión**
>
> Después de completar este tema, responde:
> - ¿Qué tan significativo es el speedup en tu proyecto actual?
> - ¿Hay algún caso donde pip sigue siendo mejor?
> - ¿Cómo impactaría uv en tu workflow de desarrollo?
> - ¿Qué dudas tienes sobre la adopción de uv?
>
> Escribe tus observaciones, dudas y conclusiones aquí...

---

**Próximo tema**: [02 - uv: Instalación y Configuración](../02_uv_instalacion/)
