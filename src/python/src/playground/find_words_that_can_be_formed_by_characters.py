# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/?envType=company&envId=datadog&favoriteSlug=datadog-all


from collections import Counter
from typing import Mapping


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        chars_count = Counter(chars)
        total = 0
        for w in words:
            if subset(chars_count, w):
                total += len(w)
        return total


def subset(chars_count: Mapping[str, int], w: str) -> bool:
    word_count = Counter(w)
    for char, count in word_count.items():
        if char not in chars_count:
            return False
        if chars_count[char] < count:
            return False
    return True
