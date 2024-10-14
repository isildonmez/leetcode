# https://leetcode.com/problems/top-k-frequent-elements/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencies = Counter(nums)
        freq_heap = []
        for n, f in frequencies.items():
            if len(freq_heap) < k:
                heapq.heappush(freq_heap, (f, n))
            elif f > freq_heap[0][0]:
                heapq.heappop(freq_heap)
                heapq.heappush(freq_heap, (f, n))
        return [n for f, n in freq_heap]
