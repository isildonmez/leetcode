# https://leetcode.com/problems/majority-element/submissions/1354756823/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res = majority = 0
        for n in nums:
            if majority == 0:
                res = n
            majority += 1 if n == res else -1
        return res
