# https://leetcode.com/problems/valid-palindrome-ii/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                sub1 = s[i:j]
                sub2 = s[i + 1 : j + 1]
                return sub1 == sub1[::-1] or sub2 == sub2[::-1]
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    s = Solution()
    assert s.validPalindrome("aba") == True
    assert s.validPalindrome("abca") == True
    assert s.validPalindrome("abc") == False
    assert s.validPalindrome("mlcupuufxoohdffdhooxfuupuculm") == True
    assert (
        s.validPalindrome(
            "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
        )
        == True
    )
    print("Done!")
