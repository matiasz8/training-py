"""
Demostración de las limitaciones del GIL tradicional en CPython.

Este módulo ilustra:
1. Serialización de operaciones CPU-bound multi-threaded
2. Convoy effect y GIL thrashing
3. Priority inversion (hilos I/O vs CPU)
4. Overhead de context switching

Conceptos clave:
- El GIL solo permite a un hilo ejecutar bytecode Python a la vez
- Operaciones CPU-bound no se benefician de threading
- El GIL introduce overhead de sincronización
- Sistemas multi-core no aprovechan su potencial completo
"""

import threading
import time
import sys
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class BenchmarkResult:
    """Resultado de un benchmark de ejecución."""
    strategy: str
    num_workers: int
    total_time: float
    speedup: float
    efficiency: float  # speedup / num_workers


def cpu_intensive_task(n: int = 10_000_000) -> int:
    """
    Tarea CPU-intensiva: suma de números.
    
    Args:
        n: Cantidad de iteraciones
        
    Returns:
        Suma total calculada
    """
    total = 0
    for i in range(n):
        total += i
    return total


def benchmark_single_threaded(iterations: int = 5) -> BenchmarkResult:
    """
    Benchmark en modo single-threaded (baseline).
    
    Args:
        iterations: Número de tareas a ejecutar
        
    Returns:
        Resultado del benchmark
    """
    print(f"\n{'='*60}")
    print("🔷 Benchmark: Single-Threaded (Baseline)")
    print(f"{'='*60}")
    
    start = time.perf_counter()
    
    for i in range(iterations):
        result = cpu_intensive_task()
        print(f"  Task {i+1}: Completado (result={result:_})")
    
    elapsed = time.perf_counter() - start
    
    print(f"\n⏱️  Tiempo total: {elapsed:.3f}s")
    
    return BenchmarkResult(
        strategy="Single-threaded",
        num_workers=1,
        total_time=elapsed,
        speedup=1.0,
        efficiency=1.0
    )


def benchmark_multi_threaded(iterations: int = 5, num_threads: int = 4) -> BenchmarkResult:
    """
    Benchmark usando múltiples threads (limitado por GIL).
    
    Args:
        iterations: Número de tareas a ejecutar
        num_threads: Número de threads a usar
        
    Returns:
        Resultado del benchmark
    """
    print(f"\n{'='*60}")
    print(f"🔶 Benchmark: Multi-Threaded ({num_threads} threads)")
    print(f"{'='*60}")
    print("⚠️  LIMITACIÓN DEL GIL: Los threads NO ejecutarán en paralelo")
    
    results: List[int] = [0] * iterations
    threads: List[threading.Thread] = []
    
    def worker(task_id: int):
        results[task_id] = cpu_intensive_task()
        print(f"  Thread {threading.current_thread().name}: Task {task_id+1} completado")
    
    start = time.perf_counter()
    
    # Crear y lanzar threads
    for i in range(iterations):
        thread = threading.Thread(target=worker, args=(i,), name=f"Worker-{i+1}")
        threads.append(thread)
        thread.start()
    
    # Esperar a que todos terminen
    for thread in threads:
        thread.join()
    
    elapsed = time.perf_counter() - start
    
    print(f"\n⏱️  Tiempo total: {elapsed:.3f}s")
    
    return BenchmarkResult(
        strategy=f"Multi-threaded ({num_threads})",
        num_workers=num_threads,
        total_time=elapsed,
        speedup=1.0,  # Se calculará después
        efficiency=1.0
    )


