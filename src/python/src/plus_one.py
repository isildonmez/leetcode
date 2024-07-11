# https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        newDigits = digits.copy()
        for i in range(len(digits)-1, -1, -1):
            total = newDigits[i] + remainder
            remainder = total // 10
            newDigits[i] = total % 10
            if remainder == 0:
                return newDigits
        if remainder != 0:
            return [remainder] + newDigits
        return newDigits
