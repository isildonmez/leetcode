# from https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75

from collections import deque
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        vals = deque()
        while head is not None:
            vals.append(head.val)
            head = head.next
        reversed = ListNode(vals.pop())
        cursor = reversed
        while len(vals) > 0:
            cursor.next = ListNode(vals.pop())
            cursor = cursor.next
        return reversed
    
    def alternativeReverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None 
        reversed = ListNode(head.val)
        rest = head.next
        while rest is not None:
            cursor = ListNode(rest.val)
            rest = rest.next
            cursor.next = reversed
            reversed = cursor
        return reversed


    def otherAlternativeReverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = None
        while head is not None:
            temp = head.next
            head.next = reversed
            reversed = head
            head = temp
        return reversed
