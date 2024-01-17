# https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def traverse_with_level(r: TreeNode, idx: int = 0, nodes_by_level: list[int] | None = None) -> list[list[int]]:
    if nodes_by_level is None:
        nodes_by_level = list()
    if r is not None:
        if idx >= len(nodes_by_level):
            nodes_by_level.append([r.val])
        else:
            nodes_by_level[idx].append(r.val)
        idx += 1
        traverse_with_level(r.left, idx, nodes_by_level)
        traverse_with_level(r.right, idx, nodes_by_level)
        return nodes_by_level
    


class Solution:
    def right_side_view(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        nodes = traverse_with_level(root)
        right_view = []
        for el in nodes:
            right_view.append(el[-1])
        return right_view



if __name__ == "__main__":
    a = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    b = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    c = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, TreeNode(4), None))
    d = TreeNode(1, TreeNode(2), None)
    s = Solution()
    print("Testing...")
    assert traverse_with_level(d) == [[1], [2]]
    assert traverse_with_level(c) == [[1], [2,3], [5, 4]]
    assert traverse_with_level(b) == [[1], [2], [3]]
    assert traverse_with_level(a) == [[1], [2,3], [5, 4]]
    assert s.right_side_view(a) == [1,3,4]
    assert s.right_side_view(b) == [1,2,3]
    assert s.right_side_view(c) == [1,3,4]
    assert s.right_side_view(d) == [1,2]
    assert s.right_side_view(None) == []
    print("Done!")