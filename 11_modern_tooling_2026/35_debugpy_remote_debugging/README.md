# debugpy y Remote Debugging

⏱️ **Tiempo estimado: 1-2 horas**

## 1. Definición

debugpy es el adaptador de debug protocol (DAP) para Python utilizado por VS Code y otros editores modernos. Permite depurar procesos Python locales y remotos adjuntándose a ellos, establecer breakpoints, inspeccionar variables y ejecutar código en el contexto del proceso detenido, todo sin modificar permanentemente el código fuente.

### Características Principales

- Implementa el Debug Adapter Protocol (DAP) estándar de Microsoft
- Debug remoto: adjuntarse a procesos en servidores, contenedores Docker o Kubernetes
- Integración nativa con VS Code mediante `launch.json`
- Modo `wait_for_client`: el proceso espera al debugger antes de ejecutar código crítico
- Compatible con threads, async/await, subprocesos y workers de Django/Flask/FastAPI

## 2. Aplicación Práctica

### Casos de Uso

- Depurar un servicio web (FastAPI, Django) que se ejecuta dentro de un contenedor Docker
- Adjuntarse a un worker de Celery en un entorno de staging para investigar un bug específico
- Depurar scripts de larga duración sin reinicios continuos

### Ejemplo de Código

```python
import debugpy

debugpy.listen(("0.0.0.0", 5678))   # escucha conexiones del debugger
debugpy.wait_for_client()           # pausa hasta que el debugger se conecta
print("Debugger conectado, continuando...")
```

```json
{
    "type": "python",
    "request": "attach",
    "connect": {"host": "localhost", "port": 5678},
    "pathMappings": [{"localRoot": "${workspaceFolder}", "remoteRoot": "/app"}]
}
```

## 3. ¿Por Qué Es Importante?

### Problema que Resuelve

Muchos bugs solo aparecen en entornos específicos (staging, producción) con datos reales, y son imposibles de reproducir localmente. El debugging tradicional con `print()` o logging es lento e incompleto: no permite inspeccionar el estado completo del programa en el momento exacto del bug.

### Solución y Beneficios

- Debugging interactivo en entornos remotos sin necesidad de acceso SSH directo
- Inspección completa del estado del programa: variables, stack, heap en tiempo real
- Sin modificaciones permanentes al código: los breakpoints son temporales
- Compatibilidad con Docker y Kubernetes para debugging en contenedores

## 4. Referencias

- https://github.com/microsoft/debugpy
- https://code.visualstudio.com/docs/python/debugging
- https://microsoft.github.io/debug-adapter-protocol/
- https://pypi.org/project/debugpy/
- https://code.visualstudio.com/docs/python/debugging#_remote-debugging

## 5. Tarea Práctica

### Nivel Básico

Añade `debugpy.listen(5678)` y `debugpy.wait_for_client()` a un script Python. Conéctate desde VS Code usando una configuración `attach` en `launch.json`. Establece un breakpoint y verifica que el debugger se detiene en él.

### Nivel Intermedio

Configura un contenedor Docker que ejecute un servidor FastAPI con debugpy habilitado. Expone el puerto 5678 y conéctate remotamente desde tu editor local. Depura una petición HTTP en tiempo real.

### Nivel Avanzado

Implementa un flag de entorno (`DEBUG_WAIT=true`) que active el modo `wait_for_client` solo cuando sea necesario. Configura un docker-compose con el puerto de debug expuesto opcionalmente para debugging en desarrollo sin afectar producción.

### Criterios de Éxito

- [ ] El debugger se conecta exitosamente y detiene la ejecución en el breakpoint configurado
- [ ] Puedes inspeccionar variables locales, globales y el stack trace completo en el editor
- [ ] El debug remoto funciona hacia un proceso en Docker (o VM)
- [ ] El código de producción puede activar/desactivar debugpy mediante configuración

## 6. Resumen

debugpy lleva el debugging interactivo de Python más allá del entorno local. La capacidad de adjuntarse a procesos remotos en Docker y Kubernetes transforma la depuración de bugs en entornos complejos de una tarea frustrante a un proceso metódico y eficiente con las herramientas del editor.

## 7. Reflexión

¿Has tenido alguna vez un bug que solo aparece en staging o producción y que tardaste mucho en diagnosticar con logs? ¿Cómo hubiera cambiado la situación con debugging remoto via debugpy?
