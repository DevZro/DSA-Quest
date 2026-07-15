# Valid Parantheses

def isValid(s):
    stack = []

    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if not stack:
                return False
            cur = stack.pop()
            if (cur == '(' and c == ')') or (cur == '[' and c == ']') or (cur == '{' and c == '}'):
                continue
            return False

    if stack:
        return False
    return True