# https://leetcode.com/problems/powx-n/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1 / x, -n)
        square_root = self.myPow(x, n // 2)
        if n % 2 == 0:
            return square_root * square_root
        return square_root * square_root * x
