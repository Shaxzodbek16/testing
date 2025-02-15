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


def test_sum():

    assert sum_(1, 1) == 2


def test__sum_error():
    pytest.raises(TypeError, sum_, 1, "1")
