from typing import List


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
        raise TypeError("Input should be a list")
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False
