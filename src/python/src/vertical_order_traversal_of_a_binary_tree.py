# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


from collections import defaultdict
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        nodes = deque([(root, 0, 0)])
        node_vals = []
        while len(nodes) > 0:
            current, col, row = nodes.popleft()
            node_vals.append((col, row, current.val))
            if current.left is not None:
                nodes.append((current.left, col - 1, row + 1))
            if current.right is not None:
                nodes.append((current.right, col + 1, row + 1))
        node_vals.sort()
        vals_by_column = defaultdict(list)
        for c, _, v in node_vals:
            vals_by_column[c].append(v)
        return vals_by_column.values()
