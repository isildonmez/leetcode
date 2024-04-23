# from https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def find_difference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        distinct_nums1 = set(nums1)
        distinct_nums2 = set(nums2)
        return [list(distinct_nums1 - distinct_nums2), list(distinct_nums2 - distinct_nums1)]
