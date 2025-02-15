def find_closest_number(nums):
    closest = nums[0]
    for el in nums:
        if abs(el) < abs(closest):
            closest = el

    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest
