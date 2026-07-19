# Binary Search

def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        cur = l + (r - l) // 2 # avoiding overflow from (l + r) // 2
        if nums[cur] < target:
            l = cur + 1
        elif nums[cur] > target:
            r = cur - 1
        else: 
            return cur
    return -1 