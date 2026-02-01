"""
Ejemplo básico: Multiprocessing en Python
==========================================

Este ejemplo demuestra el uso de multiprocessing para:
1. Ejecutar tareas en procesos separados (paralelismo real)
2. Pool de procesos
3. Comunicación entre procesos (Queue, Pipe)
4. Shared memory
5. Comparación con threading
"""

import multiprocessing as mp
import time
import os
from typing import List
import math


# =============================================================================
# EJEMPLO 1: Proceso Básico
# =============================================================================

def worker_process(name: str, duration: float) -> None:
    """
    Tarea que se ejecuta en un proceso separado.
    
    Args:
        name: Nombre del proceso
        duration: Duración del trabajo
    """
    pid = os.getpid()
    print(f"🔧 [{name}] PID={pid} - Iniciando trabajo...")
    time.sleep(duration)
    print(f"✅ [{name}] PID={pid} - Completado en {duration}s")


def example_basic_process():
    """Ejemplo básico de crear y ejecutar procesos."""
    print("\n📌 EJEMPLO 1: Procesos Básicos")
    print("=" * 60)
    print(f"PID del proceso principal: {os.getpid()}")
    
    # Crear procesos
    p1 = mp.Process(target=worker_process, args=("Worker-1", 2.0))
    p2 = mp.Process(target=worker_process, args=("Worker-2", 1.5))
    p3 = mp.Process(target=worker_process, args=("Worker-3", 1.0))
    
    # Iniciar procesos
    start = time.perf_counter()
    p1.start()
    p2.start()
    p3.start()
    
    # Esperar a que terminen
    p1.join()
    p2.join()
    p3.join()
    
    elapsed = time.perf_counter() - start
    print(f"\n⏱️  Tiempo total: {elapsed:.2f}s")
    print("💡 Los procesos ejecutaron en PARALELO (no afectados por GIL)")


# =============================================================================
# EJEMPLO 2: Pool de Procesos
# =============================================================================

def is_prime(n: int) -> bool:
    """Verifica si un número es primo (CPU-intensive)."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def count_primes_in_range(start: int, end: int) -> int:
    """Cuenta primos en un rango."""
    pid = os.getpid()
    print(f"🔢 PID={pid} - Contando primos en [{start}, {end})")
    count = sum(1 for n in range(start, end) if is_prime(n))
    print(f"✓ PID={pid} - Encontrados {count} primos")
    return count


def example_process_pool():
    """Demuestra uso de Pool para paralelizar trabajo CPU-bound."""
    print("\n📌 EJEMPLO 2: Pool de Procesos")
    print("=" * 60)
    
    # Dividir trabajo en chunks
    ranges = [
        (1, 25000),
        (25000, 50000),
        (50000, 75000),
        (75000, 100000)
    ]
    
    # Ejecutar con pool
    start = time.perf_counter()
    
    with mp.Pool(processes=4) as pool:
        results = pool.starmap(count_primes_in_range, ranges)
    
    elapsed = time.perf_counter() - start
    total_primes = sum(results)
    
    print(f"\n📊 Resultados:")
    print(f"   Total de primos encontrados: {total_primes}")
    print(f"   Tiempo: {elapsed:.2f}s")
    print(f"   💡 Pool distribuyó trabajo entre {mp.cpu_count()} CPUs")


# =============================================================================
# EJEMPLO 3: Queue para Comunicación
# =============================================================================

def producer_process(q: mp.Queue, items: int) -> None:
    """Produce items y los pone en la queue."""
    pid = os.getpid()
    for i in range(items):
        item = f"item-{i}"
        q.put(item)
        print(f"📦 PID={pid} - Producido: {item}")
        time.sleep(0.5)
    q.put(None)  # Señal de fin


def consumer_process(q: mp.Queue, name: str) -> None:
    """Consume items de la queue."""
    pid = os.getpid()
    while True:
        item = q.get()
        if item is None:
            q.put(None)  # Re-poner para otros consumers
            break
        print(f"🔄 PID={pid} [{name}] - Consumiendo: {item}")
        time.sleep(0.7)


def example_queue_communication():
    """Demuestra comunicación entre procesos con Queue."""
    print("\n📌 EJEMPLO 3: Comunicación con Queue")
    print("=" * 60)
    
    q = mp.Queue(maxsize=5)
    
    # Crear producer y consumers
    prod = mp.Process(target=producer_process, args=(q, 5))
    cons1 = mp.Process(target=consumer_process, args=(q, "Consumer-1"))
    cons2 = mp.Process(target=consumer_process, args=(q, "Consumer-2"))
    
    prod.start()
    cons1.start()
    cons2.start()
    
    prod.join()
    cons1.join()
    cons2.join()
    
    print("\n✅ Comunicación completada")


# =============================================================================
# EJEMPLO 4: Shared Memory
# =============================================================================

def increment_shared_value(shared_val: mp.Value, lock: mp.Lock, times: int) -> None:
    """Incrementa un valor compartido."""
    for _ in range(times):
        with lock:
            shared_val.value += 1


def example_shared_memory():
    """Demuestra uso de memoria compartida."""
    print("\n📌 EJEMPLO 4: Shared Memory")
    print("=" * 60)
    
    # Crear valor compartido con lock
    shared_counter = mp.Value('i', 0)  # 'i' = integer
    lock = mp.Lock()
    
    # Crear múltiples procesos que incrementan el contador
    processes = [
        mp.Process(target=increment_shared_value, args=(shared_counter, lock, 1000))
        for _ in range(4)
    ]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    print(f"\n📊 Valor final del contador: {shared_counter.value}")
    print(f"   Esperado: 4000")
    print(f"   💡 Lock previene race conditions entre procesos")


# =============================================================================
# COMPARACIÓN: Threading vs Multiprocessing
# =============================================================================

def cpu_bound_task(n: int) -> int:
    """Tarea CPU-intensive."""
    return sum(i * i for i in range(n))


def example_threading_vs_multiprocessing():
    """Compara threading vs multiprocessing para CPU-bound."""
    print("\n📌 EJEMPLO 5: Threading vs Multiprocessing")
    print("=" * 60)
    
    tasks = [10000000] * 4
    
    # Multiprocessing (paralelismo real)
    start = time.perf_counter()
    with mp.Pool(4) as pool:
        pool.map(cpu_bound_task, tasks)
    mp_time = time.perf_counter() - start
    
    print(f"\n⚡ Multiprocessing: {mp_time:.2f}s")
    print(f"   💡 Aprovecha múltiples CPUs (paralelismo real)")
    print(f"   🎯 Ideal para: CPU-bound tasks")
    print(f"   ⚠️  Overhead: mayor uso de memoria")


def main():
    """Función principal."""
    print("=" * 60)
    print("MULTIPROCESSING EN PYTHON - EJEMPLOS")
    print("=" * 60)
    print(f"CPUs disponibles: {mp.cpu_count()}")
    
    example_basic_process()
    example_process_pool()
    example_queue_communication()
    example_shared_memory()
    example_threading_vs_multiprocessing()
    
    print("\n" + "=" * 60)
    print("🎓 CONCEPTOS CLAVE:")
    print("=" * 60)
    print("1. Multiprocessing usa procesos separados (no GIL)")
    print("2. Paralelismo REAL en tareas CPU-bound")
    print("3. Pool simplifica distribución de trabajo")
    print("4. Queue y Shared Memory para comunicación")
    print("5. Mayor overhead que threading pero true parallelism")
    print("=" * 60)


if __name__ == "__main__":
    mp.freeze_support()  # Necesario para Windows
    main()
