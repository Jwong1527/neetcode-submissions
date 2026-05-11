class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = set()

        for number in range(len(nums)):
            if nums[number] > 0 and nums[number] == nums[number-1]:
                continue
            
            seen = {}

            target = -nums[number]

            for j in range (number + 1, len(nums)):
                difference = target - nums[j]
                if difference in seen:
                    ret_val = (nums[number], difference, nums[j])
                    res.add(ret_val)
                seen[nums[j]] = j 
            
        
        return list(res) #Return the tuple in 3's. 
        