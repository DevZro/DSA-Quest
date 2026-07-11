# Container with most water

def maxArea(heights):
    result = 0

    l = 0
    r = len(heights) - 1

    while l < r:
        height = (r - l) * min(heights[l], heights[r])
        result = max(height, result)
        if heights[r] > heights[l]:
            l += 1
        else:
            r -= 1

    return result