# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150

from itertools import product


class Solution:
    def _combined_letters(self, d1: set[str], d2: set[str]) -> set[str]:
        combined = set()
        for l1 in d1:
            for l2 in d2:
                combined.add(f"{l1}{l2}")
        return combined

    def letterCombinations(self, digits: str) -> list[str]:
        digits_to_letters = {
            "2": {"a", "b", "c"},
            "3": {"d", "e", "f"},
            "4": {"g", "h", "i"},
            "5": {"j", "k", "l"},
            "6": {"m", "n", "o"},
            "7": {"p", "q", "r", "s"},
            "8": {"t", "u", "v"},
            "9": {"w", "x", "y", "z"},
        }
        if len(digits) == 0:
            return []
        combinations = digits_to_letters[digits[0]]
        for i in range(1, len(digits)):
            combinations = self._combined_letters(
                combinations, digits_to_letters[digits[i]]
            )
        return list(combinations)

    def alternative_letter_combinations(self, digits: str) -> list[str]:
        digits_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
        letters = [digits_to_letters[d] for d in digits]
        combinations = product(*letters)
        return ["".join(c) for c in combinations]


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert set(s.alternative_letter_combinations("23")) == set(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )
    assert s.alternative_letter_combinations("") == []
    assert set(s.alternative_letter_combinations("2")) == set(["a", "b", "c"])
    print("Done!")
