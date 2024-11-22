# https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=a6ezkna5

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = deque()
        complements = {"}": "{", "]": "[", ")": "("}
        for c in s:
            if c in "({[":
                parentheses.append(c)
                continue
            if len(parentheses) == 0:
                return False
            last_c = parentheses.pop()
            if last_c != complements[c]:
                return False
        if len(parentheses) > 0:
            return False
        return True
