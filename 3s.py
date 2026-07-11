# 3 sum

def threeSum(nums):
    results = []
    nums.sort()
        
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and (nums[i] == nums[i - 1]):
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if (nums[l] + nums[r]) > -1 * nums[i]:
                r -= 1
            elif (nums[l] + nums[r]) < -1 * nums[i]:
                l += 1
            else:
                results.append([nums[i], nums[l], nums[r]])
                while ((nums[l] + nums[r]) == -1 * nums[i]) and (l < r):
                    l += 1
    return results
