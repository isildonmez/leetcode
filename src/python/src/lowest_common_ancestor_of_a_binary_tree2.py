# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        if p is q:
            return p
        visited_nodes = set([p, q])
        while p.parent is not None or q.parent is not None:
            if p.parent is not None:
                if p.parent in visited_nodes:
                    return p.parent
                visited_nodes.add(p.parent)
                p = p.parent
            if q.parent is not None:
                if q.parent in visited_nodes:
                    return q.parent
                visited_nodes.add(q.parent)
                q = q.parent


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
