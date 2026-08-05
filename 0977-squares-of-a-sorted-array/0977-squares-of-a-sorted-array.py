class Solution(object):
    def sortedSquares(self, nums):
        l,r = 0,len(nums) - 1
        index = len(nums) - 1
        result = [0]*len(nums)
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                result[index] = nums[r]*nums[r]
                r -= 1
            else:
                result[index] = nums[l]*nums[l]
                l += 1
            index -= 1
        return result