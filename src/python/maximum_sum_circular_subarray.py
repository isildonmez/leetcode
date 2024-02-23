# https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/1183588995/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        linear_max = current_max = nums[0]
        if len(nums) == 1:
            return linear_max
        for i in range(1, len(nums)):
            current_max = max(current_max + nums[i], nums[i])
            linear_max = max(linear_max, current_max)

        right_maximums = [nums[-1]]
        right_sum = right_max = nums[-1]
        for i in reversed(range(1, len(nums) - 1)):
            right_sum += nums[i]
            right_max = max(right_sum, right_max)
            right_maximums.append(right_max)
        right_maximums.reverse()

        left_sum = left_max = nums[0]
        circular_max = current_max = left_max + right_maximums[0]
        for i in range(1, len(nums) - 1):
            left_sum += nums[i]
            left_max = max(left_sum, left_max)
            current_max = left_max + right_maximums[i]
            circular_max = max(current_max, circular_max)

        return max(linear_max, circular_max)
    
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        linear_max = current_max = nums[0]
        linear_min = current_min = total_sum = nums[0]
        for i in range(1, len(nums)):
            current_max = max(current_max + nums[i], nums[i])
            linear_max = max(linear_max, current_max)
            total_sum += nums[i]
            current_min = min(current_min + nums[i], nums[i])
            linear_min = min(linear_min, current_min)
        sub_sum = total_sum - linear_min
        return linear_max if linear_max < 0 else max(linear_max, sub_sum)
    

if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.maxSubarraySumCircular([1,-2,3,-2]) == 3
    assert s.maxSubarraySumCircular([5,-3,5]) == 10
    assert s.maxSubarraySumCircular([-3,-2,-3]) == -2
    print("Done!")
