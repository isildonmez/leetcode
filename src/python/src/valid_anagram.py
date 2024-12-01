# https://leetcode.com/problems/valid-anagram/description/?envType=company&envId=spotify&favoriteSlug=spotify-all


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs, ct = Counter(s), Counter(t)
        return cs == ct
