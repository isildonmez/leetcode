# From https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left, right = 0, k - 1
        current_sum = sum(nums[:k])
        max_sum = current_sum
        while right < len(nums) - 1:
            current_sum = current_sum - nums[left] + nums[right + 1]
            max_sum = max(max_sum, current_sum)
            right += 1
            left += 1
        return float(max_sum / k)


if __name__ == "__main__":
    print("Testing...")
    s = Solution()
    assert s.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert s.findMaxAverage([5], 1) == 5.0
    print("All passed")
