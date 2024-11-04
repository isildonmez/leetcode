class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                idx = self.idx_to_be_swapped(nums[i:], nums[i - 1])
                nums[i - 1], nums[idx] = nums[idx], nums[i - 1]
                nums[i:] = sorted(nums[i:])
                return
        nums.reverse()

    def idx_to_be_swapped(self, nums: list[int], current: int) -> int:
        closest_min = None
        idx = None
        for i in range(-1, -len(nums) - 1, -1):
            if nums[i] > current and (closest_min is None or nums[i] < closest_min):
                closest_min = nums[i]
                idx = i
        return idx
