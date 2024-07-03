from typing import Optional


class Node:
    def __init__(
        self, next: Optional["Node"] = None, visited: Optional[int] = False
    ) -> None:
        self.visited = visited
        self.next = next


def route_between_nodes(head: Node) -> bool:
    while head is not None:
        if head.visited == True:
            return True
        head.visited = True
        head = head.next
    return False


if __name__ == "__main__":
    print("Testing...")
    # n1 -> n2 -> n3 -> n1
    n1, n2, n3 = Node(), Node(), Node()
    n1.next = n2
    n2.next = n3
    n3.next = n1
    route_between_nodes(n1) == True
    n3.next = None
    route_between_nodes(n1) == False
    print("Done!")
