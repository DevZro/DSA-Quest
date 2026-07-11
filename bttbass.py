# Best time to buy and sell stocks

# sol 1
def maxProfit(prices):
    prefix = [0] * len(prices)
    prefix[0] = prices[0]

    suffix = [0] * len(prices)
    suffix[-1] = prices[-1]

    res = 0

    for i in range(1, len(prices)):
        prefix[i] = min(prefix[i-1], prices[i])
        
    for i in range(len(prices) - 2, -1, -1):
        suffix[i] = max(prices[i], suffix[i + 1])

    for i in range(len(prices)):
        res = max(res, suffix[i] - prefix[i])
            
    return res

# sol 2

