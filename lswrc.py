# Longest Substring without repeating characters

def lengthOfLongestSubstring(s):
    dp_map = {}
    max_length = 0
    start = 0

    for i in range(len(s)):    
        if s[i] in dp_map:
            max_length = max(max_length, i - start)
            start = max(start, dp_map[s[i]] + 1)
        dp_map[s[i]] = i

    max_length = max(max_length, len(s) - start)
    return max_length


