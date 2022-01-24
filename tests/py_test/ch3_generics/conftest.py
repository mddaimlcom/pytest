import pytest
import random


@pytest.fixture(scope="module")
def get_random_num():
    rand_num = random.randint(0, 3) * 3
    return rand_num