# Search in Rotated Sorted Array

def search(nums, target):
    l, r = 0, len(nums) - 1
        
    while l < r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif target > nums[m]:
            if nums[l] == target:
                return l
            elif nums[l] > target:
                l = m + 1
            else:
                if nums[m] > nums[l]:
                    l = m + 1
                elif nums[l] > nums[m]:
                    r = m - 1
                else:
                    break
        else:
            if nums[l] == target:
                return l
            elif nums[l] > target:
                if nums[m] > nums[l]:
                    l = m + 1
                elif nums[l] > nums[m]:
                    r = m - 1
                else:
                    break
            else:
                r = m - 1

    if target == nums[l]:
        return l
    elif target == nums[r]:
        return r
    return -1