class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]
        curSum = 0
        for i in range(len(nums)):
            if(curSum < 0):
                curSum = 0
            curSum += nums[i]
            maxSum = max(maxSum,curSum)
            
        return maxSum