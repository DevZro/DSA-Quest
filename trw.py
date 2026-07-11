# Trapping Rain Water
#sol 1

def trap(height):
    prefix = [0] * len(height)
    suffix = [0] * len(height)

    l_height = r_height = 0

    for i in range(1, len(height)):
        l_height = max (l_height, height[i-1])
        r_height = max (r_height, height[-i])

        prefix[i] = l_height
        suffix[-(i + 1)] = r_height

    return sum(max(0, min(prefix[i], suffix[i]) - height[i]) for i in range(len(height))) 

def trap(height):
    prefix = [0] * len(height)
    suffix = [0] * len(height)

    l_height = r_height = 0

    for i in range(len(height)):
        l_height = max (l_height, height[i])
        r_height = max (r_height, height[-(i + 1)])

        prefix[i] = l_height
        suffix[-(i + 1)] = r_height

    return sum(min(prefix[i], suffix[i]) - height[i] for i in range(len(height)))