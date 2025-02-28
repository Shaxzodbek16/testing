from typing import Annotated, Sequence


def yosh_kirit(yosh: Annotated[int, "yosh 18 dan katta bo‘lishi kerak"]) -> None:
    print(f"Siz {yosh} yoshdasiz")

def elementlarni_chiqar(data: Sequence[int | str]) -> None:
    for element in data:
        print(element, end=" ")
    print()


elementlarni_chiqar([1, 2, 3])
elementlarni_chiqar((4, 5, 6))
elementlarni_chiqar("123")

yosh_kirit(20)
