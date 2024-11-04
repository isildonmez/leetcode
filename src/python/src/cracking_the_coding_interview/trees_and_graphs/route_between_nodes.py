from collections import deque
from typing import Optional


class GNode:
    def __init__(self, val: int, children: Optional[list["GNode"]] = None) -> None:
        self.val = val
        self.children = children


def route_between_nodes(node1: GNode, node2: GNode) -> bool:
    if node1 == node2:
        return True
    children1, children2 = deque([node1]), deque([node2])
    paths1, paths2 = set(), set()
    while len(children1) != 0 or len(children2) != 0:
        if len(children1) != 0:
            curr1 = children1.popleft()
            paths1.add(curr1)
            if node2 in paths1:
                return True
            if curr1.children is not None:
                for c in curr1.children:
                    children1.append(c)
        if len(children2) != 0:
            curr2 = children2.popleft()
            paths2.add(curr2)
            if node1 in paths2:
                return True
            if curr2.children is not None:
                for c in curr2.children:
                    children2.append(c)
    return False


if __name__ == "__main__":
    print("Testing...")
    # n1 -> n2 -> n3
    # n4 -> n5 -> n3
    n1, n2, n3, n4, n5 = GNode(1), GNode(2), GNode(3), GNode(4), GNode(5)
    n1.children = [n2]
    n2.children = [n3]
    n4.children = [n5]
    n5.children = [n2]
    assert route_between_nodes(n1, n3) is True
    assert route_between_nodes(n1, n4) is False
    print("Done!")
