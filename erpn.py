# Evaluate Reverse Polish Notation

import operator
def evalRPN(tokens):
    stack = []
    operators = {"+" : operator.add, "-": operator.sub,
                 "*" : operator.mul, "/" : operator.truediv}
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            var2 = stack.pop()
            var1 = stack.pop()
            result = int(operators[token](var1, var2))
            stack.append(result)
    return stack.pop()
