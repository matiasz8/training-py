# Activación de free-threading (--disable-gil flag)

## Definición

Guía práctica para compilar Python 3.13+ con el flag --disable-gil. Cubre proceso de compilación desde source, configuración de build options, testing de la instalación, y troubleshooting común.

## Aplicación Práctica

### Casos de Uso

1. **Compilar Python free-threaded para development**
2. **Configurar virtual environments con free-threading**
3. **Testing y validation de instalación**

### Código Ejemplo

```python
"""
Ejemplo: Activación de free-threading (--disable-gil flag)

TODO: Expandir este ejemplo con implementación completa.
"""

def main():
    print("Implementación pendiente")

if __name__ == "__main__":
    main()
```

## ¿Por Qué Es Importante?

Dominar la compilación e instalación es el primer paso práctico para experimentar con free-threading. Sin una instalación correcta, no puedes aprovechar PEP 703.

## Referencias

### Documentación Oficial
- [Python 3.13 Documentation](https://docs.python.org/3.13/)
- [PEP 703 – Free-Threading](https://peps.python.org/pep-0703/)
- [Building Python from Source](https://devguide.python.org/getting-started/setup-building/)

## Tarea de Práctica

### Nivel Básico
Compilar Python 3.13+ con --disable-gil. Verificar con sys._is_gil_enabled(). Ejecutar test suite básico.

### Nivel Intermedio
Crear script de instalación automatizada que compile Python free-threaded, configure venvs, e instale dependencies comunes.

### Nivel Avanzado
Configurar CI/CD pipeline que teste código en ambos modos (GIL/no-GIL) automáticamente.

## Summary

- 🔧 Python 3.13+ se compila con --disable-gil flag durante ./configure
- ✅ sys._is_gil_enabled() verifica si free-threading está activo
- ⚠️ Requiere compilación desde source; binaries oficiales tienen GIL enabled por defecto

## Tiempo Estimado

⏱️ **2-3 horas**

---

**Tema anterior**: [03 - PEP 703: Free-Threading](../03_pep_703_free_threading/)  
**Próximo tema**: [05 - Arquitectura interna sin GIL](../05_gil_free_architecture/)
