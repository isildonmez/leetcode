# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        options = [0] * (n + 1)
        options[1], options[2] = 1, 2
        for step in range(3, n + 1):
            options[step] = options[step - 1] + options[step - 2]
        return options[n]
