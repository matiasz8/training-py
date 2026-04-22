# Performance y Caching de Hooks pre-commit

⏱️ **Tiempo estimado: 1 hora**

## 1. Definición

pre-commit incluye un sistema de caching que evita reinstalar entornos de hooks y re-ejecutar hooks en archivos que no han cambiado. Optimizar este caching y configurar correctamente los hooks puede reducir el tiempo de ejecución de pre-commit de decenas de segundos a apenas 1-2 segundos en workflows típicos.

### Características Principales

- Cache de entornos en `~/.cache/pre-commit`: solo instala hooks nuevos o actualizados
- `stages`: controla cuándo se ejecuta cada hook (commit, push, manual)
- `pass_filenames: false` para hooks que analizan el proyecto completo, no archivos individuales
- `types` y `files`: filtran qué archivos activan cada hook para minimizar ejecuciones
- `skip` con variable de entorno `SKIP` para deshabilitar hooks en situaciones especiales

## 2. Aplicación Práctica

### Casos de Uso

- Reducir el tiempo de hooks de 30+ segundos a < 5 segundos con caching y filtros correctos
- Separar hooks rápidos (en commit) de hooks lentos (en push) para no bloquear el flujo
- Persistir el cache de pre-commit en CI/CD para acelerar pipelines

### Ejemplo de Código

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.0
    hooks:
      - id: ruff
        stages: [commit]          # solo en commit, no en push
        types: [python]           # solo archivos Python

  - repo: local
    hooks:
      - id: mypy-slow
        stages: [push]            # solo al hacer push (más lento)
        pass_filenames: false
        entry: mypy src/
        language: system
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Los hooks lentos generan fricción: los developers empiezan a saltarse pre-commit con `--no-verify` cuando tardan demasiado. Un pre-commit que tarda 30 segundos destruye el flujo de trabajo. El balance entre cobertura y velocidad es fundamental para la adopción del equipo.

### Solución y Beneficios

- Hooks rápidos en commit mantienen el flujo de trabajo sin fricción
- Hooks exhaustivos en push para verificaciones más completas y lentas
- Cache en CI/CD evita reinstalar entornos en cada run del pipeline
- Configuración por tipo de archivo reduce ejecuciones innecesarias

## 4. Referencias

- https://pre-commit.com/
- https://pre-commit.com/#filtering-files-with-types
- https://pre-commit.com/#confining-hooks-to-run-at-certain-stages
- https://pre-commit.ci/
- https://github.com/actions/cache

## 5. Tarea Práctica

### Nivel Básico

Mide el tiempo actual de `pre-commit run --all-files` en tu proyecto. Identifica cuál es el hook más lento usando `pre-commit run --hook-stage commit --verbose`.

### Nivel Intermedio

Configura `stages` para separar hooks de commit (rápidos) y push (lentos como mypy). Verifica que el tiempo en commit se reduce significativamente. Añade `types: [python]` a los hooks de Python.

### Nivel Avanzado

Configura caching de pre-commit en GitHub Actions usando `actions/cache` con la clave `~/.cache/pre-commit`. Mide el tiempo de instalación del primer run vs runs subsiguientes con cache.

### Criterios de Éxito

- [ ] `pre-commit run` en commit completa en menos de 5 segundos
- [ ] Los hooks lentos están configurados en stage `push`, no en `commit`
- [ ] El cache de pre-commit está configurado en CI/CD y se reutiliza entre runs
- [ ] Ningún developer en el equipo usa `--no-verify` de forma habitual

## 6. Resumen

La performance de pre-commit es tan importante como su funcionalidad: un framework de hooks que nadie usa porque es demasiado lento no cumple su propósito. Invertir tiempo en optimizar el caching y la configuración de stages garantiza la adopción sostenida por el equipo.

## 7. Reflexión

¿Cuál sería el tiempo máximo aceptable para tus hooks de pre-commit sin generar fricción en el equipo? ¿Cómo medirías y comunicarías las mejoras de performance a tus compañeros?
