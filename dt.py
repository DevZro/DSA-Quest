# Daily Temperatures

def dailyTemperatures(temperatures):
    stack = []
        
    n = len(temperatures)

    result = [0] * n
    for i in range(n - 1, -1, -1):
        if not stack:
            result[i] = stack[-1] - i if stack else 0
        else:
            while temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
                if not stack:
                    break
            result[i] = stack[-1] - i if stack else 0
        stack.append(i)
            
    return result
