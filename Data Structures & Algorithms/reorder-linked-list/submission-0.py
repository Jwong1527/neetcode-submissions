class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1) Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Split + reverse second half
        start = slow.next
        slow.next = None  # cut

        prev = None
        curr = start
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3) Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
