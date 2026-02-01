"""
TaskGroups en Python 3.11+ - Asyncio estructurado.

TaskGroup (PEP 654) introduce "structured concurrency" en asyncio,
permitiendo gestionar múltiples tareas de forma segura y predecible.

Conceptos clave:
- Gestión automática del ciclo de vida de tareas
- Cancelación en cascada si una tarea falla
- Exception groups para manejar múltiples errores
- Context manager para tareas concurrentes
- Reemplazo moderno de asyncio.gather()

Requiere: Python 3.11+
"""

import asyncio
import time
from typing import List
import random


# =============================================================================
# EJEMPLO 1: TaskGroup Básico
# =============================================================================

async def fetch_data(url: str, delay: float) -> str:
    """
    Simula fetch de datos con delay.
    
    Args:
        url: URL a fetchear
        delay: Tiempo de espera en segundos
        
    Returns:
        Datos obtenidos
    """
    print(f"  → Fetching {url}...")
    await asyncio.sleep(delay)
    result = f"Data from {url}"
    print(f"  ✅ Completed {url}")
    return result


async def demo_basic_taskgroup():
    """Demostración básica de TaskGroup."""
    print("\n" + "="*70)
    print("🚀 EJEMPLO 1: TaskGroup Básico")
    print("="*70)
    
    print("\nLanzando 3 tareas concurrentes...")
    start = time.perf_counter()
    
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data("api.example.com/users", 1.0))
        task2 = tg.create_task(fetch_data("api.example.com/posts", 1.5))
        task3 = tg.create_task(fetch_data("api.example.com/comments", 0.8))
    
    elapsed = time.perf_counter() - start
    
    # Resultados disponibles después del context manager
    print(f"\n✅ Todas las tareas completadas en {elapsed:.2f}s")
    print(f"   Task 1 result: {task1.result()}")
    print(f"   Task 2 result: {task2.result()}")
    print(f"   Task 3 result: {task3.result()}")
    
    print("\n💡 Ventaja: TaskGroup espera automáticamente a todas las tareas")


# =============================================================================
# EJEMPLO 2: Manejo de Excepciones
# =============================================================================

async def task_that_fails(task_id: int) -> str:
    """Tarea que puede fallar."""
    delay = random.uniform(0.5, 1.5)
    await asyncio.sleep(delay)
    
    if random.random() < 0.4:  # 40% de probabilidad de fallo
        raise ValueError(f"Task {task_id} failed!")
    
    return f"Task {task_id} succeeded"


async def demo_exception_handling():
    """Demuestra manejo de excepciones con TaskGroup."""
    print("\n" + "="*70)
    print("⚠️  EJEMPLO 2: Manejo de Excepciones")
    print("="*70)
    
    print("\nLanzando tareas que pueden fallar...")
    
    try:
        async with asyncio.TaskGroup() as tg:
            for i in range(5):
                tg.create_task(task_that_fails(i))
    
    except* ValueError as eg:  # Exception group syntax (PEP 654)
        print(f"\n❌ {len(eg.exceptions)} tarea(s) fallaron:")
        for i, exc in enumerate(eg.exceptions, 1):
            print(f"   {i}. {exc}")
    
    print("\n💡 TaskGroup cancela todas las tareas si una falla")
    print("   (comportamiento fail-fast)")


# =============================================================================
# EJEMPLO 3: Comparación con gather()
# =============================================================================

async def worker(name: str, duration: float) -> str:
    """Worker simple."""
    await asyncio.sleep(duration)
    return f"{name} finished"


async def demo_vs_gather():
    """Compara TaskGroup con asyncio.gather()."""
    print("\n" + "="*70)
    print("⚖️  EJEMPLO 3: TaskGroup vs gather()")
    print("="*70)
    
    # Usando TaskGroup
    print("\n1. Con TaskGroup:")
    start = time.perf_counter()
    
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(worker("Worker-A", 0.5))
        t2 = tg.create_task(worker("Worker-B", 0.3))
        t3 = tg.create_task(worker("Worker-C", 0.4))
    
    elapsed_tg = time.perf_counter() - start
    print(f"   Tiempo: {elapsed_tg:.3f}s")
    print(f"   ✅ Structured concurrency")
    print(f"   ✅ Cancelación automática en errores")
    
    # Usando gather()
    print("\n2. Con gather():")
    start = time.perf_counter()
    
    results = await asyncio.gather(
        worker("Worker-A", 0.5),
        worker("Worker-B", 0.3),
        worker("Worker-C", 0.4)
    )
    
    elapsed_gather = time.perf_counter() - start
    print(f"   Tiempo: {elapsed_gather:.3f}s")
    print(f"   ⚠️  Requiere manejo manual de errores")
    print(f"   ⚠️  Puede dejar tareas huérfanas")
    
    print("\n💡 TaskGroup es más seguro y predecible")


# =============================================================================
# EJEMPLO 4: Procesamiento Pipeline
# =============================================================================

async def download(item_id: int) -> dict:
    """Simula descarga de datos."""
    await asyncio.sleep(0.5)
    return {"id": item_id, "data": f"raw_data_{item_id}"}


async def process(item: dict) -> dict:
    """Simula procesamiento."""
    await asyncio.sleep(0.3)
    item["processed"] = True
    return item


