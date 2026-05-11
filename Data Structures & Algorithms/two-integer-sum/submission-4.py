class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prev_map = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in prev_map:
                return [prev_map[diff], index] #Returns the index position of the two nums
            prev_map[number] = index
        
        return 
        