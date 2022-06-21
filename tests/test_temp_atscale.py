import pytest


def test_add_Age(userFix):
    assert userFix.add_Age(5) == 31

def test_introduce_Self(userFix):
    assert userFix.introduce_Self() == 'My name is Mark'
