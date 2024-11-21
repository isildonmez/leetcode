# https://leetcode.com/problems/odd-string-difference/description/?envType=company&envId=datadog&favoriteSlug=datadog-all


from collections import defaultdict


class Solution:
    def oddString(self, words: list[str]) -> str:
        n = len(words[0])
        diff_to_word = defaultdict(list)
        for word in words:
            diff = []
            for i in range(1, n):
                diff.append(ord(word[i]) - ord(word[i - 1]))
            diff_to_word[tuple(diff)].append(word)

        for diff, words in diff_to_word.items():
            if len(words) == 1:
                return words[0]
