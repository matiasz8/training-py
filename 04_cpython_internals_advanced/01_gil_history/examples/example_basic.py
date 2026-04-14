"""
Ejemplo básico: Historia del GIL - Demostración del impacto del GIL
===================================================================

Este ejemplo demuestra el impacto del Global Interpreter Lock (GIL)
en operaciones CPU-bound vs I/O-bound en Python.

El GIL es un mutex que protege el acceso a objetos Python, permitiendo
que solo un hilo ejecute bytecode Python a la vez.
"""

import threading
import time
import sys
from typing import Callable, List
from dataclasses import dataclass


@dataclass
class BenchmarkResult:
    """Resultado de un benchmark."""
    task_name: str
    num_threads: int
    total_time: float
    time_per_task: float
    speedup: float = 1.0


def cpu_bound_task(n: int) -> int:
    """
    Tarea intensiva en CPU: cálculo de Fibonacci.
    
    Esta tarea es CPU-bound (limitada por CPU) y será afectada
    negativamente por el GIL, ya que solo un hilo puede ejecutar
    bytecode Python a la vez.
    
    Args:
        n: Número de iteraciones para calcular Fibonacci
        
    Returns:
        El n-ésimo número de Fibonacci
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def io_bound_task(duration: float) -> None:
    """
    Tarea intensiva en I/O: simula operación de red/disco.
    
    Esta tarea es I/O-bound (limitada por I/O) y NO será afectada
    significativamente por el GIL, ya que durante time.sleep() el
    hilo libera el GIL, permitiendo que otros hilos ejecuten.
    
    Args:
        duration: Duración de la operación I/O en segundos
    """
    time.sleep(duration)


def measure_execution(
    task: Callable,
    args: tuple,
    num_threads: int,
    task_name: str
) -> BenchmarkResult:
    """
    Mide el tiempo de ejecución con diferentes números de hilos.
    
    Args:
        task: Función a ejecutar
        args: Argumentos para la función
        num_threads: Número de hilos a usar
        task_name: Nombre descriptivo de la tarea
        
    Returns:
        BenchmarkResult con los resultados del benchmark
    """
    print(f"\n{'='*60}")
    print(f"Ejecutando: {task_name}")
    print(f"Hilos: {num_threads}")
    print(f"{'='*60}")
    
    start = time.perf_counter()
    
    if num_threads == 1:
        # Ejecución secuencial (baseline)
        for _ in range(num_threads):
            task(*args)
    else:
        # Ejecución multi-threaded
        threads: List[threading.Thread] = []
        for _ in range(num_threads):
            t = threading.Thread(target=task, args=args)
            threads.append(t)
            t.start()
        
        # Esperar a que todos los hilos terminen
        for t in threads:
            t.join()
    
    end = time.perf_counter()
    elapsed = end - start
    
    print(f"Tiempo total: {elapsed:.4f} segundos")
    print(f"Tiempo por tarea: {elapsed/num_threads:.4f} segundos")
    
    return BenchmarkResult(
        task_name=task_name,
        num_threads=num_threads,
        total_time=elapsed,
        time_per_task=elapsed/num_threads
    )


def main():
    """Función principal que ejecuta los benchmarks del GIL."""
    print("="*60)
    print("DEMOSTRACIÓN DEL IMPACTO DEL GIL")
    print("="*60)
    print(f"Python version: {sys.version}")
    
    # Verificar si el GIL está habilitado (Python 3.13+)
    if hasattr(sys, '_is_gil_enabled'):
        print(f"GIL habilitado: {sys._is_gil_enabled()}")
    else:
        print("GIL habilitado: Yes (Python < 3.13)")
    
    # ============================================================
    # TEST 1: Operación CPU-BOUND (afectada por GIL)
    # ============================================================
    print("\n" + "="*60)
    print("TEST 1: OPERACIÓN CPU-BOUND")
    print("="*60)
    print("El GIL previene ejecución paralela real en tareas CPU-bound.")
    print("Esperamos que multi-threading NO mejore el rendimiento.\n")
    
    # Benchmark single-threaded
    single_cpu = measure_execution(
        cpu_bound_task,
        (1000000,),
        1,
        "CPU-bound (1 hilo - baseline)"
    )
    
    # Benchmark multi-threaded
    multi_cpu = measure_execution(
        cpu_bound_task,
        (1000000,),
        4,
        "CPU-bound (4 hilos)"
    )
    
    # Calcular speedup
    speedup_cpu = single_cpu.total_time / multi_cpu.total_time
    multi_cpu.speedup = speedup_cpu
    
    print(f"\n{'='*60}")
    print(f"RESULTADO CPU-BOUND:")
    print(f"Speedup: {speedup_cpu:.2f}x")
    if speedup_cpu < 1.5:
        print("❌ El GIL está limitando el paralelismo")
        print("   (esperábamos 4x speedup con 4 hilos, pero no lo obtuvimos)")
    else:
        print("✅ Paralelismo efectivo (esto sería inusual con el GIL)")
    print(f"{'='*60}")
    
    # ============================================================
    # TEST 2: Operación I/O-BOUND (NO afectada por GIL)
    # ============================================================
    print("\n" + "="*60)
    print("TEST 2: OPERACIÓN I/O-BOUND")
    print("="*60)
    print("Durante operaciones I/O, el GIL es liberado.")
    print("Esperamos que multi-threading SÍ mejore el rendimiento.\n")
    
    # Benchmark single-threaded
    single_io = measure_execution(
        io_bound_task,
        (0.5,),
        1,
        "I/O-bound (1 hilo - baseline)"
    )
    
    # Benchmark multi-threaded
    multi_io = measure_execution(
        io_bound_task,
        (0.5,),
        4,
        "I/O-bound (4 hilos)"
    )
    
    # Calcular speedup
    speedup_io = single_io.total_time / multi_io.total_time
    multi_io.speedup = speedup_io
    
    print(f"\n{'='*60}")
    print(f"RESULTADO I/O-BOUND:")
    print(f"Speedup: {speedup_io:.2f}x")
    if speedup_io > 2.0:
        print("✅ Multi-threading es efectivo para I/O-bound")
        print("   (el GIL es liberado durante operaciones I/O)")
    else:
        print("⚠️  Speedup menor al esperado")
    print(f"{'='*60}")
    
    # ============================================================
    # RESUMEN Y CONCLUSIONES
    # ============================================================
    print("\n" + "="*60)
    print("CONCLUSIONES:")
    print("="*60)
    print(f"1. CPU-bound speedup: {speedup_cpu:.2f}x (esperado: ~1x)")
    print(f"2. I/O-bound speedup: {speedup_io:.2f}x (esperado: ~4x)")
    print("\n📝 LECCIONES CLAVE:")
    print("   • El GIL limita el paralelismo en tareas CPU-bound")
    print("   • El GIL NO afecta significativamente tareas I/O-bound")
    print("   • Para CPU-bound: usar multiprocessing")
    print("   • Para I/O-bound: threading o asyncio son efectivos")
    print("="*60)


if __name__ == "__main__":
    main()
