from src.main import Logic

from src.main import func

def test_main():
    assert 1 == 1

def test_logic():
    logic = Logic()
    assert logic.logic_param == 10


def test_func():
    assert func(1) == 2

