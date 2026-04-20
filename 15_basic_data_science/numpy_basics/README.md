# NumPy Basics

Tiempo estimado: 1.5-2.5 hours

## 1. Definición

NumPy Basics introduce arrays multidimensionales, broadcasting y operaciones vectorizadas para procesar datos numéricos sin depender de bucles explícitos.

### Características Clave

- Trabaja con arrays homogéneos y memoria contigua.
- Aprovecha operaciones vectorizadas para mejorar legibilidad y velocidad.
- Permite usar broadcasting para combinar series de distinto tamaño.
- Es la base de gran parte del ecosistema científico de Python.

## 2. Aplicación Práctica

### Casos de Uso

1. Normalizar métricas antes de entrenar un modelo simple.
1. Calcular KPIs diarios a partir de series de ventas o tráfico.
1. Preparar features numéricas para análisis exploratorio.

### Ejemplo de Código

Revisa `examples/example_basic.py` para ver una implementación ejecutable enfocada en numpy basics.

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin arrays vectorizados, el código numérico escala peor, es más verboso y mezcla la lógica del negocio con detalles iterativos.

### Solución y Beneficios

- Reduce el costo de procesar listas numéricas grandes.
- Hace más explícitas las transformaciones matemáticas.
- Sirve como puente hacia Pandas, SciPy y machine learning.

### Errores Comunes

- Confundir operaciones elemento a elemento con multiplicación matricial.
- Ignorar el tipo de dato y perder precisión sin darte cuenta.
- Abusar de conversions innecesarias entre listas y arrays.

## 4. Referencias

Consulta `references/links.md` para documentación oficial y material de profundización.

## 5. Tarea Práctica

Usa `exercises/exercise_01.py` como punto de partida. El foco del ejercicio es: Implementa una normalización z-score y un moving average reutilizable para una serie numérica.

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

- NumPy permite trabajar con datos numéricos a nivel columna o vector.
- Las operaciones vectorizadas simplifican cálculos repetitivos.
- Es el punto de partida natural para data science en Python.

## 7. Prompt de Reflexión

- ¿Qué parte del cálculo fue más clara al expresarla con arrays?
- ¿Dónde ganaste legibilidad frente a una solución con listas?
- ¿Qué validaciones agregarías antes de reutilizar esta lógica?
