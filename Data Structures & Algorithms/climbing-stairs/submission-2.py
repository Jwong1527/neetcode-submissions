class Solution:
    def climbStairs(self, n: int) -> int:

        # Compute n - 1 values
        # When the 1 variable is at the 0 index we can break out of the loop

        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        
        return one
