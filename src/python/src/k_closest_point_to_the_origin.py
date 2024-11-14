# https://leetcode.com/problems/k-closest-points-to-origin/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(max_heap, (-distance, x, y))
            while len(max_heap) > k:
                heapq.heappop(max_heap)
        return [[x, y] for _, x, y in max_heap]
