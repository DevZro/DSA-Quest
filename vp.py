# Valid Palindrome

def isPalindrome(self, s: str) -> bool:
    if not any(char.isalnum() for char in s):
        return True
    
    s = s.lower()

    left = 0
    right = len(s) - 1

    while right > left:
        while not s[left].isalnum():
            left += 1
        while not s[right].isalnum():
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

