# https://leetcode.com/problems/single-number/description/?envType=problem-list-v2&envId=a6ezkna5


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result
