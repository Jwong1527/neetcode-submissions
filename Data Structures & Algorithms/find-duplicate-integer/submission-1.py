class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        lookup = set()

        for number in nums:
            if number in lookup:
                return number
            lookup.add(number)

        return -1
        