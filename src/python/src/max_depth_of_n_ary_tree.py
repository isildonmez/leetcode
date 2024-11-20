# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/?envType=company&envId=datadog&favoriteSlug=datadog-all


from collections import deque
from typing import Optional


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[list["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if root is None:
            return 0
        nodes = deque()
        nodes.append((root, 1))
        max_depth = 1
        while len(nodes) > 0:
            current, depth = nodes.popleft()
            children = current.children
            for child in children:
                nodes.append((child, depth + 1))
                max_depth = max(max_depth, depth + 1)
        return max_depth
