# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)
        return [left, right]

    def binary_search(
        self, nums: list[int], target: int, searching_left_side: bool
    ) -> int:
        left, right, idx = 0, len(nums) - 1, -1

        while left <= right:
            mid_idx = (left + right) // 2
            if nums[mid_idx] < target:
                left = mid_idx + 1
            elif nums[mid_idx] > target:
                right = mid_idx - 1
            else:
                idx = mid_idx
                if searching_left_side:
                    right = mid_idx - 1
                else:
                    left = mid_idx + 1
        return idx
