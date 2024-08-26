# https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.sym(root.left, root.right)

    def sym(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return (
            root1.val == root2.val
            and self.sym(root1.left, root2.right)
            and self.sym(root1.right, root2.left)
        )

    def isSymmetricAlternative(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        nodes = deque([root])
        while len(nodes) > 0:
            for _ in range(len(nodes)):
                n = nodes.popleft()
                if n is not None:
                    nodes.extend([n.left, n.right])
            if len(nodes) % 2 != 0:
                return False
            mid_idx = len(nodes) // 2
            for i in range(mid_idx):
                if nodes[i] is not None and nodes[-i - 1] is not None:
                    if nodes[i].val != nodes[-i - 1].val:
                        return False
                elif nodes[i] is None and nodes[-i - 1] is None:
                    continue
                else:
                    return False
        return True
