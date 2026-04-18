# Polars Intro

Tiempo estimado: 1.5-2.5 hours

## 1. Definición

Polars Intro introduce un motor columnar moderno para análisis rápidos con expresiones explícitas y lazy evaluation.

### Características Clave

- Usa expresiones declarativas en vez de operaciones implícitas.
- Aprovecha ejecución columnar y paralelismo interno.
- Incluye modo eager y lazy según el caso de uso.
- Es una alternativa moderna a ciertos pipelines de Pandas.

## 2. Aplicación Práctica

### Casos de Uso

1. Agrupar grandes volúmenes de datos con expresiones legibles.
2. Migrar partes lentas de un pipeline exploratorio.
3. Comparar ergonomía y performance frente a Pandas.

### Ejemplo de Código

Revisa `examples/example_basic.py` para ver una implementación ejecutable enfocada en polars intro.

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Cuando un pipeline crece, algunas transformaciones tabulares necesitan una API más explícita y una ejecución mejor optimizada.

### Solución y Beneficios

- Hace más visibles las expresiones por columna.
- Suele rendir muy bien en agregaciones y filtros grandes.
- Invita a pensar el pipeline como una secuencia declarativa.

### Errores Comunes

- Traducir mentalmente Pandas 1:1 y perder ventajas de expresiones.
- Ignorar diferencias entre eager y lazy.
- No validar el schema esperado después de transformar.

## 4. Referencias

Consulta `references/links.md` para documentación oficial y material de profundización.

## 5. Tarea Práctica

Usa `exercises/exercise_01.py` como punto de partida. El foco del ejercicio es: Resume envíos por warehouse con agregaciones declarativas en Polars.

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

- Polars cambia la forma de pensar transformaciones tabulares.
- Las expresiones explícitas ayudan a razonar sobre el pipeline.
- Es útil cuando Pandas empieza a quedarse corto en ciertos flujos.

## 7. Prompt de Reflexión

- ¿Qué parte del pipeline se ve más clara con expresiones?
- ¿Qué criterio usarías para decidir entre Pandas y Polars?
- ¿Qué schema deberías validar al final?
