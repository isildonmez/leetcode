# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openings = 0
        moves = 0
        for i, p in enumerate(s):
            if p == "(":
                openings += 1
                continue
            if openings > 0:
                openings -= 1
            else:
                moves += 1
        return moves + openings
