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
        new_node = Node(insertVal)
        current = head
        insert = False
        while True:
            if current.next == head:
                insert = True
            elif current.val <= insertVal <= current.next.val:
                insert = True
            elif current.val > current.next.val:
                if current.val <= insertVal or insertVal <= current.next.val:
                    insert = True
            if insert is True:
                new_node.next = current.next
                current.next = new_node
                return head
            current = current.next
