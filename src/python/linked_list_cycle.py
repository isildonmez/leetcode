# https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        nodes = set()
        while head.next:
            if head.next in nodes:
                return True
            else:
                nodes.add(head.next)
            head = head.next
        return False
    
    def has_cycle_solution(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True 
        return False

