# From https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sub_sum = 0
        for idx in range(k):
            sub_sum += nums[idx]
        if len(nums) == k:
            return sub_sum / k
        highest_sum = sub_sum
        for starting_idx in range(1, len(nums) - k + 1):
            sub_sum -= nums[starting_idx - 1]
            sub_sum += nums[starting_idx + k -1]
            if sub_sum > highest_sum:
                highest_sum = sub_sum
        return highest_sum / k
    
if __name__ == "__main__":
    print("Testing...")
    s = Solution()
    assert s.findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75
    assert s.findMaxAverage([5], 1) == 5.0
    print("All passed")
