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

        while fast and fast.next: #Because the slow and fast will always meet if there is a cycle. 
            slow = slow.next #iTERATE by 1
            fast = fast.next.next #iterate by 2 
            if slow == fast: # if they match return True
                return True 
         
        return False  

    