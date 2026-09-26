class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        curMax,curMin = 1,1
        for i , number in enumerate(nums):
            temp = curMax * number
            curMax = max(number , number*curMax , number*curMin)
            curMin = min(number , temp , number*curMin)
            res = max(res,curMax)
        return res