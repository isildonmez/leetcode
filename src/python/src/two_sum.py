# https://leetcode.com/problems/two-sum/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_idx = {}
        for i in range(len(nums)):
            current = nums[i]
            pair = target - current
            if pair in num_to_idx:
                return [num_to_idx[pair], i]
            num_to_idx[current] = i
        return []
