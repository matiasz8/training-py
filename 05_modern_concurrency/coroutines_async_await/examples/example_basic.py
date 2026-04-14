"""
Ejemplo básico: Coroutines y Async/Await en Python
===================================================

Este ejemplo demuestra:
1. Qué son las coroutines
2. Sintaxis async/await
3. Diferencia entre coroutine y función normal
4. Composición de coroutines
5. Patrones comunes de uso
"""

import asyncio
import time
from typing import List, AsyncGenerator
import aiohttp
import json


# =============================================================================
# EJEMPLO 1: Coroutine Básica
# =============================================================================

async def simple_coroutine(name: str) -> str:
    """
    Una coroutine básica.
    
    'async def' define una función coroutine.
    Cuando se llama, retorna un objeto coroutine, no ejecuta inmediatamente.
    
    Args:
        name: Nombre a procesar
        
    Returns:
        Mensaje procesado
    """
    print(f"⚙️  Coroutine '{name}' iniciada")
    await asyncio.sleep(1)  # Simula operación asíncrona
    result = f"Procesado: {name}"
    print(f"✅ Coroutine '{name}' completada")
    return result


async def example_basic_coroutine():
    """Demuestra uso básico de coroutine."""
    print("\n📌 EJEMPLO 1: Coroutine Básica")
    print("=" * 60)
    
    # Llamar coroutine (retorna objeto coroutine, no ejecuta)
    coro = simple_coroutine("test")
    print(f"Tipo: {type(coro)}")
    print(f"Estado: {coro}")
    
    # Ejecutar con await
    result = await coro
    print(f"Resultado: {result}")


# =============================================================================
# EJEMPLO 2: Await - Esperar Coroutines
# =============================================================================

async def fetch_user(user_id: int) -> dict:
    """Simula fetch de datos de usuario."""
    print(f"🔍 Buscando usuario {user_id}...")
    await asyncio.sleep(0.5)  # Simula I/O
    return {"id": user_id, "name": f"User_{user_id}", "active": True}


async def fetch_posts(user_id: int) -> List[dict]:
    """Simula fetch de posts del usuario."""
    print(f"📝 Buscando posts del usuario {user_id}...")
    await asyncio.sleep(0.7)  # Simula I/O
    return [
        {"id": 1, "user_id": user_id, "title": "Post 1"},
        {"id": 2, "user_id": user_id, "title": "Post 2"}
    ]


async def example_sequential_await():
    """Demuestra ejecución secuencial con await."""
    print("\n📌 EJEMPLO 2: Await Secuencial")
    print("=" * 60)
    
    start = time.perf_counter()
    
    # Ejecutar secuencialmente (espera cada uno)
    user = await fetch_user(123)
    posts = await fetch_posts(123)
    
    elapsed = time.perf_counter() - start
    
    print(f"\n👤 Usuario: {user}")
    print(f"📄 Posts: {len(posts)} posts")
    print(f"⏱️  Tiempo: {elapsed:.2f}s (secuencial)")


async def example_concurrent_await():
    """Demuestra ejecución concurrente con gather."""
    print("\n📌 EJEMPLO 3: Await Concurrente")
    print("=" * 60)
    
    start = time.perf_counter()
    
    # Ejecutar concurrentemente con gather
    user, posts = await asyncio.gather(
        fetch_user(123),
        fetch_posts(123)
    )
    
    elapsed = time.perf_counter() - start
    
    print(f"\n👤 Usuario: {user}")
    print(f"📄 Posts: {len(posts)} posts")
    print(f"⏱️  Tiempo: {elapsed:.2f}s (concurrente)")
    print("💡 Mucho más rápido que secuencial!")


# =============================================================================
# EJEMPLO 4: Async Generators
# =============================================================================

async def async_range(start: int, end: int, delay: float = 0.1) -> AsyncGenerator[int, None]:
    """
    Generador asíncrono.
    
    Usa 'async def' y 'yield' para crear un async generator.
    """
    for i in range(start, end):
        await asyncio.sleep(delay)  # Simula operación asíncrona
        yield i


async def example_async_generator():
    """Demuestra uso de async generators."""
    print("\n📌 EJEMPLO 4: Async Generators")
    print("=" * 60)
    
    print("Iterando sobre async generator:")
    async for num in async_range(1, 6, 0.2):
        print(f"  → {num}")


# =============================================================================
# EJEMPLO 5: Composición de Coroutines
# =============================================================================

