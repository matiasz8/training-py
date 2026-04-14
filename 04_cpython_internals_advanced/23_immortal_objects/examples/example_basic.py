"""
Immortal Objects en CPython - Demostración completa.

Los objetos inmortales son una optimización introducida en PEP 683 y refinada
en PEP 703 para free-threading. Permiten que objetos frecuentemente usados
tengan un refcount "infinito", eliminando overhead de incremento/decremento.

Conceptos clave:
- Objetos con refcount especial (immortal)
- Eliminación de overhead en threading
- Objetos built-in comunes (None, True, False, pequeños integers)
- Verificación de inmortalidad
- Impacto en performance

NOTA: Requiere Python 3.12+ para soporte completo de immortal objects.
"""

import sys
import ctypes
from typing import Any, List, Tuple
import time


def get_refcount(obj: Any) -> int:
    """
    Obtiene el reference count de un objeto.
    
    Args:
        obj: Objeto a inspeccionar
        
    Returns:
        Reference count actual
        
    Nota: sys.getrefcount() añade +1 temporal
    """
    return sys.getrefcount(obj) - 1


def is_immortal(obj: Any) -> bool:
    """
    Verifica si un objeto es inmortal.
    
    En Python 3.12+, objetos inmortales tienen un refcount especial
    muy alto (típicamente 2^30 - 1 o similar).
    
    Args:
        obj: Objeto a verificar
        
    Returns:
        True si el objeto es inmortal
    """
    refcount = sys.getrefcount(obj)
    
    # Umbral para considerar un objeto como inmortal
    # En CPython, objetos inmortales tienen refcount >= (1 << 30)
    IMMORTAL_THRESHOLD = 1 << 29  # ~536 millones
    
    return refcount > IMMORTAL_THRESHOLD


def demonstrate_common_immortals():
    """
    Demuestra qué objetos comunes son inmortales.
    """
    print("\n" + "="*70)
    print("🔮 OBJETOS INMORTALES COMUNES")
    print("="*70)
    
    print("\nVerificando inmortalidad de objetos built-in...")
    
    immortal_candidates = [
        ("None", None),
        ("True", True),
        ("False", False),
        ("Ellipsis (...)", ...),
        ("NotImplemented", NotImplemented),
        ("int(0)", 0),
        ("int(1)", 1),
        ("int(-1)", -1),
        ("int(42)", 42),
        ("int(256)", 256),
        ("int(257)", 257),  # Fuera del rango de small ints
        ("empty str ''", ""),
        ("empty tuple ()", ()),
        ("empty frozenset", frozenset()),
    ]
    
    print(f"\n{'Objeto':<25} {'Refcount':<15} {'¿Inmortal?':<12}")
    print("-" * 70)
    
    for name, obj in immortal_candidates:
        refcount = sys.getrefcount(obj)
        immortal = is_immortal(obj)
        immortal_str = "✅ SÍ" if immortal else "❌ No"
        
        if refcount > 1_000_000:
            refcount_str = f"{refcount:_} (IMMORTAL)"
        else:
            refcount_str = f"{refcount}"
        
        print(f"{name:<25} {refcount_str:<15} {immortal_str}")


