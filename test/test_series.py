""" pytest files for series
"""
from src.series.series import *
import pytest


def test_series():
    """Test Series class def.
    """
    seq=Series(1,4,lambda x:x*x)
    assert seq.sum() == 1+4+9+16

def test_power_series():
    """Test power series
    """
    seq=Series(0,4,lambda x:2**x)
    assert seq.sum() == (1+2+4+8+16)

def test_power_series():
    """Test alternate series
    """
    seq=Series(1,1001,lambda x:(-1)**x)
    print(f"sum={seq.sum()}")
    assert seq.sum() == -1
