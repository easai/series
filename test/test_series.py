""" pytest files for series
"""
from src.series.series import *
import pytest

def f(x):
    return x*x

def test_series():
    """Test Series class def.
    """
    seq=Series(1,4,f)
    assert seq.sum() == 1+4+9+16

def power(x):
    return 2**x

def test_power_series():
    """Test power series
    """
    seq=Series(0,4,power)
    assert seq.sum() == (1+2+4+8+16)

def alternate(x):
    return (-1)**x

def test_power_series():
    """Test alternate series
    """
    seq=Series(1,1001,alternate)
    print(f"sum={seq.sum()}")
    assert seq.sum() == -1