def demonstrate_refcount_behavior():
    """
    Demuestra cómo los refcounts se comportan diferente para inmortales.
    """
    print("\n" + "="*70)
    print("📊 COMPORTAMIENTO DE REFERENCE COUNTING")
    print("="*70)
    
    print("\n1. Objeto normal (mutable):")
    normal_obj = [1, 2, 3]
    initial_rc = get_refcount(normal_obj)
    print(f"   Initial refcount: {initial_rc}")
    
    # Crear referencias adicionales
    refs = [normal_obj for _ in range(5)]
    new_rc = get_refcount(normal_obj)
    print(f"   After 5 refs: {new_rc} (incrementó {new_rc - initial_rc})")
    
    # Eliminar referencias
    refs.clear()
    final_rc = get_refcount(normal_obj)
    print(f"   After clear: {final_rc} (decrementó {new_rc - final_rc})")
    
    print("\n2. Objeto inmortal (None):")
    immortal_obj = None
    initial_rc_immortal = sys.getrefcount(immortal_obj)
    print(f"   Initial refcount: {initial_rc_immortal:_}")
    
    # Crear "referencias" (no afecta refcount)
    refs_immortal = [immortal_obj for _ in range(100)]
    new_rc_immortal = sys.getrefcount(immortal_obj)
    print(f"   After 100 refs: {new_rc_immortal:_}")
    
    if is_immortal(immortal_obj):
        print("   ✅ Refcount NO cambia - objeto inmortal")
    else:
        print(f"   Incrementó {new_rc_immortal - initial_rc_immortal}")


def benchmark_immortal_vs_normal():
    """
    Benchmark: Impacto de immortal objects en performance.
    """
    print("\n" + "="*70)
    print("⚡ BENCHMARK: Performance con Inmortales")
    print("="*70)
    
    iterations = 10_000_000
    
    # Test 1: Operaciones con None (inmortal)
    print(f"\n1. Test con None (inmortal) - {iterations:_} iteraciones:")
    
    start = time.perf_counter()
    for _ in range(iterations):
        x = None  # Asignación no incrementa refcount
        y = x     # Copia no incrementa refcount
    elapsed_immortal = time.perf_counter() - start
    
    print(f"   Tiempo: {elapsed_immortal:.4f}s")
    
    # Test 2: Operaciones con objeto normal
    print(f"\n2. Test con objeto normal - {iterations:_} iteraciones:")
    
    normal_obj = object()
    start = time.perf_counter()
    for _ in range(iterations):
        x = normal_obj  # Incrementa refcount
        y = x           # Incrementa refcount
    elapsed_normal = time.perf_counter() - start
    
    print(f"   Tiempo: {elapsed_normal:.4f}s")
    
    # Comparación
    if elapsed_immortal < elapsed_normal:
        speedup = elapsed_normal / elapsed_immortal
        print(f"\n   ⚡ Inmortales son {speedup:.2f}x más rápidos")
        print(f"   Ahorro: {(elapsed_normal - elapsed_immortal)*1000:.2f}ms")
    else:
        print(f"\n   ℹ️  Diferencia mínima o dentro del margen de error")


def demonstrate_thread_safety_benefit():
    """
    Demuestra el beneficio de inmortales para thread-safety.
    """
    print("\n" + "="*70)
    print("🔒 BENEFICIO EN THREADING")
    print("="*70)
    
    print("\n¿Por qué los objetos inmortales son importantes para free-threading?")
    print("\n1. Sin objetos inmortales:")
    print("   - Cada thread incrementa/decrementa refcount")
    print("   - Requiere sincronización (locks o atomics)")
    print("   - Overhead significativo en multi-threading")
    
    print("\n2. Con objetos inmortales:")
    print("   - Refcount nunca cambia")
    print("   - NO requiere sincronización")
    print("   - Zero overhead en acceso concurrente")
    
    print("\n3. Objetos que se benefician:")
    print("   ✅ None, True, False (usados constantemente)")
    print("   ✅ Small integers (-5 a 256)")
    print("   ✅ Empty collections ((), frozenset())")
    print("   ✅ Strings comunes (internadas)")
    
    if hasattr(sys, '_is_gil_enabled'):
        gil_enabled = sys._is_gil_enabled()
        if not gil_enabled:
            print("\n✅ Free-threading ACTIVO")
            print("   Los objetos inmortales eliminan contención en refcounts")
        else:
            print("\n⚠️  GIL tradicional activo")
            print("   Inmortales aún benefician eliminando incr/decr innecesarios")
    else:
        print("\n⚠️  Python < 3.13 (sin soporte free-threading)")
        print("   Inmortales aún optimizan refcounting normal")


