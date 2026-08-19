class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        maxlen = 0
        for n in numSet:
            if (n - 1) not in numSet:
                tempMax = 0
                while (n + tempMax) in numSet:
                    tempMax += 1
                maxlen = max(tempMax, maxlen)

        return maxlen