import pytest
from pathlib import Path
import sys

# Add the parent directory to system path to import the module
sys.path.append(str(Path(__file__).parent.parent))

from methods import *  # Import all functions from the module

from methods import *
import pytest
@pytest.fixture
def calculator():
    return Calculator()
def test_add_normal_case(calculator):
    assert calculator.add(5) == 5
def test_add_negative_value(calculator):
    assert calculator.add(-3) == -3
def test_subtract_normal_case(calculator):
    assert calculator.subtract(2) == -2
def test_subtract_negative_value(calculator):
    assert calculator.subtract(-4) == 2
def test_multiply_normal_case(calculator):
    assert calculator.multiply(3) == 6
def test_multiply_by_zero(calculator):
    assert calculator.multiply(0) == 0
def test_divide_normal_case(calculator):
    assert calculator.divide(2) == 3
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(0)
def test_clear(calculator):
    calculator.add(5)
    calculator.clear()
    assert calculator.result == 0
def test_calculate_valid_expression(calculator):
    assert calculator.calculate("2 + 3 * 4") == 14
def test_calculate_invalid_expression(calculator):
    with pytest.raises(ValueError):
        calculator.calculate("2 + * 3")