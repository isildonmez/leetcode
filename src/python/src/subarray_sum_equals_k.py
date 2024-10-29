# https://leetcode.com/problems/subarray-sum-equals-k/description/


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        sum_to_count = {0: 1}
        result = 0

        for num in nums:
            prefix_sum = prefix_sum + num
            if prefix_sum - k in sum_to_count:
                result = result + sum_to_count[prefix_sum - k]
            if prefix_sum not in sum_to_count:
                sum_to_count[prefix_sum] = 1
            else:
                sum_to_count[prefix_sum] = sum_to_count[prefix_sum] + 1
        return result
