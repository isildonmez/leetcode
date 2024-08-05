# https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        tail = dummy
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            tail.next = ListNode(carry % 10)
            tail = tail.next
            carry = carry // 10
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    l3 = ListNode(7, ListNode(0, ListNode(8)))
    print("Testing...")
    l4 = s.addTwoNumbers(l1, l2)
    assert l4.val == l3.val
    assert l4.next.val == l3.next.val
    assert l4.next.next.val == l3.next.next.val
    assert l4.next.next.next == l3.next.next.next
    print("Done!")