async def step1() -> str:
    """Primer paso del proceso."""
    print("  1️⃣ Ejecutando paso 1...")
    await asyncio.sleep(0.3)
    return "Datos del paso 1"


async def step2(data_from_step1: str) -> str:
    """Segundo paso que depende del primero."""
    print(f"  2️⃣ Ejecutando paso 2 con: {data_from_step1}")
    await asyncio.sleep(0.3)
    return "Datos del paso 2"


async def step3(data_from_step2: str) -> str:
    """Tercer paso que depende del segundo."""
    print(f"  3️⃣ Ejecutando paso 3 con: {data_from_step2}")
    await asyncio.sleep(0.3)
    return "Resultado final"


async def pipeline() -> str:
    """Pipeline que compone múltiples coroutines."""
    data1 = await step1()
    data2 = await step2(data1)
    result = await step3(data2)
    return result


async def example_coroutine_composition():
    """Demuestra composición de coroutines."""
    print("\n📌 EJEMPLO 5: Composición de Coroutines")
    print("=" * 60)
    
    print("Ejecutando pipeline...")
    result = await pipeline()
    print(f"✅ Resultado: {result}")


# =============================================================================
# EJEMPLO 6: Manejo de Errores en Coroutines
# =============================================================================

async def risky_operation(should_fail: bool) -> str:
    """Operación que puede fallar."""
    await asyncio.sleep(0.3)
    if should_fail:
        raise ValueError("❌ Operación falló!")
    return "✅ Operación exitosa"


async def example_error_handling():
    """Demuestra manejo de errores en coroutines."""
    print("\n📌 EJEMPLO 6: Manejo de Errores")
    print("=" * 60)
    
    # Operación exitosa
    try:
        result = await risky_operation(should_fail=False)
        print(f"Caso 1: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Operación que falla
    try:
        result = await risky_operation(should_fail=True)
        print(f"Caso 2: {result}")
    except ValueError as e:
        print(f"Caso 2: {e}")
    
    print("💡 Las excepciones en coroutines se manejan normalmente")


# =============================================================================
# EJEMPLO 7: Timeouts
# =============================================================================

async def slow_operation() -> str:
    """Operación que tarda mucho."""
    print("  ⏳ Iniciando operación lenta...")
    await asyncio.sleep(5)
    return "Completado"


async def example_timeout():
    """Demuestra uso de timeouts."""
    print("\n📌 EJEMPLO 7: Timeouts")
    print("=" * 60)
    
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
        print(f"Resultado: {result}")
    except asyncio.TimeoutError:
        print("⏰ Operación cancelada por timeout (esperado)")
    
    print("💡 wait_for() permite establecer timeouts en coroutines")


# =============================================================================
# EJEMPLO 8: Tareas en Background
# =============================================================================

async def background_task(name: str):
    """Tarea que ejecuta en background."""
    for i in range(5):
        print(f"  🔄 [{name}] Iteración {i+1}")
        await asyncio.sleep(0.5)
    print(f"  ✅ [{name}] Completado")


async def example_background_tasks():
    """Demuestra tareas en background."""
    print("\n📌 EJEMPLO 8: Tareas en Background")
    print("=" * 60)
    
    # Crear tarea en background
    task = asyncio.create_task(background_task("Background"))
    
    print("Tarea creada, haciendo otras cosas...")
    await asyncio.sleep(1)
    print("Continuando con otras operaciones...")
    await asyncio.sleep(1.5)
    
    # Esperar a que la tarea termine
    await task
    print("💡 create_task() permite tareas en background")


# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================

async def main():
    """Función principal que ejecuta todos los ejemplos."""
    print("=" * 60)
    print("COROUTINES Y ASYNC/AWAIT - EJEMPLOS")
    print("=" * 60)
    
    await example_basic_coroutine()
    await example_sequential_await()
    await example_concurrent_await()
    await example_async_generator()
    await example_coroutine_composition()
    await example_error_handling()
    await example_timeout()
    await example_background_tasks()
    
    print("\n" + "=" * 60)
    print("🎓 CONCEPTOS CLAVE:")
    print("=" * 60)
    print("1. Coroutines son funciones definidas con 'async def'")
    print("2. 'await' pausa la coroutine hasta que la operación complete")
    print("3. asyncio.gather() ejecuta múltiples coroutines concurrentemente")
    print("4. Async generators permiten iteración asíncrona")
    print("5. create_task() ejecuta coroutines en background")
    print("6. wait_for() permite establecer timeouts")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
