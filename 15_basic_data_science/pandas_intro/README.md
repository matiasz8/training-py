# Pandas Intro

Tiempo estimado: 1.5-2.5 hours

## 1. Definición

Pandas Intro muestra cómo representar tablas con DataFrame y Series para organizar métricas, filtros y agregaciones iniciales.

### Características Clave

- Trabaja con columnas etiquetadas y tipos mixtos.
- Ofrece filtros y agregaciones de alto nivel.
- Permite pasar de registros JSON a tablas de análisis muy rápido.
- Se integra naturalmente con CSV, Excel y bases de datos.

## 2. Aplicación Práctica

### Casos de Uso

1. Crear tableros simples de ventas desde listas de diccionarios.
1. Filtrar pedidos por región o producto.
1. Generar resúmenes mensuales para stakeholders.

### Ejemplo de Código

Revisa `examples/example_basic.py` para ver una implementación ejecutable enfocada en pandas intro.

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin una estructura tabular expresiva, limpiar y resumir datos de negocio termina disperso en listas, dicts y loops difíciles de mantener.

### Solución y Beneficios

- Hace visible la forma del dataset desde el inicio.
- Reduce el costo de filtrar, agrupar y ordenar datos.
- Facilita pasar de exploración a reporting básico.

### Errores Comunes

- Construir columnas derivadas con tipos inconsistentes.
- Olvidar parsear fechas antes de agrupar.
- Asumir que el índice tiene significado de negocio cuando no lo tiene.

## 4. Referencias

Consulta `references/links.md` para documentación oficial y material de profundización.

## 5. Tarea Práctica

Usa `exercises/exercise_01.py` como punto de partida. El foco del ejercicio es: Construye un DataFrame de ventas y calcula revenue mensual con operaciones básicas de Pandas.

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

- Pandas organiza datos tabulares con un modelo muy expresivo.
- Series y DataFrames cubren la mayoría de necesidades iniciales.
- La claridad de columnas y filtros acelera el análisis.

## 7. Prompt de Reflexión

- ¿Qué columna derivada te aportó más valor analítico?
- ¿Dónde convino usar groupby en lugar de loops?
- ¿Qué validación faltaría antes de publicar este reporte?
