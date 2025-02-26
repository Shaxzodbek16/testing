def even_index_chars(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return "".join(text[i] for i in range(0, len(text), 2))


def get_second_largest(numbers: list[int]) -> int:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) < 2:
        raise ValueError("List must contain at least 2 elements")
    numbers.sort()
    return numbers[-2]
