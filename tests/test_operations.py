import pytest
from mymath import operations

def test_add():
    assert operations.add(2, 3) == 5

def test_subtract():
    assert operations.subtract(5, 3) == 2

def test_multiply():
    assert operations.multiply(2, 3) == 6

def test_divide():
    assert operations.divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        operations.divide(1, 0)
