# From https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = right = 0
        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.removeElement([3, 2, 2, 3], 3) == 2
    assert s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
