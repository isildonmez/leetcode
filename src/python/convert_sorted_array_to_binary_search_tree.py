from typing import Optional


class TreeNode:
    def __init__(self, val: int, left: int | None = None, right: int | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        mid_idx = len(nums) // 2
        root = TreeNode(nums[mid_idx])
        if len(nums) == 1:
            return root
        root.right = self.sortedArrayToBST(nums[mid_idx+1:]) if mid_idx + 1 < len(nums) else None
        root.left = self.sortedArrayToBST(nums[:mid_idx])
        return root
    

if __name__ == "__main__":
    s = Solution()
    a = s.sortedArrayToBST([0,1,2,3,4,5])
    a
    


