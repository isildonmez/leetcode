# https://leetcode.com/problems/min-stack/?envType=study-plan-v2&envId=top-interview-150

from collections import defaultdict
from collections import deque


class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min = None
        self.vals = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min is None:
            self.min = val
        else:
            self.min = min(self.min, val)
        self.vals[val] += 1

    def pop(self) -> None:
        el = self.stack.pop()
        self.vals[el] -= 1
        if self.vals[el] == 0:
            del self.vals[el]
        if el == self.min:
            keys = self.vals.keys()
            if len(keys) == 0:
                self.min = None
            else:
                self.min = min(keys)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
