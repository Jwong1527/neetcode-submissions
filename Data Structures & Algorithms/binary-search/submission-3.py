class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0 #Pointer that is at the start of the list. 

        right = len(nums) - 1 #We start from the 0th Position.
        

        while left <= right:
            midpoint = (left+right) // 2
            if nums[midpoint] > target:
                right = midpoint - 1
            elif nums[midpoint] < target:
                left = midpoint +1
            else:
                return midpoint
        return -1 

    