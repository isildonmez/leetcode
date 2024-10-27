# https://leetcode.com/problems/toeplitz-matrix/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for idx in range(m - 1, 0, -1):
            ref = matrix[idx]
            if ref[1:] != matrix[idx - 1][: n - 1]:
                return False
        return True
