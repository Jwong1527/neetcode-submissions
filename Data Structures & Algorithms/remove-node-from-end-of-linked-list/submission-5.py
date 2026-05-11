# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
    
        left = dummy

        right = head 

        while n > 0 and right: #We want to keep shifting right for n steps so that right can be in the correct starting
            right = right.next #Position 
            n -= 1

        while right: #So we are going to keep shifting until we hit the end of the list in this case. 
            right = right.next
            left = left.next

        
        left.next = left.next.next

        return dummy.next





        