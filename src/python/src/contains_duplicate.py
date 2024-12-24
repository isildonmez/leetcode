# https://leetcode.com/problems/contains-duplicate/?envType=problem-list-v2&envId=a6ezkna5


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
