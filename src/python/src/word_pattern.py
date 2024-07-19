# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def word_pattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        pattern_to_word = {}
        word_to_pattern = {}
        for i, p in enumerate(pattern):
            w = words[i]
            if p in pattern_to_word.keys() and pattern_to_word[p] != w:
                return False
            if w in word_to_pattern.keys() and word_to_pattern[w] != p:
                return False
            pattern_to_word[p] = w
            word_to_pattern[w] = p
        return True


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.word_pattern("abba", "dog cat cat dog") == True
    assert s.word_pattern("abba", "dog cat cat fish") == False
    assert s.word_pattern("aaaa", "dog cat cat dog") == False
    print("Done!")
