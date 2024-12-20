# https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=a6ezkna5


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars_to_idx = {}
        for idx, char in enumerate(s):
            if char not in chars_to_idx:
                chars_to_idx[char] = idx
            elif chars_to_idx[char] == len(s):
                continue
            else:
                chars_to_idx[char] = len(s)
        min_idx = min(chars_to_idx.values())
        if min_idx == len(s):
            return -1
        return min_idx
