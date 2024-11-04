from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return head
        original_nodes = []
        original_nodes_to_idx = {}
        current = head
        idx_of_node = 0
        while current is not None:
            original_nodes.append(current)
            original_nodes_to_idx[current] = idx_of_node
            idx_of_node += 1
            current = current.next
        new_nodes = []
        for _ in range(len(original_nodes)):
            new_nodes.append(Node(0))
        for i, h in enumerate(original_nodes):
            current = new_nodes[i]
            current.val = h.val
            if i + 1 <= len(original_nodes) - 1:
                current.next = new_nodes[i + 1]
            else:
                current.next = None
            if h.random is None:
                current.random = None
            else:
                current.random = new_nodes[original_nodes_to_idx[h.random]]
        return new_nodes[0]


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
    assert output.random is None
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
    assert output.next.next is None
    assert output.random.random.val == 2
    print("Done!")
