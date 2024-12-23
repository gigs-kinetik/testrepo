import pytest
from pathlib import Path
import sys

# Add the parent directory to system path to import the module
sys.path.append(str(Path(__file__).parent.parent))

from main import *  # Import all functions from the module

from main import *
def test_add_normal_case():
    assert add(2, 3) == 5
def test_add_negative_numbers():
    assert add(-5, 3) == -2
def test_subtract_normal_case():
    assert subtract(5, 2) == 3
def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2
def test_multiply_normal_case():
    assert multiply(2, 3) == 6
def test_multiply_zero():
    assert multiply(5, 0) == 0
def test_add_string_input():
    with pytest.raises(TypeError):
        add("2", 3)
def test_subtract_string_input():
    with pytest.raises(TypeError):
        subtract(5, "2")
def test_multiply_string_input():
    with pytest.raises(TypeError):
        multiply("2", 3)