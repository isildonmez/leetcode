# From https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        idx = 0
        for _ in range(len(nums)):
            if nums[idx] == val:
                del nums[idx : idx + 1]
            else:
                idx += 1
        return len(nums)

    def removeElementRefactored(self, nums: list[int], val: int) -> int:
        idx = 0
        for i, el in enumerate(nums):
            if el == val:
                tmp = nums[idx]
                nums[idx] = val
                nums[i] = tmp
                idx += 1
        del nums[:idx]
        return len(nums)

    def removeElementImproved(self, nums: list[int], val: int) -> int:
        idx = len(nums) - 1
        for i in reversed(range(len(nums))):
            if nums[i] == val:
                tmp = nums[idx]
                nums[idx] = val
                nums[i] = tmp
                idx -= 1
        return len(nums) - ((len(nums) - 1) - idx)

    def removeElementBest(self, nums: list[int], val: int) -> int:
        n, current_idx, got = len(nums) - 1, len(nums) - 1, 0
        while current_idx >= 0:
            if nums[current_idx] == val:
                nums[current_idx] = nums[n - got]
                got += 1
            current_idx -= 1
        return len(nums) - got


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.removeElement([3, 2, 2, 3], 3) == 2
    assert s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert s.removeElementRefactored([3, 2, 2, 3], 3) == 2
    assert s.removeElementRefactored([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert s.removeElementImproved([3, 2, 2, 3], 3) == 2
    assert s.removeElementImproved([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert s.removeElementBest([3, 2, 2, 3], 3) == 2
    assert s.removeElementBest([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
