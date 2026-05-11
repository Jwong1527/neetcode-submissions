class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        ret_val = [1] * len(nums)

        prefix, postfix = 1, 1

        for i in range(len(nums)): #Get all the prefix for that index 
            ret_val[i] *= prefix
            prefix *= nums[i]

        for i in range(len(nums)- 1, -1, -1): #Now all the prefixes are waiting to be multiplied 
            ret_val[i] *= postfix
            postfix *= nums[i] 
        
        #After this we can just return ret_val with the correct array.

        return ret_val 
