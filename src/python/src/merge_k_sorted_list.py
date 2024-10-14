# https://leetcode.com/problems/merge-k-sorted-lists/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for linked_list in lists:
            head = linked_list
            while head is not None:
                heapq.heappush(min_heap, head.val)
                head = head.next
        dummy_head = ListNode()
        current = dummy_head
        while len(min_heap) > 0:
            val = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
        return dummy_head.next
