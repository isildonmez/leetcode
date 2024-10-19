# https://leetcode.com/problems/string-to-integer-atoi/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def myAtoi(self, s: str) -> int:
        whitespace = sign = digit = False
        num = 0
        sign_multiplier = 1
        i = 0
        while i < len(s):
            c = s[i]
            if c.isalpha():
                break
            elif c.isspace():
                if any(x for x in [whitespace, sign, digit]):
                    break
                while i < len(s) and s[i].isspace():
                    i += 1
                whitespace = True
                continue
            elif c in "+-":
                if any(x for x in [sign, digit]):
                    break
                if c == "-":
                    sign_multiplier = -1
                sign = True
            elif c.isdigit():
                num = num * 10 + int(c)
                digit = True
            else:
                break
            i += 1
        return clamp_to_32_bit(num * sign_multiplier)


def clamp_to_32_bit(num: int) -> int:
    min_int = -(2**31)
    max_int = 2**31 - 1
    return max(min_int, min(num, max_int))