def demonstrate_memory_management():
    """
    Demuestra aspectos de gestión de memoria con inmortales.
    """
    print("\n" + "="*70)
    print("🧠 GESTIÓN DE MEMORIA")
    print("="*70)
    
    print("\n1. Objetos inmortales:")
    print("   - Nunca son recolectados por GC")
    print("   - Existen durante toda la vida del proceso")
    print("   - No consumen recursos de GC")
    
    print("\n2. Identificación en CPython:")
    
    # Mostrar el bit pattern de refcount para inmortales
    if hasattr(sys, 'getrefcount'):
        none_rc = sys.getrefcount(None)
        print(f"   Refcount de None: {none_rc:_}")
        print(f"   En hexadecimal: 0x{none_rc:x}")
        
        if is_immortal(None):
            print("   ✅ Marcado como inmortal (bit pattern especial)")
    
    print("\n3. Small integer caching:")
    
    # Small ints (-5 a 256) son cached y posiblemente inmortales
    small_int = 42
    large_int = 1000
    
    print(f"   42 es inmortal: {is_immortal(small_int)}")
    print(f"   1000 es inmortal: {is_immortal(large_int)}")
    
    # Identity check
    a = 42
    b = 42
    print(f"\n   42 is 42: {a is b} (mismo objeto en memoria)")
    
    c = 1000
    d = 1000
    print(f"   1000 is 1000: {c is d} (diferentes objetos)")


def explain_implementation():
    """
    Explica la implementación técnica de immortal objects.
    """
    print("\n" + "="*70)
    print("⚙️  IMPLEMENTACIÓN TÉCNICA")
    print("="*70)
    
    print("\nPEP 683: Immortal Objects")
    print("-------------------------")
    print("Introducido en Python 3.12")
    print("\nMecanismo:")
    print("  1. Refcount especial: (1 << 30) - 1 en sistemas 32-bit")
    print("  2. Macros Py_INCREF/Py_DECREF detectan inmortales")
    print("  3. Skip increment/decrement si objeto es inmortal")
    
    print("\nBeneficios para PEP 703 (Free-Threading):")
    print("  • Elimina contención en refcounts compartidos")
    print("  • Reduce necesidad de atomic operations")
    print("  • Mejora scalability en multi-core")
    
    print("\nObjetos marcados como inmortales en startup:")
    print("  • Singletons: None, True, False")
    print("  • NotImplemented, Ellipsis")
    print("  • Small integers cache (-5 a 256)")
    print("  • Empty immutable collections")
    print("  • Type objects comunes")
    
    print("\nCódigo C relevante (PyObject):")
    print("  typedef struct {")
    print("      Py_ssize_t ob_refcnt;  // Si > (1<<30), es inmortal")
    print("      PyTypeObject *ob_type;")
    print("  } PyObject;")


def main():
    """Función principal que ejecuta todas las demostraciones."""
    print("\n" + "="*70)
    print("⚡ IMMORTAL OBJECTS EN CPYTHON")
    print("="*70)
    print(f"\nPython version: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    # 1. Objetos comunes inmortales
    demonstrate_common_immortals()
    
    # 2. Comportamiento de refcounting
    demonstrate_refcount_behavior()
    
    # 3. Benchmark de performance
    benchmark_immortal_vs_normal()
    
    # 4. Beneficios en threading
    demonstrate_thread_safety_benefit()
    
    # 5. Gestión de memoria
    demonstrate_memory_management()
    
    # 6. Implementación técnica
    explain_implementation()
    
    print("\n" + "="*70)
    print("🎯 CONCLUSIONES")
    print("="*70)
    print("\n1. Immortal objects eliminan overhead de refcounting")
    print("2. Críticos para free-threading (PEP 703)")
    print("3. Mejoran performance incluso con GIL")
    print("4. Automáticamente optimizados por CPython")
    print("5. Transparentes para el programador")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()

