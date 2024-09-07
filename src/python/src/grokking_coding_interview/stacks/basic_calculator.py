from collections import deque


def calculator(s):
    num = 0
    res = 0
    sign = 1
    operations = deque()
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c in "+-":
            res += num * sign
            num = 0
            sign = -1 if c == "-" else 1
        elif c == "(":
            operations.append(res)
            operations.append(sign)
            res = 0
            num = 0
            sign = 1
        elif c == ")":
            res += num * sign
            num = 0
            sign = 1
            s = operations.pop()
            other_pair = operations.pop()
            res = res * s + other_pair
    return res + num * sign
