# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/?envType=company&envId=datadog&favoriteSlug=datadog-all

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        running_sum = 0

        def dfs(root: Optional[TreeNode]) -> None:
            nonlocal running_sum

            if root is None:
                return None
            dfs(root.right)
            running_sum += root.val
            root.val = running_sum
            dfs(root.left)

        dfs(root)
        return root
