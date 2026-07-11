# Permutation in Strings

def checkInclusion(s1, s2):
    mp1 = {}
    for c in s1:
        mp1[c] = 1 + mp1.get(c, 0)

    for i in range(len(s2)):
        mp2 = {}
        for j in range(i, len(s2)):
            mp2[s2[j]] = 1 + mp2.get(s2[j], 0)
            if  mp2[s2[j]] > mp1.get(s2[j], 0):
                break
            if len(s1) == j - i + 1:
                return True
    return False