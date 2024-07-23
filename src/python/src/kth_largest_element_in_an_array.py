# https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        if len(nums) == k:
            return min_val
        values = [0] * (max_val - min_val + 1)
        size = 0
        for n in nums:
            values[n - min_val] += 1
        for i in range(len(values) - 1, -1, -1):
            size += values[i]
            if size >= k:
                return i + min_val


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    print("Done!")
