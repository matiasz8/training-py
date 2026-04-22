# Pre-commit: Configuración y Hooks Esenciales

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

pre-commit es un framework para gestionar y ejecutar hooks de Git que se ejecutan automáticamente antes de cada commit. Los hooks verifican y corrigen el código localmente, asegurando que solo código que pasa todos los checks llega al repositorio, sin depender únicamente del CI/CD.

### Características Principales

- Configuración en `.pre-commit-config.yaml` versionada con el proyecto
- Gestión automática de entornos aislados para cada hook
- Hooks disponibles para ruff, mypy, bandit, detect-secrets y más
- Ejecución en todos los archivos con `pre-commit run --all-files`
- Cache inteligente: solo re-ejecuta hooks en archivos modificados

## 2. Aplicación Práctica

### Casos de Uso

- Verificar formato y linting antes de cada commit sin disciplina manual
- Detectar secretos accidentales en código antes de que lleguen al repositorio
- Asegurar que los tests unitarios pasan antes de compartir el código

### Ejemplo de Código

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-merge-conflict
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin pre-commit, la calidad del código depende de que cada developer recuerde ejecutar el linter y el formatter antes de cada commit. Los commits con código sucio generan ruido en las reviews y problemas en CI/CD que hubieran podido detectarse localmente.

### Solución y Beneficios

- Aplicación automática e inevitable de estándares de calidad en cada commit
- Feedback instantáneo al developer: el problema se detecta antes de llegar al repositorio
- Reducción de ciclos de CI/CD fallidos por problemas de formato o linting triviales
- Configuración compartida garantiza el mismo comportamiento en todos los equipos

## 4. Referencias

- https://pre-commit.com/
- https://pre-commit.com/hooks.html
- https://github.com/pre-commit/pre-commit-hooks
- https://docs.astral.sh/ruff/integrations/#pre-commit
- https://pre-commit.ci/

## 5. Tarea Práctica

### Nivel Básico

Instala pre-commit con `uv tool install pre-commit`. Crea un `.pre-commit-config.yaml` con ruff y los hooks básicos de pre-commit-hooks. Ejecuta `pre-commit install` y luego intenta hacer un commit con código mal formateado.

### Nivel Intermedio

Añade hooks para mypy y trailing-whitespace. Configura `pre-commit run --all-files` en el CI/CD como verificación adicional. Mide cuánto tarda la ejecución completa de todos los hooks.

### Nivel Avanzado

Configura pre-commit.ci para que los hooks se ejecuten automáticamente en cada PR de GitHub y auto-corrijan problemas simples abriendo un commit adicional en la rama del PR.

### Criterios de Éxito

- [ ] `pre-commit install` está configurado en el onboarding del proyecto
- [ ] Los hooks rechazan commits con errores de linting o formato
- [ ] `pre-commit run --all-files` completa en menos de 30 segundos
- [ ] El archivo `.pre-commit-config.yaml` está versionado en el repositorio

## 6. Resumen

pre-commit transforma los estándares de código de recomendaciones opcionales a requisitos automáticos. Al ejecutarse localmente antes del commit, proporciona feedback inmediato y reduce la carga sobre el CI/CD, que puede centrarse en verificaciones más complejas.

## 7. Reflexión

¿Cómo afectaría pre-commit al flujo de trabajo de tu equipo? ¿Qué hooks priorizarías para equilibrar utilidad con tiempo de ejecución?
