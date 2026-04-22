# Hypothesis: Property-Based Testing

⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Hypothesis es una biblioteca de property-based testing que genera automáticamente cientos de casos de prueba basándose en las propiedades que defines. En lugar de especificar ejemplos concretos, defines invariantes que deben cumplirse para cualquier input válido, y Hypothesis busca activamente casos que las violen.

### Características Principales

- `@given()` con estrategias (`st.integers()`, `st.text()`, `st.lists()`, etc.) para generar inputs
- Shrinking automático: cuando encuentra un fallo, reduce el ejemplo al mínimo reproducible
- Base de datos de ejemplos que recuerda casos fallidos para re-ejecutarlos siempre
- Integración nativa con pytest sin configuración adicional
- Estrategias compuestas para generar datos estructurados complejos

## 2. Aplicación Práctica

### Casos de Uso

- Verificar que una función de serialización/deserialización es inversa perfecta
- Probar que algoritmos matemáticos cumplen propiedades como comutatividad o asociatividad
- Detectar edge cases en parsers, validadores y funciones de transformación de datos

### Ejemplo de Código

```python
from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_suma_es_conmutativa(a: int, b: int) -> None:
    assert a + b == b + a

@given(st.text())
def test_encode_decode_roundtrip(texto: str) -> None:
    assert texto.encode("utf-8").decode("utf-8") == texto

@given(st.lists(st.integers(), min_size=1))
def test_max_en_lista(nums: list[int]) -> None:
    assert max(nums) in nums
    assert all(x <= max(nums) for x in nums)
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Los tests basados en ejemplos solo verifican los casos que el developer pensó en probar. Los bugs más difíciles de encontrar son los que ocurren con inputs inesperados: strings con caracteres unicode, enteros muy grandes, listas vacías, o combinaciones extremas de datos.

### Solución y Beneficios

- Exploración automática del espacio de inputs: Hypothesis encuentra los casos que no pensaste
- Reducción mínima del caso fallido: siempre obtén el ejemplo más simple que reproduce el bug
- Mayor confianza en el código: has verificado propiedades para cientos de casos, no solo 3-5
- Detección de bugs imposibles de encontrar con tests manuales

## 4. Referencias

- https://hypothesis.readthedocs.io/en/latest/
- https://hypothesis.readthedocs.io/en/latest/quickstart.html
- https://hypothesis.readthedocs.io/en/latest/data.html
- https://hypothesis.works/articles/what-is-property-based-testing/
- https://github.com/HypothesisWorks/hypothesis

## 5. Tarea Práctica

### Nivel Básico

Escribe 3 tests con `@given` para una función de ordenamiento. Verifica propiedades como: el resultado tiene la misma longitud, todos los elementos del input están en el output, y está ordenado.

### Nivel Intermedio

Implementa un test de roundtrip para una función de serialización JSON personalizada. Usa `st.recursive()` para generar estructuras JSON arbitrariamente anidadas.

### Nivel Avanzado

Crea una estrategia `@composite` que genere instancias válidas de un modelo de dominio complejo (por ejemplo, un pedido con productos y cantidades válidas). Úsala para probar invariantes de negocio.

### Criterios de Éxito

- [ ] Los tests con `@given` descubren al menos un edge case que los tests manuales no cubrían
- [ ] El shrinking automático produce ejemplos mínimos y comprensibles cuando falla un test
- [ ] Al menos una estrategia `@composite` está implementada para un tipo de dominio
- [ ] Los tests de Hypothesis se integran sin problemas en la suite existente de pytest

## 6. Resumen

Hypothesis transforma la forma de pensar sobre los tests: de "¿qué ejemplos pruebo?" a "¿qué propiedades debe cumplir mi función para cualquier input?". Este cambio de perspectiva lleva a código más robusto y a bugs descubiertos antes de llegar a producción.

## 7. Reflexión

¿Qué funciones de tu código actual tienen propiedades matemáticas claras que podrías verificar con Hypothesis? ¿Cómo cambiaría tu proceso de design si empezaras pensando en propiedades antes que en ejemplos?
