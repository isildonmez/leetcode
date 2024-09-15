# https://leetcode.com/problems/k-closest-points-to-origin/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        for i, (x, y) in enumerate(points):
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-(x**2 + y**2), i))
                continue
            if x**2 + y**2 < -max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-(x**2 + y**2), i))
        return [points[i] for distance, i in list(max_heap)]
