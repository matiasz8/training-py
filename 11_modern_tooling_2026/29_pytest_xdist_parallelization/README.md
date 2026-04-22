# pytest-xdist: Paralelización de Tests

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

`pytest-xdist` distribuye la ejecución de tests entre múltiples workers (procesos o máquinas) para reducir el tiempo total de la suite de tests. Con `-n auto`, aprovecha todos los núcleos disponibles del CPU. Es especialmente valioso para suites de tests grandes donde el tiempo de ejecución secuencial es un cuello de botella.

### Características Principales

- `-n auto`: detecta automáticamente el número de CPUs y crea un worker por cada uno
- `-n <número>`: especifica manualmente el número de workers paralelos
- `--dist loadfile`: mantiene tests del mismo archivo en el mismo worker
- `--dist loadscope`: agrupa tests por scope de fixture para evitar conflictos
- Compatible con pytest-cov para coverage paralelo con `--cov-append`

## 2. Aplicación Práctica

### Casos de Uso

- Reducir suites de tests de 10+ minutos a 2-3 minutos aprovechando paralelismo de CPU
- Detectar tests con estado compartido que fallan al ejecutarse en paralelo
- Acelerar pipelines de CI/CD en máquinas multi-core

### Ejemplo de Código

```bash
pytest -n auto                           # usa todos los núcleos disponibles
pytest -n 4                              # exactamente 4 workers
pytest -n auto --dist loadfile           # tests del mismo archivo en el mismo worker
pytest -n auto --cov=src/ --cov-append   # coverage con xdist

time pytest                              # referencia: tiempo secuencial
time pytest -n auto                      # con paralelización
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Las suites de tests crecen con el proyecto. Sin paralelización, pueden tardar 10-20 minutos en ejecutarse, lo que desmotiva la ejecución frecuente de tests durante el desarrollo y alarga los ciclos de CI/CD significativamente.

### Solución y Beneficios

- Reducción proporcional al número de núcleos disponibles (2 núcleos ≈ 2x más rápido)
- Mayor frecuencia de ejecución de tests durante el desarrollo
- Pipelines CI/CD más rápidos y económicos en instancias multi-core
- Detección de tests no aislados que tienen dependencias de estado implícitas

## 4. Referencias

- https://pytest-xdist.readthedocs.io/en/latest/
- https://github.com/pytest-dev/pytest-xdist
- https://docs.pytest.org/en/stable/how-to/xdist.html
- https://pytest-cov.readthedocs.io/en/latest/subprocess.html
- https://docs.pytest.org/en/stable/reference/fixtures.html#fixture-scopes

## 5. Tarea Práctica

### Nivel Básico

Instala `pytest-xdist` y ejecuta tu suite con `pytest -n auto`. Compara el tiempo de ejecución con `time pytest` vs `time pytest -n auto`. Documenta el speedup obtenido.

### Nivel Intermedio

Si algunos tests fallan en paralelo pero no en secuencial, identifica las fixtures o variables globales que causan el problema. Corrige los tests para que sean verdaderamente independientes.

### Nivel Avanzado

Configura pytest-xdist con `--dist loadscope` para agrupar tests por scope de fixture de base de datos. Añade `pytest-randomly` para detectar dependencias de orden entre tests.

### Criterios de Éxito

- [ ] Los tests completan en menos tiempo con `-n auto` que en modo secuencial
- [ ] Todos los tests pasan en paralelo, no solo en secuencial
- [ ] El coverage funciona correctamente con `--cov-append` en modo paralelo
- [ ] Documentas el speedup obtenido: número de núcleos y reducción de tiempo

## 6. Resumen

`pytest-xdist` es una de las mejoras más impactantes que puedes hacer a una suite de tests madura. La paralelización no solo reduce el tiempo de ejecución sino que también revela tests con estado compartido implícito, mejorando la calidad e independencia de la suite.

## 7. Reflexión

¿Cuánto tarda tu suite de tests actual? ¿Cuántos núcleos tiene tu máquina de CI/CD? ¿Qué impacto tendría ejecutarla con xdist en el ciclo de desarrollo de tu equipo?
