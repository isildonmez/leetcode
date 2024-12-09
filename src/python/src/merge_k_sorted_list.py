# https://leetcode.com/problems/merge-k-sorted-lists/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from heapq import heapify
from heapq import heappop
from heapq import heappush
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        heads = [(l.val, idx) for idx, l in enumerate(lists) if l is not None]
        heapify(heads)
        while len(heads) > 0:
            val, idx = heappop(heads)
            current.next = ListNode(val)
            current = current.next
            lists[idx] = lists[idx].next
            if lists[idx] is not None:
                heappush(heads, (lists[idx].val, idx))
        return dummy_head.next
