class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def find_path(
        self,
        target: "TreeNode",
        root: "TreeNode",
        level: int,
        existing_path: set[tuple["TreeNode", int]],
    ) -> None:
        if root == target:
            existing_path.add((root, level))
            return
        if root.right is not None:
            self.find_path(target, root.right, level - 1, existing_path)
            if len(existing_path) > 0:
                existing_path.add((root, level))
                return
        if root.left is not None:
            self.find_path(target, root.left, level - 1, existing_path)
            if len(existing_path) > 0:
                existing_path.add((root, level))
                return

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        q_path = set()
        self.find_path(q, root, 0, q_path)
        p_path = set()
        self.find_path(p, root, 0, p_path)
        commons = p_path.intersection(q_path)
        lowest_node, lowest_level = None, None
        for node, level in commons:
            if lowest_level == None or lowest_level > level:
                lowest_level, lowest_node = level, node
        return lowest_node

    def lowestCommonAncestorSolution(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or root in {p, q}:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left

        return right


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
