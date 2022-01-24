import pytest
import random

@pytest.fixture(scope="function")
def get_random_num():
    rand_num = random.randint(0, 3) * 3
    return rand_num

def test_1(get_random_num):
    assert get_random_num > 9

def test_2(get_random_num):
    assert get_random_num > 9

def test_3(get_random_num):
    assert get_random_num > 9

def test_4(get_random_num):
    assert get_random_num > 9

def test_5(get_random_num):
    assert get_random_num > 9

def test_6(get_random_num):
    assert get_random_num > 9

def test_7(get_random_num):
    assert get_random_num > 9

def test_8(get_random_num):
    assert get_random_num > 9

def test_9(get_random_num):
    assert get_random_num > 9