# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1
