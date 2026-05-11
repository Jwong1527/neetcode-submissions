class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Set = set()

        for number in nums:
            if number in Set:
                return True
            Set.add(number)
        

        return False


         