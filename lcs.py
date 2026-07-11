# Longest Consecutive Sequence

# Sol 1
"""def longestConsecutive(nums):
    if len(nums) <= 1:
        return len(nums)

    num_set = set(nums)
    score = 1

    seq_start = []
    for num in nums:
        if (num - 1) not in num_set:
            seq_start.append(num)
    print(seq_start)

    for num in seq_start:
        length = 1
        while (num + 1) in num_set:
            num += 1
            length += 1
        score = max (length, score)
        
    return score"""

# Sol 2
def longestConsecutive(nums):
    if len(nums) <= 1:
        return len(nums)

    num_set = set(nums)
    score = 0
    seq = iter(num_set)

    while len(num_set) != 0:
        num = next(seq)
        if (num - 1) not in num_set:
            length = 1
            num_set.remove(num)
            while (num + 1) in num_set:
                num += 1
                length += 1
                num_set.remove(num)
            score = max(score, length)
            seq = iter(num_set)
        
    return score