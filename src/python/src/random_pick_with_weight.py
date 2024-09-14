# https://leetcode.com/problems/random-pick-with-weight/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

import bisect
import random


class Solution:
    def __init__(self, w: list[int]):
        total = sum(w)
        self.probabilities = []
        acc = 0.0
        for weight in w:
            acc += weight / total
            self.probabilities.append(acc)
        self.probabilities[-1] = 1.0

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.probabilities, random.random())
