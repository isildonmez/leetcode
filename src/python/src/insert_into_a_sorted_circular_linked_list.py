# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        if head is None:
            head = Node(insertVal)
            head.next = head
            return head
        current = head
        while current.next != head:
            if current.val <= insertVal <= current.next.val:
                break
            elif current.val > current.next.val:
                if current.val < insertVal or insertVal <= current.next.val:
                    break
            current = current.next
        current.next = Node(insertVal, current.next)
        return head
