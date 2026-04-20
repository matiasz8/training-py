"""
Tests for el ejercicio básico: Comparación Threading vs Multiprocessing

Ejecutar con: pytest test_basic.py -v
"""

import os
import sys

import pytest

# Agregar directorio padre al path para importar el ejercicio
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from exercises.basic_exercise import (
    find_primes_in_range,
    is_prime,
    multiprocessing_execution,
    sequential_execution,
    threading_execution,
)


class TestIsPrime:
    """Tests for la función is_prime."""

    def test_small_primes(self):
        """Verificar primos pequeños."""
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(5) == True
        assert is_prime(7) == True
        assert is_prime(11) == True

    def test_small_composites(self):
        """Verificar compuestos pequeños."""
        assert is_prime(4) == False
        assert is_prime(6) == False
        assert is_prime(8) == False
        assert is_prime(9) == False
        assert is_prime(10) == False

    def test_edge_cases(self):
        """Verificar casos borde."""
        assert is_prime(0) == False
        assert is_prime(1) == False
        assert is_prime(-5) == False

    def test_large_primes(self):
        """Verificar primos grandes."""
        assert is_prime(1009) == True
        assert is_prime(10007) == True
        assert is_prime(100003) == True

    def test_large_composites(self):
        """Verificar compuestos grandes."""
        assert is_prime(1000) == False
        assert is_prime(10000) == False
        assert is_prime(100000) == False


class TestFindPrimesInRange:
    """Tests for find_primes_in_range."""

    def test_small_range(self):
        """Verificar rango pequeño."""
        primes = find_primes_in_range(10, 20)
        expected = [11, 13, 17, 19]
        assert primes == expected

    def test_includes_two(self):
        """Verificar que incluye el 2."""
        primes = find_primes_in_range(1, 10)
        assert 2 in primes
        assert primes == [2, 3, 5, 7]

    def test_empty_range(self):
        """Verificar rango sin primos."""
        primes = find_primes_in_range(24, 28)
        assert primes == []

    def test_large_range(self):
        """Verificar rango grande."""
        primes = find_primes_in_range(1000, 1100)
        # Debe encontrar exactamente 16 primos en este rango
        assert len(primes) == 16
        # Verificar algunos
        assert 1009 in primes
        assert 1013 in primes
        assert 1019 in primes


class TestSequentialExecution:
    """Tests for ejecución secuencial."""

    def test_single_range(self):
        """Test con un solo rango."""
        ranges = [(100, 200)]
        primes, elapsed = sequential_execution(ranges)

        # Verificar que retorna una lista de primos
        assert isinstance(primes, list)
        assert all(is_prime(p) for p in primes)

        # Verificar que midió el tiempo
        assert isinstance(elapsed, float)
        assert elapsed > 0

    def test_multiple_ranges(self):
        """Test con múltiples rangos."""
        ranges = [(100, 200), (200, 300), (300, 400)]
        primes, elapsed = sequential_execution(ranges)

        # Todos los primos deben estar en [100, 400)
        assert all(100 <= p < 400 for p in primes)

        # Verificar que encontró los primos esperados
        expected_count = len(find_primes_in_range(100, 400))
        assert len(primes) == expected_count


class TestThreadingExecution:
    """Tests for ejecución con threading."""

    def test_correctness(self):
        """Verificar que encuentra los mismos primos que secuencial."""
        ranges = [(1000, 1100), (1100, 1200), (1200, 1300), (1300, 1400)]

        primes_seq, _ = sequential_execution(ranges)
        primes_thread, _ = threading_execution(ranges, 4)

        # Ordenar porque threading puede retornar en diferente orden
        assert sorted(primes_seq) == sorted(primes_thread)

    def test_different_thread_counts(self):
        """Verificar con diferentes números de threads."""
        ranges = [(5000, 5100), (5100, 5200)]

        for num_threads in [1, 2, 4]:
            primes, elapsed = threading_execution(ranges, num_threads)
            assert isinstance(primes, list)
            assert elapsed > 0


class TestMultiprocessingExecution:
    """Tests for ejecución con multiprocessing."""

    def test_correctness(self):
        """Verificar que encuentra los mismos primos que secuencial."""
        ranges = [(1000, 1100), (1100, 1200), (1200, 1300), (1300, 1400)]

        primes_seq, _ = sequential_execution(ranges)
        primes_mp, _ = multiprocessing_execution(ranges, 4)

        # Ordenar porque multiprocessing puede retornar en diferente orden
        assert sorted(primes_seq) == sorted(primes_mp)

    def test_different_process_counts(self):
        """Verificar con diferentes números de procesos."""
        ranges = [(5000, 5100), (5100, 5200)]

        for num_processes in [1, 2, 4]:
            primes, elapsed = multiprocessing_execution(ranges, num_processes)
            assert isinstance(primes, list)
            assert elapsed > 0

    def test_speedup(self):
        """
        Verificar que multiprocessing muestra speedup en CPU-bound.

        Nota: Este test puede ser flaky dependiendo del sistema,
        pero en general debería pasar en máquinas con 4+ cores.
        """
        ranges = [(100000, 110000), (110000, 120000), (120000, 130000), (130000, 140000)]

        _, time_seq = sequential_execution(ranges)
        _, time_mp = multiprocessing_execution(ranges, 4)

        speedup = time_seq / time_mp

        # Esperamos al menos 1.5x speedup con 4 procesos
        # (no 4x debido a overhead)
        assert speedup > 1.5, f"Speedup too low: {speedup:.2f}x"


class TestPerformanceComparison:
    """Tests comparativos de rendimiento."""

    @pytest.mark.slow
    def test_gil_limitation_on_cpu_bound(self):
        """
        Verificar que threading NO mejora rendimiento en CPU-bound
        debido al GIL, pero multiprocessing SÍ mejora.
        """
        ranges = [(100000, 125000), (125000, 150000), (150000, 175000), (175000, 200000)]

        _, time_seq = sequential_execution(ranges)
        _, time_thread = threading_execution(ranges, 4)
        _, time_mp = multiprocessing_execution(ranges, 4)

        speedup_thread = time_seq / time_thread
        speedup_mp = time_seq / time_mp

        # Threading debe tener speedup < 1.5x debido al GIL
        assert (
            speedup_thread < 1.5
        ), f"Threading speedup too high: {speedup_thread:.2f}x (GIL not limiting?)"

        # Multiprocessing debe tener speedup > 2.0x
        assert speedup_mp > 2.0, f"Multiprocessing speedup too low: {speedup_mp:.2f}x"

        # Multiprocessing debe ser significativamente mejor que threading
        assert (
            speedup_mp > speedup_thread * 1.3
        ), "Multiprocessing should be significantly better than threading"


# Fixtures


@pytest.fixture
def known_primes_100_200():
    """Primos conocidos en el rango [100, 200)."""
    return [
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        137,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
        193,
        197,
        199,
    ]


def test_known_primes(known_primes_100_200):
    """Verificar contra lista conocida de primos."""
    primes = find_primes_in_range(100, 200)
    assert primes == known_primes_100_200


# Markers para tests lentos


def pytest_configure(config):
    """Configurar markers personalizados."""
    config.addinivalue_line(
        "markers", "slow: marca tests que son lentos (deseleccionar con '-m \"not slow\"')"
    )


if __name__ == "__main__":
    # Ejecutar tests
    pytest.main([__file__, "-v"])
