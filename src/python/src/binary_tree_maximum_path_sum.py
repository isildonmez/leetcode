# https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=company&envId=datadog&favoriteSlug=datadog-all

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float("-inf")

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if root is None:
                return 0
            right = max(dfs(root.right), 0)
            left = max(dfs(root.left), 0)
            max_sum = max(max_sum, right + left + root.val)

            return max(right, left) + root.val

        dfs(root)
        return max_sum
