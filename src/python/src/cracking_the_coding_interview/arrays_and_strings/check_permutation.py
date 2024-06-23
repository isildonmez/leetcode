# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
# Hints: #7, #84, #722, #737

from collections import Counter


def check_permutations(w1: str, w2: str) -> bool:
    chars1, chars2 = Counter(w1), Counter(w2)
    return dict(chars1 - chars2) == {} or dict(chars2 - chars1) == {}
