# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openings = 0
        moves = 0
        for c in s:
            if c == "(":
                openings += 1
            elif c == ")" and openings > 0:
                openings -= 1
            elif c == ")" and openings == 0:
                moves += 1
        return moves + openings
