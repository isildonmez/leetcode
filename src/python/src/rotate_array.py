# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        nums[:k], nums[k:] = nums[len(nums) - k :], nums[: len(nums) - k]
        # nums[:] = nums[-k:] + nums[:-k]
