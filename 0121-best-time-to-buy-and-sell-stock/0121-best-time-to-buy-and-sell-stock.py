class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        k = 0
        max_profit = 0
        for i in range(1,len(prices)):
            profit = prices[i] - prices[k]
            if profit < 0:
                k = i
            else:
                max_profit = max(profit , max_profit)

        return max_profit