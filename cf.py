# Car Fleet
def carFleet(target, position, speed):
    dur = []  # (- position, duration)
    stack = []

    for s, v in zip(position, speed):
        dur.append((- s, (target - s) / v))
    dur = sorted(dur)
        
    for i in range(len(dur)):
        if not stack or dur[i][1] > stack[-1][1]:
            stack.append(dur[i])
        
    return len(stack)