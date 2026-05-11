class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        smallest = float('inf')
        largest = 0

        for price in prices:
            if price < smallest:
                smallest = price
            else:
                profit = price - smallest
                largest = max(largest, profit)

        return largest #The largest amount of money I can get from a given day. 
        