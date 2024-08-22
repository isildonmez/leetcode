# https://leetcode.com/problems/number-of-1-bits/submissions/1363618453/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n != 0:
            result += n & 1
            n = n >> 1
        return result

    def hammingWeightAlternative(self, n: int) -> int:
        count = 0
        while n > 0:
            n, m = divmod(n, 2)
            if m == 1:
                count += 1
        return count
