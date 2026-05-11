class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        ret_val = n 

        for index in range(len(nums)):

            ret_val ^= index

            ret_val ^= nums[index]

        return ret_val         

