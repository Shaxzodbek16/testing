from typing import List
from collections import Counter


def find_closest_number(nums):
    closest = nums[0]
    for el in nums:
        if abs(el) < abs(closest):
            closest = el

    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest


def contains_duplicat(nums: List[int]) -> bool:
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False


def is_anagram(s: str, t: str) -> bool:
    if not isinstance(s, str) or not isinstance(t, str):
        raise TypeError("Input must be a string")
    if set(s) != set(t):
        return False
    for char in set(s):
        if s.count(char) != t.count(char):
            return False
    return True


def max_number_of_balloons(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    counter = Counter(text)
    counter["l"] = counter.get("l") // 2
    counter["o"] = counter.get("o") // 2
    return min(
        counter.get("b", 0),
        counter.get("a", 0),
        counter.get("l", 0),
        counter.get("o", 0),
        counter.get("n", 0),
    )


def merge_alternately(word1: str, word2: str) -> str:
    if not isinstance(word1, str) or not isinstance(word2, str):
        raise TypeError("Input must be a string")
    res = ""
    len1 = len(word1)
    len2 = len(word2)
    for i in range(max(len1, len2)):
        if i < len1:
            res += word1[i]
        if i < len2:
            res += word2[i]

    return res


def main() -> None:
    pass


if __name__ == "__main__":
    main()
