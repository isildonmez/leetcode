# https://leetcode.com/problems/add-binary/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def add_binary(self, a: str, b: str) -> str:
        total = int(a, 2) + int(b, 2)
        result = ""
        while total >= 2:
            total, current_digit = total // 2, total % 2
            result = f"{current_digit}" + result
        return f"{total}" + result

    def alternative_add_binary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
