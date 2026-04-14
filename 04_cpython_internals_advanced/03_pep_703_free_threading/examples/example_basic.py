"""
PEP 703: Free-Threading Python - Demostración completa.

Este módulo demuestra las capacidades de free-threading en Python 3.13+
cuando se compila con --disable-gil.

Conceptos clave:
- Verificación de free-threading
- Benchmarking de paralelismo real vs GIL
- Análisis de overhead
- Uso de nuevas APIs thread-safe
- Recomendaciones de migración

NOTA: Requiere Python 3.13+ compilado con --disable-gil para resultados reales.
      En versiones anteriores, simula el comportamiento esperado.
"""

import sys
import threading
import time
from typing import List, Tuple, Optional
from dataclasses import dataclass
import concurrent.futures


@dataclass
class PerformanceMetrics:
    """Métricas de rendimiento para comparación."""
    mode: str
    num_threads: int
    total_time: float
    speedup: float
    efficiency: float
    overhead_percent: float


def is_free_threaded() -> bool:
    """
    Verifica si Python está corriendo con free-threading.
    
    Returns:
        True si free-threading está habilitado (GIL deshabilitado)
    """
    # Python 3.13+ tiene sys._is_gil_enabled()
    if hasattr(sys, '_is_gil_enabled'):
        return not sys._is_gil_enabled()
    return False


def get_threading_mode() -> str:
    """
    Obtiene el modo de threading actual.
    
    Returns:
        Descripción del modo de threading
    """
    if is_free_threaded():
        return "FREE-THREADING (GIL disabled)"
    return "TRADITIONAL (GIL enabled)"


def cpu_intensive_work(n: int = 10_000_000) -> int:
    """
    Trabajo CPU-intensivo: suma de números.
    
    Args:
        n: Número de iteraciones
        
    Returns:
        Resultado de la suma
    """
    total = 0
    for i in range(n):
        total += i
    return total


