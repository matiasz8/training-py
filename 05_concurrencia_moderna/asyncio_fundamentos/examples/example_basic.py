"""
Ejemplo básico: Asyncio Fundamentos
====================================

Este ejemplo demuestra los conceptos fundamentales de asyncio en Python:
- Funciones asíncronas (async def)
- Palabras clave await
- Event loop
- Tareas concurrentes
- Comparación con código síncrono
"""

import asyncio
import time
from typing import List


# =============================================================================
# EJEMPLO 1: Función asíncrona básica
# =============================================================================

async def greet(name: str, delay: float) -> str:
    """
    Función asíncrona simple que saluda después de un delay.
    
    La palabra clave 'async' define una coroutine.
    'await' permite que otras tareas se ejecuten durante la espera.
    
    Args:
        name: Nombre a saludar
        delay: Segundos a esperar antes de saludar
        
    Returns:
        Mensaje de saludo
    """
    print(f"[{name}] Esperando {delay}s...")
    await asyncio.sleep(delay)  # Operación asíncrona - libera el control
    message = f"¡Hola, {name}!"
    print(f"[{name}] {message}")
    return message


# =============================================================================
# EJEMPLO 2: Ejecutar múltiples coroutines concurrentemente
# =============================================================================

async def download_file(file_id: int, size: int) -> dict:
    """
    Simula la descarga de un archivo de manera asíncrona.
    
    Args:
        file_id: Identificador del archivo
        size: Tamaño en MB (simula tiempo de descarga)
        
    Returns:
        Información del archivo descargado
    """
    print(f"📥 Iniciando descarga de archivo #{file_id} ({size}MB)")
    
    # Simular descarga (en realidad sería una operación I/O)
    await asyncio.sleep(size * 0.1)  # 0.1s por MB
    
    result = {
        "file_id": file_id,
        "size": size,
        "status": "completado"
    }
    
    print(f"✅ Archivo #{file_id} descargado ({size}MB)")
    return result


async def download_multiple_files(file_sizes: List[int]) -> List[dict]:
    """
    Descarga múltiples archivos concurrentemente usando asyncio.gather().
    
    asyncio.gather() ejecuta múltiples coroutines de manera concurrente
    y espera a que todas terminen.
    
    Args:
        file_sizes: Lista de tamaños de archivos en MB
        
    Returns:
        Lista de resultados de descarga
    """
    print("\n🚀 Iniciando descargas concurrentes...")
    start = time.perf_counter()
    
    # Crear tareas para cada archivo
    tasks = [
        download_file(i, size) 
        for i, size in enumerate(file_sizes, 1)
    ]
    
    # Ejecutar todas las tareas concurrentemente
    results = await asyncio.gather(*tasks)
    
    elapsed = time.perf_counter() - start
    print(f"\n⏱️  Todas las descargas completadas en {elapsed:.2f}s")
    
    return results


# =============================================================================
# EJEMPLO 3: Comparación Síncrono vs Asíncrono
# =============================================================================

def download_file_sync(file_id: int, size: int) -> dict:
    """Versión síncrona de download_file (para comparar)."""
    print(f"📥 Descargando archivo #{file_id} ({size}MB) - SYNC")
    time.sleep(size * 0.1)  # Bloquea el thread completo
    print(f"✅ Archivo #{file_id} descargado - SYNC")
    return {"file_id": file_id, "size": size, "status": "completado"}


def download_multiple_files_sync(file_sizes: List[int]) -> List[dict]:
    """Versión síncrona de download_multiple_files."""
    print("\n🐌 Iniciando descargas síncronas (secuenciales)...")
    start = time.perf_counter()
    
    results = [
        download_file_sync(i, size)
        for i, size in enumerate(file_sizes, 1)
    ]
    
    elapsed = time.perf_counter() - start
    print(f"\n⏱️  Todas las descargas completadas en {elapsed:.2f}s")
    
    return results


# =============================================================================
# EJEMPLO 4: Uso de asyncio.create_task()
# =============================================================================

async def fetch_data(source: str, delay: float) -> dict:
    """Simula fetch de datos de una fuente."""
    print(f"🔍 Consultando {source}...")
    await asyncio.sleep(delay)
    data = {"source": source, "data": f"datos_de_{source}"}
    print(f"✓ Datos obtenidos de {source}")
    return data


async def aggregate_data() -> dict:
    """
    Agrega datos de múltiples fuentes usando create_task().
    
    create_task() programa la ejecución de una coroutine y retorna
    un Task object inmediatamente, permitiendo que se ejecute en
    background mientras hacemos otras cosas.
    """
    print("\n📊 Agregando datos de múltiples fuentes...")
    
    # Crear tareas que empiezan a ejecutarse inmediatamente
    task1 = asyncio.create_task(fetch_data("API_1", 1.0))
    task2 = asyncio.create_task(fetch_data("Database", 1.5))
    task3 = asyncio.create_task(fetch_data("Cache", 0.5))
    
    # Podemos hacer otras cosas aquí mientras las tareas se ejecutan...
    print("⏳ Tareas en progreso, haciendo otros trabajos...")
    await asyncio.sleep(0.2)
    
    # Esperar a que todas terminen
    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    return {
        "sources": [result1, result2, result3],
        "count": 3
    }


# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================

async def main():
    """Función principal que demuestra todos los ejemplos."""
    
    print("="*70)
    print("ASYNCIO FUNDAMENTOS - EJEMPLOS")
    print("="*70)
    
    # Ejemplo 1: Saludos concurrentes
    print("\n📌 EJEMPLO 1: Funciones asíncronas básicas")
    print("-" * 70)
    await asyncio.gather(
        greet("Alice", 1.0),
        greet("Bob", 0.5),
        greet("Charlie", 1.5)
    )
    
    # Ejemplo 2: Comparación síncrono vs asíncrono
    print("\n" + "="*70)
    print("📌 EJEMPLO 2: Comparación Síncrono vs Asíncrono")
    print("-" * 70)
    
    file_sizes = [3, 2, 4, 1]  # MB
    
    # Versión síncrona
    sync_results = download_multiple_files_sync(file_sizes)
    
    # Versión asíncrona
    async_results = await download_multiple_files(file_sizes)
    
    print(f"\n💡 Conclusión: Asyncio es {len(file_sizes)}x más rápido para I/O-bound")
    
    # Ejemplo 3: Agregación de datos
    print("\n" + "="*70)
    print("📌 EJEMPLO 3: Uso de create_task()")
    print("-" * 70)
    
    result = await aggregate_data()
    print(f"\n✅ Datos agregados: {result['count']} fuentes consultadas")
    
    print("\n" + "="*70)
    print("🎓 CONCEPTOS CLAVE APRENDIDOS:")
    print("="*70)
    print("1. async/await permite código concurrente sin threads")
    print("2. asyncio.gather() ejecuta múltiples coroutines en paralelo")
    print("3. create_task() programa tareas para ejecutarse en background")
    print("4. Ideal para operaciones I/O-bound (red, archivos, DB)")
    print("5. Mucho más simple que threading para concurrencia I/O")
    print("="*70)


if __name__ == "__main__":
    # Ejecutar el event loop
    asyncio.run(main())
