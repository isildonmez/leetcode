# https://leetcode.com/problems/top-k-frequent-elements/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from collections import defaultdict


class Solution:
    # On
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencies_by_nums = defaultdict(int)
        for n in nums:
            frequencies_by_nums[n] += 1
        min_f = float("inf")
        max_f = -float("inf")
        frequencies_to_nums = defaultdict(list)
        for n, f in frequencies_by_nums.items():
            frequencies_to_nums[f].append(n)
            min_f = min(min_f, f)
            max_f = max(max_f, f)
        res = []
        for f in range(max_f, min_f - 1, -1):
            if f in frequencies_to_nums:
                res.extend(frequencies_to_nums[f])
            if len(res) == k:
                return res

    # # Onlogk
    # def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    #     dic=Counter(nums)
    #     res=[]
    #     for key,ct in dic.items():
    #         heapq.heappush(res,[ct,key])
    #         if len(res)>k:
    #             heapq.heappop(res)
    #     return [x[1] for x in res]
