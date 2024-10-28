# https://leetcode.com/problems/binary-search-tree-iterator/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = self._inorder_dfs(root)
        self.cursor = 0

    def next(self) -> int:
        node = self.nodes[self.cursor]
        self.cursor += 1
        return node

    def hasNext(self) -> bool:
        return self.cursor < len(self.nodes)

    def _inorder_dfs(self, root: Optional[TreeNode()]) -> list[int]:
        if root is None:
            return []
        return self._inorder_dfs(root.left) + [root.val] + self._inorder_dfs(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
