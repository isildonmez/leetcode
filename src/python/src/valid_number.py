from collections import Counter


class Solution:
    def isNumber(self, s: str) -> bool:
        dot = digit = exponent = False

        for i,c in enumerate(s):
            if c.isdigit():
                digit = True
            elif c in ('+', '-'):
                if not (i==0 or s[i-1] in ('e','E')):
                    return False
            elif c in ('e','E'):
                if exponent or not digit:
                    return False
                exponent = True
                digit = False
            elif c=='.':
                if exponent or dot:
                    return False
                dot = True
            else:
                return False
        return digit


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
