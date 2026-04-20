# Exploratory Analysis

Tiempo estimado: 2-3 hours

## 1. Definición

Exploratory Analysis organiza un primer recorrido por el dataset para detectar patrones, extremos y preguntas nuevas.

### Características Clave

- Resume variables numéricas y categóricas rápidamente.
- Busca anomalías antes de profundizar en modelado.
- Conecta métricas descriptivas con hipótesis de negocio.
- Produce insumos claros para gráficos y decisiones posteriores.

## 2. Aplicación Práctica

### Casos de Uso

1. Revisar comportamiento de ventas por región y canal.
1. Detectar rangos atípicos antes de entrenar un modelo.
1. Priorizar preguntas para una visualización posterior.

### Ejemplo de Código

Revisa `examples/example_basic.py` para ver una implementación ejecutable enfocada en exploratory analysis.

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin exploración inicial, es fácil construir dashboards o modelos sobre supuestos erróneos y sesgos ocultos.

### Solución y Beneficios

- Ayuda a formular preguntas mejores antes de automatizar.
- Hace visibles outliers, skew y gaps de información.
- Reduce el costo de corregir decisiones tardías.

### Errores Comunes

- Confundir descripción con causalidad.
- Enamorarse de una sola métrica resumen.
- No separar hallazgos observados de conclusiones definitivas.

## 4. Referencias

Consulta `references/links.md` para documentación oficial y material de profundización.

## 5. Tarea Práctica

Usa `exercises/exercise_01.py` como punto de partida. El foco del ejercicio es: Construye un reporte breve de EDA con estadísticos numéricos y una categoría dominante.

### Nivel Básico

- Implementa la funcionalidad principal solicitada.
- Haz que el caso nominal quede cubierto por tests.

### Nivel Intermedio

- Valida inputs inválidos o casos borde relevantes.
- Refactoriza para que los nombres y pasos queden explícitos.

### Nivel Avanzado

- Agrega una variante reusable o una validación extra útil para producción.
- Documenta la decisión técnica clave de tu solución.

### Criterios de Éxito

- La solución produce el resultado esperado con datos representativos.
- `tests/test_basic.py` te orienta sobre el contrato mínimo a respetar.
- El código final es claro para otra persona del equipo.

## 6. Resumen

- EDA guía qué mirar antes de profundizar.
- El valor está en combinar números, contexto y preguntas.
- Un reporte pequeño bien armado puede destrabar muchos siguientes pasos.

## 7. Prompt de Reflexión

- ¿Qué hallazgo cambiaría una decisión de negocio?
- ¿Qué métrica te pareció menos informativa de lo esperado?
- ¿Qué gráfico construirías después de este reporte?
