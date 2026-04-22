# Integración de Ruff en Workflows (pre-commit y CI/CD)

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

Integrar ruff en pre-commit y CI/CD garantiza que todo el código que entra al repositorio cumple los estándares de calidad definidos. Ruff ofrece hooks oficiales para pre-commit y funciona perfectamente como paso de CI/CD en GitHub Actions, GitLab CI y otros sistemas.

### Características Principales

- Hook oficial de ruff para pre-commit (`ruff-pre-commit`)
- Integración nativa con GitHub Actions mediante `astral-sh/ruff-action`
- Modo `--fix` para corrección automática en CI si se desea
- Soporte para `ruff check` y `ruff format` como pasos separados
- Salida compatible con formatos estándar de herramientas CI

## 2. Aplicación Práctica

### Casos de Uso

- Bloquear commits que no pasen el linting para mantener calidad en el repositorio
- Ejecutar análisis estático en cada pull request como gate de calidad
- Corrección automática de problemas simples en pre-commit sin esfuerzo manual

### Ejemplo de Código

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

```yaml
name: Lint
on: [push, pull_request]
jobs:
  ruff:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/ruff-action@v1
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin automatización, los estándares de código dependen de la disciplina individual de cada desarrollador. Es común que problemas detectables por análisis estático lleguen al repositorio y sean descubiertos tarde, en code review o incluso en producción.

### Solución y Beneficios

- Calidad garantizada automáticamente en cada commit y pull request
- Code reviews más focalizados en lógica de negocio, no en estilo
- Corrección automática de problemas mecánicos sin intervención manual
- Feedback inmediato al desarrollador en su flujo de trabajo local

## 4. Referencias

- https://docs.astral.sh/ruff/integrations/
- https://pre-commit.com/
- https://github.com/astral-sh/ruff-pre-commit
- https://github.com/astral-sh/ruff-action
- https://docs.astral.sh/ruff/editors/

## 5. Tarea Práctica

### Nivel Básico

Añade el hook de ruff a `.pre-commit-config.yaml` en tu proyecto. Ejecuta `pre-commit run --all-files` y observa los resultados. Asegúrate de que el hook bloquea commits con errores.

### Nivel Intermedio

Configura un workflow de GitHub Actions que ejecute `ruff check` y `ruff format --check` en cada pull request. El workflow debe fallar si hay errores de linting o formato.

### Nivel Avanzado

Implementa una estrategia de corrección automática en CI: usa `ruff --fix` y `ruff format`, luego `git commit --amend` o abre un PR automático con las correcciones. Evalúa los trade-offs de este enfoque.

### Criterios de Éxito

- [ ] El hook de pre-commit bloquea commits con errores de ruff
- [ ] El workflow de CI falla correctamente ante problemas de lint/formato
- [ ] Los tiempos del hook de pre-commit son menores a 2 segundos
- [ ] Los developers pueden saltar el hook con `--no-verify` cuando es necesario (emergencias)

## 6. Resumen

Integrar ruff en pre-commit y CI/CD convierte los estándares de calidad de código en una verificación automática y no negociable. La velocidad de ruff hace que estos checks sean prácticamente instantáneos, eliminando la fricción habitual de los hooks de pre-commit lentos.

## 7. Reflexión

¿Qué balance encontrarías entre checks automáticos que bloquean vs los que solo alertan? ¿Cuándo tiene sentido activar la corrección automática en CI?
