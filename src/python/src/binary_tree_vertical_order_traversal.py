# https://leetcode.com/problems/binary-tree-vertical-order-traversal/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from collections import defaultdict
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self, val: int, left: int | None = None, right: int | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        nodes_by_axis = defaultdict(list)
        nodes = deque()
        nodes.append((root, 0))
        min_idx = max_idx = 0

        while len(nodes) > 0:
            n, axis = nodes.popleft()
            nodes_by_axis[axis].append(n.val)
            min_idx = min(min_idx, axis)
            max_idx = max(max_idx, axis)
            if n.left is not None:
                nodes.append((n.left, axis - 1))
            if n.right is not None:
                nodes.append((n.right, axis + 1))
        result = []
        for axis in range(min_idx, max_idx + 1):
            result.append(nodes_by_axis[axis])
        return result


if __name__ == "__main__":
    s = Solution()
    b1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    b2 = TreeNode(
        3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7))
    )
    b3 = TreeNode(
        3,
        TreeNode(9, TreeNode(4), TreeNode(0, None, TreeNode(2))),
        TreeNode(8, TreeNode(1, TreeNode(5)), TreeNode(7)),
    )
    print("Testing...")
    assert s.verticalOrder(b1) == [[9], [3, 15], [20], [7]]
    assert s.verticalOrder(b2) == [[4], [9], [3, 0, 1], [8], [7]]
    assert s.verticalOrder(b3) == [[4], [9, 5], [3, 0, 1], [8, 2], [7]]
    print("Done!")
