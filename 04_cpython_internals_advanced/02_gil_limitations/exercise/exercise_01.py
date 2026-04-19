"""
Exercise: Análisis de Limitaciones del GIL

OBJETIVO:
---------
Implementar un benchmarking framework que demuestre y mida las limitaciones
del GIL en diferentes escenarios de concurrencia.

CONTEXTO:
---------
El GIL (Global Interpreter Lock) es una limitación fundamental de CPython
que previene la ejecución paralela de bytecode Python. Tu tarea es crear
herramientas para medir su impacto en diferentes tipos de workloads.

REQUISITOS:
-----------
1. Implementar una clase GILBenchmark que mida rendimiento de:
   - Operaciones CPU-bound (cálculos matemáticos)
   - Operaciones I/O-bound (simuladas con sleep)
   - Operaciones mixtas

2. Comparar tres estrategias de ejecución:
   - Single-threaded (sequential)
   - Multi-threaded (limitado por GIL)
   - Multi-process (sin GIL)

3. Calcular métricas:
   - Tiempo total de ejecución
   - Speedup (comparado con baseline)
   - Efficiency (speedup / num_workers)
   - Overhead del GIL

4. Generar un reporte comparativo con recomendaciones

ESPECIFICACIONES:
-----------------
- Usa threading.Thread para multi-threading
- Usa multiprocessing.Process para multi-processing
- Usa time.perf_counter() para mediciones precisas
- Implementa type hints completos
- Maneja excepciones apropiadamente

DO NOT MODIFY THIS FILE DIRECTLY. Copy it into my_solution/ and work there.
"""

import threading
import multiprocessing as mp
import time
from typing import List, Callable, Dict, Any
from dataclasses import dataclass
from enum import Enum


class WorkloadType(Enum):
    """Tipos de workload para benchmarking."""
    CPU_BOUND = "cpu_bound"
    IO_BOUND = "io_bound"
    MIXED = "mixed"


class ExecutionStrategy(Enum):
    """Estrategias de ejecución."""
    SEQUENTIAL = "sequential"
    THREADED = "threaded"
    MULTIPROCESS = "multiprocess"


@dataclass
class BenchmarkResult:
    """
    Resultado de un benchmark.
    
    Attributes:
        strategy: Estrategia usada (sequential/threaded/multiprocess)
        workload_type: Tipo de carga de trabajo
        num_workers: Número de workers usados
        total_time: Tiempo total en segundos
        speedup: Factor de aceleración vs baseline
        efficiency: speedup / num_workers (0.0 - 1.0)
        overhead: Tiempo extra debido al GIL/coordinación (segundos)
    """
    strategy: str
    workload_type: str
    num_workers: int
    total_time: float
    speedup: float
    efficiency: float
    overhead: float


