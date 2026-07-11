# Minimum window Substring

def minWindow(s, t):
    if len(s) < len(t):
        return ""
        
    res = ()

    mp_t = {}
    for c in t:
        mp_t[c] = 1 + mp_t.get(c, 0)

    for l in range(len(s)):
        if s[l] not in mp_t:
            continue
        mp_s = {}
        correct = 0
        for r in range(l, len(s)):
            mp_s[s[r]] = 1 + mp_s.get(s[r], 0)

            if mp_s[s[r]] == mp_t.get(s[r], 0):
                correct += 1
                
            if correct == len(mp_t) and (len(res) == 0 or r - l < res[1] - res[0]):
                res = (l, r)
                
    if len(res) == 0:
        return ""
        
    return s[res[0] : res[1] + 1]