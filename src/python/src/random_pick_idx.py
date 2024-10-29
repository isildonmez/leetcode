# https://leetcode.com/problems/random-pick-index/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from collections import defaultdict
import random


class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.nums_to_idx = defaultdict(list)
        for i, n in enumerate(self.nums):
            self.nums_to_idx[n].append(i)

    def pick(self, target: int) -> int:
        idx = random.randint(0, len(self.nums_to_idx[target]) - 1)
        return self.nums_to_idx[target][idx]
