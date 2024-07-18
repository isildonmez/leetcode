# https://leetcode.com/problems/fibonacci-number/description/


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        left, right = 0, 1
        for i in range(2, n + 1):
            left, right = right, left + right
        return right
