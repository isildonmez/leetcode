# TODO: Check for better solutions in leetcode

from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        opening = deque()
        for i, c in enumerate(s):
            if c == "(":
                opening.append(i)
            elif c == ")":
                if len(opening) > 0:
                    opening.pop()
                else:
                    chars[i] = ""
        while len(opening) > 0:
            i = opening.pop()
            chars[i] = ""
        return "".join(chars)


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
    assert s.minRemoveToMakeValid("))((") == ""
    print("Done!")
