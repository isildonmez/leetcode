# Given a string, write a function to check if it is
# a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards
# and backwards. A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.) Hints: #106, #121, #134, #136

from collections import defaultdict


def check_permutation(s: str) -> bool:
    letter_counts = defaultdict(int)
    for char in s:
        # Assuming to compare only letters.
        if char.isalpha():
            letter_counts[char] += 1
    odd = False
    for c in letter_counts.values():
        if c % 2 == 0:
            continue
        if odd is True:
            return False
        odd = True
    return True


if __name__ == "__main__":
    print("Testing...")
    assert check_permutation("cao ttca") is True
    assert check_permutation("ca ttca") is True
    assert check_permutation("cao tca") is False
    print("Done!")
