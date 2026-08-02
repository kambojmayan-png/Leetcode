class Solution(object):
    def removeDuplicates(self, nums):
        count = 0
        for i in range(1,len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
            else:
                nums[i] = 0
        return count + 1