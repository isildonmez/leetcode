#  From https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        i, j = 0, len(s) - 1
        while j > i:
            if s[j].lower() != s[i].lower():
                return False
            i += 1
            j -= 1

        return True
    
    def isPalindromeSolution(self, s: str) -> bool:
        s = s.lower()

        l = 0
        r = len(s) - 1
        while(l < r):
            while(l < r and not s[l].isalnum() ):
                l += 1
            
            while(l < r and not s[r].isalnum()):
                r -= 1

            if(s[l] != s[r]):
                return False
            else:
                l+= 1
                r-= 1
        
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