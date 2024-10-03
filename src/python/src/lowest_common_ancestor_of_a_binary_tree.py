class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None:
            return root

        if root in {p, q}:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        return left if left is not None else right


if __name__ == "__main__":
    s = Solution()
    r = TreeNode(3)
    p = TreeNode(5)
    q = TreeNode(1)
    r.right = q
    r.left = p
    a = TreeNode(6)
    b = TreeNode(2)
    c = TreeNode(0)
    d = TreeNode(8)
    m = TreeNode(7)
    n = TreeNode(4)
    p.left = a
    p.right = b
    b.left = m
    b.right = n
    q.left = c
    q.right = d
    print("Testing...")
    assert s.lowestCommonAncestor(r, p, q) == r
    print("Done!")
