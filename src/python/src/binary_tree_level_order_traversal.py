# https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=study-plan-v2&envId=top-interview-150


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return None
        queue = []
        return_lst = []
        queue.append(root)
        while len(queue) > 0:
            ans = []
            l = len(queue)
            for _ in range(l):
                node = queue.pop(0)
                ans.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            return_lst.append(ans)
        return return_lst
