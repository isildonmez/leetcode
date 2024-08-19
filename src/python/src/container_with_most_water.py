# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        height_pair = (height[i], height[j])
        res = min(height_pair) * (j - i)
        while i < j:
            hi, hj = height_pair
            if min(height_pair) == hi:
                while height[i] <= hi and i < j:
                    i += 1
                if i == j:
                    continue
                hi = height[i]
                height_pair = (hi, hj)
                res = max(res, min(height_pair) * (j - i))
            if min(height_pair) == hj:
                while height[j] <= hj and i < j:
                    j -= 1
                if i == j:
                    continue
                hj = height[j]
                height_pair = (hi, hj)
                res = max(res, min(height_pair) * (j - i))
        return res
