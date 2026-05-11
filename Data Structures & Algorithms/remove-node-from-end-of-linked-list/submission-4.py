# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head) #Dummy node initialized with value 0 and .next to the head.

        left = dummy #Left pointer starts at the dummy node as well.

        right = head #Right pointer starts to the right of n steps.

        while n > 0 and right is not None: #Move right ptr to n steps.
            right = right.next  #When our right ptr is Null our left pointer will be at the node that we can do the .next.next
            # to delete the node. 
            n -= 1 
        
        while right: #This loop will break after it gets to the end and our ptrs will. be in the right spot.
            left = left.next
            right = right.next 
    
        left.next = left.next.next

        return dummy.next 
        