# Arquitectura interna sin GIL

## Definición

Exploración profunda de los cambios arquitectónicos en CPython para soportar free-threading. Incluye: nuevas estructuras de datos thread-safe, per-object locking scheme, memory barriers, y coordinación entre threads sin GIL global.

## Aplicación Práctica

### Casos de Uso

1. **Entender cómo CPython gestiona concurrencia sin GIL**
2. **Diseñar extensiones C compatibles con arquitectura no-GIL**
3. **Debugging de race conditions a nivel de intérprete**

### Código Ejemplo

```python
"""
Ejemplo: Arquitectura interna sin GIL

TODO: Expandir este ejemplo con implementación completa.
"""

def main():
    print("Implementación pendiente")

if __name__ == "__main__":
    main()
```

## ¿Por Qué Es Importante?

Conocer la arquitectura interna es crucial para escribir código performante y thread-safe, y para contribuir al desarrollo de CPython o extensiones complejas.

## Referencias

### Documentación Oficial
- [Python 3.13 Documentation](https://docs.python.org/3.13/)
- [PEP 703 – Free-Threading](https://peps.python.org/pep-0703/)
- [CPython Source: Include/internal/pycore_lock.h](https://github.com/python/cpython)

## Tarea de Práctica

### Nivel Básico
Leer código source de Python/ceval.c y Python/lock.c. Documentar diferencias vs versión con GIL.

### Nivel Intermedio
Implementar un 'mini-intérprete' que simule per-object locking y demuestre cómo múltiples threads acceden objetos de forma segura.

### Nivel Avanzado
Contribuir patch a CPython que mejore performance de algún aspecto del per-object locking scheme.

## Summary

- 🔓 Per-object locks reemplazan el GIL global
- 🧵 Cada PyObject puede tener su propio mutex para protección granular
- ⚡ Memory barriers y atomic operations aseguran correctness

## Tiempo Estimado

⏱️ **4-5 horas**

---

**Tema anterior**: [04 - Activación de free-threading](../04_free_threading_activation/)  
**Próximo tema**: [06 - Biased reference counting](../06_biased_reference_counting/)
