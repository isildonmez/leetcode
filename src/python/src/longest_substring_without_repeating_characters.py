# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        max_length = left = 0
        for right in range(len(s)):
            if s[right] not in chars or chars[s[right]] < left:
                max_length = max(max_length, right - left + 1)
            else:
                left = chars[s[right]] + 1
            chars[s[right]] = right
        return max_length


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    print("Done!")
