import pytest

from src.utils.age_utils import *

def test_verify_Time_valid():
    assert verify_Time(5)

def test_verify_Time_invalid():
    assert verify_Time(-5) == False