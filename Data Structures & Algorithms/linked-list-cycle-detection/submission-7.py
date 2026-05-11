# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

    #Two Pointer Solution (There are multiple ways of using two pointers side by side or front and back slow or fast.)

    #We want to return true or false if there is a cycle or not.

    #What happens if we reach null return False?

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False 

    