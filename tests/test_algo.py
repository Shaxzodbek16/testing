from src.fixture_pytest import even_index_chars, get_second_largest
from contextlib import nullcontext as does_not_raise
import pytest


@pytest.fixture(scope="session")
def get_data():
    print("\nSession scope fixture was opened")
    data = {
        "even_index_chars": ["Hello World", "HloWrd"],
        "get_second_largest": [[1, 2, 3, 4, 5], 4],
    }
    yield data

    print("\nSession scope fixture was closed")


def test_even_index_chars(get_data):
    data = get_data["even_index_chars"]
    assert even_index_chars(data[0]) == data[1]


def test_get_second_largest(get_data):
    data = get_data["get_second_largest"]
    assert get_second_largest(data[0]) == data[1]


@pytest.mark.parametrize(
    "text, expected, error",
    [
        ("Hello World", "HloWrd", does_not_raise()),
        (12345, None, pytest.raises(TypeError)),
        ("Hello", "Hlo", does_not_raise()),
    ],
)
def test_with_parametrize_even_index_chars(text, expected, error):
    with error:
        assert even_index_chars(text) == expected


@pytest.mark.parametrize(
    "numbers, expected, error",
    [
        ([1, 2, 3, 4, 5], 4, does_not_raise()),
        ([1, 2], 1, does_not_raise()),
        (12345, None, pytest.raises(TypeError)),
        ([1], None, pytest.raises(ValueError)),
    ]
)
def test_with_parametrize_get_second_largest(numbers, expected, error):
    with error:
        assert get_second_largest(numbers) == expected
