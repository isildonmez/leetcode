# https://leetcode.com/problems/valid-word-abbreviation/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        j = 0
        num = 0
        for c in abbr:
            if c.isdigit():
                if num == 0 and c == "0":
                    return False
                num = num * 10 + int(c)
                continue
            j += num
            if j >= len(word) or word[j] != c:
                return False
            j += 1
            num = 0
        if j + num != len(word):
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.validWordAbbreviation("internationalization", "i5a11o1") == True
    print("Done!")
