# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        if root is None:
            return root
        nodes = self.dfs(root)
        for i in range(len(nodes) - 1):
            current, next_node = nodes[i], nodes[i + 1]
            current.right = next_node
            next_node.left = current
        nodes[-1].right = nodes[0]
        nodes[0].left = nodes[-1]
        return nodes[0]

    def dfs(self, root: "Optional[Node]") -> list["Optional[Node]"]:
        if root is None:
            return []
        return self.dfs(root.left) + [root] + self.dfs(root.right)
