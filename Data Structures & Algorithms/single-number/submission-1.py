class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ret_val = 0

        for number in nums:
            ret_val ^= number

        return ret_val 
        