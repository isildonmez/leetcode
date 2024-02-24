# TODO: Check for better solutions in leetcode

class Solution:
    def is_palindrome(self, s: str) -> tuple[bool, int, int]:
        i, j = 0, len(s) - 1
        if i == j:
            return (True, i, j)
        while i < j:
            if s[i] != s[j]:
                return (False, i, j)
            i +=1
            j -= 1
        return (True, i, j)

    def validPalindrome(self, s: str) -> bool:
        p0, left, right = self.is_palindrome(s)
        if p0:
            return True
        p1, _, _ = self.is_palindrome(s[left+1:right+1])
        p2, _, _ = self.is_palindrome(s[left:right])
        return p1 or p2

if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    s = Solution()
    assert s.validPalindrome("aba") == True
    assert s.validPalindrome("abca") == True
    assert s.validPalindrome("abc") == False
    assert s.validPalindrome("mlcupuufxoohdffdhooxfuupuculm") == True
    assert s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga") == True
    print("Done!")