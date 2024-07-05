from collections import defaultdict
from typing import Optional


class Node:
    def __init__(
        self, val: int, left: Optional["Node"] = None, right: Optional["Node"] = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def minimal_bst(nums: list[int]) -> Node:
    mid_idx = int(len(nums) / 2)
    if len(nums) == 0:
        return
    head = Node(nums[mid_idx])
    head.left = minimal_bst(nums[:mid_idx])
    head.right = minimal_bst(nums[mid_idx + 1 :])
    return head


def find_depth_of_tree(head: Node) -> int:
    depth = 1
    if head is None:
        return depth
    nodes_by_levels = defaultdict(list)
    nodes_by_levels[depth] = [head]
    while len(nodes_by_levels[depth]) != 0:
        for n in nodes_by_levels[depth]:
            if n.left is not None:
                nodes_by_levels[depth + 1].append(n.left)
            if n.right is not None:
                nodes_by_levels[depth + 1].append(n.right)
        depth += 1
    return depth - 1


if __name__ == "__main__":
    print("Pre-Testing...")
    #     1
    #  2     3
    # 4     5
    #     6
    test_head1 = Node(1, Node(2, Node(4)), Node(3, Node(5, Node(6))))
    assert find_depth_of_tree(test_head1) == 4
    print("Testing...")
    nums0 = [1]
    head0 = minimal_bst(nums0)
    assert head0.val == 1
    assert find_depth_of_tree(head0) == 1

    nums1 = [1, 2, 3]  # 2 levels, head == 2
    head1 = minimal_bst(nums1)
    assert head1.val == 2
    assert find_depth_of_tree(head1) == 2

    nums2 = [1, 2, 3, 4, 5]  # 3 levels, head == 3
    head2 = minimal_bst(nums2)
    assert head2.val == 3
    assert find_depth_of_tree(head2) == 3

    nums3 = [1, 2, 3, 4, 5, 6, 7]  # 3 levels, head == 4
    head3 = minimal_bst(nums3)
    assert head3.val == 4
    assert find_depth_of_tree(head3) == 3

    nums4 = [1, 2, 3, 4, 5, 6, 7, 8]  # 4 levels, head == 5
    head4 = minimal_bst(nums4)
    assert head4.val == 5
    assert find_depth_of_tree(head4) == 4
    print("Done!")
