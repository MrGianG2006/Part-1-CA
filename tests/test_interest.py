import pytest
from part1 import calculate_interest

def test_check_string():
    with pytest.raises(ValueError):
        calculate_interest("231213")

def test_int_float():
    with pytest.raises(ValueError):
        calculate_interest(number)

def test_bool():
    with pytest.raises(ValueError):
        calculate_interest(True)

def test_value_0():
    with pytest.raises(ValueError):
        calculate_interest(-23)
    
def test_