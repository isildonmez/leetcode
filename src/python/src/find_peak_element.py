# https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return right


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.findPeakElement([1, 2, 3, 1]) == 2
    assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in (1, 5)
    assert s.findPeakElement([1, 2, 3]) == 2
    assert s.findPeakElement([6, 5, 4, 3, 2, 3, 2]) == 0
    print("Done!")
