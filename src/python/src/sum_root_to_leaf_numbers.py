from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        nodes = deque([(root, root.val)])
        res = 0
        while len(nodes) > 0:
            current, num = nodes.pop()
            if current.left is not None:
                nodes.append((current.left, num * 10 + current.left.val))
            if current.right is not None:
                nodes.append((current.right, num * 10 + current.right.val))
            if current.right is None and current.left is None:
                res += num
        return res


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
