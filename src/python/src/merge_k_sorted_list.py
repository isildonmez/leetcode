# https://leetcode.com/problems/merge-k-sorted-lists/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        vals_to_nodes = defaultdict(list)
        for ll in lists:
            while ll is not None:
                vals_to_nodes[ll.val].append(ll)
                ll = ll.next
        dummy_head = ListNode()
        current = dummy_head
        for val in sorted(vals_to_nodes.keys()):
            for node in vals_to_nodes[val]:
                current.next = node
                current = current.next
        return dummy_head.next
