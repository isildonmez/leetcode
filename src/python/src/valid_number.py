from collections import Counter


class Solution:
    def isNumber(self, s: str) -> bool:
        if not self.any_digit(s):
            return False
        if self.is_int(s) or self.is_decimal(s) or self.is_scientific(s):
            return True
        return False

    def any_digit(self, s: str) -> bool:
        return any(c in "0123456789" for c in s)

    def is_int(self, s: str) -> bool:
        if s[0] not in "+-0123456789":
            return False
        if any(c not in "0123456789" for c in s[1:]):
            return False
        return True

    def is_decimal(self, s: str) -> bool:
        if s[0] not in "+-.0123456789":
            return False
        if any(c not in ".0123456789" for c in s[1:]):
            return False
        chars = Counter(s)
        if chars["."] > 1:
            return False
        return True

    def is_scientific(self, s: str) -> bool:
        e_idx = None
        for i, c in enumerate(s):
            if c.lower() not in "+-.0123456789e":
                return False
            if c.lower() == "e":
                if e_idx is not None:
                    return False
                e_idx = i
        if e_idx is None:
            return False
        if not self.any_digit(s[:e_idx]) or not self.is_decimal(s[:e_idx]):
            return False
        if not self.any_digit(s[e_idx + 1 :]) or not self.is_int(s[e_idx + 1 :]):
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    numbers = [
        "2",
        "0089",
        "-0.1",
        "+3.14",
        "4.",
        "-.9",
        "2e10",
        "-90E3",
        "3e+7",
        "+6e-1",
        "53.5e93",
        "-123.456e789",
    ]
    not_numbers = [
        "abc",
        "1a",
        "1e",
        "e3",
        "99e2.5",
        "--6",
        "-+3",
        "95a54e53",
        ".",
        "4e",
        "e9",
        ".e1",
    ]
    print("Testing...")
    assert all(s.isNumber(n) for n in numbers) == True
    assert all(not s.isNumber(c) for c in not_numbers) == True
    print("Done!")
