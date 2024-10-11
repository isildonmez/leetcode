# https://leetcode.com/problems/buildings-with-an-ocean-view/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        if len(heights) == 0:
            return []
        ocean_views = [len(heights) - 1]
        max_height = heights[-1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > max_height:
                ocean_views.append(i)
                max_height = heights[i]
        return ocean_views[::-1]
