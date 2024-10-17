# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


from collections import deque


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        for c in s:
            if len(stack) > 0 and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
