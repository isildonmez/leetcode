# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
