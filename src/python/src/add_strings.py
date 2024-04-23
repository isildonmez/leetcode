from collections import deque


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        str_to_digit = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        carry = 0
        digits = deque()
        stop_idx = min(len(num1), len(num2))
        for i in range(1, stop_idx + 1):
            d1, d2 = str_to_digit[num1[-i]], str_to_digit[num2[-i]]
            carry += d1 + d2
            digit = carry % 10
            carry //= 10
            digits.appendleft(f"{digit}")
        while carry != 0:
            current_idx = len(digits) * -1 - 1
            if len(num1) >= current_idx * -1:
                carry += str_to_digit[num1[current_idx]]
            if len(num2) >= current_idx * -1:
                carry += str_to_digit[num2[current_idx]]
            digit = carry % 10
            carry //= 10
            digits.appendleft(f"{digit}")
        until = len(digits) * -1
        return num1[:until] + num2[:until] + "".join(list(digits))


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.addStrings("11", "123") == "134"
    assert s.addStrings("99", "99") == "198"
    assert s.addStrings("456", "77") == "533"
    assert s.addStrings("0", "0") == "0"
    print("Done!")
