class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {} #Map of (Value -> Index)

        # 2 + x = 9 IE 

        for index, number in enumerate(nums):
            Difference = target - number 

            if Difference in prevMap:
                return [prevMap[Difference], index]

            prevMap[number] = index 
        
        return []

        