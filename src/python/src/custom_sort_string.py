# https://leetcode.com/problems/custom-sort-string/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_chars = set(order)
        s_chars = Counter(s)
        res = ""
        common_order = [c for c in order if c in s_chars]
        for c in common_order:
            res += c * s_chars[c]
        others = s_chars.keys() - order_chars
        for c in others:
            res += c * s_chars[c]
        return res
