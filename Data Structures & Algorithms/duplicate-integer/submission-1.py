class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        init_Set = set()

        for number in nums:
            if number in init_Set:
                return True
            init_Set.add(number)
        
        return False 

        