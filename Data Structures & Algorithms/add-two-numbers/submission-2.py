# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        dummy_node = ListNode()

        current = dummy_node

        carry = 0

        while l1 or l2 or carry: #We want our algo to keeping running if there is a .next or still a carry.

            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            value = val_1 + val_2 + carry

            carry = value // 10

            value = value % 10

            current.next = ListNode(value)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_node.next 
            






        