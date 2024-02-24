# TODO: Check for better solutions in leetcode
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: int | None = None, right: int | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find_axis(self, root: TreeNode, axis: int, values: dict[int, list[int]]) -> dict[int, list[int]]:  
        queue: deque[tuple[TreeNode, int]] = deque()
        queue.append((root, axis)) 
        while len(queue) > 0:
            node, axis = queue.popleft()
            if axis in values:
                values[axis].append(node.val)
            else:
                values[axis] = [node.val]
            if node.left:
                queue.append((node.left, axis -1))
            if node.right:
                queue.append((node.right, axis + 1))
        return values

    def find_axis_dfs(self, root: TreeNode, axis: int, values: dict[int, list[int]]) -> dict[int, list[int]]:   
        if axis in values:
            values[axis].append(root.val)
        else:
            values[axis] = [root.val]
        if root.left:
            self.find_axis(root.left, axis - 1, values)
        if root.right:
            self.find_axis(root.right, axis + 1, values)
        return values

    def verticalOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        values_by_left_axis = self.find_axis(root, 0, {})
        axes = values_by_left_axis.keys()
        times, normalised = len(axes), abs(min(axes))
        result = [None] * times
        for a, v in values_by_left_axis.items():
            result[a+normalised] = v
        return result
    

if __name__ == "__main__":
    s = Solution()
    b1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    b2 = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7)))
    b3 = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0, None, TreeNode(2))), TreeNode(8, TreeNode(1, TreeNode(5)), TreeNode(7)))
    print("Testing...")
    assert s.verticalOrder(b1) == [[9], [3,15], [20],[7]]
    assert s.verticalOrder(b2) == [[4], [9], [3,0,1], [8], [7]]
    assert s.verticalOrder(b3) == [[4], [9,5], [3,0,1], [8,2], [7]]
    print("Done!")


        
