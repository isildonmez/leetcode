from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
class Traverse:
    # node -> left -> right
    def dfs_preorder(self, root: Optional['TreeNode']) -> list['TreeNode']:
        return [root.val] + self.dfs_preorder(root.left) + self.dfs_preorder(root.right) if root else []
    
    # left -> node -> right
    def dfs_inorder(self, root: Optional['TreeNode']) -> list['TreeNode']:
        return self.dfs_inorder(root.left) + [root.val] + self.dfs_inorder(root.right) if root else []
    
    # left -> right -> node
    def dfs_postorder(self, root: Optional['TreeNode']) -> list['TreeNode']:
        return self.dfs_postorder(root.left) + self.dfs_postorder(root.right) + [root.val] if root else []
    
    # node -> left -> right
    def bfs(self, root: Optional['TreeNode']) -> list['TreeNode']:
        if root is None: return None
        nodes = []
        stack = deque()
        stack.append(root)
        while len(stack) > 0:
            node = stack.popleft()
            nodes.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return nodes


if __name__ == "__main__":
    t = Traverse()
#         1
#     2      3
#    4  5
    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("Testing...")
    assert t.dfs_preorder(tree) == [1,2,4,5,3]
    assert t.dfs_inorder(tree) == [4,2,5,1,3]
    assert t.dfs_postorder(tree) == [4,5,2,3,1]
    assert t.bfs(tree) == [1,2,3,4,5]
    print("Done!")