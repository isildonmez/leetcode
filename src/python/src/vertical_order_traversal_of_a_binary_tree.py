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
        column_to_row_val_pairs = defaultdict(list)
        far_left = far_right = 0
        while len(nodes) > 0:
            current, col, row = nodes.popleft()
            column_to_row_val_pairs[col].append((row, current.val))
            far_left = min(col, far_left)
            far_right = max(col, far_right)
            if current.left is not None:
                nodes.append((current.left, col - 1, row + 1))
            if current.right is not None:
                nodes.append((current.right, col + 1, row + 1))
        result = []
        for c in range(far_left, far_right + 1):
            result.append([v for r, v in sorted(column_to_row_val_pairs[c])])
        return result
