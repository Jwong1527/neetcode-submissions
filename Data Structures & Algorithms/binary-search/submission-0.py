class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 1 Thing to note is that we know the input array is sorted. 

        # Binary Search -> Time Complexity = O(log n)

        left = 0 #Pointer that points to the start of the list.

        right = len(nums) - 1 #Pointer that starts at the end of the list - 1 because we are 0th indexed.

        while left <= right:

            mid_point = (left + right) // 2 #Floor division round down by 1 i.e 5 // 2 = 2 

            if nums[mid_point] > target:
                right = mid_point - 1
            elif nums[mid_point] < target:
                left = mid_point + 1
            else: #If we get to this condition -> We know that left and right are at the same value so this has to be either the value or the value
            #Doesn't exisit within the array so we can just return the index which is just the midpoint -> M.
                return mid_point 
        return -1 #We are going to return -1 -> If the target doesn't exist within the array.





        
        