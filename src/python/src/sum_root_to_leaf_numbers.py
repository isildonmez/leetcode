from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sum_of_branch(self, root: TreeNode, current_sum: int, leaves: list[int]) -> None:
        if root.left is not None:
            self.sum_of_branch(root.left, current_sum * 10 + root.val, leaves)
        if root.right is not None:
            self.sum_of_branch(root.right, current_sum * 10 + root.val, leaves)
        if root.left is None and root.right is None:
            leaves.append(current_sum * 10 + root.val)


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        all_leaves = []
        self.sum_of_branch(root, 0, all_leaves)
        return sum(all_leaves)


if __name__ == "__main__":
    s = Solution()
    r1 = TreeNode(1, TreeNode(2), TreeNode(3))
    r2 = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    r3 = TreeNode(1, TreeNode(0))
    print("Testing...")
    assert s.sumNumbers(r1) == 25
    assert s.sumNumbers(r2) == 1026
    assert s.sumNumbers(r3) == 10
    print("Done!")