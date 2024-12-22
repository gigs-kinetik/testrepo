import pytest
from pathlib import Path
import sys

# Add the parent directory to system path to import the module
sys.path.append(str(Path(__file__).parent.parent))

from test1 import *  # Import all functions from the module

from test1 import *
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
def test_add_string_inputs():
    assert add('hello', 'world') == 'helloworld'