async def save(item: dict) -> str:
    """Simula guardado."""
    await asyncio.sleep(0.2)
    return f"Saved item {item['id']}"


async def demo_pipeline():
    """Pipeline de procesamiento con TaskGroups anidados."""
    print("\n" + "="*70)
    print("🔄 EJEMPLO 4: Pipeline de Procesamiento")
    print("="*70)
    
    items_to_process = [1, 2, 3, 4, 5]
    
    print(f"\nProcesando {len(items_to_process)} items...")
    start = time.perf_counter()
    
    # Stage 1: Download
    print("\n1. Stage: Download")
    async with asyncio.TaskGroup() as tg:
        download_tasks = [tg.create_task(download(i)) for i in items_to_process]
    
    downloaded = [t.result() for t in download_tasks]
    print(f"   ✅ Downloaded {len(downloaded)} items")
    
    # Stage 2: Process
    print("\n2. Stage: Process")
    async with asyncio.TaskGroup() as tg:
        process_tasks = [tg.create_task(process(item)) for item in downloaded]
    
    processed = [t.result() for t in process_tasks]
    print(f"   ✅ Processed {len(processed)} items")
    
    # Stage 3: Save
    print("\n3. Stage: Save")
    async with asyncio.TaskGroup() as tg:
        save_tasks = [tg.create_task(save(item)) for item in processed]
    
    saved = [t.result() for t in save_tasks]
    print(f"   ✅ Saved {len(saved)} items")
    
    elapsed = time.perf_counter() - start
    print(f"\n⏱️  Pipeline completado en {elapsed:.2f}s")
    print("💡 Cada stage espera a que todos completen antes de continuar")


# =============================================================================
# EJEMPLO 5: Cancelación y Cleanup
# =============================================================================

async def long_running_task(task_id: int):
    """Tarea de larga duración."""
    try:
        print(f"  → Task {task_id} iniciada")
        await asyncio.sleep(10)  # Tarea larga
        print(f"  ✅ Task {task_id} completada")
    except asyncio.CancelledError:
        print(f"  ❌ Task {task_id} cancelada (cleanup aquí)")
        raise


async def demo_cancellation():
    """Demuestra cancelación con TaskGroup."""
    print("\n" + "="*70)
    print("🛑 EJEMPLO 5: Cancelación")
    print("="*70)
    
    print("\nLanzando tareas y cancelando después de 2s...")
    
    try:
        async with asyncio.timeout(2.0):  # Python 3.11+
            async with asyncio.TaskGroup() as tg:
                for i in range(5):
                    tg.create_task(long_running_task(i))
    
    except TimeoutError:
        print("\n⏱️  Timeout alcanzado")
        print("💡 TaskGroup canceló automáticamente todas las tareas pendientes")


# =============================================================================
# EJEMPLO 6: Patrón Fan-Out/Fan-In
# =============================================================================

async def process_chunk(chunk_id: int, data: List[int]) -> int:
    """Procesa un chunk de datos."""
    await asyncio.sleep(random.uniform(0.1, 0.5))
    result = sum(data) * 2
    print(f"  → Chunk {chunk_id}: processed {len(data)} items = {result}")
    return result


async def demo_fan_out_fan_in():
    """Patrón fan-out/fan-in con TaskGroup."""
    print("\n" + "="*70)
    print("🌟 EJEMPLO 6: Fan-Out/Fan-In")
    print("="*70)
    
    # Datos a procesar
    data = list(range(100))
    chunk_size = 10
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    print(f"\nProcesando {len(data)} items en {len(chunks)} chunks...")
    start = time.perf_counter()
    
    # Fan-out: procesar chunks en paralelo
    async with asyncio.TaskGroup() as tg:
        tasks = [
            tg.create_task(process_chunk(i, chunk))
            for i, chunk in enumerate(chunks)
        ]
    
    # Fan-in: combinar resultados
    results = [t.result() for t in tasks]
    total = sum(results)
    
    elapsed = time.perf_counter() - start
    
    print(f"\n✅ Resultado total: {total}")
    print(f"⏱️  Tiempo: {elapsed:.2f}s")
    print("💡 Procesamiento paralelo de chunks independientes")


# =============================================================================
# Main
# =============================================================================

async def main():
    """Función principal que ejecuta todas las demos."""
    print("\n" + "="*70)
    print("🐍 TASKGROUPS EN PYTHON 3.11+")
    print("="*70)
    print("\nStructured Concurrency con asyncio.TaskGroup")
    
    # 1. Básico
    await demo_basic_taskgroup()
    
    # 2. Excepciones
    await demo_exception_handling()
    
    # 3. Comparación
    await demo_vs_gather()
    
    # 4. Pipeline
    await demo_pipeline()
    
    # 5. Cancelación
    await demo_cancellation()
    
    # 6. Fan-out/fan-in
    await demo_fan_out_fan_in()
    
    print("\n" + "="*70)
    print("🎯 CONCLUSIONES")
    print("="*70)
    print("\n1. TaskGroup implementa structured concurrency")
    print("2. Gestión automática del ciclo de vida de tareas")
    print("3. Cancelación en cascada en caso de error")
    print("4. Más seguro que gather() para la mayoría de casos")
    print("5. Exception groups para manejar errores múltiples")
    print("6. Patrón recomendado para asyncio en Python 3.11+")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    asyncio.run(main())

