# Matplotlib Basics

Tiempo estimado: 1.5-2.5 hours

## 1. Definición

Matplotlib Basics cubre la construcción de gráficos base con control explícito de figura, ejes, etiquetas y formato.

### Características Clave

- Usa una API orientada a objetos para construir gráficos.
- Funciona bien como capa base para librerías más expresivas.
- Permite exportar figuras sin depender de una interfaz gráfica.
- Es ideal para entender qué está pasando en cada eje.

## 2. Aplicación Práctica

### Casos de Uso

1. Graficar evolución mensual de ventas o tráfico.
2. Anotar outliers o hitos en una serie temporal.
3. Exportar gráficos para reportes automatizados.

### Ejemplo de Código

Revisa `examples/example_basic.py` para ver una implementación ejecutable enfocada en matplotlib basics.

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Si no controlas figura y ejes explícitamente, los gráficos se vuelven difíciles de reutilizar, testear o exportar de forma consistente.

### Solución y Beneficios

- Hace reproducible la visualización en scripts y pipelines.
- Permite componer varias series con etiquetas claras.
- Facilita guardar salidas para QA o documentación.

### Errores Comunes

- Depender del estado global de pyplot sin cerrar figuras.
- Omitir títulos o labels y perder contexto del gráfico.
- Usar demasiados elementos decorativos antes de validar la historia del dato.

## 4. Referencias

Consulta `references/links.md` para documentación oficial y material de profundización.

## 5. Tarea Práctica

Usa `exercises/exercise_01.py` como punto de partida. El foco del ejercicio es: Construye una figura reutilizable con línea de ventas mensuales y etiquetas claras.

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

- Matplotlib ayuda a controlar cada capa del gráfico.
- La API orientada a objetos mejora testabilidad y reuso.
- Guardar figuras sin UI es clave para automatización.

## 7. Prompt de Reflexión

- ¿Qué parte del gráfico debería quedar como función reusable?
- ¿Qué label aporta más contexto al lector final?
- ¿Cómo validarías que la figura sigue correcta tras un refactor?
