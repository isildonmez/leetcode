# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)
        return [left, right]

    def binary_search(
        self, nums: list[int], target: int, searching_left_side: bool
    ) -> int:
        l, r, idx = 0, len(nums) - 1, -1

        while l <= r:
            mid_idx = (l + r) // 2
            if nums[mid_idx] < target:
                l = mid_idx + 1
            elif nums[mid_idx] > target:
                r = mid_idx - 1
            else:
                idx = mid_idx
                if searching_left_side:
                    r = mid_idx - 1
                else:
                    l = mid_idx + 1
        return idx
