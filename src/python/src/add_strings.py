# https://leetcode.com/problems/add-strings/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            carry, total = divmod(n1 + n2 + carry, 10)
            res += str(total)
            i -= 1
            j -= 1
        return res[::-1]


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.addStrings("11", "123") == "134"
    assert s.addStrings("99", "99") == "198"
    assert s.addStrings("456", "77") == "533"
    assert s.addStrings("0", "0") == "0"
    print("Done!")
