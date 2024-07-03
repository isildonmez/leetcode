# Implement an algorithm to find the kth to last element of a singly linked list.
from typing import Optional


class Node:
    def __init__(self, val: int, next: Optional["Node"] = None) -> None:
        self.val = val
        self.next = next


def kth_to_last_node(head: Node, k: int) -> Node:
    nodes = []
    while head is not None:
        nodes.append(head)
        head = head.next
    if k >= len(nodes):
        return None
    return nodes[-k]


def kth_to_last_node_alternative(head: Node, k: int) -> Node:
    num_of_nodes = 0
    current_node = head
    while current_node is not None:
        num_of_nodes += 1
        current_node = current_node.next
    for _ in range(num_of_nodes - k):
        head = head.next
    return head


if __name__ == "__main__":
    n = Node(-2, Node(-1))
    head = Node(1, Node(2, Node(3, n)))
    print("Testing...")
    assert kth_to_last_node(head, 2) == n
    assert kth_to_last_node_alternative(head, 2) == n
    print("Done!")
