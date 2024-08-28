# https://leetcode.com/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = self.dfs(root)
        difference = abs(vals[0] - vals[1])
        for i in range(2, len(vals)):
            difference = min(difference, abs(vals[i] - vals[i - 1]))
        return difference

    def dfs(self, root: Optional[TreeNode]) -> list[int]:
        return (
            self.dfs(root.left) + [root.val] + self.dfs(root.right)
            if root is not None
            else []
        )


if __name__ == "__main__":
    a = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, None, None))
    b = TreeNode(1, TreeNode(0, None, None), TreeNode(48, TreeNode(12), TreeNode(49)))
    print("Testing...")
    s = Solution()
    assert (s.getMinimumDifference(a)) == 1
    assert (s.getMinimumDifference(b)) == 1
    print("Done!")
