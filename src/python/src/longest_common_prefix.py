# https://leetcode.com/problems/longest-common-prefix/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_len = min([len(w) for w in strs])
        for i in range(shortest_len):
            ref = strs[0][i]
            if not all(w[i] == ref for w in strs):
                return strs[0][:i]
        return strs[0][:shortest_len]
