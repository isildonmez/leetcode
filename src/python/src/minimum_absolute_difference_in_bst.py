from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def traverse_for_values(root: TreeNode, values: list[int]) -> list[int]:
    if root is not None and root.val is not None:
        values.append(root.val)
        traverse_for_values(root.left, values)
        traverse_for_values(root.right, values)
        return values


class Solution:
    def minimum_absolute_difference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        vals = traverse_for_values(root, [])
        vals.sort()
        idx = 0
        min_difference = abs(vals[1] - vals[0])
        while idx < len(vals) - 1:
            if abs(vals[idx] - vals[idx + 1]) < min_difference:
                min_difference = abs(vals[idx] - vals[idx + 1])
            idx += 1
        return min_difference


if __name__ == "__main__":
    a = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, None, None))
    b = TreeNode(1, TreeNode(0, None, None), TreeNode(48, TreeNode(12), TreeNode(49)))
    print("Testing...")
    s = Solution()
    assert (s.minimum_absolute_difference(a)) == 1
    assert (s.minimum_absolute_difference(b)) == 1
    print("Done!")
