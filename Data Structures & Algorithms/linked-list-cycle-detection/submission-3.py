# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #Two Pointers 
        slow, fast = head, head

        while fast and fast.next: #If we reach the end of the list and we detect a null next then there is no cycle.
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True #Yes there is a cycle

        return False #Because this will always return false if the conditional above does not run. 