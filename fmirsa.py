# Find Minimum in Rotated Sorted Array


def findMin(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        m = l + (r - l) // 2
        if nums[m] < nums[l]:
            l += 1
            r = m
            continue
        if nums[r] < nums[m]:
            l = m + 1
            continue
        return nums[l]
    return nums[l]