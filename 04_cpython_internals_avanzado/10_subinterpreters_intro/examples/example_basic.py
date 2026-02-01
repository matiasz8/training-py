"""
Subinterpreters en Python 3.12+ - Introducción completa.

Los subinterpreters permiten ejecutar código Python en intérpretes aislados
dentro del mismo proceso, cada uno con su propio GIL y estado global.

Conceptos clave:
- Aislamiento de estado entre subinterpreters
- Per-interpreter GIL (cada subinterpreter tiene su propio GIL)
- Comunicación vía canales (channels)
- Uso de _xxsubinterpreters module
- Casos de uso: plugins, sandboxing, paralelismo

NOTA: Requiere Python 3.12+ para API stable de subinterpreters.
"""

import sys
from typing import Any, Optional
import os

# Verificar disponibilidad de subinterpreters
try:
    import _xxsubinterpreters as subinterpreters
    HAS_SUBINTERPRETERS = True
except ImportError:
    HAS_SUBINTERPRETERS = False
    print("⚠️  Module _xxsubinterpreters no disponible")
    print("   Requiere Python 3.12+ compilado con subinterpreters support")


def check_subinterpreter_support():
    """
    Verifica si los subinterpreters están disponibles.
    
    Returns:
        Tuple de (disponible, mensaje)
    """
    print("\n" + "="*70)
    print("🔍 VERIFICACIÓN DE SOPORTE")
    print("="*70)
    
    print(f"\nPython version: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    if HAS_SUBINTERPRETERS:
        print("\n✅ Subinterpreters DISPONIBLES")
        print(f"   Module: {subinterpreters.__name__}")
        return True, "Disponible"
    else:
        print("\n❌ Subinterpreters NO disponibles")
        print("   Compila Python 3.12+ o usa versión que incluya _xxsubinterpreters")
        return False, "No disponible"


def demonstrate_basic_subinterpreter():
    """
    Demostración básica: crear y ejecutar código en un subinterpreter.
    """
    if not HAS_SUBINTERPRETERS:
        print("\n⚠️  Ejemplo simulado (subinterpreters no disponibles)\n")
        return
    
    print("\n" + "="*70)
    print("🚀 EJEMPLO 1: Subinterpreter Básico")
    print("="*70)
    
    print("\n1. Crear subinterpreter:")
    interp_id = subinterpreters.create()
    print(f"   Subinterpreter creado: ID={interp_id}")
    
    print("\n2. Ejecutar código en subinterpreter:")
    code = """
import sys
print(f"  → Ejecutando en subinterpreter")
print(f"  → Python version: {sys.version_info.major}.{sys.version_info.minor}")
x = 42
print(f"  → Variable x = {x}")
"""
    
    try:
        subinterpreters.run_string(interp_id, code)
        print("   ✅ Código ejecutado exitosamente")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n3. Destruir subinterpreter:")
    try:
        subinterpreters.destroy(interp_id)
        print(f"   ✅ Subinterpreter {interp_id} destruido")
    except Exception as e:
        print(f"   ❌ Error al destruir: {e}")


def demonstrate_isolation():
    """
    Demuestra el aislamiento entre subinterpreters.
    """
    if not HAS_SUBINTERPRETERS:
        print("\n⚠️  Ejemplo simulado\n")
        print("En un entorno con subinterpreters:")
        print("  • Cada subinterpreter tiene su propio namespace global")
        print("  • Variables en un subinterpreter NO afectan a otros")
        print("  • Cada uno tiene su propio sys.modules")
        return
    
    print("\n" + "="*70)
    print("🔒 EJEMPLO 2: Aislamiento de Estado")
    print("="*70)
    
    # Crear dos subinterpreters
    print("\n1. Crear dos subinterpreters:")
    interp1 = subinterpreters.create()
    interp2 = subinterpreters.create()
    print(f"   Subinterpreter 1: ID={interp1}")
    print(f"   Subinterpreter 2: ID={interp2}")
    
    # Ejecutar código que define variable en interp1
    print("\n2. Definir variable en subinterpreter 1:")
    code1 = """
shared_var = "Soy del subinterpreter 1"
print(f"  → Subinterp 1: shared_var = '{shared_var}'")
"""
    subinterpreters.run_string(interp1, code1)
    
    # Intentar acceder en interp2
    print("\n3. Intentar acceder desde subinterpreter 2:")
    code2 = """
try:
    print(f"  → Subinterp 2: shared_var = '{shared_var}'")
except NameError as e:
    print(f"  → Subinterp 2: ❌ NameError - variable no existe aquí")
    print(f"     (Esto demuestra AISLAMIENTO)")
"""
    subinterpreters.run_string(interp2, code2)
    
    print("\n4. Definir variable diferente en subinterpreter 2:")
    code3 = """
shared_var = "Soy del subinterpreter 2"
print(f"  → Subinterp 2: shared_var = '{shared_var}'")
"""
    subinterpreters.run_string(interp2, code3)
    
    # Verificar que interp1 mantiene su valor
    print("\n5. Verificar que subinterpreter 1 mantiene su valor:")
    code4 = """
print(f"  → Subinterp 1: shared_var = '{shared_var}'")
print(f"     (No fue afectado por subinterp 2)")
"""
    subinterpreters.run_string(interp1, code4)
    
    # Limpiar
    subinterpreters.destroy(interp1)
    subinterpreters.destroy(interp2)
    print("\n6. Subinterpreters destruidos")


def demonstrate_per_interpreter_gil():
    """
    Demuestra el concepto de per-interpreter GIL.
    """
    print("\n" + "="*70)
    print("🔓 EJEMPLO 3: Per-Interpreter GIL")
    print("="*70)
    
    print("\nConcepto de Per-Interpreter GIL:")
    print("-" * 70)
    print("• GIL tradicional: Un GIL global para todo el proceso")
    print("• Per-interpreter GIL: Cada subinterpreter tiene su propio GIL")
    print()
    print("Beneficio:")
    print("  ✅ Múltiples subinterpreters pueden ejecutar bytecode Python")
    print("     SIMULTANEAMENTE en diferentes CPU cores")
    print("  ✅ True paralelismo para código Python CPU-bound")
    
    if not HAS_SUBINTERPRETERS:
        print("\n⚠️  Demostración conceptual (no ejecutable)")
        print("\nCon subinterpreters habilitados:")
        print("  1. Thread 1 ejecuta subinterp A con su GIL-A")
        print("  2. Thread 2 ejecuta subinterp B con su GIL-B")
        print("  3. Ambos pueden ejecutar en paralelo en CPUs diferentes")
        return
    
    print("\n" + "-"*70)
    print("Estado actual:")
    
    # Verificar si tenemos per-interpreter GIL
    if hasattr(sys, '_is_gil_enabled'):
        print(f"  GIL enabled: {sys._is_gil_enabled()}")
    
    main_interp = subinterpreters.get_main()
    print(f"  Main interpreter ID: {main_interp}")
    
    # Crear subinterpreter para demostrar
    interp = subinterpreters.create()
    print(f"  Nuevo subinterpreter ID: {interp}")
    
    code = """
import threading
import sys
print(f"  → Ejecutando en thread: {threading.current_thread().name}")
print(f"  → Este subinterpreter tiene su propio GIL")
"""
    subinterpreters.run_string(interp, code)
    
    subinterpreters.destroy(interp)


def demonstrate_use_cases():
    """
    Muestra casos de uso prácticos de subinterpreters.
    """
    print("\n" + "="*70)
    print("💡 CASOS DE USO")
    print("="*70)
    
    print("\n1. Plugin System:")
    print("   • Cada plugin corre en su propio subinterpreter")
    print("   • Aislamiento evita conflictos entre plugins")
    print("   • Fallo en un plugin no afecta a otros")
    
    print("\n2. Sandboxing:")
    print("   • Ejecutar código no confiable en subinterpreter")
    print("   • Limitar acceso a recursos del sistema")
    print("   • Timeouts y límites de memoria por subinterpreter")
    
    print("\n3. Paralelismo CPU-bound:")
    print("   • Evitar limitaciones del GIL global")
    print("   • True paralelismo sin overhead de multiprocessing")
    print("   • Compartir memoria del proceso padre")
    
    print("\n4. Servidor web multi-tenant:")
    print("   • Cada tenant en su propio subinterpreter")
    print("   • Aislamiento de datos entre clientes")
    print("   • Mejor performance que procesos separados")
    
    print("\n5. Testing:")
    print("   • Ejecutar tests en subinterpreters aislados")
    print("   • Limpiar estado entre tests sin reiniciar proceso")
    print("   • Paralelizar ejecución de test suites")


def demonstrate_limitations():
    """
    Explica limitaciones y consideraciones de subinterpreters.
    """
    print("\n" + "="*70)
    print("⚠️  LIMITACIONES Y CONSIDERACIONES")
    print("="*70)
    
    print("\n1. Comunicación entre subinterpreters:")
    print("   ⚠️  NO pueden compartir objetos Python directamente")
    print("   ✅ Usar channels para comunicación (datos serializables)")
    print("   ✅ Compartir memoria C-level (extensiones)")
    
    print("\n2. Extensiones C:")
    print("   ⚠️  Extensiones con estado global pueden causar problemas")
    print("   ⚠️  No todas las extensiones son subinterpreter-safe")
    print("   ✅ PEP 630 define APIs para extensiones multi-interpreter")
    
    print("\n3. Performance:")
    print("   ⚠️  Overhead de creación de subinterpreters")
    print("   ⚠️  Cada subinterpreter consume memoria adicional")
    print("   ✅ Mejor que multiprocessing para muchos casos")
    
    print("\n4. Estado del ecosistema (2026):")
    print("   ⚠️  API aún en evolución (Python 3.12+)")
    print("   ⚠️  No todas las librerías son compatibles")
    print("   ✅ PEP 554 trabaja en API de alto nivel")
    
    print("\n5. Comparación con alternativas:")
    print()
    print("   Threading:         Fácil, pero limitado por GIL")
    print("   Multiprocessing:   Paralelismo real, pero overhead alto")
    print("   Asyncio:           Excelente para I/O, no para CPU")
    print("   Subinterpreters:   Paralelismo + aislamiento + eficiencia")


def explain_architecture():
    """
    Explica la arquitectura de subinterpreters.
    """
    print("\n" + "="*70)
    print("🏗️  ARQUITECTURA")
    print("="*70)
    
    print("\nComponentes clave:")
    print("-" * 70)
    
    print("\n1. PyInterpreterState:")
    print("   • Estructura C que representa un subinterpreter")
    print("   • Contiene: módulos cargados, threads, GIL, state")
    
    print("\n2. Per-Interpreter State:")
    print("   • sys.modules: Diccionario de módulos importados")
    print("   • builtins: Namespace de built-ins")
    print("   • __main__: Módulo principal")
    print("   • Excepciones pendientes")
    
    print("\n3. Runtime State:")
    print("   • Cada proceso Python tiene un PyRuntime")
    print("   • Puede contener múltiples PyInterpreterState")
    print("   • Main interpreter + N subinterpreters")
    
    print("\n4. GIL per-interpreter:")
    print("   • Python 3.12+: Cada PyInterpreterState tiene su GIL")
    print("   • Permite paralelismo real entre subinterpreters")
    print("   • Threads del mismo subinterpreter comparten su GIL")
    
    print("\nDiagrama conceptual:")
    print("-" * 70)
    print("""
    Process
    └─ PyRuntime
       ├─ Main Interpreter (GIL-Main)
       │  ├─ Thread 1
       │  └─ Thread 2
       ├─ Subinterpreter 1 (GIL-1)
       │  └─ Thread 3
       └─ Subinterpreter 2 (GIL-2)
          └─ Thread 4
    
    → Thread 1 y 2 comparten GIL-Main
    → Thread 3 tiene GIL-1 (independiente)
    → Thread 4 tiene GIL-2 (independiente)
    → Thread 3 y 4 pueden ejecutar en paralelo!
    """)


def main():
    """Función principal que ejecuta todas las demostraciones."""
    print("\n" + "="*70)
    print("🐍 SUBINTERPRETERS EN PYTHON")
    print("="*70)
    print("\nIntroducción completa a subinterpreters en Python 3.12+")
    
    # 1. Verificar soporte
    available, msg = check_subinterpreter_support()
    
    # 2. Ejemplo básico
    demonstrate_basic_subinterpreter()
    
    # 3. Aislamiento
    demonstrate_isolation()
    
    # 4. Per-interpreter GIL
    demonstrate_per_interpreter_gil()
    
    # 5. Casos de uso
    demonstrate_use_cases()
    
    # 6. Limitaciones
    demonstrate_limitations()
    
    # 7. Arquitectura
    explain_architecture()
    
    print("\n" + "="*70)
    print("📚 RECURSOS")
    print("="*70)
    print("\n• PEP 554: Multiple Interpreters in the Stdlib")
    print("• PEP 630: Isolating Extension Modules")
    print("• Docs: https://docs.python.org/3/library/_xxsubinterpreters.html")
    print("• Eric Snow's work on subinterpreters")
    
    print("\n" + "="*70)
    print("🎯 CONCLUSIONES")
    print("="*70)
    print("\n1. Subinterpreters ofrecen aislamiento + paralelismo")
    print("2. Per-interpreter GIL permite true paralelismo CPU-bound")
    print("3. Mejor eficiencia que multiprocessing en muchos casos")
    print("4. API aún evolucionando (Python 3.12+)")
    print("5. Casos de uso: plugins, sandboxing, paralelismo")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()
