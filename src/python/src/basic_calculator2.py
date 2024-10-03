# https://leetcode.com/problems/basic-calculator-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        sign = "+"
        num = 0
        for c in s + "+":
            if c.isnumeric():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0
        return sum(stack)


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.calculate("3+2*2") == 7
    assert s.calculate(" 3/2 ") == 1
    assert s.calculate("3+5 /2") == 5
    assert s.calculate("14-3/2") == 13
    print("Done!")
