# From https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
import collections

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # On complexity?
        # s_occurences_of_unique_chars = collections.Counter(collections.Counter(s).values())
        # t_occurences_of_unique_chars = collections.Counter(collections.Counter(t).values())
        # if s_occurences_of_unique_chars != t_occurences_of_unique_chars:
        #     return False
        if len(s) != len(t):
            return False
        s_char_map = dict()
        for i in range(len(s)):
            if s[i] not in s_char_map:
                s_char_map[s[i]] = t[i]
            elif s_char_map[s[i]] != t[i]:
                return False
            else:
                continue
        if len(s_char_map) != len(set(s_char_map.values())):
            return False
        return True
    
    def isIsomorphicSolution(self, s: str, t: str) -> bool:
        zipped = set(zip(s,t))
        if len(zipped) == len(set(s)) == len(set(t)):
            return True
        else:
            return False
        


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.isIsomorphic("egg", "add") == True
    assert s.isIsomorphic("foo", "bar") == False
    assert s.isIsomorphic("paper", "title") == True
    assert s.isIsomorphic("bbbaaaba", "aaabbbba") == False
    assert s.isIsomorphicSolution("egg", "add") == True
    assert s.isIsomorphicSolution("foo", "bar") == False
    assert s.isIsomorphicSolution("paper", "title") == True
    assert s.isIsomorphicSolution("bbbaaaba", "aaabbbba") == False
    print("Done!")