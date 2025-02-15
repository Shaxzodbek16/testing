from src.main import Logic, sum_
import pytest

from src.main import func


def test_main():
    assert 1 == 1


def test_logic():
    logic = Logic()

    assert logic.logic_param == 10


def test_func():
    assert func(1) == 2


@pytest.mark.parametrize(
    "x, y, result",
    [
        (1, 1, 2),
        (1, "1", TypeError),
        (-1, -1, -2),
        (2**65, 2**65, 2**66),
        (1.1, 1.1, TypeError),
        ([1], [1], TypeError),
        (1 + 3j, 1 + 5j, TypeError),
    ],
)
def test__sum(x, y, result):
    if result == TypeError:
        with pytest.raises(TypeError):
            sum_(x, y)
    else:
        assert sum_(x, y) == result
