# Type Narrowing y Type Guards Avanzados

⏱️ **Tiempo estimado: 2 horas**

## 1. Definición

El type narrowing es la capacidad de los type checkers de inferir un tipo más específico dentro de un bloque de código condicional. Los type guards son funciones que formalizan este mecanismo, permitiendo expresar condiciones de tipo complejas que el type checker puede verificar y propagar automáticamente.

### Características Principales

- Narrowing automático con `isinstance`, `type()`, comparaciones y `is None`
- `TypeGuard[T]` (PEP 647): función que asegura al checker que el argumento es de tipo T
- `TypeIs[T]` (PEP 742, Python 3.13+): versión más precisa de TypeGuard
- `assert` statements para narrowing manual en código con invariantes conocidas
- Narrowing con `Literal` types y pattern matching (`match`/`case`)

## 2. Aplicación Práctica

### Casos de Uso

- Trabajar con `Union` types donde necesitas ramificar según el tipo específico
- Validar datos externos (JSON, formularios) y propagar el tipo validado al checker
- Implementar funciones de validación reutilizables con garantías de tipo

### Ejemplo de Código

```python
from typing import TypeGuard, Union

def es_lista_de_strings(val: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)

def procesar(datos: Union[str, int, list[str]]) -> str:
    if isinstance(datos, str):
        return datos.upper()           # checker sabe: datos es str aquí
    elif isinstance(datos, int):
        return str(datos)              # checker sabe: datos es int aquí
    return ", ".join(datos)            # checker sabe: datos es list[str]
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Al trabajar con `Union` types o datos de origen externo, el type checker no sabe qué tipo específico tiene una variable dentro de una rama condicional. Sin narrowing explícito, se producen errores de tipo falsos o se requiere un `cast()` que elimina las garantías de tipo.

### Solución y Beneficios

- Code paths seguros sin necesidad de `cast()` o `Any`
- El checker verifica exhaustividad en unions (que todas las ramas están cubiertas)
- Funciones de validación reutilizables que propagan información de tipo
- Código más expresivo que documenta las invariantes mediante tipos

## 4. Referencias

- https://mypy.readthedocs.io/en/stable/type_narrowing.html
- https://peps.python.org/pep-0647/
- https://peps.python.org/pep-0742/
- https://typing.readthedocs.io/en/latest/reference/narrowing.html
- https://microsoft.github.io/pyright/#/type-concepts-advanced

## 5. Tarea Práctica

### Nivel Básico

Escribe una función que recibe `Union[str, int, list[str]]` y devuelve un string. Usa `isinstance` para el narrowing. Verifica que mypy/pyright no reporta errores en ninguna rama.

### Nivel Intermedio

Implementa un `TypeGuard` personalizado para validar que un `dict` tiene las claves y tipos correctos (como un validador de JSON). Úsalo en una función que procese datos externos.

### Nivel Avanzado

Implementa un patrón de discriminated union con `Literal` types y `match`/`case`. Verifica que el type checker detecta si olvidas cubrir algún caso en el pattern matching.

### Criterios de Éxito

- [ ] Las funciones con `Union` types no tienen errores de tipo en ninguna rama condicional
- [ ] Al menos un `TypeGuard` personalizado está correctamente implementado y usado
- [ ] mypy/pyright detecta el caso en que falta una rama en un discriminated union
- [ ] No hay `cast()` ni `type: ignore` para evitar errores de narrowing

## 6. Resumen

Type narrowing y type guards permiten escribir código que trabaja con tipos heterogéneos de forma completamente type-safe. Son especialmente valiosos al procesar datos externos o implementar lógica de dominio compleja con múltiples variantes de tipo.

## 7. Reflexión

¿En qué partes de tu código actual usas `cast()` o `Any` para evitar errores del type checker? ¿Podrías reemplazarlos con narrowing o TypeGuard apropiados?
