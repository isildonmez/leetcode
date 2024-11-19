# https://leetcode.com/problems/most-common-word/?envType=company&envId=datadog&favoriteSlug=datadog-thirty-days

from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = re.findall(r"\w+", paragraph.lower())
        banned_words = set(banned)
        word_counts = Counter([w for w in words if w not in banned_words])
        word, _ = word_counts.most_common(1)[0]
        return word
