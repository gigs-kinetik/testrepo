import pytest
from src.test1 import add
def test_add_normal_case():
    assert add(2, 3) == 5
def test_add_negative_numbers():
    assert add(-2, -3) == -5
def test_add_zero():
    assert add(0, 0) == 0
def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
def test_add_float_numbers():
    assert add(2.5, 3.5) == 6.0
def test_add_string_input():
    with pytest.raises(TypeError):
        add("2", "3")
def test_add_mixed_input():
    with pytest.raises(TypeError):
        add(2, "3")