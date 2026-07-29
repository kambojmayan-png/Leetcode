class Solution(object):
    def twoSum(self, nums, target):
        index = {}
        for i,num in enumerate(nums):
            if((target - num) in index):
                return index[target - num],i
            index[num] = i
        