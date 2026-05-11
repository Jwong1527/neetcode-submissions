class Solution:
    def hammingWeight(self, n: int) -> int:

        ret_val = 0

        while n:
            ret_val += (n % 2)
            n = n >> 1
        
        return ret_val
        