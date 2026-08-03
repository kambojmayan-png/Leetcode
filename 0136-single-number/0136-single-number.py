class Solution(object):
    def singleNumber(self, nums):
        xxor = 0
        for i in nums:
            xxor ^= i
        return xxor