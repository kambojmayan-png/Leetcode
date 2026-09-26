class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < min_price: 
                min_price = price
            else:
                max_profit = max( price - min_price , max_profit)

        return max_profit