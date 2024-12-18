# https://leetcode.com/problems/maximum-subarray/description/?envType=problem-list-v2&envId=a6ezkna5&difficulty=MEDIUM%2CHARD


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
        return max_sum
