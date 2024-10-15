# https://leetcode.com/problems/range-sum-of-bst/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        if root is None:
            return sum
        nodes = deque([root])
        while len(nodes) > 0:
            current = nodes.popleft()
            if high > current.val and current.right is not None:
                nodes.append(current.right)
            if low < current.val and current.left is not None:
                nodes.append(current.left)
            if low <= current.val <= high:
                sum += current.val
        return sum
