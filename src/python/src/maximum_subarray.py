# https://leetcode.com/problems/maximum-subarray/description/?envType=problem-list-v2&envId=a6ezkna5&difficulty=MEDIUM%2CHARD


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if current_sum <= 0:
                current_sum = n
            else:
                current_sum += n
            max_sum = max(current_sum, max_sum)
        return max_sum
