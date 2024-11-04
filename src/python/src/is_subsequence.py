# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s):
            found_char = False
            while j < len(t):
                if s[i] == t[j]:
                    j += 1
                    found_char = True
                    break
                else:
                    j += 1
            if not found_char:
                return False
            i += 1
        return True

    def alternative_is_subsequence(self, s: str, t: str) -> bool:
        t_length = len(t)
        s_length = len(s)

        if t_length < s_length:
            return False

        i, j, count = 0, 0, 0

        while i < s_length and j < t_length:
            if s[i] == t[j]:
                i = i + 1
                j = j + 1
                count = count + 1
            else:
                j = j + 1

        return count == s_length


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.isSubsequence("abc", "ahbgdc") is True
    assert s.isSubsequence("axc", "ahbgdc") is False
    assert s.isSubsequence("acb", "ahbgdc") is False
    print("Done!")
