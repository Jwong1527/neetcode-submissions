from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)   # key: tuple(count of 26 letters), value: list of anagrams
        
        for string in strs:
            count = [0] * 26      # a-z
            
            for character in string:
                count[ord(character) - ord("a")] += 1
            
            # convert count list to a key because lists can't be dict keys
            res[tuple(count)].append(string)
            #So if the signature matches, we add it to the existing group of values associated with it
            #But if the signature doesn't, default dict will create a new pair with the new signature with
            # it being the only value in that new signature / anagram pair. 
        
        # return just the grouped lists
        return list(res.values())
