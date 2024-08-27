# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        if root is None:
            return []
        result = []
        nodes = deque([root])
        while len(nodes) > 0:
            count = len(nodes)
            total = 0
            for _ in range(count):
                n = nodes.popleft()
                total += n.val
                if n.left is not None:
                    nodes.append(n.left)
                if n.right is not None:
                    nodes.append(n.right)
            result.append(total / count)
        return result


if __name__ == "__main__":
    s = Solution()
    r1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("Testing...")
    assert s.averageOfLevels(r1) == [3.00000, 14.50000, 11.00000]
    print("Done!")
