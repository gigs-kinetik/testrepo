import pytest
from src.test2 import sub
def test_sub_normal_case():
    assert sub(5, 2) == 3
def test_sub_negative_numbers():
    assert sub(-5, -2) == -3
def test_sub_zero():
    assert sub(0, 0) == 0
def test_sub_large_numbers():
    assert sub(1000000, 999999) == 1
def test_sub_float_numbers():
    assert sub(3.5, 1.5) == 2.0
def test_sub_error_handling():
    with pytest.raises(TypeError):
        sub('a', 2)