"""
Tests for el ejercicio básico de type hints.
"""

import pytest
import sys
from pathlib import Path

# Añadir el directorio de ejercicios al path
exercises_dir = Path(__file__).parent.parent / "exercises"
sys.path.insert(0, str(exercises_dir))

try:
    from basic_exercise import calculate_discount
    SOLUTION_EXISTS = True
except (ImportError, AttributeError):
    SOLUTION_EXISTS = False


@pytest.mark.skipif(not SOLUTION_EXISTS, reason="Solución no implementada aún")
class TestCalculateDiscount:
    """Tests for la función calculate_discount."""
    
    def test_valid_discount_20_percent(self):
        """Test con descuento válido del 20%."""
        result = calculate_discount(100.0, 20.0)
        assert result == 80.0, "100.0 con 20% de descuento debe ser 80.0"
    
    def test_valid_discount_50_percent(self):
        """Test con descuento del 50%."""
        result = calculate_discount(50.0, 50.0)
        assert result == 25.0, "50.0 con 50% de descuento debe ser 25.0"
    
    def test_valid_discount_10_percent(self):
        """Test con descuento del 10%."""
        result = calculate_discount(200.0, 10.0)
        assert result == 180.0, "200.0 con 10% de descuento debe ser 180.0"
    
    def test_valid_discount_0_percent(self):
        """Test con descuento del 0% (sin descuento)."""
        result = calculate_discount(100.0, 0.0)
        assert result == 100.0, "100.0 con 0% de descuento debe ser 100.0"
    
    def test_valid_discount_100_percent(self):
        """Test con descuento del 100% (gratis)."""
        result = calculate_discount(100.0, 100.0)
        assert result == 0.0, "100.0 con 100% de descuento debe ser 0.0"
    
    def test_invalid_discount_negative(self):
        """Test con descuento negativo (inválido)."""
        result = calculate_discount(100.0, -10.0)
        assert result == 100.0, "Descuento negativo debe retornar precio original"
    
    def test_invalid_discount_over_100(self):
        """Test con descuento mayor a 100 (inválido)."""
        result = calculate_discount(100.0, 150.0)
        assert result == 100.0, "Descuento >100% debe retornar precio original"
    
    def test_invalid_discount_101(self):
        """Test con descuento de 101%."""
        result = calculate_discount(50.0, 101.0)
        assert result == 50.0, "Descuento de 101% debe retornar precio original"
    
    def test_decimal_discount(self):
        """Test con descuento decimal."""
        result = calculate_discount(100.0, 15.5)
        expected = 100.0 - (100.0 * 15.5 / 100)
        assert abs(result - expected) < 0.01, f"100.0 con 15.5% debe ser {expected}"
    
    def test_small_price(self):
        """Test con precio pequeño."""
        result = calculate_discount(1.0, 50.0)
        assert result == 0.5, "1.0 con 50% de descuento debe ser 0.5"
    
    def test_large_price(self):
        """Test con precio grande."""
        result = calculate_discount(999999.0, 25.0)
        expected = 999999.0 * 0.75
        assert abs(result - expected) < 0.01, "Descuento debe funcionar con precios grandes"


@pytest.mark.skipif(SOLUTION_EXISTS, reason="Solo mostrar cuando no hay solución")
def test_solution_not_implemented():
    """Mensaje informativo cuando no hay solución."""
    pytest.skip(
        "La solución aún no está implementada. "
        "Completa basic_exercise.py en el directorio exercises/"
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