def demonstrate_gil_contention():
    """
    Demuestra el GIL contention con múltiples threads compitiendo.
    
    Muestra cómo el overhead de adquisición del GIL puede hacer que
    el código multi-threaded sea MÁS LENTO que single-threaded.
    """
    print(f"\n{'='*60}")
    print("🔥 Demostración: GIL Contention")
    print(f"{'='*60}")
    print("Múltiples threads compitiendo agresivamente por el GIL...\n")
    
    contention_count = [0]
    lock = threading.Lock()
    
    def contentious_worker(worker_id: int, iterations: int = 1_000_000):
        """Worker que incrementa un contador compartido."""
        local_count = 0
        for _ in range(iterations):
            # Operación que requiere el GIL
            local_count += 1
        
        # Actualizar contador global
        with lock:
            contention_count[0] += local_count
            print(f"  Worker-{worker_id}: Completó {iterations:_} iteraciones")
    
    num_threads = 8
    threads = []
    
    start = time.perf_counter()
    
    for i in range(num_threads):
        thread = threading.Thread(target=contentious_worker, args=(i+1,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    elapsed = time.perf_counter() - start
    
    print(f"\n⏱️  Tiempo con {num_threads} threads: {elapsed:.3f}s")
    print(f"📊 Total de operaciones: {contention_count[0]:_}")
    print(f"\n💡 Overhead del GIL: Los threads pasan más tiempo")
    print(f"   esperando el GIL que ejecutando código útil.")


def demonstrate_priority_inversion():
    """
    Demuestra priority inversion: threads I/O-bound bloqueados por CPU-bound.
    
    Un hilo I/O que necesita respuesta rápida es bloqueado por un
    hilo CPU-intensivo que retiene el GIL.
    """
    print(f"\n{'='*60}")
    print("⚡ Demostración: Priority Inversion")
    print(f"{'='*60}")
    print("Thread I/O-bound bloqueado por thread CPU-bound...\n")
    
    io_responses: List[Tuple[int, float]] = []
    
    def io_worker(worker_id: int):
        """Simula operaciones I/O que necesitan respuesta rápida."""
        for i in range(5):
            start = time.perf_counter()
            # Simular I/O (e.g., request HTTP)
            time.sleep(0.01)  # Libera el GIL durante sleep
            elapsed = time.perf_counter() - start
            io_responses.append((worker_id, elapsed))
            print(f"  I/O-Worker-{worker_id}: Request {i+1} completada en {elapsed:.3f}s")
    
    def cpu_worker(worker_id: int):
        """Simula operación CPU-intensiva que retiene el GIL."""
        print(f"  CPU-Worker-{worker_id}: Iniciando tarea CPU-intensiva...")
        result = cpu_intensive_task(n=15_000_000)
        print(f"  CPU-Worker-{worker_id}: Completado (result={result:_})")
    
    # Lanzar thread CPU-bound primero
    cpu_thread = threading.Thread(target=cpu_worker, args=(1,))
    cpu_thread.start()
    
    # Pequeña demora para asegurar que CPU thread toma el GIL
    time.sleep(0.05)
    
    # Lanzar thread I/O-bound
    io_thread = threading.Thread(target=io_worker, args=(1,))
    io_thread.start()
    
    cpu_thread.join()
    io_thread.join()
    
    if io_responses:
        avg_latency = sum(t for _, t in io_responses) / len(io_responses)
        print(f"\n📊 Latencia promedio I/O: {avg_latency:.3f}s")
        print(f"💡 Las operaciones I/O sufrieron latencia adicional")
        print(f"   debido a que el thread CPU retenía el GIL.")


def print_gil_info():
    """Imprime información sobre el GIL en el intérprete actual."""
    print(f"\n{'='*60}")
    print("🐍 Información del GIL")
    print(f"{'='*60}")
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    # Check switch interval (Python 3.2+)
    if hasattr(sys, 'getswitchinterval'):
        interval = sys.getswitchinterval()
        print(f"GIL switch interval: {interval}s ({interval*1000}ms)")
        print(f"\n💡 El GIL se libera cada ~{interval*1000}ms para dar")
        print(f"   oportunidad a otros threads de ejecutar.")
    
    # En Python 3.13+ con free-threading
    if hasattr(sys, '_is_gil_enabled'):
        gil_enabled = sys._is_gil_enabled()
        print(f"GIL habilitado: {gil_enabled}")


def main():
    """Función principal que ejecuta todas las demostraciones."""
    print("\n" + "="*60)
    print("🔒 LIMITACIONES DEL GIL TRADICIONAL")
    print("="*60)
    
    # Info del sistema
    print_gil_info()
    
    # 1. Benchmark single-threaded (baseline)
    baseline = benchmark_single_threaded(iterations=5)
    
    # 2. Benchmark multi-threaded (limitado por GIL)
    multi = benchmark_multi_threaded(iterations=5, num_threads=4)
    
    # Calcular speedup
    multi.speedup = baseline.total_time / multi.total_time
    multi.efficiency = multi.speedup / multi.num_workers
    
    # 3. Resumen comparativo
    print(f"\n{'='*60}")
    print("📊 RESUMEN COMPARATIVO")
    print(f"{'='*60}")
    print(f"Single-threaded: {baseline.total_time:.3f}s (baseline)")
    print(f"Multi-threaded:  {multi.total_time:.3f}s ({multi.num_workers} threads)")
    print(f"Speedup:         {multi.speedup:.2f}x")
    print(f"Efficiency:      {multi.efficiency:.1%}")
    
    if multi.speedup < 1.2:
        print(f"\n⚠️  LIMITACIÓN DEL GIL DEMOSTRADA:")
        print(f"   - Speedup < 1.2x con {multi.num_workers} threads")
        print(f"   - El GIL previene paralelismo real")
        print(f"   - Operaciones CPU-bound NO se benefician de threading")
    
    # 4. GIL Contention
    demonstrate_gil_contention()
    
    # 5. Priority Inversion
    demonstrate_priority_inversion()
    
    # Conclusiones
    print(f"\n{'='*60}")
    print("🎯 CONCLUSIONES")
    print(f"{'='*60}")
    print("1. El GIL serializa ejecución de bytecode Python")
    print("2. Threading NO ayuda en tareas CPU-bound")
    print("3. Múltiples threads pueden ser PEOR que single-thread")
    print("4. Alternativas: multiprocessing, asyncio, Cython, PyO3")
    print("5. Python 3.13+ ofrece free-threading experimental")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
