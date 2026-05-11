class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ret_val = [0] * len(temperatures)

        stack = [] # Pair/Tuple of (Temp -> Index)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: # While our stack is non-empty and most recent temp is 
                stackT, stackInd = stack.pop()# Greater Than
                ret_val[stackInd] = (index - stackInd)
            stack.append([temp, index])
        return ret_val
        