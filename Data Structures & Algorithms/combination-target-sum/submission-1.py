class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Classic BackTracking Sum 

        # Combinations - We Don't want permutations - Ordering doesn't matter ie [1, 2] == [2, 1]

        # Time COMPLEXITy of this is 2 times the height of our decision tree

        # This is equal to 2^t where t is the target value big o time


        res = []


        def dfs(i, cur, total): #Cur is list of values in the current combination.
            if total == target:
                res.append(cur.copy()) # Add a list of the copy of the current combintation that is equal to the target sum.
                return # Base Case #1 == We find a combination sum
            if i >= len(nums) or total > target:
                return # Cannot find a combination exhausting all possible combinations either total greater than target or ran out of options.
            
            nums[i] # The choice to include I or to not include I

            cur.append(nums[i])
            
            dfs(i, cur, total + nums[i]) # This is decision 1

            cur.pop()

            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res



            



        