class GILBenchmark:
    """
    Framework para benchmarking de limitaciones del GIL.
    
    Permite medir el impacto del GIL en diferentes escenarios
    y comparar estrategias de ejecución.
    """
    
    def __init__(self, num_tasks: int = 10, num_workers: int = 4):
        """
        Inicializa el benchmark.
        
        Args:
            num_tasks: Número de tareas a ejecutar
            num_workers: Número de workers para estrategias paralelas
        """
        # TASK: Implementar inicialización
        pass
    
    @staticmethod
    def cpu_bound_task(n: int = 5_000_000) -> int:
        """
        Tarea CPU-intensiva: cálculo matemático.
        
        Args:
            n: Número de iteraciones
            
        Returns:
            Resultado del cálculo
            
        TASK: Implementar una operación CPU-intensiva
        Ejemplo: suma de números, cálculo de fibonacci, etc.
        """
        pass
    
    @staticmethod
    def io_bound_task(duration: float = 0.1) -> str:
        """
        Tarea I/O-bound: operación de entrada/salida simulada.
        
        Args:
            duration: Duración de la operación en segundos
            
        Returns:
            Mensaje de confirmación
            
        TASK: Simular operación I/O con time.sleep()
        Esto libera el GIL, permitiendo que otros threads ejecuten.
        """
        pass
    
    @staticmethod
    def mixed_task(cpu_ratio: float = 0.5) -> tuple[int, str]:
        """
        Tarea mixta: combina CPU y I/O.
        
        Args:
            cpu_ratio: Ratio de tiempo CPU vs I/O (0.0 - 1.0)
            
        Returns:
            Tupla (resultado_cpu, resultado_io)
            
        TASK: Implementar tarea que combine operaciones CPU e I/O
        """
        pass
    
    def run_sequential(self, workload: WorkloadType) -> BenchmarkResult:
        """
        Ejecuta tareas secuencialmente (baseline).
        
        Args:
            workload: Tipo de carga de trabajo
            
        Returns:
            Resultado del benchmark
            
        TASK: Implementar ejecución secuencial
        - Ejecutar self.num_tasks tareas una tras otra
        - Medir tiempo total
        - Retornar resultado con speedup=1.0, efficiency=1.0
        """
        pass
    
    def run_threaded(self, workload: WorkloadType) -> BenchmarkResult:
        """
        Ejecuta tareas usando threads (limitado por GIL).
        
        Args:
            workload: Tipo de carga de trabajo
            
        Returns:
            Resultado del benchmark
            
        TASK: Implementar ejecución multi-threaded
        - Crear self.num_workers threads
        - Distribuir self.num_tasks entre los threads
        - Medir tiempo total incluyendo join()
        - El speedup será bajo para CPU-bound debido al GIL
        """
        pass
    
    def run_multiprocess(self, workload: WorkloadType) -> BenchmarkResult:
        """
        Ejecuta tareas usando procesos (sin GIL).
        
        Args:
            workload: Tipo de carga de trabajo
            
        Returns:
            Resultado del benchmark
            
        TASK: Implementar ejecución multi-process
        - Crear self.num_workers procesos
        - Distribuir tareas entre procesos
        - Medir tiempo total
        - Esta estrategia NO sufre del GIL
        - Considera el overhead de creación de procesos
        """
        pass
    
    def calculate_metrics(
        self,
        baseline: BenchmarkResult,
        result: BenchmarkResult
    ) -> BenchmarkResult:
        """
        Calcula métricas comparativas.
        
        Args:
            baseline: Resultado de ejecución secuencial
            result: Resultado a evaluar
            
        Returns:
            Resultado con métricas actualizadas
            
        TASK: Implementar cálculo de métricas
        - speedup = baseline.total_time / result.total_time
        - efficiency = speedup / result.num_workers
        - overhead = result.total_time - (baseline.total_time / result.num_workers)
        """
        pass
    
    def run_full_benchmark(self) -> Dict[str, List[BenchmarkResult]]:
        """
        Ejecuta benchmark completo para todos los escenarios.
        
        Returns:
            Diccionario con resultados por tipo de workload
            
        TASK: Implementar benchmark completo
        - Para cada WorkloadType:
          - Ejecutar sequential (baseline)
          - Ejecutar threaded
          - Ejecutar multiprocess
          - Calcular métricas
        - Retornar resultados organizados por workload
        """
        pass
    
    def generate_report(self, results: Dict[str, List[BenchmarkResult]]) -> str:
        """
        Genera reporte legible de resultados.
        
        Args:
            results: Resultados del benchmark
            
        Returns:
            Reporte formateado como string
            
        TASK: Implementar generación de reporte
        - Formatear resultados en tabla
        - Incluir observaciones sobre el GIL
        - Dar recomendaciones según workload type
        
        Ejemplo de formato:
        
        WORKLOAD: CPU_BOUND
        -------------------
        Sequential:   5.234s  (speedup: 1.00x, efficiency: 100%)
        Threaded:     5.128s  (speedup: 1.02x, efficiency: 26%)  ⚠️ GIL
        Multiprocess: 1.456s  (speedup: 3.59x, efficiency: 90%)  ✓
        
        RECOMENDACIÓN: Usa multiprocessing para CPU-bound
        """
        pass


def demonstrate_gil_limitation():
    """
    Función helper para demostrar claramente la limitación del GIL.
    
    TASK: Implementar demostración clara
    - Crear dos tareas CPU-intensivas
    - Ejecutar con threads → tiempo ~2x (no hay paralelismo)
    - Ejecutar con processes → tiempo ~1x (paralelismo real)
    - Imprimir comparación clara
    """
    pass


def main():
    """
    Entry point to try your implementation.
    
    TASK: Implementar casos de prueba
    - Crear instancia de GILBenchmark
    - Ejecutar benchmark completo
    - Imprimir reporte
    - Demostrar limitaciones del GIL
    """
    print("="*60)
    print("EJERCICIO: Análisis de Limitaciones del GIL")
    print("="*60)
    
    # TASK: Tu código aquí
    
    print("\n" + "="*60)
    print("Completa la implementación en my_solution/")
    print("Ejecuta: pytest tests/test_basic.py")
    print("="*60)


if __name__ == "__main__":
    main()
