class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Current_Value + X = Target

        Dict = {}

        for index, number in enumerate(nums):

            difference = target - number
            if difference in Dict:
                return [Dict[difference],index]
            
            Dict[number] = index 

        return []

        