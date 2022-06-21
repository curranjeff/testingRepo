import pytest
from src.temp_atscale import User

@pytest.fixture(scope='session')
def userFix():
    return User('Mark', 26)