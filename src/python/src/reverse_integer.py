# https://leetcode.com/problems/reverse-integer/description/?envType=problem-list-v2&envId=a6ezkna5&difficulty=MEDIUM%2CHARD


class Solution:
    def reverse(self, x: int) -> int:
        multiplier = 1
        if x < 0:
            multiplier *= -1
            x *= -1
        reversed_x = 0
        while x > 0:
            mod = x % 10
            reversed_x = reversed_x * 10 + mod
            x = x // 10
        reversed_x *= multiplier
        min_edge, max_edge = [-(2**31), 2**31 - 1]
        if min_edge <= reversed_x <= max_edge:
            return reversed_x
        return 0
