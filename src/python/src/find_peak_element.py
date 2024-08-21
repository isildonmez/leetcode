# https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return r


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.findPeakElement([1, 2, 3, 1]) == 2
    assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in (1, 5)
    assert s.findPeakElement([1, 2, 3]) == 2
    assert s.findPeakElement([6, 5, 4, 3, 2, 3, 2]) == 0
    print("Done!")
