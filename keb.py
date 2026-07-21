# Koko Eating Bananas 

import math

def minEatingSpeed(piles, h):
    m = max(piles)
    if len(piles) == h:
        return m
        
    s = sum(piles)
    n = len(piles)

    lower = math.ceil(s / h)
    upper = min(math.ceil((s - n) / (h - n)), m)

    def check(r):
        val = 0
        for pile in piles:
            val += math.ceil(pile / r)
            if val > h:
                return False
        return True
        
    while lower < upper:
        mid = lower + (upper - lower) // 2

        if check(mid):
            upper = mid
        else:
            lower = mid + 1
        
    return lower