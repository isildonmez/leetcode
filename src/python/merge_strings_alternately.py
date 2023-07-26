# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
class Solution(object):
    def merge_alternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            result += word1[i] + word2[i]
        result += word1[min_length:] + word2[min_length:]

        return result
    
    def refactored_merge_alternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        return result

if __name__ == "__main__":
    print("Testing...")
    s = Solution()
    assert s.merge_alternately("abc", "pqr") == "apbqcr"
    assert s.merge_alternately("abcd", "pq") == "apbqcd"
    assert s.merge_alternately("ab", "pqrs") == "apbqrs"
    print("All passed")
