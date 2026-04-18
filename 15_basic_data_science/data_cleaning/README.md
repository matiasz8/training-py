# Data Cleaning

Tiempo estimado: 2-3 hours

## 1. Definición

Data Cleaning se enfoca en estandarizar columnas, tratar valores faltantes y remover inconsistencias antes del análisis.

### Características Clave

- Ataca calidad de datos antes de modelar o visualizar.
- Convierte reglas de limpieza en pasos repetibles.
- Expone supuestos sobre datos faltantes y duplicados.
- Reduce ruido en métricas y dashboards posteriores.

## 2. Aplicación Práctica

### Casos de Uso

1. Normalizar nombres y columnas al importar CSVs diversos.
2. Completar revenue faltante con una estrategia simple y justificada.
3. Eliminar duplicados antes de calcular totales.

### Ejemplo de Código

Revisa `examples/example_basic.py` para ver una implementación ejecutable enfocada en data cleaning.

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Si la limpieza queda implícita o manual, el análisis posterior se vuelve poco confiable y difícil de reproducir.

### Solución y Beneficios

- Mejora la confianza en cada paso posterior del pipeline.
- Hace auditables las decisiones sobre datos faltantes.
- Reduce errores silenciosos en joins y agregaciones.

### Errores Comunes

- Rellenar faltantes sin justificar el criterio.
- Eliminar filas sin medir impacto en el volumen total.
- No registrar qué columnas fueron renombradas o transformadas.

## 4. Referencias

Consulta `references/links.md` para documentación oficial y material de profundización.

## 5. Tarea Práctica

Usa `exercises/exercise_01.py` como punto de partida. El foco del ejercicio es: Estandariza un dataset de clientes corrigiendo nombres de columnas, valores faltantes y duplicados.

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

- La limpieza es una etapa explícita, no un detalle secundario.
- Las reglas repetibles mejoran confiabilidad y mantenimiento.
- Un dataset limpio evita errores acumulados en el análisis.

## 7. Prompt de Reflexión

- ¿Qué transformación tuvo más impacto en la calidad final?
- ¿Qué decisión de imputación conviene documentar mejor?
- ¿Cómo compararías antes y después de limpiar?
