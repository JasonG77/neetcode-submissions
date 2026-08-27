class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #keep track of min price and max profit
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            #update min price
            if price < min_price:
                min_price = price
            #calculate profit
            profit = price - min_price
            #update max profit
            if profit > max_profit:
                max_profit = profit
        return max_profit
