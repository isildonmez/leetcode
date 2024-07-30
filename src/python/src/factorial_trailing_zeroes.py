# https://leetcode.com/problems/factorial-trailing-zeroes/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n >= 5:
            result += n // 5
            n //= 5
        return result
