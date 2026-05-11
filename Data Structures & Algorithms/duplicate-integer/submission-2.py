class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        track = set()

        for number in nums:
            if number in track:
                return True #If the number encountered is already in the set Return True
                            #There is a duplicate
            track.add(number)
        
        return False #If that line doesn't return true return False by default 
                     # -> No duplicate.

        