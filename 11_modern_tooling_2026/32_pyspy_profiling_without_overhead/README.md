# py-spy: Profiling Sin Overhead

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

py-spy es un profiler de muestreo (sampling profiler) para Python implementado en Rust. Funciona adjuntándose a un proceso Python en ejecución sin modificar el código fuente ni el intérprete, con un overhead prácticamente nulo (< 1%). Puede perfilar procesos en producción sin detenerlos ni reiniciarlos.

### Características Principales

- Profiling sin modificar código: se adjunta a un PID existente
- Overhead < 1%: no afecta el rendimiento de producción
- Visualización en tiempo real con `py-spy top` (similar a `top` del sistema)
- Generación de flamegraphs SVG con `py-spy record`
- Soporte para threads, subprocesos y código nativo (C extensions)

## 2. Aplicación Práctica

### Casos de Uso

- Diagnosticar lentitud en un servicio Python en producción sin interrumpirlo
- Identificar cuellos de botella en procesos de larga duración (workers, scrapers)
- Generar flamegraphs para presentar en reviews de performance al equipo

### Ejemplo de Código

```bash
uv tool install py-spy

py-spy top --pid 12345               # monitor en tiempo real del proceso
py-spy record -o profile.svg --pid 12345  # flamegraph del proceso en ejecución
py-spy dump --pid 12345              # stack trace completo instantáneo

py-spy record -o profile.svg -- python mi_script.py   # perfilar nuevo proceso
py-spy record --subprocesses --pid 12345               # incluir subprocesos
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Los profilers tradicionales como `cProfile` requieren modificar el código, reiniciar el proceso y añaden overhead significativo que puede cambiar el comportamiento del sistema que intentas analizar. Esto hace imposible perfilar procesos de producción sin impacto.

### Solución y Beneficios

- Profiling de procesos de producción sin downtime ni modificación de código
- Overhead negligible que no afecta a los usuarios del servicio
- Diagnóstico inmediato adjuntándose al PID del proceso lento
- Flamegraphs visuales que comunican cuellos de botella de forma clara al equipo

## 4. Referencias

- https://github.com/benfred/py-spy
- https://pypi.org/project/py-spy/
- https://www.brendangregg.com/flamegraphs.html
- https://docs.astral.sh/uv/guides/tools/
- https://github.com/benfred/py-spy/blob/master/README.md

## 5. Tarea Práctica

### Nivel Básico

Instala py-spy con `uv tool install py-spy`. Ejecuta un script Python que tenga una función lenta. Usa `py-spy record -o profile.svg -- python script.py` y abre el SVG en el navegador.

### Nivel Intermedio

Identifica el cuello de botella más grande en el flamegraph. Optimiza esa función y genera un nuevo flamegraph. Compara ambos SVGs para verificar la mejora.

### Nivel Avanzado

Configura py-spy para adjuntarse a un servidor web (FastAPI/Django) bajo carga. Usa `wrk` o `locust` para generar tráfico mientras perfila. Analiza el flamegraph resultante e identifica optimizaciones.

### Criterios de Éxito

- [ ] py-spy genera un flamegraph SVG legible para un proceso Python en ejecución
- [ ] El flamegraph identifica correctamente la función más costosa en tiempo de CPU
- [ ] El overhead de py-spy es negligible (el proceso sigue respondiendo normalmente)
- [ ] Puedes adjuntarte a un proceso existente con solo su PID

## 6. Resumen

py-spy democratiza el profiling de producción: ya no necesitas entornos de staging especiales ni modificaciones de código para entender dónde pasa el tiempo tu aplicación Python. La combinación de overhead cero y visualización con flamegraphs lo hace indispensable para optimización de rendimiento.

## 7. Reflexión

¿Tienes algún proceso Python en producción que sospechas que es lento pero nunca has podido medir? ¿Qué impacto tendría poder perfilarlo directamente sin interrupciones?
