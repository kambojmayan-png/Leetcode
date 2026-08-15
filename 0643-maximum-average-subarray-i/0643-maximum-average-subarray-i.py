class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxlen = 0
        temp = 0
        l,r = 0,k

        for i in range(k):
            temp += nums[i]
        
        maxlen = temp

        while r < len(nums):
            temp = temp - nums[l] + nums[r]
            maxlen = max(maxlen,temp)
            
            l += 1
            r += 1
        
        return maxlen/k