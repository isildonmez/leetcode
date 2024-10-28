# https://leetcode.com/problems/diagonal-traverse/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        res = []
        r = c = 0
        m, n = len(mat), len(mat[0])
        direction = True

        for _ in range(m * n):
            res.append(mat[r][c])

            if direction is True:
                if r == 0 and c != n - 1:
                    direction = False
                    c += 1
                elif c == n - 1:
                    direction = False
                    r += 1
                else:
                    r -= 1
                    c += 1
            else:
                if c == 0 and r != m - 1:
                    direction = True
                    r += 1
                elif r == m - 1:
                    direction = True
                    c += 1
                else:
                    r += 1
                    c -= 1
        return res