def parallel_computation(num_workers: int, workload_per_worker: int) -> PerformanceMetrics:
    """
    Ejecuta computación paralela con múltiples threads.
    
    Args:
        num_workers: Número de threads a usar
        workload_per_worker: Carga de trabajo por thread
        
    Returns:
        Métricas de rendimiento
    """
    results: List[int] = []
    
    def worker():
        result = cpu_intensive_work(workload_per_worker)
        results.append(result)
    
    start = time.perf_counter()
    
    threads = [threading.Thread(target=worker) for _ in range(num_workers)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    elapsed = time.perf_counter() - start
    
    return PerformanceMetrics(
        mode=get_threading_mode(),
        num_threads=num_workers,
        total_time=elapsed,
        speedup=0.0,  # Se calculará después
        efficiency=0.0,
        overhead_percent=0.0
    )


def sequential_baseline(num_tasks: int, workload_per_task: int) -> float:
    """
    Ejecuta tareas secuencialmente para obtener baseline.
    
    Args:
        num_tasks: Número de tareas
        workload_per_task: Carga por tarea
        
    Returns:
        Tiempo total en segundos
    """
    start = time.perf_counter()
    
    for _ in range(num_tasks):
        cpu_intensive_work(workload_per_task)
    
    return time.perf_counter() - start


def benchmark_free_threading():
    """
    Benchmark completo comparando diferentes configuraciones.
    """
    print("\n" + "="*70)
    print("🚀 BENCHMARK: PEP 703 Free-Threading")
    print("="*70)
    
    # Información del sistema
    print(f"\nPython version: {sys.version}")
    print(f"Threading mode: {get_threading_mode()}")
    
    if hasattr(sys, 'getswitchinterval'):
        print(f"GIL switch interval: {sys.getswitchinterval()}s")
    
    if is_free_threaded():
        print("\n✅ Free-threading HABILITADO - Esperamos paralelismo real")
    else:
        print("\n⚠️  Free-threading NO disponible - GIL está activo")
        print("   Compilar Python 3.13+ con --disable-gil para free-threading")
    
    # Configuración del benchmark
    num_tasks = 8
    workload_per_task = 5_000_000
    
    print(f"\nConfiguración:")
    print(f"  - Tareas totales: {num_tasks}")
    print(f"  - Carga por tarea: {workload_per_task:_} iteraciones")
    
    # 1. Baseline secuencial
    print(f"\n{'='*70}")
    print("📊 1. Baseline Secuencial")
    print(f"{'='*70}")
    
    baseline_time = sequential_baseline(num_tasks, workload_per_task)
    print(f"⏱️  Tiempo: {baseline_time:.3f}s")
    
    # 2. Test con diferentes números de threads
    thread_counts = [2, 4, 8]
    results: List[PerformanceMetrics] = []
    
    for num_threads in thread_counts:
        print(f"\n{'='*70}")
        print(f"📊 2. Parallel con {num_threads} threads")
        print(f"{'='*70}")
        
        metrics = parallel_computation(num_threads, workload_per_task)
        
        # Calcular métricas
        metrics.speedup = baseline_time / metrics.total_time
        metrics.efficiency = metrics.speedup / num_threads
        
        # Overhead: cuánto más lento vs ideal
        ideal_time = baseline_time / num_threads
        metrics.overhead_percent = ((metrics.total_time - ideal_time) / ideal_time) * 100
        
        results.append(metrics)
        
        print(f"⏱️  Tiempo: {metrics.total_time:.3f}s")
        print(f"⚡ Speedup: {metrics.speedup:.2f}x")
        print(f"📈 Efficiency: {metrics.efficiency:.1%}")
        print(f"⚠️  Overhead: {metrics.overhead_percent:.1f}%")
    
    # 3. Resumen y análisis
    print(f"\n{'='*70}")
    print("📊 RESUMEN COMPARATIVO")
    print(f"{'='*70}")
    
    print(f"\n{'Threads':<10} {'Tiempo':<12} {'Speedup':<10} {'Efficiency':<12}")
    print("-" * 70)
    print(f"{'Baseline':<10} {baseline_time:>8.3f}s    {'1.00x':<10} {'100.0%':<12}")
    
    for m in results:
        print(f"{m.num_threads:<10} {m.total_time:>8.3f}s    {m.speedup:>4.2f}x      {m.efficiency:>6.1%}")
    
    # Análisis de resultados
    print(f"\n{'='*70}")
    print("🎯 ANÁLISIS")
    print(f"{'='*70}")
    
    best_result = max(results, key=lambda r: r.speedup)
    
    if is_free_threaded():
        if best_result.speedup > 3.0:
            print("\n✅ EXCELENTE: Free-threading funciona como esperado")
            print(f"   - Speedup de {best_result.speedup:.2f}x con {best_result.num_threads} threads")
            print(f"   - Paralelismo real sin el GIL")
        elif best_result.speedup > 1.5:
            print("\n⚠️  MODERADO: Algún speedup, pero con overhead")
            print(f"   - Speedup de {best_result.speedup:.2f}x")
            print(f"   - Overhead: {best_result.overhead_percent:.1f}%")
            print(f"   - Posible contención en estructuras compartidas")
        else:
            print("\n❌ LIMITADO: Poco beneficio del free-threading")
            print(f"   - Speedup solo {best_result.speedup:.2f}x")
            print(f"   - Posibles cuellos de botella")
    else:
        if best_result.speedup < 1.3:
            print("\n⚠️  ESPERADO: GIL limita el paralelismo")
            print(f"   - Speedup solo {best_result.speedup:.2f}x")
            print(f"   - El GIL serializa la ejecución de bytecode")
            print(f"   - Con free-threading (--disable-gil) se esperaría 4-6x")
        else:
            print("\n❓ INESPERADO: Speedup mayor a lo esperado con GIL")
            print(f"   - Speedup de {best_result.speedup:.2f}x")


def demonstrate_thread_safety_improvements():
    """
    Demuestra mejoras en thread-safety con free-threading.
    """
    print(f"\n{'='*70}")
    print("🔒 THREAD-SAFETY CON FREE-THREADING")
    print(f"{'='*70}")
    
    if is_free_threaded():
        print("\n✅ Free-threading habilitado")
        print("\nNuevas garantías:")
        print("  - Biased reference counting para objetos locales")
        print("  - Deferred reference counting reduce contención")
        print("  - Immortal objects para built-ins comunes")
        print("  - Thread-safe garbage collector")
    else:
        print("\n⚠️  GIL tradicional activo")
        print("\nCaracterísticas actuales:")
        print("  - GIL protege estructuras internas de CPython")
        print("  - Reference counting NO es thread-safe sin GIL")
        print("  - Necesario usar threading.Lock para compartir datos")
    
    # Demostración de incremento atómico
    counter = [0]
    lock = threading.Lock()
    
    def increment_safe(iterations: int):
        """Incremento thread-safe con lock."""
        for _ in range(iterations):
            with lock:
                counter[0] += 1
    
    print("\n🧪 Test: Incremento concurrente de contador")
    
    num_threads = 4
    iterations_per_thread = 100_000
    expected = num_threads * iterations_per_thread
    
    counter[0] = 0
    threads = [
        threading.Thread(target=increment_safe, args=(iterations_per_thread,))
        for _ in range(num_threads)
    ]
    
    start = time.perf_counter()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    elapsed = time.perf_counter() - start
    
    print(f"\nResultado: {counter[0]:_} (esperado: {expected:_})")
    print(f"Tiempo: {elapsed:.3f}s")
    
    if counter[0] == expected:
        print("✅ Contador correcto - thread-safety garantizada")
    else:
        print("❌ Race condition detectada")


def migration_recommendations():
    """
    Provee recomendaciones para migración a free-threading.
    """
    print(f"\n{'='*70}")
    print("📋 RECOMENDACIONES DE MIGRACIÓN")
    print(f"{'='*70}")
    
    print("\n1. ¿Tu aplicación se beneficiará?")
    print("   ✅ SÍ: Cargas de trabajo CPU-bound paralelas")
    print("   ✅ SÍ: Procesamiento de datos, cálculos científicos")
    print("   ✅ SÍ: Múltiples cores disponibles (8+)")
    print("   ❌ NO: Principalmente I/O-bound (usa asyncio)")
    print("   ❌ NO: Single-threaded por diseño")
    
    print("\n2. Preparación del código:")
    print("   - Auditar extensiones C (deben ser thread-safe)")
    print("   - Reemplazar locks globales por locks granulares")
    print("   - Usar estructuras thread-safe (queue.Queue, etc.)")
    print("   - Evitar shared mutable state cuando sea posible")
    
    print("\n3. Testing:")
    print("   - Ejecutar con --gil=0 y --gil=1 para comparar")
    print("   - Usar ThreadSanitizer para detectar data races")
    print("   - Benchmarking extensivo")
    print("   - Monitorear overhead en código single-threaded")
    
    print("\n4. Cronograma esperado:")
    print("   - Python 3.13 (2024): Experimental, --disable-gil")
    print("   - Python 3.14 (2025): Refinamiento, mejoras")
    print("   - Python 3.15-16 (2026-27): Stable, posible default")
    
    print("\n5. Recursos:")
    print("   - PEP 703: https://peps.python.org/pep-0703/")
    print("   - Nogil CPython: https://github.com/colesbury/nogil")
    print("   - Discourse: discuss.python.org/t/pep-703")


def main():
    """Función principal que ejecuta todas las demostraciones."""
    print("\n" + "="*70)
    print("🐍 PEP 703: FREE-THREADING PYTHON")
    print("="*70)
    print("\nDemostración completa de capacidades de free-threading en Python 3.13+")
    
    # 1. Benchmark principal
    benchmark_free_threading()
    
    # 2. Thread-safety
    demonstrate_thread_safety_improvements()
    
    # 3. Recomendaciones
    migration_recommendations()
    
    print("\n" + "="*70)
    print("✨ Demo completada")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
