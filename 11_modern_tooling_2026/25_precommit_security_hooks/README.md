# Hooks de Seguridad en Pre-commit

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

Los hooks de seguridad en pre-commit detectan automáticamente vulnerabilidades comunes antes de que lleguen al repositorio: secretos hardcodeados, dependencias con vulnerabilidades conocidas, y patrones de código inseguro. Herramientas como `detect-secrets`, `bandit` y `safety` se integran perfectamente como hooks de pre-commit.

### Características Principales

- `detect-secrets`: detecta claves API, contraseñas y tokens hardcodeados
- `bandit` (via ruff `S` rules o hook directo): análisis de seguridad estático
- `safety` / `pip-audit`: verifica dependencias con CVEs conocidos
- Baseline de secretos para marcar falsos positivos de forma auditada
- Bloqueo de commits con problemas de seguridad hasta que se resuelvan

## 2. Aplicación Práctica

### Casos de Uso

- Prevenir la publicación accidental de claves AWS, tokens GitHub, contraseñas de BD
- Detectar patrones inseguros como `eval()`, `exec()` o deserialización peligrosa
- Verificar que ninguna dependencia instalada tiene CVEs críticos conocidos

### Ejemplo de Código

```yaml
repos:
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: [--baseline, .secrets.baseline]

  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.8
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]

  - repo: local
    hooks:
      - id: pip-audit
        name: pip-audit
        entry: pip-audit
        language: system
        pass_filenames: false
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Los secretos hardcodeados en código son una de las causas más comunes de brechas de seguridad. Una vez que un secreto llega al historial de Git, aunque se elimine después, puede haber sido copiado. El daño ocurre en el momento del push, no después.

### Solución y Beneficios

- Prevención proactiva: el secreto nunca llega al repositorio ni al historial
- Reducción del riesgo de brechas de seguridad por errores humanos
- Cumplimiento facilitado con requisitos de seguridad (SOC 2, ISO 27001)
- Auditoría clara de secretos conocidos mediante el archivo `.secrets.baseline`

## 4. Referencias

- https://github.com/Yelp/detect-secrets
- https://bandit.readthedocs.io/en/latest/
- https://pypi.org/project/pip-audit/
- https://pre-commit.com/hooks.html
- https://owasp.org/www-project-top-ten/

## 5. Tarea Práctica

### Nivel Básico

Configura `detect-secrets` en `.pre-commit-config.yaml`. Genera el baseline con `detect-secrets scan > .secrets.baseline`. Intenta hacer un commit con una clave API fake e intenta que sea detectada.

### Nivel Intermedio

Añade bandit como hook de pre-commit configurado desde `pyproject.toml`. Introduce un patrón inseguro (`subprocess` con `shell=True`) y verifica que bandit lo detecta y bloquea el commit.

### Nivel Avanzado

Implementa un proceso completo de gestión de secretos: detect-secrets para prevención, `.secrets.baseline` para falsos positivos auditados y documentados, y pip-audit integrado en CI/CD para vulnerabilidades de dependencias.

### Criterios de Éxito

- [ ] detect-secrets bloquea un commit con un token o clave API hardcodeada
- [ ] El archivo `.secrets.baseline` existe, está versionado y documenta los falsos positivos
- [ ] bandit no reporta vulnerabilidades de severidad alta o media en el código propio
- [ ] pip-audit no reporta CVEs críticos en las dependencias del proyecto

## 6. Resumen

Los hooks de seguridad en pre-commit crean una primera línea de defensa automatizada contra errores de seguridad comunes. La clave está en configurarlos al inicio del proyecto, no cuando ya ha ocurrido un incidente. Prevenir es siempre menos costoso que remediar.

## 7. Reflexión

¿Qué tipos de secretos son más probables de aparecer accidentalmente en tu código? ¿Cómo educarías a tu equipo sobre seguridad en commits sin crear fricción excesiva?
