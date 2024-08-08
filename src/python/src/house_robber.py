# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def rob(self, nums: list[int]) -> int:
        evens = 0
        odds = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                evens += nums[i]
            else:
                odds += nums[i]
        return max(evens, odds)


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
    print("Done!")
