from src.algorithms import find_closest_number, contains_duplicat
import pytest
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 1),
        ([-1, -2, -3], -1),
        ([2, 3, -1, 1, -2, -3], 1),
        ([1, 2, 3, -1, -2, -3, 0], 0),
        ([1, 2, 3, -1, -2, -3, 0, 0], 0),
        ([1, 2, 3, -1, -2, -3, 0, 0, 0], 0),
        ([1, 2, 3, -1, -2, -3, 0, 0, 0, 0], 0),
        ([1, 2, 3, -1, -2, -3, 0, 0, 0, 0, 0], 0),
        ([-1000, -1000], -1000),
        ([42], 42),
        ([-7], -7),
        ([-5, 5], 5),
        ([1000, -1000], 1000),
        ([10, -10, 5, -2, 2, 1, 0], 0),
        ([0, 0, 5, -5, 2, -2], 0),
        ([3, 3, -3, -2, -2, 2, 2, 1, 1], 1),
        ([999999999, -1000000000, 500, -500], 500),
        ([100, 50, 25, -3, 3, 10, 20], 3),
    ],
)
def test_find_numbers_closest_to_zero(numbers, expected):
    assert find_closest_number(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected, expectation",
    [
        ([1, 2, 3], False, does_not_raise()),
        ([-1, -2, -3], False, does_not_raise()),
        ([2, 3, -1, 1, -2, -3], False, does_not_raise()),
        ([1, 2, 3, -1, -2, -3, 0], False, does_not_raise()),
        ([1, 2, 3, -1, -2, -3, 0, 0], True, does_not_raise()),
        ([1, 2, 3, -1, -2, -3, 0, 0, 0], True, does_not_raise()),
        ([1, 2, 3, -1, -2, -3, 0, 0, 0, 0], True, does_not_raise()),
        ([1, 2, 3, -1, -2, -3, 0, 0, 0, 0, 0], True, does_not_raise()),
        ([-1000, -1000], True, does_not_raise()),
        ([42], False, does_not_raise()),
        ([-7], False, does_not_raise()),
        ([-5, 5], False, does_not_raise()),
        ([1000, -1000], False, does_not_raise()),
        ([10, -10, 5, -2, 2, 1, 0], False, does_not_raise()),
        ([0, 0, 5, -5, 2, -2], True, does_not_raise()),
        ([3, 3, -3, -2, -2, 2, 2, 1, 1], True, does_not_raise()),
        ([999999999, -1000000000, 500, -500], False, does_not_raise()),
        ([100, 50, 25, -3, 3, 10, 20], False, does_not_raise()),
        ("[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]", True, pytest.raises(TypeError)),
    ],
)
def test_contains_duplicate(numbers, expected, expectation):
    with expectation:
        assert contains_duplicat(numbers) == expected
