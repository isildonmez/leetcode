# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-interview-150

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = deque()
        current = root
        while len(stack) > 0 or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            count += 1
            if count == k:
                return current.val
            current = current.right
