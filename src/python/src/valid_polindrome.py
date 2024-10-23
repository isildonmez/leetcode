#  From https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while l <= r and (not s[l].isalnum()):
                l += 1
            while l <= r and (not s[r].isalnum()):
                r -= 1
            if l <= r and s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.isPalindrome("A man, a plan, a canal: Panama") == True
    assert s.isPalindrome("race a car") == False
    assert s.isPalindrome(" ") == True
    assert s.isPalindromeSolution("A man, a plan, a canal: Panama") == True
    assert s.isPalindromeSolution("race a car") == False
    assert s.isPalindromeSolution(" ") == True
    print("Done!")
