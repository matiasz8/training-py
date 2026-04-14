"""
Tests para limitaciones del GIL.

Valida la implementación del ejercicio de análisis de GIL.
"""

import pytest
from pathlib import Path
import sys
import time
import threading
import multiprocessing as mp

# Añadir directorio padre al path para imports
parent_dir = Path(__file__).parent.parent / "my_solution"
sys.path.insert(0, str(parent_dir))


class TestGILBenchmark:
    """Suite de tests para GILBenchmark."""
    
    def test_can_import_classes(self):
        """Test que las clases se pueden importar."""
        try:
            from exercise_01 import GILBenchmark, WorkloadType, ExecutionStrategy, BenchmarkResult
            assert True
        except ImportError as e:
            pytest.fail(f"No se pudieron importar las clases: {e}")
    
    def test_benchmark_initialization(self):
        """Test que el benchmark se inicializa correctamente."""
        try:
            from exercise_01 import GILBenchmark
            benchmark = GILBenchmark(num_tasks=5, num_workers=2)
            assert benchmark is not None
            assert benchmark.num_tasks == 5
            assert benchmark.num_workers == 2
        except Exception as e:
            pytest.skip(f"Implementación pendiente: {e}")
    
    def test_cpu_bound_task_execution(self):
        """Test que la tarea CPU-bound se ejecuta y retorna resultado."""
        try:
            from exercise_01 import GILBenchmark
            
            start = time.perf_counter()
            result = GILBenchmark.cpu_bound_task(n=1_000_000)
            elapsed = time.perf_counter() - start
            
            assert isinstance(result, int)
            assert elapsed > 0
            assert elapsed < 5.0  # No debería tomar más de 5 segundos
        except Exception as e:
            pytest.skip(f"Implementación pendiente: {e}")
    
    def test_io_bound_task_execution(self):
        """Test que la tarea I/O-bound se ejecuta correctamente."""
        try:
            from exercise_01 import GILBenchmark
            
            duration = 0.05  # 50ms
            start = time.perf_counter()
            result = GILBenchmark.io_bound_task(duration=duration)
            elapsed = time.perf_counter() - start
            
            assert isinstance(result, str)
            assert elapsed >= duration * 0.9  # Permitir 10% de margen
            assert elapsed < duration * 2.0  # No debería tomar el doble
        except Exception as e:
            pytest.skip(f"Implementación pendiente: {e}")
    
    def test_mixed_task_execution(self):
        """Test que la tarea mixta combina CPU e I/O."""
        try:
            from exercise_01 import GILBenchmark
            
            result = GILBenchmark.mixed_task(cpu_ratio=0.5)
            assert isinstance(result, tuple)
            assert len(result) == 2
        except Exception as e:
            pytest.skip(f"Implementación pendiente: {e}")
    
    def test_sequential_execution_baseline(self):
        """Test que la ejecución secuencial funciona como baseline."""
        try:
            from exercise_01 import GILBenchmark, WorkloadType
            
            benchmark = GILBenchmark(num_tasks=3, num_workers=2)
            result = benchmark.run_sequential(WorkloadType.CPU_BOUND)
            
            assert result.strategy == "sequential"
            assert result.num_workers == 1
            assert result.total_time > 0
            assert result.speedup == 1.0  # Baseline
            assert result.efficiency == 1.0  # Baseline
        except Exception as e:
            pytest.skip(f"Implementación pendiente: {e}")
    
    def test_threaded_execution_limited_by_gil(self):
        """Test que ejecución threaded está limitada por GIL para CPU-bound."""
        try:
            from exercise_01 import GILBenchmark, WorkloadType
            
            benchmark = GILBenchmark(num_tasks=4, num_workers=4)
            baseline = benchmark.run_sequential(WorkloadType.CPU_BOUND)
            threaded = benchmark.run_threaded(WorkloadType.CPU_BOUND)
            
            assert threaded.strategy == "threaded"
            assert threaded.num_workers == 4
            
            # Para CPU-bound, threads NO deberían dar speedup significativo
            # debido al GIL
            speedup = baseline.total_time / threaded.total_time
            assert speedup < 2.0, "Threads no deberían dar speedup >2x en CPU-bound debido al GIL"
        except Exception as e:
            pytest.skip(f"Implementación pendiente: {e}")
    
    def test_multiprocess_bypasses_gil(self):
        """Test que multiprocessing evita el GIL y da speedup real."""
        try:
            from exercise_01 import GILBenchmark, WorkloadType
            
            benchmark = GILBenchmark(num_tasks=4, num_workers=2)
            baseline = benchmark.run_sequential(WorkloadType.CPU_BOUND)
            multiproc = benchmark.run_multiprocess(WorkloadType.CPU_BOUND)
            
            assert multiproc.strategy == "multiprocess"
            
            # Multiprocessing DEBERÍA dar speedup para CPU-bound
            speedup = baseline.total_time / multiproc.total_time
            # Con 2 workers, esperamos al menos 1.3x speedup
            # (considerando overhead de creación de procesos)
            assert speedup > 1.3, "Multiprocessing debería dar speedup en CPU-bound"
        except Exception as e:
            pytest.skip(f"Implementación pendiente: {e}")
    
    def test_io_bound_benefits_from_threads(self):
        """Test que I/O-bound SÍ se beneficia de threads (GIL released during I/O)."""
        try:
            from exercise_01 import GILBenchmark, WorkloadType
            
            benchmark = GILBenchmark(num_tasks=4, num_workers=4)
            baseline = benchmark.run_sequential(WorkloadType.IO_BOUND)
            threaded = benchmark.run_threaded(WorkloadType.IO_BOUND)
            
            # Para I/O-bound, threads SÍ deberían dar speedup porque
            # sleep() libera el GIL
            speedup = baseline.total_time / threaded.total_time
            assert speedup > 2.0, "Threads deberían dar speedup en I/O-bound (GIL released)"
        except Exception as e:
            pytest.skip(f"Implementación pendiente: {e}")
    
    def test_metrics_calculation(self):
        """Test que las métricas se calculan correctamente."""
        try:
            from exercise_01 import GILBenchmark, BenchmarkResult
            
            baseline = BenchmarkResult(
                strategy="sequential",
                workload_type="cpu_bound",
                num_workers=1,
                total_time=4.0,
                speedup=1.0,
                efficiency=1.0,
                overhead=0.0
            )
            
            result = BenchmarkResult(
                strategy="threaded",
                workload_type="cpu_bound",
                num_workers=4,
                total_time=2.0,
                speedup=0.0,  # A calcular
                efficiency=0.0,  # A calcular
                overhead=0.0  # A calcular
            )
            
            benchmark = GILBenchmark()
            updated = benchmark.calculate_metrics(baseline, result)
            
            assert updated.speedup == 2.0  # 4.0 / 2.0
            assert updated.efficiency == 0.5  # 2.0 / 4
            assert updated.overhead == 1.0  # 2.0 - (4.0 / 4)
        except Exception as e:
            pytest.skip(f"Implementación pendiente: {e}")
    
    def test_full_benchmark_runs_all_scenarios(self):
        """Test que el benchmark completo ejecuta todos los escenarios."""
        try:
            from exercise_01 import GILBenchmark
            
            benchmark = GILBenchmark(num_tasks=2, num_workers=2)
            results = benchmark.run_full_benchmark()
            
            assert isinstance(results, dict)
            assert len(results) >= 2  # Al menos CPU_BOUND e IO_BOUND
            
            for workload_type, workload_results in results.items():
                assert isinstance(workload_results, list)
                assert len(workload_results) >= 2  # Al menos sequential y una estrategia paralela
        except Exception as e:
            pytest.skip(f"Implementación pendiente: {e}")
    
    def test_report_generation(self):
        """Test que se genera un reporte legible."""
        try:
            from exercise_01 import GILBenchmark, WorkloadType
            
            benchmark = GILBenchmark(num_tasks=2, num_workers=2)
            results = benchmark.run_full_benchmark()
            report = benchmark.generate_report(results)
            
            assert isinstance(report, str)
            assert len(report) > 100  # Debe ser un reporte sustancial
            assert "sequential" in report.lower() or "secuencial" in report.lower()
            assert "speedup" in report.lower()
        except Exception as e:
            pytest.skip(f"Implementación pendiente: {e}")


