# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        m = [0] * n
        m[0], m[1] = nums[0], max(nums[1], nums[0])
        for i in range(2, len(nums)):
            m[i] = max(m[i - 1], m[i - 2] + nums[i])
        return m[-1]


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
    assert s.rob([2, 1, 1, 2]) == 4
    print("Done!")
