# From https://leetcode.com/problems/valid-palindrome/submissions/1140280670/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, r = 0, 1
        shortest_len = None
        if r >= len(nums) and sum(nums) >= target:
            shortest_len = 1
        current_sum = nums[l]
        while r < len(nums):
            if current_sum < target:
                current_sum += nums[r]
                r += 1
            while current_sum >= target:
                if shortest_len is None:
                    shortest_len = r - l
                elif shortest_len > r - l:
                    shortest_len = r - l
                else:
                    pass
                current_sum -= nums[l]
                l += 1

        if shortest_len is None:
            return 0
        return shortest_len


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert s.minSubArrayLen(4, [1, 4, 4]) == 1
    assert s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert s.minSubArrayLen(213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]) == 8
    assert s.minSubArrayLen(7, [8]) == 1
    assert s.minSubArrayLen(7, [8, 8, 8, 8, 8, 8]) == 1
    print("Done!")
