# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            current = min(height[left], height[right]) * width
            max_area = max(max_area, current)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
