# TODO: Check for better solutions in leetcode

from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = deque()
        right = deque()
        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            if c == ")":
                if len(left) > 0:
                    left.pop()
                else:
                    right.append(i)
        to_remove = set(left + right)
        result = []
        for i, c in enumerate(s):
            if i not in to_remove:
                result.append(c)
        return "".join(result)


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
    assert s.minRemoveToMakeValid("))((") == ""
    print("Done!")
