# TODO: Check for better solutions in leetcode

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_ancestors, q_ancestors = {p}, {q}
        p_ancestor, q_ancestor = p, q
        while p_ancestor is not None or q_ancestor is not None:
            if p_ancestor is not None:
                if p_ancestor in q_ancestors:
                    return p_ancestor
                p_ancestors.add(p_ancestor)
                p_ancestor = p_ancestor.parent
            if q_ancestor is not None:
                if q_ancestor in p_ancestors:
                    return q_ancestor
                q_ancestors.add(q_ancestor)
                q_ancestor = q_ancestor.parent


if __name__ == "__main__":
    s = Solution()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.left = n2
    n1.right = n3
    n2.right = n4
    print("Testing...")
    assert s.lowestCommonAncestor(n4, n3) == 1
    print("Done!")



        # Find the parent: compare parents sets.
