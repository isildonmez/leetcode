# https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            if i == 0:
                return [1] + digits
            i -= 1
