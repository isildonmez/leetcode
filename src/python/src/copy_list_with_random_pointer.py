from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        idx_by_node = {}  # node -> idx
        nodes = []
        idx = 0
        root = head
        while root is not None:
            idx_by_node[root] = idx
            nodes.append(root)
            root = root.next
            idx += 1

        root = None
        new_nodes = []
        for node in reversed(nodes):
            root = Node(node.val, root, None)
            new_nodes.append(root)
        new_nodes.reverse()

        for idx, node in enumerate(new_nodes):
            old_random_node = nodes[idx].random
            if old_random_node is None:
                continue
            random_idx = idx_by_node[old_random_node]
            node.random = new_nodes[random_idx]

        if root is None:
            return None
        return root


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    n4 = Node(1, None, None)
    n3 = Node(10, n4, None)
    n2 = Node(11, n3, n4)
    n1 = Node(13, n2, None)
    n0 = Node(7, n1, None)
    n4.random = n0
    n3.random = n2
    n1.random = n0
    output = s.copyRandomList(n0)
    assert output.val == 7  # n0
    assert output.random == None
    assert output.next.val == 13  # n1
    assert output.next.random.val == 7
    assert output.next.next.val == 11  # n2
    assert output.next.next.random.val == 1
    assert output.next.next.next.val == 10  # n3
    assert output.next.next.next.random.val == 11
    assert output.next.next.next.next.val == 1  # n4
    assert output.next.next.next.next.random.val == 7
    n_1 = Node(1)
    n_2 = Node(2)
    n_1.next = n_1.random = n_2
    n_2.random = n_2
    n_2.next = None
    output = s.copyRandomList(n_1)
    assert output.val == 1
    assert output.next.val == 2
    assert output.random.val == 2
    assert output.next.next == None
    assert output.random.random.val == 2
    print("Done!")
