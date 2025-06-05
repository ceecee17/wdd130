import pytest
def func(x):
    return x + 2


def test_answer():
    assert func(3) == 5

    pytest.main(["-v", "-s", __file__])


