# Mutation Testing con mutmut

⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

El mutation testing evalúa la calidad de tu suite de tests introduciéndole modificaciones pequeñas (mutaciones) al código fuente y verificando si los tests detectan estos cambios. Si un test no falla ante una mutación, indica que esa parte del código está infra-testeada aunque aparezca cubierta en el reporte de cobertura.

### Características Principales

- `mutmut` genera mutantes automáticamente: cambia `>` por `>=`, `+` por `-`, `True` por `False`, etc.
- Los mutantes "sobrevivientes" (tests que no fallan) revelan huecos en la suite de tests
- Caché de resultados: no re-ejecuta mutantes ya analizados
- Integración con pytest y cualquier runner de tests
- Reporte de mutantes vivos, muertos y con errores de ejecución

## 2. Aplicación Práctica

### Casos de Uso

- Evaluar la calidad real de una suite de tests con alta cobertura pero tests débiles
- Identificar lógica de negocio crítica que necesita tests más específicos
- Medir el impacto de mejorar los tests antes de un refactor importante

### Ejemplo de Código

```bash
mutmut run                          # ejecuta mutation testing en el proyecto
mutmut results                      # muestra resumen de mutantes
mutmut show 3                       # muestra el mutante número 3

mutmut run --paths-to-mutate src/   # limitar a directorio específico
mutmut html                         # genera reporte HTML
```

```python
def descuento(precio: float, pct: float) -> float:
    if pct > 100:            # mutante: cambia > por >= (¿tests detectan el cambio?)
        raise ValueError("Descuento mayor a 100%")
    return precio * (1 - pct / 100)
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Un 80% de cobertura de código no garantiza que los tests sean buenos. Es posible tener alta cobertura con tests que no verifican el resultado correcto (solo que el código no lanza excepciones). El mutation testing mide la efectividad real de los tests, no solo si se ejecutan.

### Solución y Beneficios

- Métrica de calidad de tests más rigurosa que la cobertura de líneas
- Identificación específica de condiciones lógicas sin verificar
- Guía clara sobre qué tests añadir para mejorar la robustez de la suite
- Mayor confianza en los tests antes de realizar refactors importantes

## 4. Referencias

- https://mutmut.readthedocs.io/en/latest/
- https://github.com/boxed/mutmut
- https://pitest.org/ (referencia conceptual desde Java)
- https://testing.googleblog.com/2021/04/mutation-testing.html
- https://en.wikipedia.org/wiki/Mutation_testing

## 5. Tarea Práctica

### Nivel Básico

Ejecuta `mutmut run` en un módulo pequeño de tu proyecto. Analiza los mutantes supervivientes con `mutmut show <id>`. Escribe tests que maten al menos 3 mutantes supervivientes.

### Nivel Intermedio

Identifica un módulo de lógica de negocio crítica. Ejecuta mutation testing, documenta el mutation score, añade tests específicos para los mutantes supervivientes y mide la mejora del score.

### Nivel Avanzado

Integra mutation testing en CI/CD con un threshold mínimo de mutation score. Configura `mutmut run --paths-to-mutate` para enfocarte solo en código de dominio crítico, excluyendo código boilerplate.

### Criterios de Éxito

- [ ] El mutation score inicial está documentado antes de añadir tests
- [ ] Al menos 5 mutantes supervivientes han sido "matados" con nuevos tests
- [ ] El mutation score mejoró al menos un 10% tras añadir tests dirigidos
- [ ] Puedes explicar qué tipo de bug representa cada mutante superviviente

## 6. Resumen

Mutation testing con mutmut revela la verdad incómoda sobre la calidad de los tests: la cobertura de código puede dar falsa seguridad. El mutation score, en cambio, mide si los tests realmente detectan los bugs que se supone deben detectar, siendo un complemento invaluable a la cobertura tradicional.

## 7. Reflexión

¿Qué parte de tu código tiene más lógica condicional crítica que podría beneficiarse de mutation testing? ¿Cuánto tiempo del ciclo de tests estás dispuesto a dedicar al mutation testing en CI/CD?
