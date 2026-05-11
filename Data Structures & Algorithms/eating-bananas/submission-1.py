import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles) #Init left and right Pointers
        ret_val = right  # Max amount within our range to eat all the BANANAS.

        while left <= right: # While our pointers don't cross.

            mid_point = (left + right) // 2
            hours = 0

            for p in piles:
                hours += math.ceil( p / mid_point) #Round Up

            if hours <= h:
                ret_val = min(ret_val, mid_point)
                right = mid_point - 1
            else:
                left = mid_point + 1

        return ret_val

