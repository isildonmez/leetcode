# https://leetcode.com/problems/valid-word-abbreviation/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        j = 0
        num = 0
        for i, c in enumerate(abbr):
            if c.isdigit():
                if num == 0 and c == "0":
                    return False
                num = num * 10 + int(c)
                if i == len(abbr) - 1:
                    return len(word) - j == num
                continue
            if num != 0:
                j += num
            num = 0
            if j >= len(word):
                return False
            if c != word[j]:
                return False
            j += 1
        if j != len(word):
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.validWordAbbreviation("internationalization", "i5a11o1") == True
    print("Done!")
