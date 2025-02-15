class Logic:
    logic_param = 10


def func(x):
    return x + 1


def sum_(x: int, y: int):
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Arguments must be integers")
    return x + y
