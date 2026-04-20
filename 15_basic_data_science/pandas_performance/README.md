# Pandas Performance

Tiempo estimado: 2-3 hours

## 1. Definición

Pandas Performance muestra cuándo conviene vectorizar transformaciones, medir tiempos y evitar apply innecesario.

### Características Clave

- Compara estrategias con métricas simples y repetibles.
- Favorece operaciones columnares en lugar de loops fila a fila.
- Ayuda a detectar cuellos de botella tempranos.
- Se complementa con profiling más profundo cuando hace falta.

## 2. Aplicación Práctica

### Casos de Uso

1. Acelerar pipelines de cálculo de descuentos o revenue.
1. Reducir tiempos de preprocesamiento antes de entrenar modelos.
1. Tomar decisiones informadas sobre cuándo migrar a Polars.

### Ejemplo de Código

Revisa `examples/example_basic.py` para ver una implementación ejecutable enfocada en pandas performance.

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin medir ni vectorizar, un pipeline aparentemente correcto puede degradarse mucho al crecer el volumen de datos.

### Solución y Beneficios

- Permite justificar cambios con evidencia y no intuición.
- Reduce CPU desperdiciada en operaciones repetitivas.
- Mejora la escalabilidad de transformaciones frecuentes.

### Errores Comunes

- Medir una sola vez y sacar conclusiones definitivas.
- Optimizar antes de validar corrección de resultados.
- Ignorar el costo de conversiones entre tipos o estructuras.

## 4. Referencias

Consulta `references/links.md` para documentación oficial y material de profundización.

## 5. Tarea Práctica

Usa `exercises/exercise_01.py` como punto de partida. El foco del ejercicio es: Implementa una estrategia vectorizada de descuentos y compárala con una variante más lenta.

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

- La performance mejora cuando la transformación se expresa por columnas.
- Medir pequeños cambios evita optimizaciones imaginarias.
- Vectorizar no siempre es todo, pero suele ser el primer paso correcto.

## 7. Prompt de Reflexión

- ¿Qué parte del pipeline vale la pena medir más profundamente?
- ¿Qué optimización mantiene mejor legibilidad?
- ¿Cuándo convendría cambiar de herramienta en lugar de micro-optimizar?
