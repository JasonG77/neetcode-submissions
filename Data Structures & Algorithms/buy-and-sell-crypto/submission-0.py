class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initiate left and right pointer variables
        l, r = 0, 1; #left ptr is buy; right ptr is sell
        maxP = 0

        while r < len(prices):
            #profitable transaction?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit) #use max function
            else:
                l = r
            r+= 1
        return maxP