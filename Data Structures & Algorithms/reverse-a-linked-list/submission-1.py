# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None #Dummy Pointer that is None at first but points to the head. i.e 1
        curr = head #Init Head pointer 

        while curr: # While the Current node is not None:
            next_node = curr.next #Save the next link because we are going to break it.
            curr.next = prev #Point the current node's next to 
            prev = curr #Shift the previous to Current 
            curr = next_node # Shift the Current to next_node
    
        return prev  #Return Prev which will always be the first node. 
        