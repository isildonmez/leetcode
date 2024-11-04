from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(r: TreeNode) -> str:
    if r is not None:
        return f"{r.val}, {traverse(r.left)}, {traverse(r.right)}"


class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return traverse(p) == traverse(q)

    def is_same_solution(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is not None and q is not None:
            if p.val == q.val:
                return self.is_same_solution(p.left, q.left) and self.is_same_solution(
                    p.right, q.right
                )
        elif p is None and q is None:
            return True
        else:
            return False


if __name__ == "__main__":
    x = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), None)
    )
    y = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(3, TreeNode(6), None)
    )
    a = TreeNode(1, TreeNode(2, TreeNode(3), None), None)
    b = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    c = TreeNode(1, TreeNode(2, TreeNode(3), None), None)
    d = TreeNode(1, TreeNode(2, TreeNode(3), None), None)
    s = Solution()
    print("Testing...")
    assert s.is_same_tree(a, b) is False
    assert s.is_same_tree(c, d) is True
    assert s.is_same_solution(a, b) is False
    assert s.is_same_solution(c, d) is True
    print("Done!")
