# https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-interview-150

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        nodes = deque([root])
        res = []
        while len(nodes) > 0:
            for _ in range(len(nodes)):
                n = nodes.popleft()
                if n.left is not None:
                    nodes.append(n.left)
                if n.right is not None:
                    nodes.append(n.right)
            res.append(n.val)
        return res
