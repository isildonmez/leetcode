# https://www.educative.io/courses/grokking-coding-interview-in-python/flatten-binary-tree-to-linked-list


from typing import Optional


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def flatten_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None

    current = root
    while current is not None:
        if current.left is not None:
            last = current.left
            while last.right is not None:
                last = last.right
            last.right = current.right
            current.right = current.left
            current.left = None
        current = current.right
    return root
