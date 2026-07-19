# Largest Area Rectangle

def largestRectangleArea(heights):
    stack = []
    n = len(heights)
    res = 0

    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            res = max(res, height * width)
        stack.append(i)

    while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        res = max(res, height * width)
        
    return res
