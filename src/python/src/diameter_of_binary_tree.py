# https://leetcode.com/problems/diameter-of-binary-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-all&status=SOLVED


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.calculate_edges(root)
        return self.diameter

    def calculate_edges(self, current: TreeNode) -> int:
        if current.left is None and current.right is None:
            return 0
        left = right = 0
        if current.left is not None:
            left = self.calculate_edges(current.left) + 1
        if current.right is not None:
            right = self.calculate_edges(current.right) + 1
        self.diameter = max(self.diameter, left + right)
        return max(left, right)
