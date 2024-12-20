# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.isSubsequence("abc", "ahbgdc") is True
    assert s.isSubsequence("axc", "ahbgdc") is False
    assert s.isSubsequence("acb", "ahbgdc") is False
    print("Done!")
