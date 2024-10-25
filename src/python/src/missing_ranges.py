# https://leetcode.com/problems/missing-ranges/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def findMissingRanges(
        self, nums: list[int], lower: int, upper: int
    ) -> list[list[int]]:
        if len(nums) == 0:
            return [[lower, upper]]
        res = []
        if nums[0] != lower:
            res.append([lower, nums[0] - 1])
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                res.append([nums[i - 1] + 1, nums[i] - 1])
        if nums[-1] != upper:
            res.append([nums[-1] + 1, upper])
        return res
