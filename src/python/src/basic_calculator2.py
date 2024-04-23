from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = deque()
        current_number = 0
        operator = None
        for i, c in enumerate(s):
            if c.isdigit():
                current_number = current_number * 10 + int(c)
            if not c.isdigit() or i == len(s)-1:
                if operator == "*":
                    stack.append(stack.pop() * current_number)
                elif operator == "/":
                    stack.append(int(stack.pop() / current_number))
                elif operator == "-":
                    stack.append(-current_number)
                else:
                    stack.append(current_number)
                current_number = 0
                operator = c
        return sum(stack)


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.calculate("3+2*2") == 7
    assert s.calculate(" 3/2 ") == 1
    assert s.calculate("3+5 /2") == 5
    assert s.calculate("14-3/2") == 13
    print("Done!")