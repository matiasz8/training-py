# Pandas Operations

Tiempo estimado: 2-3 hours

## 1. Definición

Pandas Operations profundiza en merges, groupby, transformaciones por columna y resúmenes orientados a preguntas de negocio.

### Características Clave

- Combina datasets con joins explícitos.
- Agrupa métricas por segmento, categoría o período.
- Permite derivar nuevas columnas en pipelines pequeños.
- Hace visibles agregaciones intermedias para debugging.

## 2. Aplicación Práctica

### Casos de Uso

1. Cruzar órdenes con clientes para segmentar revenue.
2. Agregar métricas por categoría de producto.
3. Construir tablas resumen antes de visualizar resultados.

### Ejemplo de Código

Revisa `examples/example_basic.py` para ver una implementación ejecutable enfocada en pandas operations.

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Cuando las transformaciones tabulares crecen sin estructura, aparecen merges opacos y agregaciones repetidas difíciles de verificar.

### Solución y Beneficios

- Permite separar cada paso de transformación en piezas auditables.
- Hace más simple comparar revenue, ticket promedio y volumen.
- Prepara mejor los datos para visualización o modelado.

### Errores Comunes

- Hacer merges sin validar cardinalidad.
- Perder columnas clave después de un rename o reset_index.
- Ocultar demasiada lógica en una sola cadena larga.

## 4. Referencias

Consulta `references/links.md` para documentación oficial y material de profundización.

## 5. Tarea Práctica

Usa `exercises/exercise_01.py` como punto de partida. El foco del ejercicio es: Resume revenue y ticket promedio por segmento combinando órdenes y clientes.

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

- Las operaciones tabulares ganan claridad cuando cada paso tiene intención.
- Joins y groupby son la base de muchos reportes de negocio.
- Las métricas derivadas deben quedar explícitas y verificables.

## 7. Prompt de Reflexión

- ¿Qué supuestos de cardinalidad tuviste que validar?
- ¿Qué métrica derivada aporta más contexto que el total bruto?
- ¿Qué harías para volver este pipeline reusable?
