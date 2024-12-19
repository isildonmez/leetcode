# https://leetcode.com/problems/squares-of-a-sorted-array/description/?envType=problem-list-v2&envId=a6ezkna5


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        left, right = 0, len(nums) - 1
        idx = len(nums) - 1
        while left <= right:
            if nums[right] ** 2 > nums[left] ** 2:
                res[idx] = nums[right] ** 2
                right -= 1
            else:
                res[idx] = nums[left] ** 2
                left += 1
            idx -= 1
        return res
