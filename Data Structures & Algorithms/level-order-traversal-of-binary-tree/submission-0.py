# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Time + Mem complexity -> O(n)

        ret_val = []

        q = collections.deque() # Init Queue 
        
        q.append(root) # Process the starting node. Append to Queue.

        while q: # While there is still a node to be processed. 
            qLen = len(q)

            level = [] # Storing the result for each level. 

            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                ret_val.append(level)

        return ret_val 





