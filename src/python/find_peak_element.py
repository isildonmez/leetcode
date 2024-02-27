class Solution:
    # On
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        for i, n in enumerate(nums):
            if i == 0:
                if n > nums[i+1]: return i
            elif i == len(nums)-1:
                if n > nums[i-1]: return i
            else:
                if nums[i-1] < n > nums[i+1]:
                    return i


    # Ologn
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r ) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return r


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.findPeakElement([1,2,3,1]) == 2
    assert s.findPeakElement([1,2,1,3,5,6,4]) in (1,5)
    assert s.findPeakElement([1,2,3]) == 2
    assert s.findPeakElement([6,5,4,3,2,3,2]) == 0
    print("Done!")

