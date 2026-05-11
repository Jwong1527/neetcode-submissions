class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        freq = [ [] for i in range(len(nums)+1) ]


        for number in nums:
            count[number] = 1 + count.get(number, 0) #If not exist init 0 and + 1 to count.

        for number, count in count.items():

            freq[count].append(number)


        ret_val = [] #Now we can start building our solution.

        for index in range(len(freq) - 1, 0, -1 ): #Start at the end off by 1, Stop at 0, -1 Step
            for number in freq[index]: #Access list of numbers with that count based on the index.
                ret_val.append(number) #Appending 1 at a time to that list.
                if len(ret_val) == k: #If length of answer == k we know that we can stop and return.
                    return ret_val

        