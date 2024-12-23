import pytest
from pathlib import Path
import sys

# Add the parent directory to system path to import the module
sys.path.append(str(Path(__file__).parent.parent))

from test2 import *  # Import all functions from the module

from test2 import *
def test_sub_normal_case():
    assert sub(5, 2) == 3
def test_sub_negative_result():
    assert sub(2, 5) == -3
def test_sub_zero_result():
    assert sub(0, 0) == 0
def test_sub_large_numbers():
    assert sub(1000000, 999999) == 1
def test_sub_float_numbers():
    assert sub(3.5, 1.5) == 2.0
def test_sub_error_handling():
    try:
        sub('a', 2)
    except TypeError:
        assert True
    else:
        assert False