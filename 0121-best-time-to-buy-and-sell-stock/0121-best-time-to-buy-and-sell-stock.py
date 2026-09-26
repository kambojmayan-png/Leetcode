class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        k = 0
        Max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] - prices[k] < 0:
                k = i
            else:
                Max_profit = max(prices[i] - prices[k] , Max_profit)

        return Max_profit