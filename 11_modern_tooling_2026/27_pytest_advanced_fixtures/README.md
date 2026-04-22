# pytest Avanzado: Fixtures y Parametrize

⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

Las fixtures de pytest son funciones que proveen datos, objetos o estado a los tests de forma reutilizable y con control de ciclo de vida (setup/teardown). Los scopes permiten compartir fixtures entre tests, módulos o toda la sesión. `@pytest.mark.parametrize` ejecuta el mismo test con múltiples conjuntos de datos.

### Características Principales

- Scopes de fixture: `function` (por defecto), `class`, `module`, `package`, `session`
- Fixtures que devuelven generadores para teardown automático con `yield`
- `conftest.py` para fixtures compartidas entre múltiples archivos de test
- `@pytest.mark.parametrize` con `indirect` para parametrizar vía fixtures
- Fixtures con dependencias: una fixture puede solicitar otras fixtures

## 2. Aplicación Práctica

### Casos de Uso

- Crear una conexión a base de datos compartida entre todos los tests del módulo
- Proveer datos de prueba variados para validar el comportamiento de una función
- Setup y teardown automático de recursos externos (archivos, servidores, BD temporales)

### Ejemplo de Código

```python
import pytest

@pytest.fixture(scope="module")
def cliente_db():
    db = crear_conexion_test()
    yield db
    db.close()

@pytest.mark.parametrize("entrada,esperado", [
    ("hola", "HOLA"),
    ("mundo", "MUNDO"),
    ("", ""),
])
def test_mayusculas(entrada: str, esperado: str) -> None:
    assert entrada.upper() == esperado

@pytest.fixture
def usuario_admin(cliente_db):
    return crear_usuario(cliente_db, rol="admin")
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Sin fixtures bien diseñadas, el código de setup/teardown se duplica entre tests, los tests son frágiles por dependencias entre sí, y probar con múltiples valores de entrada requiere escribir el mismo test varias veces con mínimas variaciones.

### Solución y Beneficios

- DRY en tests: el setup se define una vez y se reutiliza en múltiples tests
- Tests más legibles: cada test describe qué verifica, no cómo se configura
- Cobertura mejorada con parametrize: múltiples casos de prueba con un test
- Teardown garantizado aunque el test falle, evitando recursos no liberados

## 4. Referencias

- https://docs.pytest.org/en/stable/reference/fixtures.html
- https://docs.pytest.org/en/stable/how-to/parametrize.html
- https://docs.pytest.org/en/stable/reference/fixtures.html#fixture-scopes
- https://docs.pytest.org/en/stable/how-to/fixtures.html
- https://realpython.com/pytest-python-testing/

## 5. Tarea Práctica

### Nivel Básico

Crea una fixture con `scope="module"` que provea un cliente HTTP de prueba. Úsala en al menos 3 tests diferentes. Verifica que la fixture se inicializa solo una vez por módulo.

### Nivel Intermedio

Implementa un test con `@pytest.mark.parametrize` que verifique 5 casos distintos de una función de validación. Añade un `ids` parameter para que los nombres de los tests sean descriptivos.

### Nivel Avanzado

Crea un `conftest.py` con una fixture `scope="session"` que levante una base de datos SQLite temporal. Implementa fixtures dependientes para crear usuarios, productos y órdenes de prueba. Verifica que el teardown limpia correctamente.

### Criterios de Éxito

- [ ] Las fixtures con `scope="module"` se ejecutan solo una vez por módulo de test
- [ ] Los tests parametrizados muestran nombres descriptivos en la salida de pytest
- [ ] El `conftest.py` centraliza las fixtures compartidas sin duplicación
- [ ] El teardown con `yield` se ejecuta incluso cuando los tests fallan

## 6. Resumen

Las fixtures y `parametrize` son las características más poderosas de pytest para escribir tests mantenibles y con buena cobertura. Dominar los scopes y el patrón `yield` para teardown transforma la forma en que se organizan y reutilizan los recursos de test.

## 7. Reflexión

¿Cuánto código de setup se repite en tus tests actuales? ¿Qué fixtures de módulo o sesión simplificarían más tu suite de tests?
