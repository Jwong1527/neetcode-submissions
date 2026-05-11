class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i]) #Decision to Include I 
            dfs(i + 1) #Keeping running until we reach the leaf node.

            #Decision to not include I
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return res 


        