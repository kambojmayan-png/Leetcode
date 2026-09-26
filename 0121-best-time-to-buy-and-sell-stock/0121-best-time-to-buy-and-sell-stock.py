class Solution(object):
    def maxProfit(self, prices):
        l,r = 0,1
        maxP = 0
        while(r < len(prices)):
            profit = prices[r] - prices[l]
            if(profit > 0):
                maxP = max(maxP,profit)
            if(profit < 0):
                l = r
            r += 1
        return maxP
            