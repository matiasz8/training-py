# pytest-cov y Análisis de Coverage

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

`pytest-cov` es el plugin de pytest que integra `coverage.py` para medir qué porcentaje del código fuente es ejecutado durante los tests. Proporciona métricas de cobertura por archivo, rama y línea, ayudando a identificar código sin tests y áreas de riesgo en la base de código.

### Características Principales

- Integración nativa con pytest: ejecuta coverage en el mismo comando
- Cobertura de ramas (`--cov-branch`) para detectar caminos condicionales no testeados
- Múltiples formatos de reporte: terminal, HTML interactivo, XML para CI/CD
- Umbral mínimo de cobertura con `--cov-fail-under=80` para bloquear CI
- Configuración en `pyproject.toml` bajo `[tool.coverage]`

## 2. Aplicación Práctica

### Casos de Uso

- Establecer un umbral mínimo de cobertura que debe mantenerse en el proyecto
- Identificar módulos críticos sin tests antes de hacer un deploy
- Generar reportes HTML para revisiones de calidad del equipo

### Ejemplo de Código

```bash
pytest --cov=src/ --cov-report=term-missing
pytest --cov=src/ --cov-report=html --cov-branch
pytest --cov=src/ --cov-fail-under=80
```

```toml
[tool.coverage.run]
source = ["src"]
branch = true
omit = ["tests/*", "*/migrations/*"]

[tool.coverage.report]
fail_under = 80
show_missing = true
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin métricas de cobertura, es fácil tener una suite de tests que parece completa pero deja sin probar ramas de código críticas (manejo de errores, casos edge, código de seguridad). Los bugs en código no cubierto solo aparecen en producción.

### Solución y Beneficios

- Visibilidad objetiva sobre qué código está siendo verificado por los tests
- Identificación de dead code que nunca se ejecuta
- Umbrales de CI que previenen que la cobertura disminuya con nuevas funcionalidades
- Reportes HTML que facilitan la revisión del equipo en sprint reviews

## 4. Referencias

- https://pytest-cov.readthedocs.io/en/latest/
- https://coverage.readthedocs.io/en/latest/
- https://coverage.readthedocs.io/en/latest/branch.html
- https://docs.pytest.org/en/stable/how-to/plugins.html
- https://github.com/pytest-dev/pytest-cov

## 5. Tarea Práctica

### Nivel Básico

Ejecuta `pytest --cov=src/ --cov-report=term-missing` en tu proyecto. Identifica los archivos con menor cobertura y los números de línea faltantes según el reporte.

### Nivel Intermedio

Activa la cobertura de ramas con `--cov-branch`. Analiza el reporte HTML. Escribe tests específicamente para cubrir al menos 2 ramas de código que estaban sin cubrir.

### Nivel Avanzado

Configura un umbral de cobertura del 80% en CI/CD que bloquee merges si la cobertura cae. Añade un step que genere y publica el reporte HTML como artefacto del pipeline.

### Criterios de Éxito

- [ ] La cobertura global del proyecto es visible y superior al umbral configurado
- [ ] `--cov-fail-under` bloquea el CI cuando la cobertura cae debajo del umbral
- [ ] La cobertura de ramas está activada y el reporte muestra ramas no cubiertas
- [ ] El reporte HTML está disponible como artefacto en el pipeline CI/CD

## 6. Resumen

`pytest-cov` convierte la cobertura de tests de una métrica opcional a una garantía medible de calidad. La cobertura de ramas, más rigurosa que la cobertura de líneas, detecta condiciones lógicas no probadas que son fuente frecuente de bugs en producción.

## 7. Reflexión

¿Qué nivel de cobertura es razonable para tu proyecto? ¿Qué riesgos ves en perseguir el 100% de cobertura vs un umbral más realista del 80%?
