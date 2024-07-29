from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(second_half)

        return self.merge(left, right)

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy.next

    def alternativeSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        temp = head
        arr.sort()
        for i in arr:
            temp.val = i
            temp = temp.next
        return head


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
