# From https://leetcode.com/problems/search-insert-position/description/?envType=study-plan-v2&envId=top-interview-150
import math


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        start_idx = 0
        end_idx = len(nums) - 1
        while end_idx - start_idx > 1:
            mid_idx = (start_idx + end_idx) // 2
            if target == nums[mid_idx]:
                return mid_idx
            if target < nums[mid_idx]:
                end_idx = mid_idx
            else:
                start_idx = mid_idx
        if target <= nums[start_idx]:
            return start_idx
        if target <= nums[end_idx]:
            return end_idx
        if target > nums[end_idx]:
            return end_idx + 1
        

    def searchInsertRefactored(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        start_idx = 0
        end_idx = len(nums) - 1
        while start_idx != end_idx:
            left_mid_idx = math.floor((start_idx + end_idx) / 2)
            right_mid_idx = math.ceil((start_idx + end_idx) / 2)
            if nums[left_mid_idx] < target and target <= nums[right_mid_idx]:
                return right_mid_idx
            elif target == nums[left_mid_idx]:
                return left_mid_idx
            elif target < nums[left_mid_idx]:
                end_idx = left_mid_idx
            else:
                start_idx = right_mid_idx
        if target <= nums[start_idx]:
            return start_idx
        else:
            return start_idx + 1
        
    def searchInsertImproved(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)

        while right - left > 1:
            mid = (right + left) // 2

            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid
            else:
                return mid
            
        if nums[left] >= target:      
            return left
        else:
            return right


    def searchInsertBest(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)

        while right - left > 1:
            mid = (right + left) // 2

            if target < nums[mid]:
                right = mid
            else:
                left = mid
            
        if nums[left] >= target:      
            return left
        else:
            return right
        






if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.searchInsert([1,3,5,6], 5) == 2
    assert s.searchInsert([1,3,5,6], 2) == 1
    assert s.searchInsert([1,3,5,6], 7) == 4
    assert s.searchInsertRefactored([1], 1) == 0
    assert s.searchInsertRefactored([1,3,5,6], 5) == 2
    assert s.searchInsertRefactored([1,3,5,6], 2) == 1
    assert s.searchInsertRefactored([1,3,5,6], 7) == 4
    assert s.searchInsertRefactored([1], 1) == 0
    print("Done!")
