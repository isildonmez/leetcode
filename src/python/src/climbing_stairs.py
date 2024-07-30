# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150

import math


class Solution:
    def climbStairs(self, n: int) -> int:
        opt = [0] * (n + 1)
        opt[0] = 1
        opt[1] = 1

        for i in range(2, n + 1):
            opt[i] = opt[i - 1] + opt[i - 2]

        return opt[n]

    def climbStairsAlternative(self, n: int) -> int:
        paths = 0
        num_of_2s = n // 2
        for twos in range(num_of_2s + 1):
            ones = n - 2 * twos
            paths += math.factorial(ones + twos) / (
                math.factorial(ones) * math.factorial(twos)
            )
        return int(paths)
