# https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/1183588995/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        max_sum = min_sum = current_min = current_max = total_sum = nums[0]
        for n in nums[1:]:
            total_sum += n
            current_min, current_max = min(current_min + n, n), max(current_max + n, n)
            min_sum, max_sum = min(current_min, min_sum), max(current_max, max_sum)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.maxSubarraySumCircular([1, -2, 3, -2]) == 3
    assert s.maxSubarraySumCircular([5, -3, 5]) == 10
    assert s.maxSubarraySumCircular([-3, -2, -3]) == -2
    assert s.maxSubarraySumCircularAlternative([1, -2, 3, -2]) == 3
    assert s.maxSubarraySumCircularAlternative([5, -3, 5]) == 10
    assert s.maxSubarraySumCircularAlternative([-3, -2, -3]) == -2
    print("Done!")