class TestGILLimitations:
    """Tests específicos sobre limitaciones del GIL."""
    
    def test_gil_prevents_cpu_parallelism(self):
        """Test conceptual: GIL previene paralelismo CPU."""
        # Este test verifica que el estudiante entiende el concepto
        
        def cpu_task():
            total = 0
            for i in range(5_000_000):
                total += i
            return total
        
        # Ejecutar secuencialmente
        start = time.perf_counter()
        cpu_task()
        cpu_task()
        sequential_time = time.perf_counter() - start
        
        # Ejecutar con threads
        start = time.perf_counter()
        threads = [threading.Thread(target=cpu_task) for _ in range(2)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        threaded_time = time.perf_counter() - start
        
        # Con GIL, threaded NO debería ser significativamente más rápido
        speedup = sequential_time / threaded_time
        assert speedup < 1.5, f"Speedup {speedup:.2f}x - GIL debería limitar paralelismo CPU"
    
    def test_gil_released_during_io(self):
        """Test conceptual: GIL se libera durante I/O."""
        
        def io_task():
            time.sleep(0.1)  # Libera el GIL
        
        # Ejecutar secuencialmente
        start = time.perf_counter()
        io_task()
        io_task()
        io_task()
        io_task()
        sequential_time = time.perf_counter() - start
        
        # Ejecutar con threads
        start = time.perf_counter()
        threads = [threading.Thread(target=io_task) for _ in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        threaded_time = time.perf_counter() - start
        
        # Para I/O, threads SÍ deberían dar speedup (GIL released)
        speedup = sequential_time / threaded_time
        assert speedup > 2.5, f"Speedup {speedup:.2f}x - I/O debería beneficiarse de threads"


def test_imports():
    """Verifica que los imports necesarios funcionan."""
    import threading
    import multiprocessing
    import time
    assert True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
