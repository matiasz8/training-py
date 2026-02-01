"""
Ejemplo básico: Threading en Python
====================================

Este ejemplo demuestra el uso de threads en Python para:
1. Ejecutar tareas concurrentes
2. Sincronización con locks
3. Comunicación entre threads con Queue
4. Thread pools con ThreadPoolExecutor
5. Daemon threads
"""

import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List
import random


# =============================================================================
# EJEMPLO 1: Thread Básico
# =============================================================================

def worker_task(name: str, duration: float) -> None:
    """
    Tarea simple que simula trabajo.
    
    Args:
        name: Nombre del worker
        duration: Tiempo de ejecución en segundos
    """
    print(f"🔧 [{name}] Iniciando trabajo...")
    time.sleep(duration)
    print(f"✅ [{name}] Trabajo completado en {duration}s")


def example_basic_thread():
    """Ejemplo básico de crear y ejecutar threads."""
    print("\n📌 EJEMPLO 1: Threads Básicos")
    print("=" * 60)
    
    # Crear threads
    t1 = threading.Thread(target=worker_task, args=("Worker-1", 2.0))
    t2 = threading.Thread(target=worker_task, args=("Worker-2", 1.5))
    t3 = threading.Thread(target=worker_task, args=("Worker-3", 1.0))
    
    # Iniciar threads
    start = time.perf_counter()
    t1.start()
    t2.start()
    t3.start()
    
    # Esperar a que terminen
    t1.join()
    t2.join()
    t3.join()
    
    elapsed = time.perf_counter() - start
    print(f"\n⏱️  Tiempo total: {elapsed:.2f}s")
    print("💡 Los threads ejecutaron concurrentemente")


# =============================================================================
# EJEMPLO 2: Sincronización con Lock
# =============================================================================

counter = 0
lock = threading.Lock()


def increment_counter_unsafe(times: int) -> None:
    """Incrementa contador SIN lock (race condition)."""
    global counter
    for _ in range(times):
        temp = counter
        time.sleep(0.00001)  # Simular operación
        counter = temp + 1


def increment_counter_safe(times: int) -> None:
    """Incrementa contador CON lock (thread-safe)."""
    global counter
    for _ in range(times):
        with lock:
            temp = counter
            time.sleep(0.00001)
            counter = temp + 1


def example_thread_synchronization():
    """Demuestra necesidad de sincronización."""
    print("\n📌 EJEMPLO 2: Sincronización con Lock")
    print("=" * 60)
    
    global counter
    
    # Test sin lock
    print("\n❌ Sin lock (race condition):")
    counter = 0
    threads = [
        threading.Thread(target=increment_counter_unsafe, args=(100,))
        for _ in range(5)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    print(f"   Esperado: 500")
    print(f"   Obtenido: {counter}")
    
    # Test con lock
    print("\n✅ Con lock (thread-safe):")
    counter = 0
    threads = [
        threading.Thread(target=increment_counter_safe, args=(100,))
        for _ in range(5)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    print(f"   Esperado: 500")
    print(f"   Obtenido: {counter}")


# =============================================================================
# EJEMPLO 3: Queue para Comunicación
# =============================================================================

def producer(q: queue.Queue, items: int) -> None:
    """Produce items y los pone en la queue."""
    for i in range(items):
        item = f"item-{i}"
        q.put(item)
        print(f"📦 Producido: {item}")
        time.sleep(random.uniform(0.1, 0.3))
    q.put(None)  # Señal de fin


def consumer(q: queue.Queue, name: str) -> None:
    """Consume items de la queue."""
    while True:
        item = q.get()
        if item is None:
            q.put(None)  # Re-poner para otros consumers
            break
        print(f"🔄 [{name}] Consumiendo: {item}")
        time.sleep(random.uniform(0.2, 0.4))
        q.task_done()


def example_queue_communication():
    """Demuestra comunicación entre threads con Queue."""
    print("\n📌 EJEMPLO 3: Comunicación con Queue")
    print("=" * 60)
    
    q = queue.Queue(maxsize=5)
    
    # Crear producer y consumers
    prod = threading.Thread(target=producer, args=(q, 8))
    cons1 = threading.Thread(target=consumer, args=(q, "Consumer-1"))
    cons2 = threading.Thread(target=consumer, args=(q, "Consumer-2"))
    
    prod.start()
    cons1.start()
    cons2.start()
    
    prod.join()
    cons1.join()
    cons2.join()
    
    print("\n✅ Todos los items fueron procesados")


# =============================================================================
# EJEMPLO 4: ThreadPoolExecutor
# =============================================================================

def download_file(file_id: int) -> dict:
    """Simula descarga de archivo."""
    duration = random.uniform(0.5, 2.0)
    print(f"📥 Descargando archivo #{file_id}...")
    time.sleep(duration)
    return {
        "file_id": file_id,
        "size": random.randint(100, 1000),
        "duration": duration
    }


def example_thread_pool():
    """Demuestra uso de ThreadPoolExecutor."""
    print("\n📌 EJEMPLO 4: ThreadPoolExecutor")
    print("=" * 60)
    
    file_ids = list(range(1, 6))
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit all tasks
        futures = [executor.submit(download_file, fid) for fid in file_ids]
        
        # Process results as they complete
        for future in as_completed(futures):
            result = future.result()
            print(f"✅ Completado: Archivo #{result['file_id']} "
                  f"({result['size']}KB en {result['duration']:.2f}s)")
    
    print("\n💡 ThreadPoolExecutor gestiona threads automáticamente")


# =============================================================================
# EJEMPLO 5: Daemon Threads
# =============================================================================

def daemon_task():
    """Tarea que ejecuta indefinidamente (daemon)."""
    count = 0
    while True:
        print(f"⚙️  Daemon trabajando... (iteración {count})")
        time.sleep(1)
        count += 1


def example_daemon_threads():
    """Demuestra daemon threads."""
    print("\n📌 EJEMPLO 5: Daemon Threads")
    print("=" * 60)
    
    daemon = threading.Thread(target=daemon_task, daemon=True)
    daemon.start()
    
    print("Daemon thread iniciado. Esperando 3 segundos...")
    time.sleep(3)
    
    print("\n💡 Daemon threads terminan automáticamente cuando el programa termina")


def main():
    """Función principal."""
    print("=" * 60)
    print("THREADING EN PYTHON - EJEMPLOS")
    print("=" * 60)
    
    example_basic_thread()
    example_thread_synchronization()
    example_queue_communication()
    example_thread_pool()
    example_daemon_threads()
    
    print("\n" + "=" * 60)
    print("🎓 CONCEPTOS CLAVE:")
    print("=" * 60)
    print("1. Threads permiten concurrencia en Python")
    print("2. Lock previene race conditions")
    print("3. Queue es thread-safe para comunicación")
    print("4. ThreadPoolExecutor simplifica manejo de threads")
    print("5. GIL limita paralelismo CPU-bound")
    print("=" * 60)


if __name__ == "__main__":
    main()
