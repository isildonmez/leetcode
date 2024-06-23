# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?
from typing import Optional


class Node:
    def __init__(self, val: int, next: Optional["Node"] = None):
        self.val = val
        self.next = next


def remove_dups(n: Node) -> None:
    vals = set()
    if n is None:
        return n
    current = n
    vals.add(current.val)
    while current.next is not None:
        if current.next.val in vals:
            current.next = current.next.next
        else:
            vals.add(current.next.val)
            current = current.next


def remove_dups_alternative(n: Node) -> None:
    vals = set()
    previous = None
    while n is not None:
        if n.val in vals:
            previous.next = n.next
        else:
            vals.add(n.val)
            previous = n
        n = n.next


def remove_wo_buffer(n: Node) -> None:
    while n is not None:
        current = n
        while current.next is not None:
            if current.next.val == n.val:
                current.next = current.next.next
            else:
                current = current.next
        n = n.next


if __name__ == "__main__":
    print("Testing remove_dups")
    n = Node(1, Node(2, Node(1, Node(2, Node(3, Node(3, Node(3, Node(1))))))))
    remove_dups(n)
    while n is not None:
        print(f"{n.val}")
        n = n.next
    print("Testing remove_dups_alternative")
    n = Node(1, Node(2, Node(1, Node(2, Node(3, Node(3, Node(3, Node(1))))))))
    remove_dups_alternative(n)
    while n is not None:
        print(f"{n.val}")
        n = n.next
    print("Testing remove_wo_buffer")
    n = Node(1, Node(2, Node(1, Node(2, Node(3, Node(3, Node(3, Node(1))))))))
    remove_wo_buffer(n)
    while n is not None:
        print(f"{n.val}")
        n = n.next
    print("Done!")
