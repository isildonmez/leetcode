from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        nodes = deque()
        nodes.append(root)
        while len(nodes) > 0:
            depth += 1
            for _ in range(len(nodes)):
                head = nodes.popleft()
                if head.left is not None:
                    nodes.append(head.left)
                if head.right is not None:
                    nodes.append(head.right)
        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.right) + 1, self.maxDepth(root.left) + 1)
