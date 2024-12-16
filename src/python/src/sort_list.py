from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# This is Onlogn (time) and Ologn(space);
# TODO: Check Editorial for O1(space)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        mid = self.get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list2 is None else list2
        return dummy.next

    def get_mid(self, current: Optional[ListNode]) -> Optional[ListNode]:
        if current is None:
            return current
        slow, fast = current, current.next
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid


if __name__ == "__main__":
    print("Testing...")
    s = Solution()
    n1 = ListNode(4)
    n2 = ListNode(2)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    h1 = s.sortList(n1)
    assert h1.val == n3.val
    assert h1.next.val == n2.val
    assert h1.next.next.val == n4.val
    assert h1.next.next.next.val == n1.val
    print("Done!")
